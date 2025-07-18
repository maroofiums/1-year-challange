import PageWrapper from '../components/PageWrapper';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <PageWrapper>
      <h1>🏠 Home Page</h1>
      <p>This is the home page</p>
      <Link to="/about">Go to About →</Link>
    </PageWrapper>
  );
}
