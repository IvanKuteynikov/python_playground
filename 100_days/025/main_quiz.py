import turtle
import pandas as pd

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("US States")
turtle.addshape(image)

turtle.shape(image)


data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()

game_is_on = True
n = 0
total = len(data)
states_user_know = []


while game_is_on:
    answer_input = screen.textinput(title=f"{n}/{total} guessed States", prompt="What's another state name?: ").title()
    if answer_input == 'Quit':
        game_is_on = False
        missing_states = [state for state in all_states if state not in states_user_know]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('missing_states.csv')
        break
    if answer_input in all_states and answer_input in states_user_know:
        continue
    if answer_input in all_states:
        state_data = data[data['state'] == answer_input]
        turtle.penup()
        turtle.teleport(state_data.x.item(), state_data.y.item())
        turtle.write(state_data.state.item(), align='left', font=('Arial', 8, 'normal'))
        turtle.teleport(0, 0)
        n += 1
        states_user_know.append(answer_input)
        if n == total:
            game_is_on = False



#turtle.mainloop()
