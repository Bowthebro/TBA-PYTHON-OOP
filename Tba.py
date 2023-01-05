# TEXT BASED ADVENTURE. OOP. PYTHON PROGRAM #

# START OF CLASSES AND INITIALISING

# defines level class
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

        # for loop to print gate in player location
        elif len(self.gates) == 1:
            print("There is a gate to", end=' ')
            for g in self.gates:
                g.print_gate()

        # for loop to print items for use in a for loop
        if len(self.items) > 1:
            print("There is", end=' ')
            for i in self.items:
                i.print_items()

        # for loop to print item for use in a for loop
        elif len(self.items) == 1:
            print("There is", end=' ')
            for i in self.items:
                i.print_item()

    # removes item from level for use in take function
    def remove_item(self, item):
        self.items.remove(item)

    # adds item to level for use in drop function
    def add_item(self, item):
        self.items.append(item)


# defines gate class
class Gate:

    def __init__(self, direction, gate_to):
        self.gate_to = gate_to
        self.direction = direction

    # returns direction of gate
    def is_gate(self, text):
        return self.direction in text

    # prints direction of gate
    def print_gates(self):
        print("the %s," % self.direction)

    # second print gate function for grammar reasons
    def print_gate(self):
        print("the %s." % self.direction)


# defines player class
class Player:

    def __init__(self, name, player_level):
        self.health = 100
        self.name = name
        self.location = player_level
        self.inventory = []

    # changes player location
    def move(self, player_level):
        self.location = player_level

    # adds items to player inventory and removes from level
    def take(self, take_user_input):
        for i in self.location.items:
            if i.name in take_user_input:
                self.inventory.append(i)
                print("you take a %s" % i.name)
                self.location.remove_item(i)
            else:
                print("?")

    # removes item from inventory and adds to level
    def drop(self, drop_user_input):
        success = False
        for i in self.inventory:
            if i.name in drop_user_input:
                self.inventory.remove(i)
                self.location.add_item(i)
                print("You drop the %s" % i.name)
                success = True
        if not success:
            print("?")

    # prints inventory
    def print_inventory(self):
        print("Your inventory: ")
        for i in self.inventory:
            print("%s," % i.name)


# defines item class
class Item:

    def __init__(self, name):
        self.name = name

    # function called for use in a for loop to print item
    def print_item(self):
        print("a %s." % self.name)

    # function called for use in a for loop to print list of items
    def print_items(self):
        print("a %s," % self.name)


# defines commands in list
commands = ["go (direction)", "look", "take (item)", "inventory", "drop (item)"]

# initialises levels
start_area = Level()
deep_forest_area = Level()

# initialises sword instance
player_sword = Item("sword")

# start area setup
gate1 = Gate("north", deep_forest_area)
start_area.setup("forest", [gate1], "You are in a dusk lit forest surrounded by trees. "
                                    "The only direction is deeper into the forest.", [player_sword])

# deep forest area setup
gate1 = Gate("south", start_area)
deep_forest_area.setup("deep forest", [gate1], "You are in a seemingly endless tunnel of dark oak trees.", [])


# END OF CLASSES AND INITIALISING

# START OF FUNCTIONS AND MAIN GAME LOOPS

# defines function to loop player for incorrect answers
def incorrect_answer_loop(answers):
    while True:
        user_input_for_loop = str.lower(input(">"))

        if user_input_for_loop in answers:
            return user_input_for_loop

        else:
            print("?")
            continue


# defines function for players sword creation
def sword_sequence():
    # print functions will not be commented because they are straight forward

    print("You are offered a sword.\n")

    print("What type of sword. \n Options: katana, claymore, dagger")

    # puts player in loop to collect sword type
    player_sword.sword_type = incorrect_answer_loop({"katana", "claymore", "dagger"})

    print("Your sword type is:", player_sword.sword_type, "\n")

    print("What colour sword.")

    # puts player in loop to collect sword colour
    player_sword.colour = str.lower(input(">"))

    print("Your sword colour is:", player_sword.colour, "\n")

    print("What damage type.\n Options: holy, blood, fire")

    # puts player in loop to collect damage type
    player_sword.damage_type = incorrect_answer_loop({"holy", "blood", "fire"})

    print("Your swords damage type is:", player_sword.damage_type, "\n")

    print("Your sword is finished.\n")


# begins sword sequence
sword_sequence()

# asks name and stores in player instance
print("What is your name.")
user_input = input(">")
the_player = Player(user_input, start_area)

# gives player information and area setting
print("\n(Cry help for commands)")
print(start_area.description)

# starts game loop
while user_input != "exit":

    # asks user for input and stores as lower case
    user_input = str.lower(input(">"))

    # looks for direction in input and if the direction is valid, moves player in that direction
    for d in the_player.location.gates:
        if d.is_gate(user_input):
            the_player.move(d.gate_to)
            print("\n", the_player.location.description)

    # tells player the commands when asked
    if "help" in user_input:
        print("\nthe commands are:", commands)

    # gives player location information
    elif "look" in user_input:
        the_player.location.enter()

    # takes items from level and gives to player
    elif "take" in user_input:
        the_player.take(user_input)

    # prints inventory to player
    elif "inventory" in user_input:
        the_player.print_inventory()

    # takes items from player and gives to level
    elif "drop" in user_input:
        the_player.drop(user_input)
