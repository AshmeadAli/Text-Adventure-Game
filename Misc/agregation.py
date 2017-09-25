class Room():
        def __init__(self,name):
            self.name = name
            self.room = None
            self.key = None
        def set_room(self,name):
            self.room = name

        def describe(self):
            print(self.name)
            print(self.room)

        def set_key(self,key):
            self.key = key

        def try_key(self,key):
            if self.key == key:
               print(" Congratulations! You are in the Secret Room.")
               print(" Hold on to your hat. ")
               print(" You are going to the planet of the two suns ")
            else:
                print ("Try again")
                           
        
ballroom = Room ("Ballroom")  # first room 
secret_room = Room ("Secret Room" ) # second room 
ballroom.set_room( "Secret Room")   # secret room is now inside ballroom
secret_room.set_key("apple")
ballroom.describe()
print ("--------------")
secret_room.describe()
print("To open the secret room you need a key.")
print(" Choose: apple or banana or cherry")
while True:
    key = input()
    secret_room.try_key(key)


        
