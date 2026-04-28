const API = "http://127.0.0.1:8000";

// --------------------
// REFRESH UI
// --------------------
async function refresh() {
  const data = await window.api.getTransactions();

  document.getElementById("balance").innerText =
    `💰 Egyenleg: ${data.balance}`;

  const list = document.getElementById("list");
  list.innerHTML = "";

  data.transactions.forEach(t => {
    const li = document.createElement("li");
    li.innerText = `${t.is_income ? "+" : "-"} ${t.amount} Ft | ${t.category}`;
    list.appendChild(li);
  });
}

// --------------------
// ADD TRANSACTION
// --------------------
async function add(isIncome) {
  const amount = document.getElementById("amount").value;
  const category = document.getElementById("category").value;

  console.log("ADDING:", amount, isIncome, category);

  await window.api.addTransaction(
    Number(amount),
    isIncome,
    category || "Egyéb"
  );

  await refresh(); // FONTOS: await
}

// --------------------
// BUTTON WRAPPERS
// --------------------
function addIncome() { add(true); }
function addExpense() { add(false); }

// --------------------
// STATS / CHART DATA
// --------------------
let chartInstance = null;

async function showChart() {
  const data = await window.api.getStats();

  const labels = Object.keys(data);
  const values = Object.values(data);

  const ctx = document.getElementById("chart");

  if (chartInstance) {
    chartInstance.destroy();
  }

  chartInstance = new Chart(ctx, {
    type: "pie",
    data: {
      labels,
      datasets: [{
        data: values
      }]
    }
  });
}

// --------------------
// INIT
// --------------------
window.onload = () => {
  refresh();
};