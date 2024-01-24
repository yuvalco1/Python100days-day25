import turtle
import csv
import pandas

data = pandas.read_csv("50_states.csv")
states = list(data.state)
print(states)


def get_mouse_click_coor(x, y):
    print(x, y)


screen = turtle.Screen()
screen.title("US states game")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

for i in range(50):
    state_guess = turtle.textinput(title=f"Guess the state {i}/50",
                                   prompt="What's another state's name?").title()
    if state_guess == "exit":
        break
    elif state_guess in states:
        print(state_guess)
        state_data = data[data.state == state_guess]
        print(state_data)
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.color("black")
        state_name.write(state_guess)
        states.remove(state_guess)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
