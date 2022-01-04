import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import SaveAltIcon from '@material-ui/icons/SaveAlt';
import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import http from '../common/http';
import wait from '../common/wait';
import BookCard from '../components/BookCard';
import { Book } from '../types/Book';


const FetchBook: React.FC = () => {
  const { isbn } = useParams<{ isbn: string }>();
  const [isPending, setIsPending] = useState<boolean>(true);
  const [message, setMessage] = useState<string>("");
  const [book, setBook] = useState<Book>();

  useEffect(() => {
    const url = new URL(`${process.env.REACT_APP_API_ENDPOINT}/search/${isbn}`);

    const source = axios.CancelToken.source();
    const fetchIsbnSummary = async () => {
      const res = await http.get(url.toString(), {
        cancelToken: source.token
      });
      await wait(1000);
      const data: Array<Book> = await res.data;
      if (data.length === 0) {
        setIsPending(false);
        setMessage("書籍情報がなかったよ。ぴえん");
        console.log("response data is null");
        return;
      }
      setBook(data[0]);
      setIsPending(false);
      setMessage("書籍情報が見つかったよ！");
      console.log("data fetched successfully!")
    }
    fetchIsbnSummary();

    // アンマウントされる時にabort!してfetchを強制中止する
    return () => source.cancel("Component got unmounted");
  }, [isbn]);

  const handleSave = async () => {
    const url = new URL(`${process.env.REACT_APP_API_ENDPOINT}/save`);
    const data = JSON.stringify(book)
    const res = await http.put(url.toString(), data);
    if (res.status === 200) {
      alert("書籍情報がDBに保存されたよ！")
    } else {
      alert("保存に失敗したっぽい・・・")
    }
  }

  return (
    <div>
      {isPending ?
        <h2 className="title font-yumin">
          <span>データ取得中。</span>
          <span>ちょっと待ってね...</span>
        </h2> :
        <h2 className="font-yumin">{message}</h2>
      }
      {book &&
        <div>
          <Box m={2}>
            <BookCard book={book} />
          </Box>
          <Box m={2}>
            <Button
              variant="outlined"
              size="large"
              startIcon={<SaveAltIcon />}
              onClick={handleSave}
            >
              DBに保存
            </Button>
          </Box>
        </div>
      }
      <Link to={"/search-book"}>
        <p className="font-yumin">検索に戻る</p>
      </Link>
    </div>
  );
}

export default FetchBook;
