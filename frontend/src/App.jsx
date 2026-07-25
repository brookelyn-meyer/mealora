import { useEffect, useState } from "react";

function App() {
  const [groceries, setGroceries] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/groceries")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setGroceries(data);
      });
  }, []);

  return (
    <>
      <h1>🍎 MealOra</h1>

      {groceries.map((grocery) => (
        <div key={grocery.id}>
          <h3>{grocery.name}</h3>
          <p>Quantity: {grocery.quantity}</p>
          <p>Location: {grocery.location}</p>
          <p>Expires: {grocery.expiration_date}</p>
          <hr />
        </div>
      ))}
    </>
  );
}

export default App;