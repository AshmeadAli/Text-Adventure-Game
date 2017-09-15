from room import Room
from character import Character
from character import Enemy

kitchen = Room("kitchen")
kitchen.set_description( " A small,cluttered and dingy space filled with broken down appliances")

dining_hall = Room("Dining_Hall")
dining_hall.set_description( " A bare room with very old table and chairs")

ballroom = Room("Ballroom")
ballroom.set_description(" A much larger place with antique furniture ")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(kitchen, "north")
ballroom.link_room(dining_hall, "east")

#dining_hall.get_details()
#kitchen.get_details()
#ballroom.get_details()



dave = Enemy("Dave", "A smelly zombie")
dining_hall.set_character(dave)
dave.describe()
dave.set_conversation(" What do you want, Human?")
dave.set_weakness("cheese")
dave.talk()
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)



current_room = kitchen          

while True:		
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")    
    current_room = current_room.move(command)

    
                 
#Just some experiments, nothing to do with the game
#class Parameter():
#   def __init__(self , first , *argv,):
#        self.first = first
#        self.arg = argv
              
 
#parameter = Parameter( "a","b","c",4,5,6,7,8)        # lots of parameters
#print(parameter.first)    # will print a
#rint(parameter.arg)      # will print ('b','c',4,5,6,7,8)


