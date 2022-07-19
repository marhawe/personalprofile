'''
Project 4 Template

@author: Marhawe Asmerom
@pid: howie18
@date: 5/02/20

I have neither given or received unauthorized assistance on this assignment.
Signed: Marhawe Asmerom
'''

class Person:
    
    def __init__(self, first_name, last_name, traits): #initializes first name , last name and traits for a person 
        self.first_name = first_name
        self.last_name  = last_name
        self.traits = traits
         
    
    def determine_lifestyle(self): #determines the lifestyle of a person 
        x = ""
        count = 0
        count2 = 0 
        if self.traits["Eat"]== 0 or self.traits["Sleep"]== 0: # if Eat and Sleep are equal to zero the person is unbalanced
            x = "unbalanced"                     
        else :
            for j in self.traits: # adds to two difference counts , for every time there is a "3" or "2"
                if self.traits[j]==3: 
                    count +=1
                elif self.traits[j]==2:
                    count2 +=1
            if count == 3 : # if there is three "3's" then balanced or if there are more 3's than 2's it is balanced , if not then it is unbalanced
                x = "balanced"
            if count2 >= 3:
                x = "balanced"
            else:
                x = "unbalanced" 
        return x

    
    def __str__(self): # returns a string based off determined lifestyle method
        x = self.determine_lifestyle()
        if x == "balanced" :
            return self.first_name + " " + self.last_name +  " has a balanced lifestyle."
        elif x == "unbalanced":
            return self.first_name + " " + self.last_name +  " has an unbalanced lifestyle."
        else:
           pass
        

        
    
    #Do not alter or remove this method
    def __eq__(self, other):
        return (self.first_name == other.first_name) and (self.last_name == other.last_name) and (self.traits == other.traits)
    
