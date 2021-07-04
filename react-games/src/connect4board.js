import fill from './utils'

class Board {
    constructor() {
        this.board = fill(0, [7, 6])
        this.next = fill(6, [6])
        this.turn = 1
        this.active = -1
        this.move_stack = []
    }

    make_move(move) {
        if (this.next[move] >= 0) {
            this.board[this.next[move]][move] = this.turn
            this.move_stack.push(move)
            this.next[move] -= 1
            this.turn *= -1
            return true
        }
        return false
    }

    unmake() {
        if (this.move_stack.length > 0) {
            var move = this.move_stack.pop()
            this.next[move] += 1
            this.board[this.next[move]][move] = 0
            this.turn *= -1
            return move
        }
        return null
    }

    filled(x, y, turn) {
        return 0 <= x && x < 7 && 0 <= y && y < 6
            ? this.board[x][y] == turn
            : false
    }

    is_over() {
        if (this.next.reduce((a, b) => a + b, 0) == -6) {
            return [true, 0]
        }
        for (var i = 0; i < 7; i++) {
            for (var j = 0; j < 6; j++) {
                for (var turn = -1; turn <= 1; turn += 2) {
                    if (
                        (this.filled(i, j, turn) &&
                            this.filled(i, j + 1, turn) &&
                            this.filled(i, j + 2, turn) &&
                            this.filled(i, j + 3, turn)) ||
                        (this.filled(i, j, turn) &&
                            this.filled(i + 1, j, turn) &&
                            this.filled(i + 2, j, turn) &&
                            this.filled(i + 3, j, turn)) ||
                        (this.filled(i, j, turn) &&
                            this.filled(i + 1, j + 1, turn) &&
                            this.filled(i + 2, j + 2, turn) &&
                            this.filled(i + 3, j + 3, turn)) ||
                        (this.filled(i, j, turn) &&
                            this.filled(i - 1, j + 1, turn) &&
                            this.filled(i - 2, j + 2, turn) &&
                            this.filled(i - 3, j + 3, turn))
                    ) {
                        return [true, turn]
                    }
                }
            }
        }
        return [false, 0]
    }
}

export default Board
