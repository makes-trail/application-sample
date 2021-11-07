const COGNITO_REGION = 'us-west-2';
const COGNITO_USER_POOL = 'us-west-2_xxxxxx';
const COGNITO_USER_POOL_CLIENT = 'xxxxxx';
const COGNITO_DOMAIN_PREFIX = 'xxxxxx';

const amplifyConfig = {
  Auth: {
    region: COGNITO_REGION,
    userPoolId: COGNITO_USER_POOL,
    userPoolWebClientId: COGNITO_USER_POOL_CLIENT,
    oauth: {
      domain: `${COGNITO_DOMAIN_PREFIX}.auth.${COGNITO_REGION}.amazoncognito.com`,
      scope: [
        'openid',
        'profile'
      ],
      redirectSignIn: 'https://xxxxxx.cloudfront.net',
      redirectSignOut: 'https://xxxxxx.cloudfront.net',
      responseType: 'code'
    }
  }
};

export default amplifyConfig;
