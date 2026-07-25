import { useEffect } from "react";

function App() {

  useEffect(() => {
    console.log("The page loaded!");
  }, []);

  return (
    <>
      <h1>🍎 MealOra</h1>
      <p>Loading groceries...</p>
    </>
  );
}

export default App;