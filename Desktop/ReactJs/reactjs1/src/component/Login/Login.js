import React, { Component } from 'react';
import './Login.css';


class Login extends Component{
    render() {
        return(
            <div id="LoginFormId">
                <h3>Login</h3><br />
                <form action="." method='post'>
                    <label>
                        Email:
                        <input/><br /><br />
                    </label>
                    <label>
                        Password:
                        <input/><br /><br />
                    </label>
                    <button id="LoginButton">Login</button>
                </form>
            </div>
        );
    }
}


export default Login;
