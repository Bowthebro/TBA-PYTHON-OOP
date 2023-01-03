# TEXT BASED ADVENTURE. OOP. PYTHON PROGRAM #

# defines Level class
class Level:
    def __init__(self):
        self.name = ""
        self.description = None
        self.gates = None
        self.items = None

    #  defines level setup function, defines instances of level class
    def setup(self, name, gates, text, items):
        self.name = name
        self.gates = gates
        self.description = text
        self.items = items

    # defines enter function, gives player info of area
    def enter(self):
        print("\n", self.description)

        # for loop to print gates in player location
        if len(self.gates) > 1:
            print("There is a gate to", end=' ')
            for g in self.gates:
                g.print_gates()

        elif len(self.gates) == 1:
            print("There is a gate to", end=' ')
            for g in self.gates:
                g.print_gate()

        if player_sword.picked_up is False and the_player.location == start_area:
            print("There is a sword that resonates as you grow closer")

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)


# defines gate class
class Gate:

    def __init__(self, direction, gate_to):
        self.gate_to = gate_to
        self.direction = direction

    # defines is gate function, returns direction of gate
    def is_gate(self, text):
        return self.direction in text

    # defines print gate function, prints direction of gate
    def print_gates(self):
        print("the %s," % self.direction)

    def print_gate(self):
        print("the %s." % self.direction)


# defines player class
class Player:

    def __init__(self, name, player_level, inventory):
        self.health = 100
        self.name = name
        self.location = player_level
        self.inventory = inventory

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


def print_sword():
    print("a sword that resonates as you grow closer")


# initialises Levels
start_area = Level()
deep_forest_area = Level()

player_sword = Sword("", "", "")

# start area setup
gate1 = Gate("north", deep_forest_area)
start_area.setup("forest", [gate1], "You are in a dusk lit forest surrounded by trees. "
                                    "The only direction is deeper into the forest.", player_sword)

# deep forest area (level 2) setup
gate1 = Gate("south", start_area)
deep_forest_area.setup("deep forest", [gate1], "You are in a seemingly endless tunnel of dark oak trees.", [])


# defines function to loop player for incorrect answers
def incorrect_answer_loop(answers):
    while True:
        user_input_for_loop = str.lower(input(">"))

        if user_input_for_loop in answers:
            return user_input_for_loop

        else:
            print("Incorrect input")
            continue


# defines sequence for players Sword creation
def sword_sequence():
    print("You are offered a sword.\n")

    # asks user for input/type of Sword. Uses while loop to stop incorrect input breaking program
    print("What type of sword. \n Options: katana, claymore, dagger")

    # puts player in loop to collect Sword type
    player_sword.sword_type = incorrect_answer_loop({"katana", "claymore", "dagger"})

    print("Your sword type is:", player_sword.sword_type, "\n")

    # asks user input and stores as variable, lets player use whatever colour.
    print("What colour sword.")
    player_sword.colour = str.lower(input(">"))

    print("Your sword colour is:", player_sword.colour, "\n")

    # asks user what damage type they want, using a while loop for accepted input
    print("What damage type.\n Options: holy, blood, fire")

    # puts player in loop to collect damage type
    player_sword.damage_type = incorrect_answer_loop({"holy", "blood", "fire"})

    # prints Sword stats to player
    print("Your swords damage type is:", player_sword.damage_type, "\n")


# defines commands in list
commands = ["go (direction)", "look"]

# begins sword sequence (disabled for bug testing)
# sword_sequence()

# asks name and stores in player instance
print("What is your name.")
user_input = input(">")
the_player = Player(user_input, start_area, [])

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
            print("\n", the_player.location.description)

    # tells player the commands when asked
    if user_input == "help":
        print("\nthe commands are:", commands)

    # gives player location information
    elif user_input == "look":
        the_player.location.enter()
