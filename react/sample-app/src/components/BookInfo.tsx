import React from 'react';
import { Book } from '../types/Book';

const BookInfo: React.FC<{ book: Book }> = ({ book }) => {
  if (!book) {
    return null;
  }
  return (
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
  );
}

export default BookInfo;
