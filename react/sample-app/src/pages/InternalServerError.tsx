import React from 'react';
import { Link } from 'react-router-dom';

const InternalServerError: React.FC = () => {
  return (
    <div>
      <h1>Internal Server Error</h1>
      <Link to={"/"}>
        <p className="font-yumin">Homeに戻る</p>
      </Link>
    </div>
  )
}

export default InternalServerError;
