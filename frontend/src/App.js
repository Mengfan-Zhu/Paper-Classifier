/* global chrome */
//import requests;
import ReactTable from "react-table-6";  
import 'react-table-6/react-table.css';
import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';

export const App = () => {
  const [url, setUrl] = useState('');
  const [results, setResults] = useState([]);
  //get chrome tab url
  useEffect(() => {
    const queryInfo = {active: true, lastFocusedWindow: true};
    chrome.tabs && chrome.tabs.query(queryInfo, tabs => {
        const url = tabs[0].url;
        setUrl(url);
    });
  }, []);

  //make fetch call
  function getResult() {
    
    return fetch('http://127.0.0.1:5000/backend/classifier', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({url})
      }).then(res=>res.json()).then(data=>{
        var result_list = []
        for (var topic in data) {
            result_list.push({topic:topic, papers:data[topic]})
        }
        setResults(result_list)
        })
  }
  return (
    <div className="App">
            <h2>Paper Classifier</h2>
            <button onClick={getResult}>Get Result</button>
            <ReactTable NoDataComponent={() => null}
                data={results}
                columns={[
                    {
                      Header: "Topic",
                      accessor: "topic"
                    }]}
                minRows={0}
                defaultPageSize={10}
                className="-striped -highlight"
                showPagination={false}
                getTdProps={(state, rowInfo, col, instance) => {
                return {
                    onClick: (e) => {
                    if (col.Header === undefined) {
                        const { expanded } = state;
                        const path = rowInfo.nestingPath[0];
                        const diff = { [path]: expanded[path] ? false : true };
                        instance.setState({
                        expanded: {
                            ...expanded,
                            ...diff
                        }
                        });
                    } 
                    }
                };
                }}
                SubComponent={(row) => {
                return (
                    <ul>
                        {row.original.papers.map(paper=><li><a href = {paper.link}  target="_blank" rel="noreferrer noopener">{paper.title}</a></li>)}
                    </ul>
                );
                }}
            />
    </div>
);
};
export default App;