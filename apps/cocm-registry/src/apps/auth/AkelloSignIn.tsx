import {SignIn} from '@akello/react'
import {AkelloProvider} from '@akello/react-hook'
import {AkelloClient} from '@akello/core'


const AkelloSignIn = () => {
    const akello = new AkelloClient({
        baseUrl: process.env.REACT_APP_AKELLO_API_URL,
        cognitoUserPoolId: process.env.REACT_APP_AWS_COGNITO_USERPOOL_ID,
        cognitoClientId: process.env.REACT_APP_AWS_COGNITO_APP_CLIENT_ID,
        cognitoEndpoint: process.env.REACT_APP_AKELLO_COGNITO_URL,
    })
    
     
    return (
        <>
            <AkelloProvider akello={akello}>
                <SignIn onSuccess={(token: string) => {
                    console.log(token)
                    debugger
                }} onFail={(err: string) => {
                    console.log(err)
                    debugger
                }}/>
            </AkelloProvider>            
        </>
    )
}

export default AkelloSignIn