import random
import pygame
import matplotlib.pyplot as plt
from tkinter import *
import time
import turtle
import numpy as np

class Phone:
    def __init__(self, hardware, cover):
        self.hardware = hardware
        self.cover = cover


def biography():

    name = input("Enter your name: ")

    dob = input("Enter your Date of Birth: ")

    address = input("Enter your address: ")

    pg = input("Enter your Personal Goals: ")

    print("Name: {}".format(name))

    print("Date of Birth: {}".format(dob))

    print("Address: {}".format(address))

    print(("Personal Goals: {}").format(pg))


def calc():

    num1 = float(input("Enter your first number: "))

    op = input("Enter your operator: ")

    num2 = float(input("Enter your second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("Invalid operator!")

def createPythonDoc():
    
    PythonDoc = open("doc.py", "w")
    PythonDoc.write("")
    
    
    PythonDoc.close

def fahrenheitCelcius():
    lower_temperature = 0
    step_temperature = 20
    upper_temperature = 300

    fahr = lower_temperature
    while(fahr <= upper_temperature):
        celcius = (5.0/9.0) * (fahr-32.0)
        print(fahr, celcius)
        fahr = fahr + step_temperature


def form():
    root = Tk()

    entry1 = Entry(root, width=50, borderwidth=5)
    entry1.grid(row=0, column=0)
    entry1.insert(0, "First Name")

    entry2 = Entry(root, width=50, borderwidth=5)
    entry2.grid(row=1, column=0)
    entry2.insert(0, "Last Name")

    entry3 = Entry(root, width=50, borderwidth=5)
    entry3.grid(row=2, column=0)
    entry3.insert(0, "Email")

    def execution():
        entries = entry1.get()
        entries2 = entry2.get()
        entries3 = entry3.get()
        label = Label(root, text=entries)
        label.grid(row=4, column=0)
        label2 = Label(root, text=entries2)
        label2.grid(row=5, column=0)
        label3 = Label(root, text=entries3)
        label3.grid(row=6, column=0)

    button = Button(root, text="Enter", command=execution)
    button.grid(row=3, column=0)

    root.mainloop()

def OddOrEven():
    main = int(input("Enter a number: "))


    if (main % 2) == 0:
        print("{} is an even number.".format(main))
    else:
        print("{} is an odd number.".format(main))

def sampleGraph():

    x = np.linspace(0, 2*np.pi)
    y = np.sin(x)

    plt.plot(x, y)

    plt.show()


def snake():

    #smashedfrenzy16's snake game


    pygame.init()

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (216, 50, 80)
    green = (0, 255, 0)
    blue = (100, 153, 213)

    dis_width = 1000
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game by SmashedFrenzy16 Copied For Some')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 7

    font_style = pygame.font.SysFont("snellroundhand", 45)
    score_font = pygame.font.SysFont("comicsansms", 35)


    def Your_score(score):
        value = score_font.render("Score: " + str(score), True, black)
        dis.blit(value, [0, 0])


    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])


    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(green)
                message("You Lose! Press C to Play Again or Q to Quit.", red)
                Your_score(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(green)
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(
                    0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(
                    0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()


    gameLoop()

def turtlePaint():
    wn = turtle.Screen()

    wn.title("Turtle Draw Program")
    wn.setup(width=800, height=600)

    pen = turtle.Turtle()
    pen.shapesize(10)

    def f():
        pen.color("red")
        y = pen.ycor()
        pen.sety(y + 100)

    def b():
        pen.color("blue")
        y = pen.ycor()
        pen.sety(y - 100)

    def l():
        pen.color("green")
        x = pen.xcor()
        pen.setx(x-100)

    def r():
        pen.color("yellow")
        x = pen.xcor()
        pen.setx(x+100)

    wn.listen()
    wn.onkeypress(f, "Up")
    wn.onkeypress(b, "Down")
    wn.onkeypress(l, "Left")
    wn.onkeypress(r, "Right")

    while True:
        wn.update()

def wordCounter():
    print("What's on you mind today?")

    response = input("Enter your response: ")

    words_split = response.split()

    word_count = len(words_split)


    print("Wow, you just answered me in {}".format((word_count)),"words!")
    
numbers_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    
sampleInput = input("Sample input: ")

helloWorld = print("Hello World")
