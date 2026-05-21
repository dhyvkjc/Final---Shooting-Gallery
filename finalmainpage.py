import turtle
import random
import time


screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.tracer(0)
playing_screen = turtle.Turtle()
playing_screen.hideturtle()
playing_screen.color("white")
playing_screen.pensize(5)
playing_screen.penup()
playing_screen.goto(-220 , 260)
playing_screen.pendown()
for _ in range(2):
    playing_screen.goto(220, 260)
    playing_screen.goto(220, -260)
    playing_screen.goto(-220,-260)
    playing_screen.goto(-220, 260)

fill = turtle.Turtle()
fill.hideturtle()
fill.color("white")
fill.penup()
fill.goto(-220 + 2, 260  - 2)
fill.begin_fill()
fill.goto(220 - 2, 260 - 2)
fill.goto(220 - 2, -260 + 2)
fill.goto(-220 + 2, -260 + 2)
fill.goto(-220 + 2, 260 - 2)
fill.end_fill()

class Player:
    def __init__(self):
        self.x = 0
        self.y = -220
        self.speed = 30
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.shape("turtle")
        self.t.color("hot pink")
        self.t.setheading(270)
        self.t.goto(self.x, self.y)

    def move_left(self):
        self.x -= self.speed
        if self.x < -220 + 10:
            self.x = -220 + 10
        self.t.goto(self.x, self.y)

    def move_right(self):
        self.x += self.speed
        if self.x > 220 - 10:
            self.x = 220 - 10
        self.t.goto(self.x, self.y)
player = Player()

class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.green = (color == "green")
        self.colors = ["grey", "orange", "red"]
        self.color_health = 0
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.shape("square")
        self.set_color(color)
        self.t.goto(self.x, self.y)

    def set_color(self, color):
        self.t.color(color)

    def move_down(self):
        self.y -= 20
        self.t.goto(self.x, self.y)

    def hit(self):
        if self.green:
            self.explode()
        else:
            self.color_health += 1
            if self.color_health >= len(self.colors):
                score.add(1)
                self.destroy()
            else:
                self.set_color(self.colors[self.color_health])

    def explode(self):
        explosion_radius = 45
        for block in blocks[:]:
            if self.t.distance(block.t) <= explosion_radius:
                score.add(1)
                block.destroy()

    def destroy(self):
        self.t.hideturtle()
        if self in blocks:
            blocks.remove(self)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.shape("circle")
        self.t.shapesize(0.4, 0.4)
        self.t.color("saddle brown")
        self.t.goto(self.x, self.y)

    def move(self):
        self.y += 15
        self.t.goto(self.x, self.y)

    def collision(self, block):
        return self.t.distance(block.t) < 15

class Score:
    def __init__(self):
        self.score = 0
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.color("hot pink" )
        self.update()

    def add(self, amount):
        self.score += amount
        self.update()

    def update(self):
        self.t.clear()
        self.t.goto(-350, 50)
        self.t.write(
            f"PINK: {self.score}",
            font=("Arial", 20, "bold")
        )
score = Score()

game_over = False
def show_game_over():
    text = turtle.Turtle()
    text.hideturtle()
    text.color("black")
    text.penup()
    text.goto(0, 0)

    text.write(
        "GAME OVER",
        align="center",
        font=("Arial", 30, "bold")
    )

blocks = []
def create_row():
    y = 260 - 20
    for x in range(-180, 181, 30):
        if random.randint(1, 5) == 1:
            color = "green"
        else:
            color = "grey"
        blocks.append(Block(x, y, color))

for y in range(3):
    for x in range(-180, 181, 30):
        if random.randint(1, 5) == 1:
            color = "green"
        else:
            color = "grey"
        blocks.append(Block(x, 260 - 20 - (y * 30), color))

bullets = []
def shoot():
    bullets.append(Bullet(player.x, player.y))

##########################################################################################################################################################################################
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(shoot, "space")
start = time.time()
def update():
    global start
    global game_over
    if time.time() - start > 1:
        start = time.time()
        for block in blocks[:]:
            block.move_down()
            if block.y <= -260 + 20:
                game_over = True
        create_row()

    for bullet in bullets[:]:
        bullet.move()
        if bullet.y > 260:
            bullet.t.hideturtle()
            if bullet in bullets:
                bullets.remove(bullet)
            continue

        for block in blocks[:]:
            if bullet.collision(block):
                block.hit()
                bullet.t.hideturtle()
                if bullet in bullets:
                    bullets.remove(bullet)
                break

while not game_over:
    update()
    screen.update()

show_game_over()
screen.update()
turtle.done()
