import turtle
import pandas


def write_to_map(answer_state, xcor, ycor):
    state_text = turtle.Turtle()
    state_text.penup()
    state_text.hideturtle()
    state_text.goto(xcor, ycor)
    state_text.write(answer_state)


correct_guesses = 0
correct_guesses_list = []
screen = turtle.Screen()
screen.title("United States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
df = pandas.DataFrame(states_data)

while len(correct_guesses_list) < 50:
    answer_state = screen.textinput(title=f"{correct_guesses} / 50 states correct", prompt="What's another state's name?:").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:

        filtered_rows = df[df.state == answer_state]
        state_dict = filtered_rows.to_dict('records')
        write_to_map(state_dict[0]['state'], state_dict[0]['x'], state_dict[0]['y'])
        correct_guesses += 1
        screen.title(f"States Guessed: {correct_guesses} / 50")
        correct_guesses_list.append(answer_state)




