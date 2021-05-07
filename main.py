# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1

# Create variable for every player that scored 
goal_0_player = "Ruud Gullit"
goal_1_player = "Marco van Basten"

# Create a variable for each minute of the match that a goal was scored in
goal_0 = 32
goal_1 = 54

# Using + create a string that reports on who scored when
goal_0_total = goal_0_player + " " + str(goal_0)
goal_1_total = goal_1_player + " " + str(goal_1)

scorers = goal_0_total + ", " + goal_1_total
print(scorers)

# Create a single string with information about who scored when
report = f"{goal_0_player} scored in the {goal_0}nd minute\n{goal_1_player} scored in the {goal_1}th minute"
print(report)

# Part 2

player = "Erwin Koeman"
first_name = player[0:player.find(" ")]
last_name_len = len(player[player.find(" ")+1:])
name_short = player[0] + ". " + player[player.find(" ")+1:]

chant = ' '.join([first_name + "!"] * len(player[0:player.find(" ")]))

good_chant = chant[-1] != " "
