import turtle as t

from random import randint

# screen settings
WIDTH, HEIGHT = 1500, 800
screen = t.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)

# turtle settings
leo = t.Turtle()
leo.pensize(3)
leo.speed(0)
leo.setpos(0, -HEIGHT // 2)
leo.color('green')

# l- system settings
gens = 11
axiom = 'XY'
chr_1, rule_1 = 'X', 'F[@[-X]+X]'
step = 80
angle = lambda: randint(0, 45)
stack = []
color = [0.35, 0.2, 0.0]
thickness = 20


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


# print information
t.pencolor('white')
t.goto(-WIDTH // 2 + 60, -HEIGHT // 2 - 100)
t.clear()
t.write(f'generation: {gens}', font=('Arial', 50, 'normal'))


axiom = get_result(gens, axiom)

leo.left(90)
leo.pensize(thickness)
for chr in axiom:
    leo.color(color)
    if chr == 'F' or chr == 'X':
        leo.forward(step)
    elif chr == '@':
        step -= 6
        color[1] += 0.05
        thickness -= 2
        thickness = max(1, thickness)
        leo.pensize(thickness)
    elif chr == '+':
        leo.right(angle())
    elif chr == '-':
        leo.left(angle())
    elif chr == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_, thickness, step, color[1]))
    elif chr == ']':
        angle_, pos_, thickness, step, color[1] = stack.pop()
        leo.pensize(thickness)
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

screen.exitonclick()
