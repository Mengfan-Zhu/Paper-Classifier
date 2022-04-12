import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';

function App() {
  const [result, setResult] = useState("Defalut");
  function getResult() {
    return fetch("http://127.0.0.1:5000/backend/classifier").then(response => response.json()
    .then(data => {setResult(data.result);}));
  }

  return (
    <div className="App">
      <header className="App-header">
        <button onClick={getResult}>Get Result</button>
        <p> Result is : {result} </p>
      </header>
    </div>
  );
}

export default App;
