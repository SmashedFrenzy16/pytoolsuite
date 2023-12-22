import random
import matplotlib.pyplot as plt
from tkinter import *
import time
from time import strftime
import turtle
import numpy as np
import sys
import os
import datetime
from rich import print
import platform
from segno import *
from github import Github


class Phone:
    def __init__(self, hardware, cover):
        self.hardware = hardware
        self.cover = cover


class turtleShapes:
    def filled_rectangle(horizontal, vertical, color):
        turtle.pendown()
        turtle.pensize(1)
        turtle.color(color)
        turtle.begin_fill()
        for counter in range(2):
            turtle.forward(horizontal)
            turtle.right(90)
            turtle.forward(vertical)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()

    def filled_star(length, points, color):
        turtle.penup()
        angle = 180 - (180/points)
        turtle.color(color)
        turtle.begin_fill()
        for point in range(points):
            turtle.forward(length)
            turtle.right(angle)
        turtle.end_fill()
        turtle.penup()

    def any_filled_polygon(length, angles, color):
        sumangle = (angles - 2) * 180
        oneangle = (sumangle/angles) - 180
        turtle.color(color)
        turtle.pensize(1)
        turtle.begin_fill()
        turtle.pendown()
        for counter in range(angles):
            turtle.forward(length)
            turtle.right(oneangle)
        turtle.end_fill()
        turtle.penup()

    def unfilled_rectangle(horizontal, vertical, color, pensize):
        turtle.pendown()
        turtle.pensize(pensize)
        turtle.color(color)
        for counter in range(2):
            turtle.forward(horizontal)
            turtle.right(90)
            turtle.forward(vertical)
            t.right(90)
        turtle.penup()

    def unfilled_star(length, points, color, pensize):
        turtle.pendown()
        angle = 180 - (180/points)
        turtle.color(color)
        turtle.pensize(pensize*2)
        for point in range(points):
            turtle.forward(length)
            turtle.right(angle)
        turtle.penup()
        turtle.right((angle/4))
        turtle.forward(pensize/4)
        turtle.setheading(0)
        turtle.pensize(1)
        turtle.forward(pensize/4)
        turtle.color('#FFFFFF')
        turtle.pendown()
        turtle.begin_fill()
        for point in range(points):
            turtle.forward(length - (pensize))
            turtle.right(angle)
        turtle.end_fill()
        turtle.penup()

    def any_unfilled_polygon(length, angles, color, pensize):
        sumangle = (angles - 2) * 180
        oneangle = (sumangle/angles) - 180
        turtle.color(color)
        turtle.pensize(pensize)
        turtle.pendown()
        for counter in range(angles):
            turtle.forward(length)
            turtle.right(oneangle)
        turtle.penup()

def about():

    print("PytoolSuite Version 4.0")


def biography():

    name = input("Enter your name: ")

    dob = input("Enter your Date of Birth: ")

    address = input("Enter your address: ")

    pg = input("Enter your Personal Goals: ")

    print(f"Name: {name}")

    print(f"Date of Birth: {dob}")

    print(f"Address: {address}")

    print((f"Personal Goals: {pg}"))

def bmi_calc(height_in, weight_lb):

    bmi = (weight_lb/(pow(height_in, 2))) * 703

    print(f"BMI: {bmi}")

def calc(number1, operator, number2):

    num1 = float(number1)

    op = operator

    num2 = float(number2)

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


def celebration_countdown(day, month, year, message_for_end_celebration):

    celebration = datetime.datetime(year, month, day)

    delta = datetime.timedelta(microseconds=-0.0000000000001)

    close = datetime.timedelta(seconds=60)

    while True:

        timeleft = celebration - datetime.datetime.now()
        secondsleft = timeleft.total_seconds()
        hours, remainder = divmod(secondsleft, 3600)
        minutes, seconds = divmod(remainder, 60)

        if timeleft < close:

            if timeleft < delta:

                print(
                    f"[bold red]{message_for_end_celebration} :partying_face:[/]")

                break

            else:

                print(f"[bold]{int(seconds)} seconds[/]")

        else:

            print(
                f"{int(hours)} hours : {int(minutes):02d} minutes : {int(seconds):02d} seconds")

        time.sleep(1)


def code_comment_rem(from_file_p, to_file_p):

    with open(from_file_p) as file:

        contents = file.readlines()

    open_paren_count = 0

    closed_paren_count = 0

    decrease_count = 0

    for num in range(len(contents)):

        if "#" in contents[num - decrease_count]:

            if contents[num - decrease_count].startswith("#"):

                contents.remove(contents[num - decrease_count])

                decrease_count += 1

            else:

                nline = ""

                for char in contents[num - decrease_count]:

                    if char == '(':

                        open_paren_count += 1

                        nline += char

                    elif char == ')':

                        closed_paren_count += 1

                        nline += char

                    elif char == '#' and open_paren_count == closed_paren_count:

                        break

                    else:

                        nline += char

                contents.remove(contents[num - decrease_count])

                contents.insert(num - decrease_count, nline)

    with open(to_file_p, "w") as nfile:

        nfile.writelines(contents)

def collatz_conjecture(numbers):

    n = numbers

    while n != 1:

        if (n % 2) == 0:

            n = n // 2

        else:

            n = (n * 3) + 1

        print(n)

def create_doc(doc_name_with_ext):

    PythonDoc = open(doc_name_with_ext, "w")
    PythonDoc.write("")

    PythonDoc.close

def fahrenheit_celcius(start_temp, end_temp, increment):
    lower_temperature = start_temp
    step_temperature = increment
    upper_temperature = end_temp

    fahr = lower_temperature
    while (fahr <= upper_temperature):
        celcius = (5.0/9.0) * (fahr-32.0)
        print(fahr, celcius)
        fahr = fahr + step_temperature

def fibonacci_sequence(terms):

    xterms = terms

    x1, x2 = 0, 1

    count = 0

    if xterms <= 0:

        print("Error! Please enter a positive integer!")

    elif xterms == 1:

        print(x1)

    else:

        while count < xterms:

            print(x1)

            newx = x1 + x2

            x1 = x2

            x2 = newx

            count += 1

def file_size_calc(file_with_ext):

    file_size = os.path.getsize(file_with_ext)

    print(f"File size: {file_size}B")

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

def github_find_repo_by_topic(token, number_of_repos_to_display, topic):

    g_cred = Github(f"{token}")

    count = int(number_of_repos_to_display)

    repo_count = count

    icount = 0

    for i in g_cred.search_repositories(f"topic:{topic}"):

        print(f"{icount + 1}. {i}")

        icount += 1

        if icount >= repo_count:

            break

def github_repo_stars(token, repo_name):

    g_cred = Github(f"{token}")

    repo = g_cred.get_repo(repo_name)

    print(repo.stargazers_count)

def my_sys_info():

    print('System info:', platform.system())

def nrr_calc(runs_s, overs_f, runs_c, overs_b):

    nrr = (runs_s / overs_f) - (runs_c / overs_b)

    print(f"Net Run Rate: {nrr}")

def odd_or_even():
    main = int(input("Enter a number: "))

    if (main % 2) == 0:
        print("{} is an even number.".format(main))
    else:
        print("{} is an odd number.".format(main))


def ping(address):

    ipAddress = address

    os.system(f"ping {ipAddress}")


def prime_factors(num):
    def Quotient():
        quotient = 1
        for n in PrimeFactor:
            quotient *= n
        return quotient
    number = abs(num)
    x = num
    global PrimeFactors
    PrimeFactor = []
    composites = set(j for i in range(2, math.ceil(math.sqrt(number)))
                     for j in range(i*2, number, i))
    primes = [x for x in range(2, number) if x not in composites]
    for prime in primes:
        while x % prime == 0:
            PrimeFactor.append(prime)
            x /= prime
    if num != number:
        PrimeFactor.append(-1)
    if PrimeFactor.sort() != None:
        PrimeFactor = PrimeFactor.sort()
    factor_str = ''
    for y in PrimeFactor:
        z = PrimeFactor.count(y)
        if z == 1:
            factor_str += (f' * {y}')
        else:
            factor_str += (f' * {y}^{z}')
        for counter in range(z-1):
            PrimeFactor.pop(0)
    print('The prime factors of ' + str(num) + ' are' + factor_str[2:])


def qr_gen(contents, backg, foreg, data_b, data_f, file_name):

    code = make_qr(contents)

    code.save(
        file_name,
        scale = 10,
        dark = foreg,
        light = backg,
        data_dark = data_b,
        data_light = data_f

    )


def sample_graph():

    x = np.linspace(0, 2*np.pi)
    y = np.sin(x)

    plt.plot(x, y)

    plt.show()

def sci_calc():

    class SciCalc:

        def __init__(self, master):

            self.master = master

            master.title("Scientific Calculator by @SmashedFrenzy16")

            self.total = StringVar()

            self.entry = Entry(master, textvariable=self.total, borderwidth=5)
            self.entry.grid(row=0, column=0, columnspan=6, pady=6)

            self.button_creator()

        def button_creator(self):

            b_list = [
                [ 'sin', 'cos', 'tan', '^2', '^3'],
                ['log(x)', '1/x', 'x!', 'sqrt', 'cbrt'],
                ['7', '8', '9', 'C', 'pi'],
                ['4', '5', '6', '*', '/'],
                ['1', '2', '3', '+', '-'],
                ['0', '.', '10^x', 'e', '=']
            ]

            for i, row in enumerate(b_list):

                for j, b_text in enumerate(row):

                    button = Button(self.master, text=b_text, width=5, height=3, command=lambda text=b_text: self.click(text))

                    button.grid(row=i + 1, column=j, sticky="nsew")
                
                self.master.rowconfigure(i + 1, weight=1)
            self.master.columnconfigure(0, weight=1)
            self.master.columnconfigure(1, weight=1)
            self.master.columnconfigure(2, weight=1)
            self.master.columnconfigure(3, weight=1)
            self.master.columnconfigure(4, weight=1)
            self.master.columnconfigure(5, weight=1)

        def click(self, b_text):

            if b_text == '=':

                try:

                    result = eval(self.entry.get())

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            elif b_text == 'C':

                    self.total.set("")

            elif b_text == 'sin':

                try:

                    result = sin(radians(float(self.entry.get())))

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            elif b_text == 'cos':

                try:

                    result = cos(radians(float(self.entry.get())))

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            elif b_text == 'tan':

                try:

                    result = tan(radians(float(self.entry.get())))

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            elif b_text == '^2':

                try:

                    result = float(self.entry.get()) ** 2

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            elif b_text == '^3':

                try:

                    result = float(self.entry.get()) ** 3

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            elif b_text == 'log(x)':

                try:

                    result = log(float(self.entry.get()))

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            elif b_text == '1/x':

                try:

                    result = 1 / float(self.entry.get())

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            elif b_text == 'x!':

                try:

                    result = factorial(int(self.entry.get()))

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            elif b_text == 'sqrt':

                try:

                    result = sqrt(float(self.entry.get()))

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            elif b_text == 'cbrt':

                try:

                    result = cbrt(float(self.entry.get()))

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            elif b_text == '10^x':

                try:

                    result = 10 ** float(self.entry.get())

                    self.total.set(result)

                except:

                    self.total.set("Error!")
                    
            elif b_text == 'pi':

                try:

                    result = pi

                    self.total.set(result)

                except:

                    self.total.set("Error!")
                    
            elif b_text == 'e':

                try:

                    result = e

                    self.total.set(result)

                except:

                    self.total.set("Error!")

            else:

                self.total.set(self.entry.get() + b_text)


    if __name__ == "__main__":

        root = Tk()

        calc = SciCalc(root)

        root.mainloop()


def snake():

    # smashedfrenzy16's snake game

    delay = 0.1

    score = 0
    high_score = 0

    win = turtle.Screen()
    win.title("Snake")
    win.bgcolor("black")
    win.setup(width=800, height=600)
    win.tracer(0)

    head = turtle.Turtle()
    head.shape("square")
    head.color("white")
    head.up()
    head.goto(0, 0)
    head.direction = "Stop"

    food = turtle.Turtle()
    colors = random.choice(['red', 'orange', 'green'])
    food.speed(0)
    food.shape("square")
    food.color(colors)
    food.up()
    food.goto(0, 100)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Score: 0  High Score: 0", align="center",
              font=("arial", 24, "bold"))

    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y+20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y-20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x-20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x+20)

    win.listen()
    win.onkeypress(go_up, "w")
    win.onkeypress(go_down, "s")
    win.onkeypress(go_left, "a")
    win.onkeypress(go_right, "d")
    win.onkeypress(go_up, "Up")
    win.onkeypress(go_down, "Down")
    win.onkeypress(go_left, "Left")
    win.onkeypress(go_right, "Right")

    segments = []

    while True:

        win.update()

        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:

            time.sleep(1)

            head.goto(0, 0)

            head.direction = "Stop"

            colors = random.choice(['red', 'blue', 'green'])

            for segment in segments:

                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()

            pen.write("Score: {} High Score: {} ".format(
                score, high_score), align="center", font=("arial", 24, "bold"))

        if head.distance(food) < 20:

            x = random.randint(-270, 270)

            y = random.randint(-270, 270)

            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.up()
            segments.append(new_segment)

            delay -= 0.001

            score += 1

            if score > high_score:

                high_score = score

            pen.clear()

            pen.write("Score: {} High Score: {} ".format(
                score, high_score), align="center", font=("arial", 24, "bold"))

        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()

        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                colors = random.choice(['red', 'blue', 'green'])
                for segment in segments:
                    segment.goto(1000, 1000)
                segment.clear()

                score = 0
                delay = 0.1
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("arial", 24, "bold"))
        time.sleep(delay)

    win.mainloop()


def show_time():

    root = Tk()

    root.title("Digital Clock")

    root.geometry("235x60")

    clock = Label(root, fg="black", font=("Arial", 30, 'bold'))

    clock.place(x=0, y=0)

    def digital_clock():
        time = strftime('%H: %M: %S')

        clock.configure(text=time)

        clock.after(1000, digital_clock)

    digital_clock()

    root.mainloop()


def timer(time_in_seconds):

    t = time_in_seconds

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Blast Off!!!')


def turtle_paint():
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


def word_counter(sentence):

    words_split = sentence.split()

    word_count = len(words_split)

    print(f"Word count: {word_count}")
