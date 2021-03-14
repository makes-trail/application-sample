import React from 'react';
import { Link } from 'react-router-dom';

const ServiceUnavailable: React.FC = () => {
  return (
    <div>
      <h1>Service Temporarily Unavailable</h1>
      <Link to={"/"}>
        <p className="font-yumin">Homeに戻る</p>
      </Link>
    </div>
  )
}

export default ServiceUnavailable;
