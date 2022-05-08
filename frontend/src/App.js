/* global chrome */
import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';
export const App = () => {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState('');
  useEffect(() => {
      const queryInfo = {active: true, lastFocusedWindow: true};

      chrome.tabs && chrome.tabs.query(queryInfo, tabs => {
          const url = tabs[0].url;
          setUrl(url);
      });
  }, []);


  function getResult() {

    return fetch("http://127.0.0.1:5000/backend/classifier").then(response => response.json()
    .then(data => {setResult(data.result);}));
  }
  return (
    <div className="App">
        <header className="App-header">
            <img src={logo} className="App-logo" alt="logo"/>
            <p>URL:</p>
            <p>
                {url}
            </p>
            <button onClick={getResult}>Get Result</button>
            <p>Result:</p>
            <p>
                {result}
            </p>
        </header>
    </div>
);
};
/*
function App() {
  const [result, setResult] = useState("Default");
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
}*/
export default App;