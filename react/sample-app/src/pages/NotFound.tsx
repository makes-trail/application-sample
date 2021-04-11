import React from 'react';
import { Link } from 'react-router-dom';

const NotFound: React.FC = () => {
  return (
    <div>
      <h1>Page Not Found</h1>
      <Link to={"/"}>
        <p className="font-yumin">Homeに戻る</p>
      </Link>
    </div>
  )
}

export default NotFound;
