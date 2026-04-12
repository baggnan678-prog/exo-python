"""
Calculatrice Scientifique - Backend Flask
Auteur  : Seydou
Projet  : Génie Logiciel - UTM Burkina Faso
Version : 1.0

Architecture REST :
  POST /api/calc   -> Calculs standards + fonctions scientifiques
  POST /api/matrix -> Opérations matricielles (NumPy)
  POST /api/stats  -> Statistiques descriptives
"""

from flask import Flask, request, jsonify, render_template
import math
import statistics
import numpy as np

app = Flask(__name__)


# ─────────────────────────────────────────────
#  Évaluateur sécurisé d'expressions
# ─────────────────────────────────────────────

def safe_eval(expression: str, mode: str = "deg") -> float:
    """
    Évalue une expression mathématique dans un contexte sécurisé.
    - mode="deg" : les fonctions trig attendent des degrés
    - mode="rad" : les fonctions trig attendent des radians
    Aucune fonction __builtins__ n'est exposée (protection contre l'injection).
    """

    # Fonctions trig selon le mode
    if mode == "deg":
        trig = {
            "sin":  lambda x: math.sin(math.radians(x)),
            "cos":  lambda x: math.cos(math.radians(x)),
            "tan":  lambda x: math.tan(math.radians(x)),
            "asin": lambda x: math.degrees(math.asin(x)),
            "acos": lambda x: math.degrees(math.acos(x)),
            "atan": lambda x: math.degrees(math.atan(x)),
        }
    else:
        trig = {
            "sin":  math.sin,
            "cos":  math.cos,
            "tan":  math.tan,
            "asin": math.asin,
            "acos": math.acos,
            "atan": math.atan,
        }

    safe_dict = {
        **trig,
        "sqrt":      math.sqrt,
        "log":       math.log10,      # log en base 10
        "ln":        math.log,        # logarithme naturel
        "log2":      math.log2,
        "abs":       abs,
        "ceil":      math.ceil,
        "floor":     math.floor,
        "factorial": math.factorial,
        "exp":       math.exp,
        "pow":       math.pow,
        "pi":        math.pi,
        "e":         math.e,
        "__builtins__": {},           # Isolation totale
    }

    # Remplacement syntaxique : ^ -> ** (notation mathématique standard)
    expression = expression.replace("^", "**")

    return eval(expression, {"__builtins__": {}}, safe_dict)


# ─────────────────────────────────────────────
#  Routes
# ─────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/calc", methods=["POST"])
def calculate():
    """
    Corps JSON attendu :
      { "expression": "sin(45) + sqrt(16)", "mode": "deg" }
    Réponse :
      { "result": 4.707..., "error": null }
    """
    data = request.get_json()
    expression = data.get("expression", "").strip()
    mode = data.get("mode", "deg")

    if not expression:
        return jsonify({"result": None, "error": "Expression vide"}), 400

    try:
        result = safe_eval(expression, mode)
        # Arrondi à 10 décimales pour éviter le bruit flottant
        result = round(result, 10)
        return jsonify({"result": result, "error": None})
    except ZeroDivisionError:
        return jsonify({"result": None, "error": "Division par zéro"}), 422
    except ValueError as e:
        return jsonify({"result": None, "error": f"Valeur invalide : {e}"}), 422
    except Exception as e:
        return jsonify({"result": None, "error": f"Erreur : {e}"}), 422


@app.route("/api/matrix", methods=["POST"])
def matrix_op():
    """
    Corps JSON attendu :
      {
        "operation": "add" | "multiply" | "det" | "transpose" | "inverse",
        "matrix_a": [[1,2],[3,4]],
        "matrix_b": [[5,6],[7,8]]   (optionnel selon l'opération)
      }
    """
    data = request.get_json()
    operation = data.get("operation")
    matrix_a  = data.get("matrix_a")
    matrix_b  = data.get("matrix_b")

    if not matrix_a or not operation:
        return jsonify({"result": None, "error": "Données manquantes"}), 400

    try:
        A = np.array(matrix_a, dtype=float)

        if operation == "det":
            if A.shape[0] != A.shape[1]:
                raise ValueError("Le déterminant exige une matrice carrée.")
            result = round(float(np.linalg.det(A)), 8)
            return jsonify({"result": result, "type": "scalar", "error": None})

        elif operation == "transpose":
            result = A.T.tolist()
            return jsonify({"result": result, "type": "matrix", "error": None})

        elif operation == "inverse":
            if A.shape[0] != A.shape[1]:
                raise ValueError("L'inverse exige une matrice carrée.")
            det = np.linalg.det(A)
            if abs(det) < 1e-10:
                raise ValueError("Matrice singulière (det ≈ 0) : non inversible.")
            inv = np.linalg.inv(A)
            result = [[round(x, 8) for x in row] for row in inv.tolist()]
            return jsonify({"result": result, "type": "matrix", "error": None})

        elif operation in ("add", "multiply"):
            if matrix_b is None:
                raise ValueError("La matrice B est requise pour cette opération.")
            B = np.array(matrix_b, dtype=float)

            if operation == "add":
                if A.shape != B.shape:
                    raise ValueError("Les matrices doivent avoir les mêmes dimensions pour l'addition.")
                result = (A + B).tolist()
            else:  # multiply
                if A.shape[1] != B.shape[0]:
                    raise ValueError(
                        f"Dimensions incompatibles : ({A.shape[0]}×{A.shape[1]}) · ({B.shape[0]}×{B.shape[1]})"
                    )
                result = np.dot(A, B).tolist()

            result = [[round(x, 8) for x in row] for row in result]
            return jsonify({"result": result, "type": "matrix", "error": None})

        else:
            return jsonify({"result": None, "error": "Opération inconnue"}), 400

    except np.linalg.LinAlgError as e:
        return jsonify({"result": None, "error": f"Erreur algèbre linéaire : {e}"}), 422
    except ValueError as e:
        return jsonify({"result": None, "error": str(e)}), 422
    except Exception as e:
        return jsonify({"result": None, "error": f"Erreur : {e}"}), 422


@app.route("/api/stats", methods=["POST"])
def stats_op():
    """
    Corps JSON attendu :
      { "numbers": [4, 8, 15, 16, 23, 42] }
    Réponse : dictionnaire complet de statistiques descriptives
    """
    data = request.get_json()
    raw = data.get("numbers", [])

    if not raw:
        return jsonify({"result": None, "error": "Aucune donnée fournie"}), 400

    try:
        nums = [float(x) for x in raw]

        if len(nums) < 1:
            raise ValueError("La liste doit contenir au moins un nombre.")

        # Mode : gestion du cas sans mode unique
        try:
            mode_val = statistics.mode(nums)
        except statistics.StatisticsError:
            mode_val = None  # Plusieurs modes ou aucun

        result = {
            "count":    len(nums),
            "sum":      round(sum(nums), 8),
            "mean":     round(statistics.mean(nums), 8),
            "median":   round(statistics.median(nums), 8),
            "mode":     mode_val,
            "variance": round(statistics.variance(nums), 8) if len(nums) > 1 else 0,
            "stdev":    round(statistics.stdev(nums), 8) if len(nums) > 1 else 0,
            "min":      min(nums),
            "max":      max(nums),
            "range":    round(max(nums) - min(nums), 8),
        }
        return jsonify({"result": result, "error": None})

    except ValueError as e:
        return jsonify({"result": None, "error": str(e)}), 422
    except Exception as e:
        return jsonify({"result": None, "error": f"Erreur : {e}"}), 422


# ─────────────────────────────────────────────
#  Point d'entrée
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import webbrowser
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)