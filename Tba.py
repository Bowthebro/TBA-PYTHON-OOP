#TEXT BASED ADVENTURE OOP PYTHON PROGRAM

#defines level class
class level():
    def __init__(self):
        self.name = ("")

    #level setup function
    def setup(self, name, directions, description):
        self.name = name
        self.directions = directions
        self.description = description
        

    def enter(self):
        print(self.description)
        if len(self.directions) >= 1:
            print("there is a gate to ", end=" ")
            for d in self.directions:
                d.print_gate()

#defines gate class
class gate:

    def __init__(self, direction, gate_to):
        self.gate_to = gate_to
        self.direction = direction

    def is_gate(self, text):
        return self.direction in text

    def print_gate(self):
        print("the %s," % self.direction, end= " ")



class player():

    def __init__(self, name):
        self.health = 100
        self.name = name
        self.location = level

    def move(self, level):
        self.location = level

    def player_is_in_room(self, level):
        return self.location == level


class sword():
    damagetype= ""
    type = ""
    colour = ""
    pickedup = False

    def __init__(self, damagetype, type, colour):
        self.damagetype = damagetype
        self.type = type
        self.colour = colour

#initialises levels
start_area = level()
deep_forest_area = level()


#defines gates and levels
gate1 = gate("north", deep_forest_area)
start_area.setup("forest", [gate1], "You are in a dusk lit forest surrounded by trees. The only direction is deeper into the forest")

gate1 = gate("south", start_area)
deep_forest_area.setup("deep forest", [gate1], "You are in a seemingly endless tunnel of dark oak trees")

#defines function to loop player for incorrect answers
def incorrectAnswerLoop(answers):
    while True:
        user_input=input()

        if user_input in answers:
            return user_input
            break

        else:
            print("incorrect input")
            continue

#defines sequence for players sword creation
def sword_sequence():

    #asks user for input/type of sword. Uses while loop to stop incorrect input breaking program
    print("Type of sword \n katana, claymore, dagger")

    #puts player in loop to collect sword type
    sword.type = incorrectAnswerLoop({"katana", "claymore", "dagger"})

    print("\n Cool your sword type is:", sword.type, "\n")

    #asks user input and stores as variable, lets player use whatever colour.
    print("what colour sword?\n")
    sword.colour=input()
    
    print("\nCool, your sword colour is:", sword.colour, "\n")

    #asks user what damage type they want, using a while loop for accepted input
    print("What damage type?\n holy, blood, fire\n")
    
    #puts player in loop to collect damage type
    sword.damagetype = incorrectAnswerLoop({"holy", "blood", "fire"})

    #prints sword stats to player
    print("\nCool, your  sword type is", sword.type, ", your sword colour is", sword.colour, ", and your swords damage type is", sword.damagetype)

#defines level (unfinished btw)
def forest_sequence():
    #defines commands inorder to print to player
    commands = ["forward", "left", "right",\
        "sword stats", "location", "help", "pick up", "attack"]

    #asks players name to use in later dialogue (which is not yet implemented)
    print("what is your name?")
    player.name = input()

    #outlines area around player and gives help command
    print("You are in a forest and your sword is next to you.\n (type help for list of commands)")

    #starts while loop inorder to "kill" player when health reaches zero (however combat system not yet implemented)
    while player.health > 0:
        #asks for user input
        user_input = input().lower()
        
        #big array of user input possibilities which most are fairly simple
        if user_input == "help":
            print("your commands are:", commands)

        elif user_input == "sword stats":
            print("\nCool, your  sword type is", sword.type, ", your sword colour is", sword.colour, ", and your swords damage type is", sword.damagetype)

        elif user_input == "location":
            print(player.location)

        #prints string 1 if sword is picked up. String 2 if not
        elif user_input == "attack":
            if sword.pickedup == True:
                print("you swing your sword and hack off a branch")
            else:
                print("you dont have your sword")

        #assigns True boolean to sword class if pick up is entered. if already picked up it says you already have your sword
        elif user_input== "pick up":
            if sword.pickedup == False and player.location == "start point":
                print("you pick up your sword")
                sword.pickedup = True
            else:
                print("you already have your sword")

        #inputs other than defined continues loop
        else:
            print("incorrect input")
            continue
    
    #prints string if player is dead
    if player.health > 0:
        print("You Died")
    
    #pass statement to prevent possible errors
    else:
        pass

#defines player instance
the_player = player

#asks name and stores in player instance
print("what is your name?")
user_input = input(">")
the_player.name = user_input

the_player.location = start_area
print("(type help for commands)")

while user_input != "exit":
    #sword_sequence()
    print(start_area.description)
    user_input = input(">")

    for d in the_player.location.directions:
        if d.is_gate(user_input):
            the_player.move(d.gate_to)



    else:
        print("incorrect input")
        continue