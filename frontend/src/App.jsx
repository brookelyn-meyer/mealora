import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [groceries, setGroceries] = useState([]);

  useEffect(() => {
  fetch("http://127.0.0.1:8000/groceries")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Could not load groceries");
      }

      return response.json();
    })
    .then((data) => {
      console.log("Groceries received:", data);
      setGroceries(data);
    })
    .catch((error) => {
      console.error("Error loading groceries:", error);
    });
}, []);

  return (
    <main className="app">
      <header>
        <h1>🍎 MealOra</h1>
        <p>Keep track of what you have before it expires.</p>
      </header>

      <section className="grocery-list">
        {groceries.length === 0 ? (
          <p>No groceries found.</p>
        ) : (
          groceries.map((grocery) => (
            <article className="grocery-card" key={grocery.id}>
              <h2>{grocery.name}</h2>
              <p>
                <strong>Quantity:</strong> {grocery.quantity}
              </p>
              <p>
                <strong>Location:</strong> {grocery.location}
              </p>
              <p>
                <strong>Expires:</strong>{" "}
                {grocery.expiration_date || "No expiration date"}
              </p>
            </article>
          ))
        )}
      </section>
    </main>
  );
}

export default App;