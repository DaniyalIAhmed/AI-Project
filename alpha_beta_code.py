import tkinter as tk
import random
import copy

BOARD_SIZE = 6
PLAYER_COLORS = {1: 'blue', 2: 'red'}
BOOSTER_EFFECTS = ['extra_turn', 'reveal_tile']

class Tile:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.type = random.choice(['scorer', 'trap', 'advantage', 'neutral'])
        self.revealed = False
        self.owned_by = None

class BoardGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=600, height=650)
        self.canvas.pack()

        self.score_label = tk.Label(root, text="", font=('Arial', 14))
        self.score_label.pack()

        self.board = [[Tile(i, j) for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
        self.players = {
            1: {'pos': (0, 0), 'score': 0, 'boosters': [], 'memory': {}, 'tile_visit_count': {}},
            2: {'pos': (BOARD_SIZE - 1, BOARD_SIZE - 1), 'score': 0, 'boosters': [], 'memory': {}, 'tile_visit_count': {}}
        }
        self.board[0][0].owned_by = 1
        self.board[BOARD_SIZE - 1][BOARD_SIZE - 1].owned_by = 2
        self.current_player = 1
        self.draw_board()
        self.canvas.bind("<Button-1>", self.click_event)

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                x1, y1 = j * 100, i * 100
                x2, y2 = x1 + 100, y1 + 100
                tile = self.board[i][j]
                color = 'gray' if not tile.revealed else self.get_tile_color(tile)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                if tile.owned_by:
                    self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2,
                                            text=f"P{tile.owned_by}", fill='white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score_label.config(text=f"Player 1 Score: {self.players[1]['score']}    Player 2 Score: {self.players[2]['score']}")

    def get_tile_color(self, tile):
        return {
            'scorer': 'green',
            'trap': 'black',
            'advantage': 'yellow',
            'neutral': 'white'
        }.get(tile.type, 'gray')

    def click_event(self, event):
        if self.current_player != 1:
            return
        row, col = event.y // 100, event.x // 100
        self.flip_tile(row, col)

    def flip_tile(self, row, col):
        tile = self.board[row][col]
        if tile.revealed:
            return

        tile.revealed = True
        self.draw_board()
        self.root.after(100, lambda: self.ask_player_decision(row, col))

    def ask_player_decision(self, row, col):
        decision = tk.messagebox.askyesno("Move Decision", "Do you want to move to this tile?")
        if decision:
            self.make_move(row, col)
        else:
            self.board[row][col].revealed = False
            self.draw_board()
            self.switch_player()
            if self.current_player == 2:
                self.root.after(1000, self.ai_move)

    def make_move(self, row, col):
        tile = self.board[row][col]
        tile.revealed = True
        tile.owned_by = self.current_player
        player = self.players[self.current_player]

        prev_row, prev_col = player['pos']
        if (prev_row, prev_col) != (row, col):
            self.board[prev_row][prev_col].owned_by = None
            self.board[prev_row][prev_col].revealed = False

        player['pos'] = (row, col)
        player['memory'][(row, col)] = tile.type
        player['tile_visit_count'][(row, col)] = player['tile_visit_count'].get((row, col), 0) + 1

        extra_turn = False

        if tile.type == 'scorer':
            player['score'] += 2
        elif tile.type == 'trap':
            player['score'] = max(0, player['score'] - 1)
        elif tile.type == 'advantage':
            booster = random.choice(BOOSTER_EFFECTS)
            player['boosters'].append(booster)
            if booster == 'extra_turn':
                extra_turn = True

        self.draw_board()

        if player['score'] >= 20 or self.all_tiles_revealed():
            self.end_game(f"Player {self.current_player} wins!")
            return

        if extra_turn:
            return

        self.switch_player()

        if self.current_player == 2:
            self.root.after(1000, self.ai_move)

    def switch_player(self):
        self.current_player = 1 if self.current_player == 2 else 2

    def ai_move(self):
        move = self.best_move()
        if move:
            self.make_move(*move)

    def best_move(self):
        state = {
            'board': [[{
                'revealed': tile.revealed,
                'type': tile.type,
                'owned_by': tile.owned_by
            } for tile in row] for row in self.board],
            'players': copy.deepcopy(self.players)
        }
        _, move = self.alpha_beta(state, 2, float('-inf'), float('inf'), True)
        return move

    def alpha_beta(self, state, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.is_terminal(state):
            return self.evaluate(state), None

        best_move = None
        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_possible_moves(state):
                new_state = self.simulate_move(copy.deepcopy(state), move, 2)
                eval, _ = self.alpha_beta(new_state, depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in self.get_possible_moves(state):
                new_state = self.simulate_move(copy.deepcopy(state), move, 1)
                eval, _ = self.alpha_beta(new_state, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def get_possible_moves(self, state):
        moves = []
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if not state['board'][i][j]['revealed']:
                    moves.append((i, j))
        return moves

    def simulate_move(self, state, move, player):
        row, col = move
        tile = state['board'][row][col]
        tile['revealed'] = True
        tile['owned_by'] = player

        if tile['type'] == 'scorer':
            state['players'][player]['score'] += 2
        elif tile['type'] == 'trap':
            state['players'][player]['score'] = max(0, state['players'][player]['score'] - 1)
        elif tile['type'] == 'advantage':
            state['players'][player]['boosters'].append('extra_turn')

        state['players'][player]['pos'] = (row, col)
        visit_count = state['players'][player].setdefault('tile_visit_count', {})
        visit_count[(row, col)] = visit_count.get((row, col), 0) + 1
        return state

    def evaluate(self, state):
        score_diff = state['players'][2]['score'] - state['players'][1]['score']
        revisit_penalty = sum(v - 1 for v in state['players'][2].get('tile_visit_count', {}).values() if v > 1)
        return score_diff - (2 * revisit_penalty)

    def is_terminal(self, state):
        for row in state['board']:
            for tile in row:
                if not tile['revealed']:
                    return False
        return True

    def all_tiles_revealed(self):
        return all(tile.revealed for row in self.board for tile in row)

    def end_game(self, message):
        self.canvas.unbind("<Button-1>")
        self.canvas.create_text(300, 300, text=message, font=('Arial', 24), fill='white')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mind-Maze: AI Strategy Game")
    game = BoardGame(root)
    root.mainloop()