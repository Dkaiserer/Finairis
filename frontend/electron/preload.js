const { contextBridge } = require("electron");

const API = "http://127.0.0.1:8000";

async function handleResponse(res) {
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`API error: ${res.status} - ${text}`);
  }
  return res.json();
}

contextBridge.exposeInMainWorld("api", {

  // ------------------------
  // GET ALL TRANSACTIONS
  // ------------------------
  getTransactions: async () => {
    try {
      const res = await fetch(`${API}/transactions`);
      return await handleResponse(res);
    } catch (err) {
      console.error("getTransactions error:", err);
      return { balance: 0, transactions: [] };
    }
  },

  // ------------------------
  // ADD TRANSACTION
  // ------------------------
  addTransaction: async (amount, is_income, category) => {
    try {
      console.log("API ADD:", amount, is_income, category);

      const res = await fetch(`${API}/transactions`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          amount,
          is_income,
          category
        })
      });

      return await handleResponse(res);
    } catch (err) {
      console.error("addTransaction error:", err);
      return { status: "error" };
    }
  },

  // ------------------------
  // DELETE
  // ------------------------
  deleteTransaction: async (id) => {
    try {
      const res = await fetch(`${API}/transactions/${id}`, {
        method: "DELETE"
      });

      return await handleResponse(res);
    } catch (err) {
      console.error("deleteTransaction error:", err);
      return { status: "error" };
    }
  },

  // ------------------------
  // STATS
  // ------------------------
  getStats: async () => {
    try {
      const res = await fetch(`${API}/stats`);
      return await handleResponse(res);
    } catch (err) {
      console.error("getStats error:", err);
      return {};
    }
  }

});