import React from 'react';
import http from '../common/http';
import { Book } from '../types/Book';

const BookInfo: React.FC<{ book: Book }> = ({ book }) => {
  const saveBookInfo = async (isbn: string) => {
    const urlOpenbd = new URL(`${process.env.REACT_APP_API_ENDPOINT}/save-openbd/${isbn}`);
    const urlGbooks = new URL(`${process.env.REACT_APP_API_ENDPOINT}/save-gbooks/${isbn}`);
    const resOpenbd = await http.put(urlOpenbd.toString());
    const resGbooks = await http.put(urlGbooks.toString());
    if (resOpenbd.status === 200 || resGbooks.status === 200) {
      alert("書籍情報がDynamoDBに保存されたよ！")
    }
  }

  if (!book) {
    return null;
  }
  return (
    <div className="font-yumin">
      <div>
        <p>{book.isbn}</p>
        <p>{book.title}</p>
        <p>{book.author}</p>
        <p>{book.publisher}</p>
        {book.cover && <img
          src={book.cover}
          alt=""
        />}
      </div>
      <button className="font-yumin" onClick={() => saveBookInfo(book.isbn)}>保存</button>
    </div>
  );
}

export default BookInfo;
