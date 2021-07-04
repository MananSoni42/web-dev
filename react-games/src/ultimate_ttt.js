import React, { useState, useLayoutEffect } from 'react'
import Board from './ultimatetttboard'

import token0 from './assets/img/token0.png'
import token1 from './assets/img/token1.png'
import token2 from './assets/img/token2.png'
import pointer from './assets/img/pointer.png'

const UltimateTicTacToe = () => {
    const [game, setGame] = useState(new Board())
    const turn_col = game.turn == 1 ? 'danger' : 'primary'

    const miniboards_col = [
        'f2f2f2',
        'd7d7d7',
        'f2f2f2',
        'd7d7d7',
        'f2f2f2',
        'd7d7d7',
        'f2f2f2',
        'd7d7d7',
        'f2f2f2',
        'b2dce5', // 10 - 1
        'ffff9f', // 10  + 0
        'f58f84', //  10 + 1
    ]

    function add_token(move) {
        const valid = game.make_move(move)

        game.mini_boards_won()
        if (game.miniboard[game.active] != 2) {
            game.active = -1
        }

        if (!valid[0]) {
            alert('Illegal move: ' + valid[1])
        }
        setGame(Object.assign(Object.create(Object.getPrototypeOf(game)), game))
    }

    function remove_token() {
        game.unmake()

        game.mini_boards_won()
        if (game.miniboard[game.active] != 2) {
            game.active = -1
        }

        setGame(Object.assign(Object.create(Object.getPrototypeOf(game)), game))
    }

    useLayoutEffect(() => {
        // checks if game is over
        var result = game.is_over()
        if (result[0]) {
            alert(`Player ${result[1] == 1 ? 1 : 2} has won !!!`)
            setGame(new Board())
        }
    }, [game])

    return (
        <div className="row mx-5">
            <div className="col-8 py-2 p-5">
                {game.board.map((row, rowid) => (
                    <div key={'row' + rowid} className="row mx-5 text-center">
                        {row.map((col, colid) => (
                            <div
                                key={'col' + colid}
                                style={{
                                    backgroundColor:
                                        game.miniboard[
                                            Board.miniboard_pos(
                                                rowid * 9 + colid
                                            )
                                        ] == 2
                                            ? '#' +
                                              miniboards_col[
                                                  Board.miniboard_pos(
                                                      rowid * 9 + colid
                                                  )
                                              ]
                                            : '#' +
                                              miniboards_col[
                                                  10 +
                                                      game.miniboard[
                                                          Board.miniboard_pos(
                                                              rowid * 9 + colid
                                                          )
                                                      ]
                                              ],
                                    border:
                                        game.active == -1 ||
                                        Board.miniboard_pos(
                                            rowid * 9 + colid
                                        ) == game.active
                                            ? '0.2em solid #1dc254'
                                            : '0.2em solid black',
                                }}
                                className="col m-1 btn click"
                                onClick={(e) => add_token(rowid * 9 + colid)}
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
                                    alt="token"
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
                        Todo
                        <hr />
                        <div className="col-6 text-left"></div>
                        <b>Miniboard Colors:</b>
                        <br />
                        Default:
                        <span style={{ color: '#' + miniboards_col[1] }}>
                            &nbsp; Gray
                        </span>
                        <br />
                        Won (Player 1):
                        <span style={{ color: '#' + miniboards_col[10 - 1] }}>
                            &nbsp; Red
                        </span>
                        <br />
                        Won (Player 2):
                        <span style={{ color: '#' + miniboards_col[10 + 1] }}>
                            &nbsp; Blue
                        </span>
                        <br />
                        Drawn:
                        <span style={{ color: '#' + miniboards_col[10 + 0] }}>
                            &nbsp; Yellow
                        </span>
                        <br />
                        Active:
                        <span style={{ color: '#1dc254' }}>
                            &nbsp; Green
                        </span>{' '}
                        border
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

export default UltimateTicTacToe
