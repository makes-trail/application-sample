import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Amplify from 'aws-amplify';
import amplifyConfig from '../amplifyConfig';
import { CognitoUserSession } from 'amazon-cognito-identity-js';

import UserCard from '../components/UserCard';
import { User } from '../types/User';


Amplify.configure(amplifyConfig);

const UserInfo: React.FC<{ userSession: CognitoUserSession }> = ({ userSession }) => {
  const [message, setMessage] = useState<string>("please wait ......")
  const [errorMessage, setErrorMessage] = useState<string>("")
  const [user, setUser] = useState<User>();

  useEffect(() => {
    const source = axios.CancelToken.source();
    const fetchSession = async () => {
      try {
        const jwtToken = userSession.getIdToken().getJwtToken();
        console.log(jwtToken);

        const url = new URL(`${process.env.REACT_APP_API_ENDPOINT}/userinfo`);
        const res = await axios.get(url.toString(), {
          headers: {
            Authorization: jwtToken
          }
        });

        const currentUser: User = await res.data;
        setUser(currentUser);
        setMessage("Welcome!!");
      } catch (error: any) {
        setMessage("ERROR");
        setErrorMessage(error.message);
        console.error(error);
      }
    }
    fetchSession();

    return () => source.cancel("Component got unmounted");
  }, [])

  return (
    <div>
      <h2>{message}</h2>
      {errorMessage && <p>{errorMessage}</p>}
      {user && <UserCard user={user} />}
    </div>
  );
}

export default UserInfo;
