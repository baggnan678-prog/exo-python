# CalcSci — Calculatrice Scientifique

**Projet Génie Logiciel — UTM Burkina Faso**
Stack : Python 3 · Flask · HTML/CSS/JS · NumPy

---

## Structure du projet

```
calculatrice/
├── app.py                  ← Backend Flask (API REST)
├── requirements.txt        ← Dépendances Python
├── templates/
│   └── index.html          ← Interface principale (Jinja2)
└── static/
    ├── css/
    │   └── style.css       ← Styles (thème phosphore sombre)
    └── js/
        └── script.js       ← Logique frontend (fetch API)
```

---

## Installation

```bash
# 1. Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le serveur
python app.py
```

Le serveur démarre sur `http://localhost:5000`

---

## Fonctionnalités

### Onglet CALCUL
- Opérations : `+` `-` `*` `/` `%` `^`
- Fonctions : `sin` `cos` `tan` `asin` `acos` `atan`
- Fonctions avancées : `sqrt` `log` `ln` `abs` `factorial` `ceil` `floor`
- Constantes : `pi` `e`
- Modes : DEG / RAD
- Historique des 20 derniers calculs
- Saisie clavier complète

### Onglet MATRICES
- Tailles : 2×2, 3×3, 4×4
- Opérations : Addition (A+B), Multiplication (A·B)
- Sur A seule : Transposée (Aᵀ), Déterminant (det A), Inverse (A⁻¹)

### Onglet STATISTIQUES
- Entrée libre (espace, virgule, point-virgule, retour à la ligne)
- Résultats : N, Somme, Moyenne, Médiane, Mode, Variance,
  Écart-type, Min, Max, Étendue

---

## API REST

| Endpoint      | Méthode | Corps JSON                                              |
|---------------|---------|--------------------------------------------------------|
| `/api/calc`   | POST    | `{"expression": "sin(45)+sqrt(16)", "mode": "deg"}`    |
| `/api/matrix` | POST    | `{"operation": "det", "matrix_a": [[1,2],[3,4]]}`      |
| `/api/stats`  | POST    | `{"numbers": [4, 8, 15, 16, 23, 42]}`                  |

---

## Améliorations possibles (niveaux suivants)
- Grapheur de fonctions (Matplotlib → image ou Chart.js)
- Intégration numérique (scipy.integrate)
- Résolution d'équations (sympy)
- Export PDF des résultats
- Base de données pour l'historique (SQLite)
