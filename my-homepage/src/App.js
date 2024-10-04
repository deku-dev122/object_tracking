// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

// 各ページコンポーネント
const Home = () => (
  <div>
    <h2>Home</h2>
    <p>Welcome to the homepage!</p>
  </div>
);

const About = () => (
  <div>
    <h2>About</h2>
    <p>Learn more about us here.</p>
  </div>
);

const Contact = () => (
  <div>
    <h2>Contact</h2>
    <p>Contact us through this page.</p>
  </div>
);

const Header = () => (
  <header style={styles.header}>
    <h1>My Website</h1>
    <nav>
      <ul style={styles.nav}>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/contact">Contact</Link></li>
      </ul>
    </nav>
  </header>
);

const Footer = () => (
  <footer style={styles.footer}>
    <p>&copy; 2024 My Website</p>
  </footer>
);

const App = () => (
  <Router>
    <div style={styles.container}>
      <Header />
      <main style={styles.main}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </main>
      <Footer />
    </div>
  </Router>
);

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100vh',
  },
  header: {
    backgroundColor: '#4CAF50',
    padding: '10px',
    textAlign: 'center',
  },
  nav: {
    display: 'flex',
    justifyContent: 'center',
    listStyle: 'none',
    padding: 0,
  },
  main: {
    flex: '1',
    padding: '20px',
  },
  footer: {
    backgroundColor: '#4CAF50',
    padding: '10px',
    textAlign: 'center',
    marginTop: 'auto',
  },
};

export default App;
