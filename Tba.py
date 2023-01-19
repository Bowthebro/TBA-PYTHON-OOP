# TEXT BASED ADVENTURE. OOP. PYTHON PROGRAM #
#
# MAP OF GAME
#                #   #   #  #   #    #  #
#                #   moldy skeleton     #
#   #   #   #   #   #   #   ~   #   #   #    #  #
#   dense shrubs  /  cross roads  /   old tree  #
#   #   #   #   /   #   #   #   #   #   #   #   #
#    deep forest    #
#   #   /   #   #   #
#     start     #
#   #   #   #   #

# START OF CLASSES AND INITIALISING

# defines level class
class Level:
    def __init__(self):
        # defining variables to avoid pep-8 violations
        self.level_name = None
        self.level_description = None
        self.level_gates = None
        self.level_items = None

    #  defines level setup function, defines instances of level class
    def setup(self, level_name, level_gates, level_description, level_items):
        self.level_name = level_name  # defines name string for level
        self.level_gates = level_gates  # defines list of gates for level
        self.level_description = level_description  # defines description string for level
        self.level_items = level_items  # defines list of items in level

    # defines enter function, gives player info of area
    def enter(self):
        print(self.level_description)

        # for loop to print gate in player location
        if len(self.level_gates) >= 1:
            print("There are gates to:")
            for a in self.level_gates:
                a.print_gate()

        # for loop to print items for use in a for loop
        if len(self.level_items) >= 1:
            print("There is", end=" ")
            for i in self.level_items:
                i.print_item()

    # removes item from level for use in take function
    def remove_item(self, item):
        self.level_items.remove(item)

    # adds item to level for use in drop function
    def add_item(self, item):
        self.level_items.append(item)


# defines gate class
class Gate:

    def __init__(self, gate_direction, gate_to, locked, key):
        self.gate_to = gate_to  # defines the level the gate leads to
        self.gate_direction = gate_direction  # defines the direction the gate points to
        self.locked = locked  # defines a boolean for if the gate is locked
        self.key = key  # defines a string for what key is needed for lock

    # toggles lock on gate
    def toggle_lock(self):
        self.locked = not self.locked

    # defines unlock function for locked gates
    def unlock(self, gate_list):
        success = False
        for i in gate_list:
            if self.key == i.item_name:
                self.locked = False
                print("You turn the key and the %s gate is blown open by a gust of wind." % self.gate_direction)
                success = True
        if not success and self.locked:
            print("You do not have the key for this door.")

    # returns locked boolean
    def is_locked(self):
        return self.locked

    # returns direction of gate
    def is_gate(self, text):
        return self.gate_direction in text

    # prints direction of gate
    def print_gate(self):
        print("the %s." % self.gate_direction)


# defines player class
class Player:

    def __init__(self, player_name, player_level):
        self.player_health = 100  # defines player health as 100
        self.player_name = player_name  # defines players name
        self.player_location = player_level  # defines where the player is located
        self.inventory = []  # defines the players inventory

    # changes player location
    def move(self, player_level):
        self.player_location = player_level

    # adds items to player inventory and removes from level
    def take(self, take_user_input):
        for i in self.player_location.level_items:
            if i.item_name in take_user_input:
                self.inventory.append(i)
                print("you take a %s" % i.item_name)
                self.player_location.remove_item(i)
            else:
                print("?")

    # removes item from inventory and adds to level
    def drop(self, drop_user_input):
        success = False
        for i in self.inventory:
            if i.item_name in drop_user_input:
                self.inventory.remove(i)
                self.player_location.add_item(i)
                print("You drop the %s" % i.item_name)
                success = True
        if not success:
            print("?")

    # prints inventory
    def print_inventory(self):
        print("Your inventory: ")
        for i in self.inventory:
            print("%s," % i.item_name)


# defines item class
class Item:

    def __init__(self, item_name):
        self.item_name = item_name  # defines items name

    # function called for use in a for loop to print item
    def print_item(self):
        print("a %s." % self.item_name)


# defines commands in list
commands = "go 'direction', look, take 'item', 'inventory', drop 'item' and unlock"

# initialises levels
start_area = Level()
deep_forest_area = Level()
cross_road_area = Level()
moldy_skeleton_area = Level()
dense_shrubs_area = Level()
old_tree_area = Level()

# initialises items
player_sword = Item("sword")
rusted_key = Item("rusted key")

# start area setup
gate1 = Gate("north", deep_forest_area, False, "")
start_area.setup("forest", [gate1], "You are in a dusk lit forest surrounded by trees. "
                                    "The only direction is deeper into the forest.", [player_sword])

# the level setup function is given a name variable, a list of gates in the level, a description string and items list
# gates are given four variables, direction, where the gate goes to, if the gate is locked and what the gates key is
# deep forest area setup
gate1 = Gate("south", start_area, False, "")
gate2 = Gate("north", cross_road_area, False, "")
deep_forest_area.setup("deep forest", [gate1, gate2], "You are in a seemingly endless tunnel of dark oak trees.", [])

# cross road area setup
gate1 = Gate("south", deep_forest_area, False, "")
gate2 = Gate("north", moldy_skeleton_area, True, "rusted key")
gate3 = Gate("west", dense_shrubs_area, False, "")
gate4 = Gate("east", old_tree_area, False, "")
cross_road_area.setup("cross road area", [gate2, gate4, gate1, gate3], "You are at a crossroads. "
                                                                       "The path spirals into three directions."
                                                                       " It is suddenly dark. ", [])

gate1 = Gate("east", cross_road_area, False, "")
dense_shrubs_area.setup("dense shrubs area", [gate1], "You are in an area with dense shrubbery."
                                                      "The only direction is back", [])

gate1 = Gate("west", cross_road_area, False, "")
old_tree_area.setup("old tree area", [gate1],
                    "You see a large old tree. Something is hanging off a branch", [rusted_key])

gate1 = Gate("south", cross_road_area, False, "")
moldy_skeleton_area.setup("moldy skeleton area", [gate1], "There is a skeleton covered in mold, the path is too "
                                                          "tight to walk around it", [])


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

    print("Your swords damage type is:", player_sword.damage_type)

    print("Your sword is finished.\n")


# begins sword sequence
# sword_sequence()

# asks name and stores in player instance
print("What is your name.")
user_input = input(">")
the_player = Player(user_input, start_area)

# gives player information and area setting
print("\n(Cry help for commands)")
print(start_area.level_description)

# starts game loop
while user_input != "exit":

    # asks user for input and stores as lower case
    user_input = str.lower(input(">"))

    # looks for direction in input and if the direction is valid, moves player in that direction
    for d in the_player.player_location.level_gates:
        if d.is_gate(user_input):
            if d.locked:
                print("The gate rattles and doesnt budge.")

            else:
                the_player.move(d.gate_to)
                print(the_player.player_location.level_description)

    # tells player the commands when asked
    if "help" in user_input:
        print("the commands are:", commands)

    # gives player location information
    elif "look" in user_input:
        the_player.player_location.enter()

    # takes items from level and gives to player
    elif "take" in user_input:
        the_player.take(user_input)

    # prints inventory to player
    elif "inventory" in user_input:
        the_player.print_inventory()

    # takes items from player and gives to level
    elif "drop" in user_input:
        the_player.drop(user_input)

    elif "unlock" in user_input:
        for g in the_player.player_location.level_gates:
            g.unlock(the_player.inventory)
