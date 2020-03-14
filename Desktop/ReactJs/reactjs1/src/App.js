import React from 'react';
// import logo from './logo.svg';
import './App.css';
import Head from './component/head/Head';
import Login from './component/Login/Login';
import Footer from './component/footer/Footer'
import DashBoard from './component/dashboard/DashBoard';

function App() {
  return (
    <div>
        <Head/>
        <Login/>
        {/*<Footer/>*/}
        <DashBoard name="Amit" />
    </div>
  );
}

export default App;
