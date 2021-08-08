import '../styles/globals.css'
import Navigation from '../components/navigation/Navigation'
import 'react-toastify/dist/ReactToastify.css';


function MyApp({ Component, pageProps }) {
  return <Navigation>
    <Component {...pageProps} />
  </Navigation>
}

export default MyApp
