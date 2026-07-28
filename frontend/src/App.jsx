import { useEffect, useState } from "react";
import "./App.css";

// JSX = JavaScript XML
function App() {
  const [groceries, setGroceries] = useState([]);

  const [name, setName] = useState("");
  const [quantity, setQuantity] = useState("");
  const [location, setLocation] = useState("");
  const [expirationDate, setExpirationDate] = useState("");

  // null means we are adding a new grocery.
  // A grocery ID means we are editing that grocery.
  const [editingId, setEditingId] = useState(null);

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

  function clearForm() {
    setName("");
    setQuantity("");
    setLocation("");
    setExpirationDate("");
    setEditingId(null);
  }

  async function handleSubmit(event) {
    event.preventDefault();

    if (editingId === null) {
      await addGrocery();
    } else {
      await updateGrocery();
    }
  }

  async function addGrocery() {
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

    if (!response.ok) {
      console.error("Could not add grocery");
      return;
    }

    const newGrocery = await response.json();

    setGroceries([...groceries, newGrocery]);
    clearForm();
  }

  function startEditing(grocery) {
    setEditingId(grocery.id);
    setName(grocery.name);
    setQuantity(grocery.quantity);
    setLocation(grocery.location);
    setExpirationDate(grocery.expiration_date || "");

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }

  async function updateGrocery() {
    const response = await fetch(
      `http://127.0.0.1:8000/groceries/${editingId}`,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name,
          quantity: quantity,
          location: location,
          expiration_date: expirationDate || null,
        }),
      }
    );

    if (!response.ok) {
      console.error("Could not update grocery");
      return;
    }

    const updatedGrocery = await response.json();

    setGroceries(
      groceries.map((grocery) =>
        grocery.id === editingId ? updatedGrocery : grocery
      )
    );

    clearForm();
  }

  async function deleteGrocery(groceryId) {
    const response = await fetch(
      `http://127.0.0.1:8000/groceries/${groceryId}`,
      {
        method: "DELETE",
      }
    );

    if (!response.ok) {
      console.error("Could not delete grocery");
      return;
    }

    setGroceries(
      groceries.filter((grocery) => grocery.id !== groceryId)
    );

    if (editingId === groceryId) {
      clearForm();
    }
  }

  return (
    <main className="app">
      <header>
        <p className="eyebrow">Your digital pantry</p>
        <h1>MealOra</h1>
        <p>Keep track of what you have before it expires.</p>
      </header>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(event) => setName(event.target.value)}
          required
        />

        <input
          type="text"
          placeholder="Quantity"
          value={quantity}
          onChange={(event) => setQuantity(event.target.value)}
          required
        />

        <input
          type="text"
          placeholder="Location"
          value={location}
          onChange={(event) => setLocation(event.target.value)}
          required
        />

        <input
          type="date"
          value={expirationDate}
          onChange={(event) => setExpirationDate(event.target.value)}
        />

        <button type="submit">
          {editingId === null ? "Add Grocery" : "Save Changes"}
        </button>

        {editingId !== null && (
          <button type="button" onClick={clearForm}>
            Cancel
          </button>
        )}
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

              <button onClick={() => startEditing(grocery)}>
                Edit
              </button>

              <button onClick={() => deleteGrocery(grocery.id)}>
                Delete
              </button>
            </article>
          ))
        )}
      </section>
    </main>
  );
}

export default App;