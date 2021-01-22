import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const regex = new RegExp(/^\d{13}$/);
  const [isbn, setIsbn] = useState("9784");
  const [errorMessage, setErrorMessage] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!regex.test(isbn)) {
      setErrorMessage("13桁の数字で入力してね");
    } else {
      setErrorMessage("");
    }

    console.log(isbn);
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <div className="content font-yumin">
        <h2>ISBNコードから書籍情報を取得するよ！</h2>
        <form onSubmit={handleSubmit}>
          <label className="font-yumin">ISBN(13桁)
          </label>
          <input
            type="text"
            inputMode="numeric"
            pattern="\d*"
            required
            value={isbn}
            onChange={(e) => setIsbn(e.target.value)}
          />
          <span className="text-error font-yumin">{errorMessage}</span>
          <button type="submit" className="font-yumin">検索</button>
        </form>
      </div>
    </div>
  );
}

export default App;
