class Class(): 
 def __init__(self, class_name): 
     self.name = class_name
     self.more = "Next course : Linux OS in the RPi ?"
     self.description = None 

 def set_description(self, class_description): 
     self.description = class_description 

 def describe(self):
     print (self.name)
     print ( self.description )
     print ( self.more)


my_class = Class("OOP & Python Course, 2017")
my_class.set_description("Grade=A+. Thanks Laura & Staff!" )
my_class.describe()

