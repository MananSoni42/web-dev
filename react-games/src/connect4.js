import React, { useState, useLayoutEffect } from 'react'
import Board from './connect4board'

import token0 from './assets/img/token0.png'
import token1 from './assets/img/token1.png'
import token2 from './assets/img/token2.png'
import pointer from './assets/img/pointer.png'

const Connect4 = () => {
    const [game, setGame] = useState(new Board())
    const turn_col = game.turn == 1 ? 'danger' : 'primary'

    function add_token(move) {
        if (!game.make_move(move)) {
            alert('Illegal move: Column is already full')
        }
        setGame(Object.assign(Object.create(Object.getPrototypeOf(game)), game))
    }

    function sample_test_fn(a, b) {
        return a + b
    }

    function remove_token() {
        game.unmake()
        //console.log(game)
        setGame(Object.assign(Object.create(Object.getPrototypeOf(game)), game))
    }

    useLayoutEffect(() => {
        // checks if game is over
        var result = game.is_over()
        if (result[0]) {
            alert(`Player ${result[1] == 1 ? 1 : 2} has won !!!`)
            //setGame(new Board())
        }
    }, [game])

    return (
        <div className="row mx-5">
            <div className="col-7 py-2 px-5 mx-3">
                <div className="row mx-5 text-center">
                    {[0, 1, 2, 3, 4, 5].map((row, rowid) => (
                        <div
                            id={'btn' + rowid}
                            key={'btn' + rowid}
                            className="col click ptr"
                            onClick={(e) => add_token(rowid)}
                        >
                            <img
                                className="img-fluid"
                                src={pointer}
                                alt="pointer"
                            />
                        </div>
                    ))}
                </div>

                {game.board.map((row, rowid) => (
                    <div
                        id={'row' + rowid}
                        key={'row' + rowid}
                        className="row mx-5 text-center"
                    >
                        {row.map((col, colid) => (
                            <div
                                id={'col' + colid}
                                key={'col' + colid}
                                className="col m-1 border border-dark grid"
                            >
                                <img
                                    className="img-fluid"
                                    src={
                                        col == 0
                                            ? token0
                                            : col == 1
                                            ? token1
                                            : token2
                                    }
                                    alt="token1"
                                />
                            </div>
                        ))}
                    </div>
                ))}
            </div>
            <div className="col-4 text-center p-1 mt-3">
                <div className="row">
                    <div className="col-1"></div>
                    <div className="col-5">
                        <button
                            type="button"
                            className="btn btn-outline-dark border border-dark mx-auto text-center"
                            onClick={(e) => {
                                setGame(new Board())
                            }}
                        >
                            <div className="h3">New Game</div>
                        </button>
                    </div>
                    <div className="col-5">
                        <button
                            type="button"
                            className="btn btn-outline-dark border border-dark mx-auto text-center"
                            onClick={(e) => {
                                remove_token()
                            }}
                        >
                            <div className="h3">Undo move</div>
                        </button>
                    </div>
                </div>

                <div className="card m-3 text-center">
                    <div className="card-body bg-dark text-light">
                        INSTRUCTIONS
                        <hr className="bg-light" />
                        Press the arrows on top of the board to drop a token
                        into the corresponding column <br />
                        the first to form a horizontal, vertical, or diagonal
                        line of <span className="font-weight-bold"> 4 </span>
                        tokens wins!
                        <hr className="bg-light" />
                        The current turn is shown in the respective player's
                        color below.
                        <br />
                        Player 1: <span className="text-danger">Red </span>
                        <br />
                        Player 2: <span className="text-primary">Blue</span>
                    </div>
                </div>
                <div className={`card bg-${turn_col} m-3 mb-0 text-center`}>
                    <div className="card-body h3">
                        Turn: {game.turn == 1 ? 'Player 1' : 'Player 2'}
                    </div>
                </div>
                <div>
                    <small>
                        <div>
                            Icons made by{' '}
                            <a href="https://www.freepik.com" title="Freepik">
                                Freepik
                            </a>{' '}
                            from{' '}
                            <a
                                href="https://www.flaticon.com/"
                                title="Flaticon"
                            >
                                www.flaticon.com
                            </a>
                        </div>
                    </small>
                </div>
            </div>
        </div>
    )
}

export default Connect4
