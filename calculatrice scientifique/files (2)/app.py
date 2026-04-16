from flask import Flask, request, jsonify, render_template
import numpy as np
import scipy.stats as stats
from scipy import linalg
import sympy as sp
import json, math, io, base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# ── BASIC CALCULATION ──────────────────────────────────────────────────────────
@app.route('/api/calc', methods=['POST'])
def calculate():
    try:
        expr = request.json.get('expression', '')
        x = sp.Symbol('x')
        safe_ns = {
            'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
            'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
            'sinh': sp.sinh, 'cosh': sp.cosh, 'tanh': sp.tanh,
            'log': sp.log, 'ln': sp.log, 'log10': lambda a: sp.log(a, 10),
            'log2': lambda a: sp.log(a, 2),
            'sqrt': sp.sqrt, 'exp': sp.exp, 'abs': sp.Abs,
            'pi': sp.pi, 'e': sp.E, 'inf': sp.oo,
            'factorial': sp.factorial, 'gcd': sp.gcd, 'lcm': sp.lcm,
            'ceiling': sp.ceiling, 'floor': sp.floor,
            'x': x
        }
        result = sp.sympify(expr, locals=safe_ns)
        evaled = sp.N(result, 15)
        return jsonify({'result': str(evaled), 'symbolic': str(result)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ── FUNCTION PLOT ──────────────────────────────────────────────────────────────
@app.route('/api/plot', methods=['POST'])
def plot():
    try:
        data = request.json
        functions = data.get('functions', [])
        x_min = float(data.get('x_min', -10))
        x_max = float(data.get('x_max', 10))
        points = int(data.get('points', 1000))

        x_sym = sp.Symbol('x')
        safe_ns = {
            'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
            'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
            'sinh': sp.sinh, 'cosh': sp.cosh, 'tanh': sp.tanh,
            'log': sp.log, 'ln': sp.log, 'log10': lambda a: sp.log(a, 10),
            'log2': lambda a: sp.log(a, 2),
            'sqrt': sp.sqrt, 'exp': sp.exp, 'abs': sp.Abs,
            'pi': sp.pi, 'e': sp.E, 'x': x_sym
        }

        fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0d0d1a')
        ax.set_facecolor('#0d0d1a')
        ax.grid(True, color='#1e1e3a', linewidth=0.8, alpha=0.7)
        ax.spines['bottom'].set_color('#00f5ff')
        ax.spines['left'].set_color('#00f5ff')
        ax.spines['top'].set_color('#1e1e3a')
        ax.spines['right'].set_color('#1e1e3a')
        ax.tick_params(colors='#a0a0c0', labelsize=10)
        ax.axhline(0, color='#00f5ff', linewidth=0.8, alpha=0.5)
        ax.axvline(0, color='#00f5ff', linewidth=0.8, alpha=0.5)

        colors = ['#00f5ff', '#ff6b9d', '#ffd700', '#7cff7c', '#ff8c42', '#c77dff']
        x_vals = np.linspace(x_min, x_max, points)

        for i, func_str in enumerate(functions):
            try:
                expr = sp.sympify(func_str, locals=safe_ns)
                f_lamb = sp.lambdify(x_sym, expr, modules=['numpy'])
                y_vals = f_lamb(x_vals).astype(float)
                y_vals = np.where(np.abs(y_vals) > 1e10, np.nan, y_vals)
                color = colors[i % len(colors)]
                ax.plot(x_vals, y_vals, color=color, linewidth=2.2,
                        label=f'f(x) = {func_str}', alpha=0.95)
            except Exception as fe:
                pass

        ax.legend(facecolor='#0d0d1a', edgecolor='#00f5ff',
                  labelcolor='#e0e0ff', fontsize=10)
        ax.set_xlabel('x', color='#a0a0c0', fontsize=12)
        ax.set_ylabel('f(x)', color='#a0a0c0', fontsize=12)
        ax.set_title('Tracé de Fonction', color='#00f5ff', fontsize=14, pad=12)
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=130, bbox_inches='tight',
                    facecolor='#0d0d1a')
        plt.close()
        buf.seek(0)
        img_b64 = base64.b64encode(buf.read()).decode()
        return jsonify({'image': img_b64})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ── MATRIX ────────────────────────────────────────────────────────────────────
@app.route('/api/matrix', methods=['POST'])
def matrix_ops():
    try:
        data = request.json
        op = data.get('operation')
        A_raw = data.get('A')
        B_raw = data.get('B')

        A = np.array(A_raw, dtype=complex)

        results = {}

        if op == 'info':
            results['shape'] = list(A.shape)
            results['rank'] = int(np.linalg.matrix_rank(A.real))
            results['trace'] = _fmt(np.trace(A))
            if A.shape[0] == A.shape[1]:
                results['determinant'] = _fmt(np.linalg.det(A))
                try:
                    results['inverse'] = _mat(np.linalg.inv(A))
                except:
                    results['inverse'] = 'Singulière'
                eigenvalues, eigenvectors = np.linalg.eig(A)
                results['eigenvalues'] = [_fmt(v) for v in eigenvalues]
                results['eigenvectors'] = _mat(eigenvectors)
                U, s, Vh = np.linalg.svd(A)
                results['singular_values'] = [_fmt(v) for v in s]
                results['norm_frobenius'] = _fmt(np.linalg.norm(A, 'fro'))
                results['norm_2'] = _fmt(np.linalg.norm(A, 2))

        elif op == 'add' and B_raw:
            B = np.array(B_raw, dtype=complex)
            results['result'] = _mat(A + B)
        elif op == 'subtract' and B_raw:
            B = np.array(B_raw, dtype=complex)
            results['result'] = _mat(A - B)
        elif op == 'multiply' and B_raw:
            B = np.array(B_raw, dtype=complex)
            results['result'] = _mat(A @ B)
        elif op == 'power':
            n = int(data.get('n', 2))
            results['result'] = _mat(np.linalg.matrix_power(A.astype(int), n))
        elif op == 'transpose':
            results['result'] = _mat(A.T)
        elif op == 'rref':
            M = sp.Matrix(A_raw)
            rref, pivots = M.rref()
            results['result'] = [[str(v) for v in row] for row in rref.tolist()]
            results['pivots'] = list(pivots)
        elif op == 'cholesky':
            L = np.linalg.cholesky(A.real)
            results['L'] = _mat(L)
        elif op == 'lu':
            P, L, U = linalg.lu(A)
            results['P'] = _mat(P)
            results['L'] = _mat(L)
            results['U'] = _mat(U)
        elif op == 'qr':
            Q, R = np.linalg.qr(A)
            results['Q'] = _mat(Q)
            results['R'] = _mat(R)

        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def _fmt(v):
    v = complex(v)
    if abs(v.imag) < 1e-10:
        r = v.real
        return int(r) if abs(r - round(r)) < 1e-10 else round(r, 8)
    return f"{round(v.real,6)}+{round(v.imag,6)}j"

def _mat(M):
    return [[_fmt(M[i,j]) for j in range(M.shape[1])] for i in range(M.shape[0])]

# ── STATISTICS ────────────────────────────────────────────────────────────────
@app.route('/api/stats', methods=['POST'])
def statistics():
    try:
        data = request.json
        dataset = np.array(data.get('data', []), dtype=float)
        op = data.get('operation', 'descriptive')

        if op == 'descriptive':
            q1, q2, q3 = np.percentile(dataset, [25, 50, 75])
            desc = stats.describe(dataset)
            return jsonify({
                'n': int(desc.nobs),
                'mean': round(float(desc.mean), 8),
                'median': round(float(np.median(dataset)), 8),
                'mode': round(float(stats.mode(dataset, keepdims=True).mode[0]), 8),
                'std': round(float(np.std(dataset, ddof=1)), 8),
                'variance': round(float(np.var(dataset, ddof=1)), 8),
                'min': float(dataset.min()),
                'max': float(dataset.max()),
                'range': float(dataset.max() - dataset.min()),
                'Q1': round(float(q1), 8),
                'Q2': round(float(q2), 8),
                'Q3': round(float(q3), 8),
                'IQR': round(float(q3 - q1), 8),
                'skewness': round(float(desc.skewness), 8),
                'kurtosis': round(float(desc.kurtosis), 8),
                'sem': round(float(stats.sem(dataset)), 8),
                'cv': round(float(np.std(dataset, ddof=1)/np.mean(dataset)*100), 4),
            })

        elif op == 'distribution_plot':
            fig, axes = plt.subplots(1, 2, figsize=(12, 5), facecolor='#0d0d1a')
            for ax in axes:
                ax.set_facecolor('#0d0d1a')
                ax.tick_params(colors='#a0a0c0')
                for sp_ in ax.spines.values(): sp_.set_color('#1e1e3a')

            axes[0].hist(dataset, bins='auto', color='#00f5ff', alpha=0.75,
                         edgecolor='#0d0d1a', linewidth=0.5)
            axes[0].set_title('Histogramme', color='#00f5ff', fontsize=13)
            axes[0].set_xlabel('Valeurs', color='#a0a0c0')
            axes[0].set_ylabel('Fréquence', color='#a0a0c0')

            axes[1].boxplot(dataset, patch_artist=True,
                            boxprops=dict(facecolor='#00f5ff', alpha=0.5, color='#00f5ff'),
                            medianprops=dict(color='#ffd700', linewidth=2),
                            whiskerprops=dict(color='#a0a0c0'),
                            capprops=dict(color='#a0a0c0'),
                            flierprops=dict(marker='o', color='#ff6b9d', alpha=0.7))
            axes[1].set_title('Boîte à moustaches', color='#00f5ff', fontsize=13)
            axes[1].tick_params(colors='#a0a0c0')

            plt.tight_layout()
            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=130, bbox_inches='tight', facecolor='#0d0d1a')
            plt.close(); buf.seek(0)
            return jsonify({'image': base64.b64encode(buf.read()).decode()})

        elif op == 'normality':
            stat_sw, p_sw = stats.shapiro(dataset)
            stat_ks, p_ks = stats.kstest(dataset, 'norm',
                args=(np.mean(dataset), np.std(dataset)))
            return jsonify({
                'shapiro_wilk': {'statistic': round(float(stat_sw),6), 'p_value': round(float(p_sw),6)},
                'kolmogorov_smirnov': {'statistic': round(float(stat_ks),6), 'p_value': round(float(p_ks),6)},
                'is_normal_5pct': bool(p_sw > 0.05)
            })

        elif op == 'confidence_interval':
            conf = float(data.get('confidence', 0.95))
            n = len(dataset)
            m = np.mean(dataset)
            se = stats.sem(dataset)
            ci = stats.t.interval(conf, df=n-1, loc=m, scale=se)
            return jsonify({
                'mean': round(float(m), 8),
                'lower': round(float(ci[0]), 8),
                'upper': round(float(ci[1]), 8),
                'confidence': conf
            })

        elif op == 'ttest_one':
            mu0 = float(data.get('mu', 0))
            t_stat, p_val = stats.ttest_1samp(dataset, mu0)
            return jsonify({'t_statistic': round(float(t_stat),6),
                           'p_value': round(float(p_val),6),
                           'significant': bool(p_val < 0.05)})

        elif op == 'ttest_two':
            dataset2 = np.array(data.get('data2', []), dtype=float)
            t_stat, p_val = stats.ttest_ind(dataset, dataset2)
            return jsonify({'t_statistic': round(float(t_stat),6),
                           'p_value': round(float(p_val),6),
                           'significant': bool(p_val < 0.05)})

        elif op == 'correlation':
            dataset2 = np.array(data.get('data2', []), dtype=float)
            r, p = stats.pearsonr(dataset, dataset2)
            rho, p2 = stats.spearmanr(dataset, dataset2)
            return jsonify({
                'pearson_r': round(float(r), 8),
                'pearson_p': round(float(p), 8),
                'spearman_rho': round(float(rho), 8),
                'spearman_p': round(float(p2), 8)
            })

        elif op == 'regression':
            x_data = np.array(data.get('x_data', []), dtype=float)
            slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, dataset)
            fig, ax = plt.subplots(figsize=(9, 5), facecolor='#0d0d1a')
            ax.set_facecolor('#0d0d1a')
            ax.scatter(x_data, dataset, color='#00f5ff', alpha=0.8, s=50, zorder=5)
            x_line = np.linspace(x_data.min(), x_data.max(), 200)
            ax.plot(x_line, slope*x_line + intercept, color='#ff6b9d', linewidth=2.5,
                    label=f'y = {slope:.4f}x + {intercept:.4f}')
            ax.legend(facecolor='#0d0d1a', edgecolor='#00f5ff', labelcolor='#e0e0ff')
            ax.tick_params(colors='#a0a0c0')
            for sp_ in ax.spines.values(): sp_.set_color('#1e1e3a')
            ax.set_title('Régression Linéaire', color='#00f5ff', fontsize=13)
            plt.tight_layout()
            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=130, bbox_inches='tight', facecolor='#0d0d1a')
            plt.close(); buf.seek(0)
            return jsonify({
                'slope': round(float(slope),8),
                'intercept': round(float(intercept),8),
                'r_squared': round(float(r_value**2),8),
                'p_value': round(float(p_value),8),
                'std_err': round(float(std_err),8),
                'image': base64.b64encode(buf.read()).decode()
            })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ── PROBABILITY ───────────────────────────────────────────────────────────────
@app.route('/api/probability', methods=['POST'])
def probability():
    try:
        data = request.json
        dist = data.get('distribution')
        action = data.get('action', 'pdf')
        x_val = float(data.get('x', 0))
        params = data.get('params', {})

        dist_map = {
            'normal': (stats.norm, ['loc', 'scale']),
            'binomial': (stats.binom, ['n', 'p']),
            'poisson': (stats.poisson, ['mu']),
            'exponential': (stats.expon, ['loc', 'scale']),
            'uniform': (stats.uniform, ['loc', 'scale']),
            'gamma': (stats.gamma, ['a', 'loc', 'scale']),
            'beta': (stats.beta, ['a', 'b', 'loc', 'scale']),
            'chi2': (stats.chi2, ['df']),
            't': (stats.t, ['df']),
            'f': (stats.f, ['dfn', 'dfd']),
            'geometric': (stats.geom, ['p']),
            'hypergeometric': (stats.hypergeom, ['M', 'n', 'N']),
            'negative_binomial': (stats.nbinom, ['n', 'p']),
            'weibull': (stats.weibull_min, ['c', 'loc', 'scale']),
            'lognormal': (stats.lognorm, ['s', 'loc', 'scale']),
        }

        if dist not in dist_map:
            return jsonify({'error': f'Distribution inconnue: {dist}'}), 400

        dist_obj, param_keys = dist_map[dist]
        kw = {k: float(params[k]) for k in param_keys if k in params}
        d = dist_obj(**kw)

        result = {}
        if action == 'pdf':
            result['value'] = round(float(d.pdf(x_val) if hasattr(d, 'pdf') else d.pmf(x_val)), 10)
            result['type'] = 'PDF' if hasattr(d, 'pdf') else 'PMF'
        elif action == 'cdf':
            result['value'] = round(float(d.cdf(x_val)), 10)
        elif action == 'ppf':
            result['value'] = round(float(d.ppf(x_val)), 10)
        elif action == 'stats_dist':
            m, v, s, k = d.stats(moments='mvsk')
            result = {
                'mean': round(float(m), 8),
                'variance': round(float(v), 8),
                'std': round(float(np.sqrt(v)), 8),
                'skewness': round(float(s), 8),
                'kurtosis': round(float(k), 8)
            }
        elif action == 'plot':
            fig, axes = plt.subplots(1, 2, figsize=(12, 5), facecolor='#0d0d1a')
            is_discrete = not hasattr(d, 'pdf')
            mean, var = d.stats()
            std = float(np.sqrt(var))
            mean = float(mean)

            for ax in axes:
                ax.set_facecolor('#0d0d1a')
                ax.tick_params(colors='#a0a0c0')
                for sp_ in ax.spines.values(): sp_.set_color('#1e1e3a')
                ax.grid(True, color='#1e1e3a', alpha=0.5)

            if is_discrete:
                x_range = np.arange(max(0, int(mean - 4*std)), int(mean + 4*std) + 2)
                pmf_vals = d.pmf(x_range)
                axes[0].bar(x_range, pmf_vals, color='#00f5ff', alpha=0.8, edgecolor='#0d0d1a')
                axes[0].set_title('PMF', color='#00f5ff')
                axes[1].step(x_range, d.cdf(x_range), color='#ff6b9d', linewidth=2)
                axes[1].set_title('CDF', color='#00f5ff')
            else:
                x_range = np.linspace(d.ppf(0.001), d.ppf(0.999), 500)
                axes[0].fill_between(x_range, d.pdf(x_range), alpha=0.3, color='#00f5ff')
                axes[0].plot(x_range, d.pdf(x_range), color='#00f5ff', linewidth=2.5)
                axes[0].set_title('PDF', color='#00f5ff')
                axes[1].plot(x_range, d.cdf(x_range), color='#ff6b9d', linewidth=2.5)
                axes[1].set_title('CDF', color='#00f5ff')

            for ax in axes:
                ax.set_xlabel('x', color='#a0a0c0')
                ax.set_ylabel('Probabilité', color='#a0a0c0')

            plt.suptitle(f'Distribution {dist.capitalize()}', color='#00f5ff',
                         fontsize=14, y=1.01)
            plt.tight_layout()
            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=130, bbox_inches='tight', facecolor='#0d0d1a')
            plt.close(); buf.seek(0)
            result['image'] = base64.b64encode(buf.read()).decode()

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ── CALCULUS ──────────────────────────────────────────────────────────────────
@app.route('/api/calculus', methods=['POST'])
def calculus():
    try:
        data = request.json
        op = data.get('operation')
        expr_str = data.get('expression', '')
        x = sp.Symbol('x')
        safe_ns = {
            'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
            'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
            'sinh': sp.sinh, 'cosh': sp.cosh, 'tanh': sp.tanh,
            'log': sp.log, 'ln': sp.log, 'exp': sp.exp,
            'sqrt': sp.sqrt, 'abs': sp.Abs, 'pi': sp.pi, 'e': sp.E, 'x': x
        }
        expr = sp.sympify(expr_str, locals=safe_ns)

        if op == 'derivative':
            n = int(data.get('n', 1))
            result = sp.diff(expr, x, n)
            return jsonify({'result': str(result), 'latex': sp.latex(result)})

        elif op == 'integral':
            a = data.get('a'); b = data.get('b')
            if a is not None and b is not None:
                result = sp.integrate(expr, (x, sp.sympify(str(a)), sp.sympify(str(b))))
                num = sp.N(result, 12)
                return jsonify({'result': str(result), 'numeric': str(num), 'latex': sp.latex(result)})
            else:
                result = sp.integrate(expr, x)
                return jsonify({'result': str(result) + ' + C', 'latex': sp.latex(result) + ' + C'})

        elif op == 'limit':
            point = data.get('point', '0')
            direction = data.get('direction', '+-')
            dir_map = {'left': '-', 'right': '+', '+-': '+-'}
            result = sp.limit(expr, x, sp.sympify(point), dir_map.get(direction, '+-'))
            return jsonify({'result': str(result), 'latex': sp.latex(result)})

        elif op == 'series':
            n = int(data.get('n', 6))
            point = sp.sympify(data.get('point', '0'))
            result = sp.series(expr, x, point, n)
            return jsonify({'result': str(result), 'latex': sp.latex(result)})

        elif op == 'solve':
            solutions = sp.solve(expr, x)
            return jsonify({'solutions': [str(s) for s in solutions],
                           'numeric': [str(sp.N(s,10)) for s in solutions]})

        elif op == 'simplify':
            result = sp.simplify(expr)
            return jsonify({'result': str(result), 'latex': sp.latex(result)})

        elif op == 'factor':
            result = sp.factor(expr)
            return jsonify({'result': str(result), 'latex': sp.latex(result)})

        elif op == 'expand':
            result = sp.expand(expr)
            return jsonify({'result': str(result), 'latex': sp.latex(result)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
