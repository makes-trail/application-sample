import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import Home from './pages/Home';
import SearchBook from './pages/SearchBook';
import FetchBook from './pages/FetchBook';
import NotFound from './pages/NotFound';
import InternalServerError from './pages/InternalServerError';
import ServiceUnavailable from './pages/ServiceUnavailable';

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
            <Route path="/search-book">
              <SearchBook />
            </Route>
            <Route path="/fetch-book/:isbn">
              <FetchBook />
            </Route>
            <Route path="/500">
              <InternalServerError />
            </Route>
            <Route path="/503">
              <ServiceUnavailable />
            </Route>
            <Route path="*">
              <NotFound />
            </Route>
          </Switch>
        </Router>
      </div>
    </div>
  );
}

export default App;
