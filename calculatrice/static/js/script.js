/**
 * Calculatrice Scientifique v2.0 — Script principal
 * Nouvelles fonctionnalités : mode 2nd, fonctions hyperboliques,
 * puissances, racine cubique, combinatoire, touche ±
 */

"use strict";

/* ═══════════════════════════════════════════
   1. GESTION DES ONGLETS
   ═══════════════════════════════════════════ */

document.querySelectorAll(".tab-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
    document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
    btn.classList.add("active");
    document.getElementById(btn.dataset.tab).classList.add("active");
  });
});


/* ═══════════════════════════════════════════
   2. CALCULATRICE SCIENTIFIQUE
   ═══════════════════════════════════════════ */

let calcExpression = "";
let calcHistory    = [];
let calcMode       = "deg";
let mode2nd        = false;   // Mode fonction inverse actif

const displayInput  = document.getElementById("display-input");
const displayResult = document.getElementById("display-result");
const btn2nd        = document.getElementById("btn-2nd");
const calcGrid      = document.querySelector(".calc-grid");

// ── Mode DEG / RAD ──
document.querySelectorAll(".mode-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".mode-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    calcMode = btn.dataset.mode;
  });
});

// ── Bouton 2nd : bascule les fonctions inverses ──
btn2nd.addEventListener("click", () => {
  mode2nd = !mode2nd;
  btn2nd.classList.toggle("active", mode2nd);
  calcGrid.classList.toggle("mode-2nd", mode2nd);
});

// ── Clics sur les touches de la calculatrice ──
document.querySelectorAll(".calc-key").forEach(btn => {
  btn.addEventListener("click", () => {
    // Si mode 2nd actif et que la touche a une valeur alternative
    const value = (mode2nd && btn.dataset.alt) ? btn.dataset.alt : btn.dataset.value;

    // Désactiver le mode 2nd après usage (comme sur une vraie calc)
    if (mode2nd && btn.dataset.alt) {
      mode2nd = false;
      btn2nd.classList.remove("active");
      calcGrid.classList.remove("mode-2nd");
    }

    handleCalcKey(value);
  });
});

// ── Saisie clavier ──
document.addEventListener("keydown", e => {
  const panel = document.querySelector(".tab-panel.active");
  if (!panel || panel.id !== "tab-calc") return;

  const key = e.key;
  if ("0123456789.+-*/%()".includes(key)) { handleCalcKey(key); return; }
  if (key === "Enter" || key === "=")      { handleCalcKey("="); return; }
  if (key === "Backspace")                 { handleCalcKey("⌫"); return; }
  if (key === "Escape")                    { handleCalcKey("C"); return; }
  if (key === "^")                         { handleCalcKey("^"); return; }
});

/**
 * Traite une valeur de touche.
 * Cas spéciaux : C, ⌫, =, +/-, et toutes les fonctions
 */
function handleCalcKey(value) {
  switch (value) {
    case "C":
      calcExpression = "";
      displayInput.textContent  = "";
      displayResult.textContent = "0";
      displayResult.classList.remove("error");
      break;

    case "⌫":
      calcExpression = calcExpression.slice(0, -1);
      displayInput.textContent = calcExpression;
      break;

    case "=":
      if (!calcExpression.trim()) return;
      evaluateExpression();
      break;

    // Touche ± : inverse le signe du dernier nombre
    case "+/-":
      if (calcExpression === "") return;
      if (calcExpression.startsWith("-")) {
        calcExpression = calcExpression.slice(1);
      } else {
        calcExpression = "-" + calcExpression;
      }
      displayInput.textContent = calcExpression;
      break;

    default:
      calcExpression += value;
      displayInput.textContent = calcExpression;
  }
}

/**
 * Envoie l'expression au backend Flask et affiche le résultat.
 */
async function evaluateExpression() {
  displayResult.textContent = "…";
  displayResult.classList.remove("error");

  try {
    const response = await fetch("/api/calc", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ expression: calcExpression, mode: calcMode })
    });

    const data = await response.json();

    if (data.error) {
      displayResult.textContent = data.error;
      displayResult.classList.add("error");
    } else {
      const result = formatNumber(data.result);
      displayResult.textContent = result;
      addToHistory(calcExpression, result);
      calcExpression = String(data.result);
    }
  } catch {
    displayResult.textContent = "Erreur réseau";
    displayResult.classList.add("error");
  }
}

function formatNumber(n) {
  if (Number.isInteger(n) && Math.abs(n) < 1e15) return String(n);
  if (Math.abs(n) < 1e-7 || Math.abs(n) > 1e12) return n.toExponential(6);
  return parseFloat(n.toPrecision(10)).toString();
}

function addToHistory(expr, result) {
  calcHistory.unshift({ expr, result });
  if (calcHistory.length > 20) calcHistory.pop();
  renderHistory();
}

function renderHistory() {
  const list = document.getElementById("history-list");
  list.innerHTML = calcHistory.map(h => `
    <div class="history-item" onclick="reuseHistory('${h.result}')">
      <span class="history-expr">${escapeHtml(h.expr)}</span>
      <span class="history-res">${escapeHtml(h.result)}</span>
    </div>
  `).join("");
}

function reuseHistory(val) {
  calcExpression = val;
  displayInput.textContent = val;
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}


/* ═══════════════════════════════════════════
   3. MODULE MATRICES
   ═══════════════════════════════════════════ */

let matrixSizeA = 2;
let matrixSizeB = 2;

const sizeSelectA = document.getElementById("size-a");
const sizeSelectB = document.getElementById("size-b");

sizeSelectA.addEventListener("change", () => {
  matrixSizeA = parseInt(sizeSelectA.value);
  buildMatrixGrid("matrix-a-grid", matrixSizeA);
});

sizeSelectB.addEventListener("change", () => {
  matrixSizeB = parseInt(sizeSelectB.value);
  buildMatrixGrid("matrix-b-grid", matrixSizeB);
});

function buildMatrixGrid(containerId, n) {
  const container = document.getElementById(containerId);
  container.style.gridTemplateColumns = `repeat(${n}, 1fr)`;
  container.innerHTML = "";

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const input = document.createElement("input");
      input.type        = "number";
      input.className   = "matrix-cell";
      input.value       = (i === j) ? "1" : "0";
      input.dataset.row = i;
      input.dataset.col = j;
      container.appendChild(input);
    }
  }
}

buildMatrixGrid("matrix-a-grid", 2);
buildMatrixGrid("matrix-b-grid", 2);

function readMatrix(containerId) {
  const container = document.getElementById(containerId);
  const cells = container.querySelectorAll(".matrix-cell");
  const n = Math.sqrt(cells.length);
  const matrix = Array.from({ length: n }, () => Array(n).fill(0));
  cells.forEach(cell => {
    matrix[parseInt(cell.dataset.row)][parseInt(cell.dataset.col)] = parseFloat(cell.value) || 0;
  });
  return matrix;
}

async function matrixOperation(op) {
  const matrixA = readMatrix("matrix-a-grid");
  const matrixB = ["add", "multiply"].includes(op) ? readMatrix("matrix-b-grid") : null;
  const resultDisplay = document.getElementById("matrix-result");
  resultDisplay.textContent = "calcul en cours…";

  try {
    const response = await fetch("/api/matrix", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ operation: op, matrix_a: matrixA, matrix_b: matrixB })
    });
    const data = await response.json();

    if (data.error) {
      resultDisplay.textContent = `⚠ ${data.error}`;
      resultDisplay.style.color = "var(--red-err)";
    } else {
      resultDisplay.style.color = "";
      if (data.type === "scalar") {
        resultDisplay.textContent = `det(A) = ${data.result}`;
      } else {
        resultDisplay.textContent = formatMatrixDisplay(data.result);
      }
    }
  } catch {
    resultDisplay.textContent = "⚠ Erreur réseau";
    resultDisplay.style.color = "var(--red-err)";
  }
}

function formatMatrixDisplay(matrix) {
  const cols = matrix[0].length;
  const widths = Array.from({ length: cols }, (_, j) =>
    Math.max(...matrix.map(row => String(row[j]).length))
  );
  return matrix.map(row =>
    "[ " + row.map((v, j) => String(v).padStart(widths[j])).join("  ") + " ]"
  ).join("\n");
}

document.querySelectorAll(".matrix-op-btn").forEach(btn => {
  btn.addEventListener("click", () => matrixOperation(btn.dataset.op));
});


/* ═══════════════════════════════════════════
   4. MODULE STATISTIQUES
   ═══════════════════════════════════════════ */

async function computeStats() {
  const raw = document.getElementById("stats-input").value.trim();
  if (!raw) return;

  const numbers = raw.split(/[\s,;]+/).filter(Boolean).map(Number);

  if (numbers.some(isNaN)) {
    showStatsError("Valeurs non numériques détectées.");
    return;
  }

  const container = document.getElementById("stats-results");
  container.innerHTML = `<div class="stat-item" style="grid-column:span 2">
    <span class="stat-key">calcul…</span></div>`;

  try {
    const response = await fetch("/api/stats", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ numbers })
    });
    const data = await response.json();

    if (data.error) {
      showStatsError(data.error);
    } else {
      renderStats(data.result);
    }
  } catch {
    showStatsError("Erreur réseau");
  }
}

function showStatsError(msg) {
  document.getElementById("stats-results").innerHTML = `
    <div class="stat-item" style="grid-column:span 2; color:var(--red-err)">${msg}</div>`;
}

function renderStats(stats) {
  const labels = {
    count: "N", sum: "Somme", mean: "Moyenne", median: "Médiane",
    mode: "Mode", variance: "Variance", stdev: "Écart-type",
    min: "Min", max: "Max", range: "Étendue"
  };
  const container = document.getElementById("stats-results");
  container.innerHTML = Object.entries(labels).map(([key, label]) => `
    <div class="stat-item">
      <span class="stat-key">${label}</span>
      <span class="stat-val">${stats[key] ?? "—"}</span>
    </div>`).join("");
}

document.getElementById("btn-stats-calc").addEventListener("click", computeStats);

