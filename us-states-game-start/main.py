# สร้างเกมทายมลรัฐของอเมริกา version 2 หลังจากไม่ได้เรียน code เลยเป็นเวลา 11 วันเพราะฝึกงานอยู่

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./us-states-game-start/us-states-game-start/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data_state = pandas.read_csv("./us-states-game-start/us-states-game-start/50_states.csv")

state_list = data_state.state.to_list()
position_x_list = data_state.x.to_list()
position_y_list = data_state.y.to_list()
state_remain = []

again = True
while again:
    answer_state = screen.textinput(title=f"{len(state_remain)}/{len(state_list)} States correct", prompt="What another state's name?").title()

    if answer_state in state_list:
        if len(state_remain) >= 50:
            again = False
        else:
            state_remain.append(answer_state)
            position_state = state_list.index(answer_state)
            
            style = ('Courier', 9, 'italic')
            timmy = turtle.Turtle()
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(position_x_list[position_state], position_y_list[position_state])
            timmy.write(answer_state, font=style, align="center")

    elif answer_state == "Exit":
        overcome_states = []
        for n in state_list:
            if n not in state_remain:
                overcome_states.append(n)
        csv_overcome_states = pandas.DataFrame(overcome_states)
        state_to_learn = csv_overcome_states.to_csv("./us-states-game-start/us-states-game-start/state_to_learn.csv")
        again = False

    else:
        pass


screen.exitonclick()