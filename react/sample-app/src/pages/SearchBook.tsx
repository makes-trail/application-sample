import React, { useState } from 'react';
import { useHistory, Link } from 'react-router-dom';

const SearchBook: React.FC = () => {
  const history = useHistory();
  const regex = new RegExp(/^\d{13}$/);
  const [isbn, setIsbn] = useState<string>("9784");
  const [errorMessage, setErrorMessage] = useState<string>("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!regex.test(isbn)) {
      setErrorMessage("13桁の数字で入力してね");
      return;
    }
    history.push(`/fetch-book/${isbn}`);
  }

  return (
    <div>
      <h2 className="title font-yumin">
        <span>ISBNコードから</span>
        <span>書籍情報を取得するよ！</span>
      </h2 >
      <form onSubmit={handleSubmit}>
        <label className="font-yumin">ISBN(13桁)</label>
        <input
          type="text"
          inputMode="numeric"
          pattern="\d*"
          required
          value={isbn}
          onChange={(e) => setIsbn(e.target.value)}
        />
        <span className="text-error font-yumin">{errorMessage}</span>
        <button type="submit" className="font-yumin react-btn">検索</button>
      </form>
      <Link to={"/"}>
        <p className="font-yumin">Homeに戻る</p>
      </Link>
    </div>
  )
}

export default SearchBook;
