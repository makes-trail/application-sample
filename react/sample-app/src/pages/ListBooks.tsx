import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import http from '../common/http';
import BookCard from '../components/BookCard';
import { Book } from '../types/Book';

const ListBooks: React.FC = () => {
  const [books, setBooks] = useState<Array<Book>>();

  useEffect(() => {
    const url = new URL(`${process.env.REACT_APP_API_ENDPOINT}/list`);

    const source = axios.CancelToken.source();
    const fetchBookList = async () => {
      const res = await http.get(url.toString(), {
        cancelToken: source.token
      });
      const data: Array<Book> = await res.data;
      setBooks(data);
    }
    fetchBookList();

    return () => source.cancel("Component got unmounted");
  }, []);

  return (
    <div>
      <h2 className="title font-yumin">
        みんなが保存した本たち
      </h2>
      <Link to={"/"}>
        <p className="font-yumin">Homeに戻る</p>
      </Link>
      <Container>
        <Grid container justify="center" spacing={3}>
          {books && books.map(book => (
            <Grid item key={book.isbn} xs={12} sm={6} md={4}>
              <BookCard book={book} />
            </Grid>
          ))}
        </Grid>
      </Container>
    </div>
  )
}

export default ListBooks;
