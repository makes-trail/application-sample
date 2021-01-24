import React from 'react';

interface BookInfo {
  isbn: string;
  title: string;
  author: string;
  publisher: string;
  cover: string;
}

const Book: React.FC<{ bookInfo: BookInfo }> = ({ bookInfo }) => {
  return (
    <div>
      <p>{bookInfo.isbn}</p>
      <p>{bookInfo.title}</p>
      <p>{bookInfo.author}</p>
      <p>{bookInfo.publisher}</p>
      {bookInfo.cover && <img
        src={bookInfo.cover}
        alt=""
      />}
    </div>
  );
}

export default Book;
