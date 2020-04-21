import React from 'react';
import logo from './logo.svg';
import './App.css';
import Flask from './components/Flask';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p><b>JacksonLabs</b> fullstack boilerplate</p>
        <br />
        <small>You are running this application in <b>{process.env.NODE_ENV}</b> mode.</small>
        <Flask />
      </header>
    </div>
  );
}

export default App;
