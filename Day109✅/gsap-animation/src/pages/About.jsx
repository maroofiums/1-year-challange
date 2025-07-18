import PageWrapper from '../components/PageWrapper';
import { Link } from 'react-router-dom';

export default function About() {
  return (
    <PageWrapper>
      <h1>ℹ️ About Page</h1>
      <p>This is the about page</p>
      <Link to="/">← Back to Home</Link>
    </PageWrapper>
  );
}
