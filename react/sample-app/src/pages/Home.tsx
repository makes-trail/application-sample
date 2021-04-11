import React from 'react';
import { Link } from 'react-router-dom';

const Home: React.FC = () => {

  return (
    <div>
      <h1 className="font-yumin">MAKES TRAIL</h1>
      <h2 className="font-yumin">サンプル版</h2>
      <Link to={"/search-book"}>
        <p className="font-yumin">クリックして始める</p>
      </Link>
    </div>
  )
}

export default Home;
