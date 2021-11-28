import './App.css';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import logo from './logo.svg';

import Home from './pages/Home';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <h1>Cognito認証サンプル</h1>
      <Router>
        <Switch>
          <Route exact path="/" component={Home} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
