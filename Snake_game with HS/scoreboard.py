from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score(self.high_score)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write("Press SPACE to restart", align=ALIGNMENT, font=FONT)
        self.goto(0, 270)

    def reset_game(self, snake):
        """Resets the game state: clears the snake, resets current score."""
        snake.clear_snake()
        snake.__init__()  # Re-initialize snake
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        try:
            with open("score.txt", "r") as file:
                return int(file.read())
        except:
            return 0

    def write_high_score(self, score):
        with open("score.txt", "w") as file:
            file.write(str(score))
