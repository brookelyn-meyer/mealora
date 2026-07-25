import { useEffect, useState } from "react";

function App() {
  const [groceries, setGroceries] = useState([]); // gives react a place to remember data

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

      {groceries.map((grocery) => ( // .map() is the react equivalent of for grocery in groceries (python loop!)
        <div key={grocery[0]}>
          <h3>{grocery[1]}</h3>
          <p>{grocery[2]}</p>
          <p>{grocery[3]}</p>
          <p>{grocery[4]}</p>
          <hr />
        </div>
      ))}
    </>
  );
}

export default App;