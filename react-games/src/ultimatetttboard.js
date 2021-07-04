import fill from './utils'

class Board {
    constructor() {
        this.board = fill(0, [9, 9])
        this.turn = 1
        this.move_stack = []
        this.active = -1
        this.miniboard = fill(2, [9])
    }

    static miniboard_pos(pos) {
        return (Math.floor(pos / 3) % 3) + Math.floor(pos / 27) * 3
    }

    static next_miniboard_pos(pos) {
        return 3 * (Math.floor(pos / 9) % 3) + ((pos % 9) % 3)
    }

    win(x, y) {
        if (
            (this.board[x][y] == 1 &&
                this.board[x + 1][y] == 1 &&
                this.board[x + 2][y] == 1) ||
            (this.board[x][y + 1] == 1 &&
                this.board[x + 1][y + 1] == 1 &&
                this.board[x + 2][y + 1] == 1) ||
            (this.board[x][y + 2] == 1 &&
                this.board[x + 1][y + 2] == 1 &&
                this.board[x + 2][y + 2] == 1) ||
            (this.board[x][y] == 1 &&
                this.board[x][y + 1] == 1 &&
                this.board[x][y + 2] == 1) ||
            (this.board[x + 1][y] == 1 &&
                this.board[x + 1][y + 1] == 1 &&
                this.board[x + 1][y + 2] == 1) ||
            (this.board[x + 2][y] == 1 &&
                this.board[x + 2][y + 1] == 1 &&
                this.board[x + 1][y + 2] == 1) ||
            (this.board[x][y] == 1 &&
                this.board[x + 1][y + 1] == 1 &&
                this.board[x + 2][y + 2] == 1) ||
            (this.board[x][y + 2] == 1 &&
                this.board[x + 1][y + 1] == 1 &&
                this.board[x + 2][y] == 1)
        ) {
            return 1
        } else if (
            (this.board[x][y] == -1 &&
                this.board[x + 1][y] == -1 &&
                this.board[x + 2][y] == -1) ||
            (this.board[x][y + 1] == -1 &&
                this.board[x + 1][y + 1] == -1 &&
                this.board[x + 2][y + 1] == -1) ||
            (this.board[x][y + 2] == -1 &&
                this.board[x + 1][y + 2] == -1 &&
                this.board[x + 2][y + 2] == -1) ||
            (this.board[x][y] == -1 &&
                this.board[x][y + 1] == -1 &&
                this.board[x][y + 2] == -1) ||
            (this.board[x + 1][y] == -1 &&
                this.board[x + 1][y + 1] == -1 &&
                this.board[x + 1][y + 2] == -1) ||
            (this.board[x + 2][y] == -1 &&
                this.board[x + 2][y + 1] == -1 &&
                this.board[x + 1][y + 2] == -1) ||
            (this.board[x][y] == -1 &&
                this.board[x + 1][y + 1] == -1 &&
                this.board[x + 2][y + 2] == -1) ||
            (this.board[x][y + 2] == -1 &&
                this.board[x + 1][y + 1] == -1 &&
                this.board[x + 2][y] == -1)
        ) {
            return -1
        }

        var sum = 0
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                sum += Math.abs(this.board[x + i][y + j])
            }
        }
        if (sum == 9) {
            return 0
        }

        return 2
    }

    mini_boards_won() {
        for (var m = 0; m < 9; m++) {
            const x = Math.floor(m / 3) * 3
            const y = (m % 3) * 3
            this.miniboard[m] = this.win(x, y)
        }
    }

    make_move(move) {
        var x = Math.floor(move / 9)
        var y = move % 9
        if (this.active != -1 && Board.miniboard_pos(move) != this.active) {
            return [false, 'Make a move on the active miniboard only']
        }
        if (this.board[x][y] == 0) {
            this.board[x][y] = this.turn
            this.move_stack.push(move)
            this.turn *= -1
            this.active = Board.next_miniboard_pos(move)

            return [true, '']
        }
        return [false, 'Token already exists here']
    }

    unmake() {
        if (this.move_stack.length > 0) {
            var move = this.move_stack.pop()
            this.board[Math.floor(move / 9)][move % 9] = 0
            this.turn *= -1

            if (this.move_stack.length > 0) {
                this.active = Board.next_miniboard_pos(
                    this.move_stack[this.move_stack.length - 1]
                )
            } else {
                this.active = -1
            }

            return move
        }
        return null
    }

    is_over() {
        return [false, 0]
    }
}

export default Board
