import React, { useState } from 'react'
import ReactDOM from 'react-dom'
import { Router, Link } from '@reach/router'

import Home from './home'
import Connect4 from './connect4'
import UltimateTicTacToe from './ultimate_ttt'

const App = () => {
    return (
        <div className="container-fluid m-0 p-0">
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <Link to="/">
                        <div className="navbar-brand">Home</div>
                    </Link>
                    <button
                        className="navbar-toggler"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#navbarNav"
                        aria-controls="navbarNav"
                        aria-expanded="false"
                        aria-label="Toggle navigation"
                    >
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav">
                            <li className="nav-item">
                                <Link to="connect4">
                                    <div className="nav-link">Connect 4</div>
                                </Link>
                            </li>
                            <li className="nav-item">
                                <Link to="ultimate_ttt">
                                    <div className="nav-link">
                                        Ultimate TicTacToe
                                    </div>
                                </Link>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <Router>
                <Home path="/" />
                <Connect4 path="connect4" />
                <UltimateTicTacToe path="ultimate_ttt" />
            </Router>
        </div>
    )
}

ReactDOM.render(React.createElement(App), document.getElementById('root'))
