import React, { useEffect, useState } from 'react';
import Amplify, { Auth } from 'aws-amplify';
import { CognitoHostedUIIdentityProvider } from "@aws-amplify/auth/lib/types";
import amplifyConfig from '../amplifyConfig';
import { CognitoUserSession } from 'amazon-cognito-identity-js';

import UserInfo from './UserInfo'


Amplify.configure(amplifyConfig);

const Home: React.FC = () => {
  const [userSession, setUserSession] = useState<CognitoUserSession>();
  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    Auth.federatedSignIn({ provider: CognitoHostedUIIdentityProvider.Google });
  }
  const handleLogout = async (e: React.FormEvent) => {
    e.preventDefault();
    Auth.signOut();
  }

  useEffect(() => {
    const fetchSession = async () => {
      const session = await Auth.currentSession();
      setUserSession(session)
    }
    fetchSession();
  }, []);

  return userSession ? (
    <div>
      <UserInfo userSession={userSession}></UserInfo>
      <button className="Line-login-btn" onClick={handleLogout}>Sign out</button>
    </div>
  ) : (
    <div>
      <button className="Line-login-btn" onClick={handleLogin}>Sign in with Google</button>
    </div>
  );
}

export default Home;
