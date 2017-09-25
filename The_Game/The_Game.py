from room import Room
from character import Character
from character import Enemy


# Define The Planets
dalex = Room("Planet of the Dalexs")
dalex.set_description("Strange robots on wheels, programmed to destroy")

piton = Room("PiTon Planet")
piton.set_description( "A wet and slimy place, reminiscent of a prehistoric time")

tron = Room("Tron Planet")
tron.set_description( "A metallic planet built by Robots, all named Sophie")

ghost = Room("Ghost Planet")
ghost.set_description("No living beings here, only wisps of eerie cloud like apparitions ")

crystal = Room ("Crystal Planet")
crystal.set_description( "Everything here is made out of glass and crystalline substance")

# Define The Planets relative positions
dalex.link_room(tron, "south")
dalex.link_room(piton, "north")
dalex.link_room(ghost, "west")
dalex.link_room(crystal, "east")

ghost.link_room(piton, "north")
ghost.link_room(tron, "south")
ghost.link_room(dalex, "east")

piton.link_room(dalex, "south")
piton.link_room(crystal, "east")
piton.link_room(ghost,"west")

crystal.link_room(piton, "north")
crystal.link_room(tron, "south")
crystal.link_room(dalex, "west")

tron.link_room(dalex, "north")
tron.link_room(crystal, "east")
tron.link_room(ghost, "west")


# Define The Cast 
dalit = Enemy("Dalit", "A robot on wheels, with a bad attitude, who uses toilet plunger weapons")
serpy = Enemy("Serpy", " A hungry, two headed serpent who is looking for a meal")
rennie = Enemy("Rennie", " A stupid, humanoid robot who resembles R2D2")
crystalline = Enemy( "Crystalline", " The wicked witch of the East, reborn as a piece of stone cold frigid ICE")
ghosty = Enemy( "Ghosty", " An apparition of dead souls who has a zombie wife")

# Locate The Cast
dalex.set_character(dalit)
piton.set_character(serpy)
crystal.set_character(crystalline)
ghost.set_character(ghosty)
tron.set_character(rennie)              
              
# Set the Conversations
dalit.set_conversation("Get Out Human!.. or I will Destroy! Destroy!")
serpy.set_conversation("I am hungry. You look nice to swallow. Do you have salt with you?")
rennie.set_conversation ("Robots are smarter than humans..DOTARD ! Get Lost !  ")
crystalline.set_conversation ("Don't touch me Bozo !..or I will turn you into ice.")
ghosty.set_conversation("Don't be afraid , stranger. Come into me.")
              
# Set the Weaknesses
dalit.set_weakness("toilet paper")
serpy.set_weakness("snake oil")
crystalline.set_weakness("hammer")
ghosty.set_weakness("bug spray")
rennie.set_weakness("raspberry pi")

# Set The Items
dalex.set_items( 'screw driver', 'water', 'toilet paper')
piton.set_items( 'wicker basket','snake oil','bugs spray')
crystal.set_items ( 'hammer', 'water', 'shovel')
ghost.set_items ( 'blanket', 'bug spray', 'wicker basket')
tron.set_items ('screw driver', 'raspberry pi','water')


print("You have been transported to the planet of the two SUNS, the home world of the Daleks. ")
print("Your mission, JIM, should you  decide to accept it, is to ")
print("fight your way across the five planets and defeat their strange inhabitants.")
print("Your prize is to belong to the JEDI Club. If you fail....well .... ")
print("The secretary will disavow your actions")

Game = True
life = 10
enemies = 5
current_room = dalex


while Game  :		
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        inhabitant.talk()
        print("What will you fight with?")
        current_room.get_items()
        fight_with = input()
        win = inhabitant.fight(fight_with)
        if (win == True):
            current_room.delete_character()
            enemies = enemies - 1
        if (win == False):
            life = life -1 
            print(" Oh Shit ! You now have " + str(life) + " lives remaining")
    if life == 0:
        print("Game Over. You are now ghosty's new wife ")
        Game = False
    if enemies == 0 :
        print ( "Congratulations ! You are now a Jedi knight and Dr. Who's new mate. Happy Trails !!" )
        Game = False
    command = input("> where do you want to go? ")    
    current_room = current_room.move(command)


   
                 



