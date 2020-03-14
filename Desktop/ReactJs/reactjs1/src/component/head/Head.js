import React from 'react';
import './Head.css';


class Head extends React.Component{

    constructor() {
        super();
        this.state = {
            isLogged: false,
        }
        this.handleClick = this.handleClick.bind(this)
    }

    handleClick(){
        this.setState(prevState => {
            return {
                isLogged: !this.state.isLogged
            }
        })
    }

    
    render() {
        let isLoggedIn = this.state.isLogged ? "Hello, Amit" : "Login"
        return(
            <div>
                <ul>
                    <li>Home</li>
                    <li>About</li>
                    <li>{ this.state.count }</li>
                    <li>
                        <button onClick={this.handleClick}>{ isLoggedIn}</button>
                    </li>
                </ul>
            </div>
        );
    }
}

export default Head;
