# TEXT BASED ADVENTURE. OOP. PYTHON PROGRAM #

# defines Level class
class Level:
    def __init__(self):
        self.name = ""
        self.description = None
        self.gates = None

    #  defines level setup function, defines instances of level class
    def setup(self, name, gates, text):
        self.name = name
        self.gates = gates
        self.description = text

    # defines enter function, gives player info of area
    def enter(self):
        print(self.description)

        # for loop to print gates in player location
        # (weird error causing 'none' value to appear)
        if len(self.gates) >= 1:
            print("there is a gate to ", end=' ')
            for g in self.gates:
                g.print_gate()
        print("\n", end=' ')


# defines gate class
class Gate:

    def __init__(self, direction, gate_to):
        self.gate_to = gate_to
        self.direction = direction

    # defines is gate function, returns direction of gate
    def is_gate(self, text):
        return self.direction in text

    # defines print gate function, prints direction of gate
    def print_gate(self):
        print("the %s," % self.direction)


# defines player class
class Player:

    def __init__(self, name, player_level):
        self.health = 100
        self.name = name
        self.location = player_level

    # defines move function, changes player location
    def move(self, player_level):
        self.location = player_level


# defines sword class
class Sword:
    picked_up = False

    def __init__(self, sword_type, damage_type, colour):
        self.sword_type = sword_type
        self.damage_type = damage_type
        self.colour = colour


# initialises Levels
start_area = Level()
deep_forest_area = Level()

# start area setup
gate1 = Gate("north", deep_forest_area)
start_area.setup("forest", [gate1], "You are in a dusk lit forest surrounded by trees. "
                                    "The only direction is deeper into the forest.")

# deep forest area (level 2) setup
gate1 = Gate("south", start_area)
deep_forest_area.setup("deep forest", [gate1], "You are in a seemingly endless tunnel of dark oak trees.")


# defines function to loop player for incorrect answers
def incorrect_answer_loop(answers):
    while True:
        user_input_for_loop = input()

        if user_input_for_loop in answers:
            return user_input_for_loop

        else:
            print("incorrect input")
            continue


# defines sequence for players Sword creation
def sword_sequence():
    # defines players sword, adds default values to catch errors
    player_sword = Sword("claymore", "blood", "red")

    print("You are offered a sword.\n")

    # asks user for input/type of Sword. Uses while loop to stop incorrect input breaking program
    print("What type of sword. \n Options: katana, claymore, dagger")

    # puts player in loop to collect Sword type
    player_sword.sword_type = incorrect_answer_loop({"katana", "claymore", "dagger"})

    print("Your sword type is:", player_sword.sword_type, "\n")

    # asks user input and stores as variable, lets player use whatever colour.
    print("What colour sword.")
    player_sword.colour = input()

    print("Your sword colour is:", player_sword.colour, "\n")

    # asks user what damage type they want, using a while loop for accepted input
    print("What damage type.\n Options: holy, blood, fire")

    # puts player in loop to collect damage type
    player_sword.damage_type = incorrect_answer_loop({"holy", "blood", "fire"})

    # prints Sword stats to player
    print("\nYour sword type is", player_sword.sword_type, ", your sword colour is",
          player_sword.colour, ", and your swords damage type is", player_sword.damage_type, "\n")


# defines commands in list
commands = ["go (direction)", "look"]

# begins sword sequence (disabled for bug testing)
sword_sequence()

# asks name and stores in player instance
print("what is your name?")
user_input = input(">")
the_player = Player(user_input, start_area)

# gives player information and area setting
print("\n(Cry help for commands)")
print(start_area.description)

# starts game loop
while user_input != "exit":

    user_input = str.lower(input(">"))

    # looks for direction in input and if the direction is valid, moves player in that direction
    for d in the_player.location.gates:
        if d.is_gate(user_input):
            the_player.move(d.gate_to)
            print(the_player.location.description)

    # tells player the commands when asked
    if user_input == "help":
        print("the commands are:", commands)

    # gives player location information
    elif user_input == "look":
        the_player.location.enter()
