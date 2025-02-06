from django.db import models

class Game(models.Model):
    board = models.CharField(max_length=9, default='         ')  # 3x3 board
    current_player = models.CharField(max_length=1, default='X')
    winner = models.CharField(max_length=1, null=True, blank=True)
    is_over = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_board(self):
        return [list(self.board[i*3:(i+1)*3]) for i in range(3)]

    def make_move(self, row, col):
        board = list(self.board)
        position = row * 3 + col
        if board[position] == ' ':
            board[position] = self.current_player
            self.board = ''.join(board)
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.save()

    def check_winner(self):
        board = self.board
        # Check rows
        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] != ' ':
                return board[i]
        # Check columns
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] != ' ':
                return board[i]
        # Check diagonals
        if board[0] == board[4] == board[8] != ' ':
            return board[0]
        if board[2] == board[4] == board[6] != ' ':
            return board[2]
        # Check draw
        if ' ' not in board:
            return 'D'
        return None 