import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Book from './Book';

function App() {
  interface BookInfo {
    isbn: string;
    title: string;
    author: string;
    publisher: string;
    cover: string;
  }

  const regex = new RegExp(/^\d{13}$/);
  const [isbn, setIsbn] = useState<string>("9784");
  const [errorMessage, setErrorMessage] = useState<string>("");
  const [isPending, setIsPending] = useState<boolean>(false);
  const [isNoData, setIsNoData] = useState<boolean>(false);
  const [bookInfo, setBookInfo] = useState<BookInfo>();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!regex.test(isbn)) {
      setErrorMessage("13桁の数字で入力してね");
      return;
    }

    setErrorMessage("");
    setIsPending(true);
    setIsNoData(false);
    setBookInfo(undefined);
    const url = new URL(`${process.env.REACT_APP_SERVERLESS_ENDPOINT}/fetch-isbn-summary`);
    const params = new URLSearchParams();
    params.append("isbn", isbn);
    url.search = params.toString();

    setTimeout(
      async () => {
        const res = await fetch(url.toString());
        if (res.status !== 200) {
          setIsPending(false);
          setIsNoData(true);
          return;
        }
        const data: Array<BookInfo> = await res.json();
        if (data.length === 0) {
          setIsPending(false);
          setIsNoData(true);
          return;
        }
        setBookInfo(data[0]);
        setIsPending(false);
      }, 2000
    )
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <div className="content">
        <h2 className="title font-yumin">
          <span>ISBNコードから</span>
          <span>書籍情報を取得するよ！</span>
        </h2>
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
        <div>
          {isPending && <p>データ取得中。ちょっと待ってね...</p>}
          {!isPending && isNoData && <p>書籍情報がなかったよ。ぴえん</p>}
          {!isPending && bookInfo && <Book bookInfo={bookInfo} />}
        </div>
      </div>
    </div>
  );
}

export default App;
