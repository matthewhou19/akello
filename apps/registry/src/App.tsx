import { Routes, Route } from "react-router-dom";
import { useEffect, useState } from 'react';
import { ThemeProvider } from '@aws-amplify/ui-react';
import { fetchAuthSession } from '@aws-amplify/auth';

import { theme } from './theme';
import '@aws-amplify/ui-react/styles.css';
import {
  withAuthenticator,
  useAuthenticator,
} from '@aws-amplify/ui-react';

import {AccountService} from '@akello/account';

interface AppProps {
  isPassedToWithAuthenticator: boolean;
}

const App:React.FC<AppProps> = () => {
  const [themeMode, setThemeMode] = useState('');
  const { authStatus, user } = useAuthenticator(context => [context.authStatus]);

  useEffect(() => {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      setThemeMode('dark');
    }

    const handleChangeTheme = (event: MediaQueryListEvent) => {
      setThemeMode(event.matches ? "dark" : "light");
    };

    const mediaQueryList = window.matchMedia('(prefers-color-scheme: dark)');
    mediaQueryList.addEventListener('change', handleChangeTheme);

    return () => {
      mediaQueryList.removeEventListener('change', handleChangeTheme);
    };
  }, []);

  if(authStatus === 'configuring') {
    return <></>
  }

  if(authStatus !== 'authenticated') {
    return <>not authenticated</>
  }

  // Function to print access token and id token
  const printAccessTokenAndIdToken = async () => {
    try {
      const session = await fetchAuthSession();   // Fetch the authentication session
      console.log('Access Token:', session.tokens!.accessToken.toString());
      console.log('ID Token:', session.tokens!.idToken!.toString());
    }
    catch (e) { console.log(e); }
  };

  printAccessTokenAndIdToken()


  /////////////////////////
  // DBUG - test the account service
  const accountService = new AccountService(
      import.meta.env.VITE_MICROSERVICE_ACCOUNT_API
  );
  accountService.getAccount(
    "ACCESS_TOKEN",
    "ACCOUNT_ID",
    (data: any) => {
      console.log(data);
    },
    (error: any) => {
      console.log(error);
    }
  )
  /////////////////////////


  return (
    <ThemeProvider theme={theme} colorMode={themeMode}>
      <Routes>
          <Route path="/" element={<>
            <div className="text-8xl font-bold underline">
              Hello world!
            </div>
            <div className='bg-green-200 font-semibold'>root</div>
          </>} />
      </Routes>
    </ThemeProvider>
  );
};

export default withAuthenticator(App);

