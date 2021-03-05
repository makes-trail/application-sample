import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import BookInfo from '../components/BookInfo';
import { Book } from '../types/Book';

const FetchBook: React.FC = () => {
  const { isbn } = useParams<{ isbn: string }>();
  const [isPending, setIsPending] = useState<boolean>(true);
  const [message, setMessage] = useState<string>("");
  const [book, setBook] = useState<Book>();

  useEffect(() => {
    const url = new URL(`${process.env.REACT_APP_API_ENDPOINT}/fetch-isbn-summary`);
    const params = new URLSearchParams();
    params.append("isbn", isbn);
    url.search = params.toString();

    const abortController = new AbortController();
    setTimeout(
      async () => {
        try {
          const res = await fetch(url.toString(), {
            signal: abortController.signal
          });
          if (res.status !== 200) {
            setIsPending(false);
            setMessage("サーバから正しいステータスコードが返ってこなかったよ。ぴえん");
            console.log("status code not 200");
            return;
          }
          const data: Array<Book> = await res.json();
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
        catch (err) {
          if (err.name === 'AbortError') {
            console.log("fetch aborted!");
          } else {
            setMessage("予期せぬエラーが出たよ。ぴえん");
            console.error(`Error:\n${err.message}`);
          }
        }
      }, 2000
    )

    // アンマウントされる時にabort!してfetchを強制中止する
    return () => abortController.abort();
  }, [isbn]);

  return (
    <div>
      {isPending && <h2 className="title font-yumin"><span>データ取得中。</span><span>ちょっと待ってね...</span></h2>}
      {!isPending && message && <p>{message}</p>}
      {!isPending && book && <BookInfo book={book} />}
      <Link to={"/"}>
        <p className="font-yumin">Homeに戻る</p>
      </Link>
    </div>
  );
}

export default FetchBook;
