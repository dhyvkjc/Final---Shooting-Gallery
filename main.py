from turtle import *
import random
import time

screen.setup(900, 700)
screen.bgcolor("black")



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = -220
        self.speed = 30
        self.alive = True
        
        self.t = Turtle()
        self.t.penup()
        self.t.shape("turtle")
        self.t.color("hot pink")
        self.t.goto(self.x, self.y) # turtle at 0,-250
        self.t.setheading(90)

        self.direction = ("left", "right")
        screen.onkeypress(self.left, "Left")
        screen.onkeypress(self.right, "Right")

    def left(self):
        self.x -= self.speed
        if self.x < -220 + 10:
            self.x = -220 + 10
        self.t.goto(self.x, self.y)

    def right(self):
        self.x += self.speed
        if self.x > 220 - 10:
            self.x = 220- 10
        self.t.goto(self.x, self.y)
 

class Block:
    def __init__(self, x, y, color):
        super().__init__(self)######################
        self.x = x
        self.y = y

        self.green = (color == "green")
        self.colors("gray", "orange", "red")
        self.color = 0 # color is gray

        self.t = Turtle()
        self.t.penup()
        self.t.shape("square")

        self.set_color(color) #gray
        self.goto()
        self.t.goto(self.x, self.y)

    def color(self, color):
        self.t.color(color)

    def move_down(self, speed = 1):
        self.y -= speed
        self.t.goto(self.x, self.y)

    def hit(self):
        if self.green:
            self.explode() #green ones explode
        else:
            self.color += 1
            if self.color >= len(self.colors):
                self.die # while gray ones just disapear
            else:
                self.set_color(self.colors[self.color])

        def explode(self):
            explode_radius = 20
            for block in blocks[:]:
                distance = self.t.distance(block.t)
                if distance < explode_radius:
                    block.die()

        def die(self):
            self.t.ht()
            if self in blocks:
                blocks.remove(self)


class Bullet:
    def __init__(self,x,y, color):
        self.x = x
        self.y = y
        self.t = Turtle()
        self.t.penup()
        self.t.shape("circle")
        self.t.color("white")
        self.t.shapesize(0.3, 0.3)
        self.t.goto(self.x, self.y)

    def move(self):
        self.y += 10
        self.t.goto(self.x, self.y)

    def collision(self, block):
        return self.t.distance(block.t) < 20

class Score:
    def __init__(self):

        self.score = 0

        self.t = Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.color("hot pink")

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

game_over = False

def game_over():

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


score = Score()



blocks = []

for y in range(200, 100, -20):
    for x in range(-200, 220,20):
        if len(blocks) % 3 == 0:
            color = "green"
        else:
            color = "grey"
        blocks.append(Block(x, y, color))

bullets = []

def shoot():
    bullets.append(Bullet(player.x, player.y))

player = Player()
screen.listen()
screen.onkeypress(self.left, "Left")
screen.onkeypress(self.right, "Right")
screen.onkeypress(shoot, "Space")

while True:
    for block in blocks[:]:
        block.move_down(0.2)
        if block.y < -320:
            block.y = 250
            block.t.goto(block.x, block.y)

    for bullet in bullets[:]:
        bullet.move()
        if bullet.y > 320:
            bullet.t.hideturtle()
            bullets.remove(bullet)
            continue
        for block in blocks[:]:
            if bullet.collision(block):
                block.hit()
                bullet.t.ht()
                if bullet in bullets:
                    bullets.remove(bullet)
                    break
    
    screen.update()




screen.exitonclick()
