from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 500
SPEED = 150
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "White"
FOOD_COLOR = "Red"
BACKGROUND_COLOR = "BLACK"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.circle = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            circle = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.circle.append(circle)


class Food:
    def __init__(self):
        x = random.randint(1, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(1, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")


def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    circle = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.circle.insert(0, circle)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    else:

        del snake.coordinates[-1]

        canvas.delete(snake.circle[-1])

        del snake.circle[-1]
    if check_collisions(snake):
        game_over()
    else:

        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=("Times nwe roman", 70), text="GAME OVER", fill="Red", tags="gameover")


window = Tk()
window.title("Snake Game")
window.resizable(True, True)
score = 0
direction = 'down'
label1 = Label(window, text="Sunway snake game for kids", font=('consoles', 20))
label = Label(window, text="Score : {}".format(score), font=('consoles', 20))
label1.pack()
label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<A>', lambda event: change_direction("left"))
window.bind('<D>', lambda event: change_direction('right'))
window.bind('<W>', lambda event: change_direction('up'))
window.bind('<S>', lambda event: change_direction('down'))
window.bind('<a>', lambda event: change_direction("left"))
window.bind('<d>', lambda event: change_direction('right'))
window.bind('<w>', lambda event: change_direction('up'))
window.bind('<s>', lambda event: change_direction('down'))
window.bind('<Left>', lambda event: change_direction("left"))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()
