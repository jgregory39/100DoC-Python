import turtle
import pandas

FONT = ('Arial', 8, 'normal')
#Initialize Screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer()

#Intitialize data
data = pandas.read_csv('50_states.csv')
remaining_states = data.state.to_list()
guessed_states = []

#Add state to map
def label_state(state):
    state_data = data[data.state == state]
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()

    writer.goto(int(state_data.x), int(state_data.y))
    writer.write(state, align='center', font=FONT)

#Main Game
game_is_on = True
while game_is_on:
    #Collect Answer
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="What's another state's name?").title()

    #Exit Game
    if answer_state == "Exit":
        game_is_on == False
        break

    # Check Answer
    if answer_state in remaining_states:
        guessed_states.insert(0, answer_state)
        remaining_states.remove(answer_state)
        label_state(answer_state)

#End Game
missed_states = pandas.DataFrame({"Missed States": remaining_states})
missed_states.to_csv("states_to_learn")
exit()

