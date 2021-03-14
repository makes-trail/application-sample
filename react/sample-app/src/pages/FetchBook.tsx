import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import axios from 'axios';
import http from '../common/http';
import wait from '../common/wait';
import BookInfo from '../components/BookInfo';
import { Book } from '../types/Book';

const FetchBook: React.FC = () => {
  const { isbn } = useParams<{ isbn: string }>();
  const [isPending, setIsPending] = useState<boolean>(true);
  const [message, setMessage] = useState<string>("");
  const [book, setBook] = useState<Book>();

  useEffect(() => {
    const url = new URL(`${process.env.REACT_APP_API_ENDPOINT}/fetch/${isbn}`);

    const source = axios.CancelToken.source();
    const fetchIsbnSummary = async () => {
      const res = await http.get(url.toString(), {
        cancelToken: source.token
      });
      await wait(2000);
      const data: Array<Book> = await res.data;
      if (data.length === 0) {
        setIsPending(false);
        setMessage("書籍情報がなかったよ。ぴえん");
        console.log("response data is null");
        return;
      }
      setBook(data[0]);
      setIsPending(false);
      console.log("data fetched successfully!")
    }
    fetchIsbnSummary();

    // アンマウントされる時にabort!してfetchを強制中止する
    return () => source.cancel("Component got unmounted");
  }, [isbn]);

  return (
    <div>
      {isPending && <h2 className="title font-yumin"><span>データ取得中。</span><span>ちょっと待ってね...</span></h2>}
      {!isPending && message && <h3 className="font-yumin">{message}</h3>}
      {!isPending && book && <BookInfo book={book} />}
      <Link to={"/search-book"}>
        <p className="font-yumin">検索に戻る</p>
      </Link>
    </div>
  );
}

export default FetchBook;
