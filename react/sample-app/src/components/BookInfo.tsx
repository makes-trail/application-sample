import React from 'react';
import http from '../common/http';
import { Book } from '../types/Book';

const BookInfo: React.FC<{ book: Book }> = ({ book }) => {
  const saveBookToDynamo = async (isbn: string) => {
    const urlOpenbd = new URL(`${process.env.REACT_APP_API_ENDPOINT}/save-openbd/${isbn}`);
    const urlGbooks = new URL(`${process.env.REACT_APP_API_ENDPOINT}/save-gbooks/${isbn}`);
    const resOpenbd = await http.put(urlOpenbd.toString());
    const resGbooks = await http.put(urlGbooks.toString());
    if (resOpenbd.status === 200 || resGbooks.status === 200) {
      alert("書籍情報がDynamoDBに保存されたよ！")
    } else {
      alert("保存に失敗したっぽい・・・")
    }
  }
  const saveBookToRds = async (isbn: string) => {
    const url = new URL(`${process.env.REACT_APP_API_ENDPOINT}/save/${isbn}`);
    const res = await http.put(url.toString());
    if (res.status === 200) {
      alert("書籍情報がRDSに保存されたよ！")
    }
    if (res.status === 204) {
      alert("保存する書籍情報が見つからなかったっぽい・・・\n先に「DynamoDBに保存」ボタンを押してからもう一度試してみて！")
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
      <button className="font-yumin react-btn" onClick={() => saveBookToDynamo(book.isbn)}>DynamoDBに保存</button>
      <button className="font-yumin react-btn" onClick={() => saveBookToRds(book.isbn)}>RDSに保存</button>
    </div>
  );
}

export default BookInfo;
