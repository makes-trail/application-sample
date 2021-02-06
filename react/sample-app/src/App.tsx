import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import Home from './pages/Home';
import FetchBook from './pages/FetchBook';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <div className="content">
        <Router>
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route path="/fetch-book/:isbn">
              <FetchBook />
            </Route>
            <Route path="*">
              <div>
                <h1>Page Not Found</h1>
              </div>
            </Route>
          </Switch>
        </Router>
      </div>
    </div>
  );
}

export default App;
