import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [groceries, setGroceries] = useState([]);
  const [name, setName] = useState("");
  const [quantity, setQuantity] = useState("");
  const [location, setLocation] = useState("");
  const [expirationDate, setExpirationDate] = useState("");

async function addGrocery(event) {
  event.preventDefault();

  const response = await fetch("http://127.0.0.1:8000/groceries", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: name,
      quantity: quantity,
      location: location,
      expiration_date: expirationDate || null,
    }),
  });

  const newGrocery = await response.json();

  setGroceries([...groceries, newGrocery]);

  setName("");
  setQuantity("");
  setLocation("");
  setExpirationDate("");
}






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

    <form onSubmit={addGrocery}>
  <input
    type="text"
    placeholder="Name"
    value={name}
    onChange={(event) => setName(event.target.value)}
  />

  <input
    type="text"
    placeholder="Quantity"
    value={quantity}
    onChange={(event) => setQuantity(event.target.value)}
  />

  <input
    type="text"
    placeholder="Location"
    value={location}
    onChange={(event) => setLocation(event.target.value)}
  />

  <input
    type="date"
    value={expirationDate}
    onChange={(event) => setExpirationDate(event.target.value)}
  />

  <button type="submit">
    Add Grocery
  </button>
</form>

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