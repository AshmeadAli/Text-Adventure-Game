class Room:
    
    def __init__(self,room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms ={}
        self.character = None
        self.items = [None]


    def set_items(self,item1,item2,item3):
        self.items = [item1,item2,item3]

    def get_items (self):
        print( self.items)
       
    def get_name(self):
        return self.name
        
    def set_description (self,room_description):
        self.description = room_description

    def get_description(self):
        return (self.description)

    def set_character (self,character):
        self.character = character

    def get_character(self):
        return self.character

    def delete_character(self):
        self.character = None
    
    def describe(self):
        print(self.name)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
  #      print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_details(self):
        print(self.name)
        
        print("----------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)
        print()
        print()
        

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
