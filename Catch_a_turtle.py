#-----import statements-----

import turtle as turt
import random as rand
import leaderboard as lb

#-----game configuration-----

# all the variable used
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
spot_speed = 0
score = 0
timer = 10
counter_interval = 1000
timer_up = False
colors = [ "red", "blue", "green", "yellow", "purple", "orange",
          "white", "gray", "cyan", "magenta", "lime",
          "navy", "maroon", "violet", "indigo"]
sizes = [ 4, 3.2, 3, 2.8, 2.6, 2.4, 
          2.2, 2, 1.8, 1.6, 1.4, 
          1.2, 1, 0.9, 0.7, 0.5 ]
font_setup = ("Arial", 20, "normal")
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("what is your name? ")


#-----initialize the turtles-----

# creates the screen
wn = turt.Screen()
wn.bgcolor("black")

# the turtle used to play the game by clicking on it
spot = turt.Turtle()
spot.hideturtle()
spot.speed(spot_speed)
spot.pensize(spot_size)
spot.shape(spot_shape)
spot.fillcolor(spot_color)

# writes the score
write = turt.Turtle()
write.speed(0)
write.hideturtle()
write.penup()
write.pencolor("gold")
write.goto(-180,170)
write.pendown()

# writes the timer
counter = turt.Turtle()
counter.speed(0)
counter.hideturtle()
counter.penup()
counter.pencolor("gold")
counter.goto(-180,200)
counter.pendown()

# writes the start screen
start = turt.Turtle()
start.speed(0)
start.penup()
start.hideturtle()
start.shape("square")
start.pencolor("blue")
start.fillcolor("blue")
start.turtlesize(10)
start.stamp()
start.pencolor("red")
start.goto(0,40)
start.write("Click", font=("Arial", 40,), align="center")
start.goto(0,0)
start.write("To", font=("Arial", 40,), align="center")
start.goto(0,-40)
start.write("Start", font=("Arial", 40,), align="center")
start.goto(0,-65)
start.fillcolor("red")
start.turtlesize(3.5)
start.showturtle()

#-----game functions-----

# used to show start screen and starts the game when clicked
def start_game(x,y):
    # sets bg color and clears start screen while writing the score
    wn.bgcolor("white")
    start.clearstamps()
    start.clear()  
    start.hideturtle()
    write.write("score: 0", font=("Arial", 19, "normal"), align="center")
    spot.showturtle()
    countdown()

# handles when spot is clicked
def spot_clicked(x,y):
    global score
    # changes the bg color
    random_color = rand.choice(colors)
    wn.bgcolor(random_color)
    
    # increases score then displays it
    score += 1
    write.clear()
    write.write(f"score: {score}", font=("Arial", 19, "normal"), align="center")
    
    # chnages color and size of spot and hides it when game over
    change_size()
    change_color()
    change_position()
    spot.fillcolor(spot_color)
    change_size()
    if timer_up == True:
        spot.hideturtle()

# changes the position of the spot to random location
def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150,150)
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos,new_ypos)
    spot.pendown()
    spot.showturtle()

# changes color of the spot and stamp it
def change_color():
    new_color = rand.choice(colors)
    spot.fillcolor(new_color)
    spot.stamp()

#changes size of the spot
def change_size():
    new_size = rand.choice(sizes)
    spot.turtlesize(new_size)
    

# a count down i dont fully understand yet
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup, align="center")
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup, align="center")
    timer -= 1
    wn.ontimer(countdown, counter_interval) 

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

#----------events----------

# a event the start game and play the game
start.onclick(start_game)
spot.onclick(spot_clicked)

wn.mainloop()
