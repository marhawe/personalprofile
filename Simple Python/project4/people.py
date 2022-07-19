'''
Project 4 Template

@author: Marhawe Asmerom
@pid: howie18
@date: 05/01/20

I have neither given or received unauthorized assistance on this assignment.
Signed: Marhawe Asmerom
'''

from person import *
from tkinter import *


 def read_file(filename): #reads line in filep
    people = []
    file = open (filename, 'r')
    
    line = file.readline()
    for line in file: # for each line adds triats to a name ()(first and last)
        line = line.rstrip("\n") 
        entries = line.split(',')
        traits = {"Work" : int(entries[2]), "Hobbies":int(entries[3]) , "Socialize": int(entries[4]),"Eat" : int(entries[5]), "Sleep": int(entries[6])}
        p = Person(entries[0],entries[1], traits)
        people.append(p)
     
    
    file.close()
    
    return people


def get_lifestyle_percentages(population):
    bal = 0
    unbal = 0
    count = 0
    for person in population: # determines the type of lifestyle a person is livng
        if person.determine_lifestyle() == "balanced":
            bal += 1
        else:
            unbal += 1
    count = (bal / (unbal + bal)) * 100 # finds the count by dividing bal by the total of unbal and bal 
    t = (round(count,2) , round(100 - count,2)) # tuple that returns percentage of balanced , unbalanced
    return t
    

def get_trait_totals(population):
    traits_total = {"Work": 0, "Hobbies": 0, "Socialize": 0, "Eat": 0, "Sleep":0}
    for person in population:
        g = (person.traits) #finds the traits
        for j,k in g.items():
            traits_total[j] += k #adds each key while updating traits_total
    return(traits_total)

def get_trait_averages(population):
    #stats[0]= Work average
    #stats[1]= Hobbies average
    #stats[2]= Socialize average
    #stats[3]= Eat average
    #stats[4]= Sleep average  
    stats = [0.0,0.0,0.0,0.0,0.0]
    s = get_trait_totals(population) # using the trait totals method with population passed 
    i = 0
    for trait in s:
        stats[i] = round(s[trait] /len(population),2) # uses the total divided the length of the population to get the average
        i+=1
    return (stats)

            
     
    

def get_names(population): 
    names = []po
    for person in population: # appends together the first and last name    
        names.append(person.first_name + " " + person.last_name)
    return names   
        

def get_person_index(fname, lname, population): # searchs through popultaion to find the index of a certain person 
    for person in population:
        if (person.first_name == fname and person.last_name == lname):
            return population.index(person)
    
    
 
 
 
###########################################################population.index(#########################################################################
def main(filename):
    
    person_list = read_file(filename)

    def display(full_name):
        
        full_name = full_name.split()
        
        fname = full_name[0] 
        lname = full_name[1] 
        
        individual_index = get_person_index(fname,lname, person_list)
        
        if person_list[individual_index].determine_lifestyle() == "balanced":
            my_image = PhotoImage(file = "balanced.png") 
            canvas.image = my_image 
            canvas.create_image(100, 110, image = my_image) 
        else:
            my_image = PhotoImage(file = "unbalanced.png") 
            canvas.image = my_image
            canvas.create_image(100, 110, image = my_image) 
        
        
        
        person_label.configure(text=str(person_list[individual_index]))
    
    def show_stats1():
        
        percentages = get_lifestyle_percentages(person_list)
        if stats1.get() == "balanced": 
            stats1_label.configure(text = "Percent of the population that is balanced:\n\n" + str(percentages[0]) + "%")
        else: 
            stats1_label.configure(text = "Percent of the population that is unbalanced:\n\n" + str(percentages[1]) + "%")


    def show_stats2():
        
        if not(CheckVar0.get() or CheckVar1.get() or CheckVar2.get() or CheckVar3.get() or CheckVar4.get()):
            stats2_label.configure(text = "")
            return
        
        averages = get_trait_averages(person_list)
        
        entire_string = "Average Energy Level(s) for the population:\n"
        

        if CheckVar0.get():
            entire_string += "\n" + CheckVar0.get() + ": " + str(averages[0])
        if CheckVar1.get():
            entire_string += "\n" + CheckVar1.get() + ": " + str(averages[1])
        if CheckVar2.get():
            entire_string += "\n" + CheckVar2.get() + ": " + str(averages[2])
        if CheckVar3.get():
            entire_string += "\n" + CheckVar3.get() + ": " + str(averages[3])
        if CheckVar4.get():
            entire_string += "\n" + CheckVar4.get() + ": " + str(averages[4])
          

        stats2_label.configure(text = entire_string)
    
    
    root = Tk()
    root.title("Macroperspective")
    root.configure(background = "lightblue")
    root.minsize(500,500)
    
    title_micro = Label(root, bg = "yellow", fg="red", width = 50, text = "Population Stats")
    title_micro.pack(pady=(0,30))

    
    stats1_title_label = Label(root, background = "#ffcccb", width = 40, text = "Select a Lifestyle to get its percentage:\n", font="-weight bold")
    stats1_title_label.pack()
    stats1_label = Label(root, background = "#ffcccb", width = 40)
    stats1_label.pack()

    radio_Frame = Frame(root, background="lightgray")
    radio_Frame.pack(pady = (0, 30))

    
    stats1 = StringVar()


    Radiobutton(radio_Frame,text="balanced", background = "lightgray", value = "balanced", var= stats1, command=show_stats1).pack(anchor=W)
    Radiobutton(radio_Frame,text="unbalanced", background = "lightgray", value = "unbalanced", var= stats1, command=show_stats1).pack(anchor=W)


    stats2_title_label = Label(root, background = "#ffcccb", width = 40, text = "Check a trait to get its average:\n", font="-weight bold")
    stats2_title_label.pack()
    stats2_label = Label(root, background = "#ffcccb", width = 40)
    stats2_label.pack()


    checkbox_Frame = Frame(root, background="lightgray")
    checkbox_Frame.pack(pady = (0, 10))
    
    CheckVar0 = StringVar()
    CheckVar1 = StringVar()
    CheckVar2 = StringVar()
    CheckVar3 = StringVar()
    CheckVar4 = StringVar()

    
    Checkbutton(checkbox_Frame, text = "Work", bg="lightgray",  onvalue = "Work", offvalue="" , variable = CheckVar0,
                command = show_stats2).pack(anchor=W)
    Checkbutton(checkbox_Frame, text = "Hobbies", bg = "lightgray" , onvalue = "Hobbies", offvalue="" , variable = CheckVar1,
                command = show_stats2).pack(anchor=W)
    Checkbutton(checkbox_Frame, text = "Socialize", bg = "lightgray", onvalue = "Socialize", offvalue="" , variable = CheckVar2,
                command = show_stats2).pack(anchor=W)
    Checkbutton(checkbox_Frame, text = "Eat", bg = "lightgray", onvalue = "Eat", offvalue="" , variable = CheckVar3,
                command = show_stats2).pack(anchor=W)
    Checkbutton(checkbox_Frame, text = "Sleep", bg = "lightgray", onvalue = "Sleep", offvalue="" , variable = CheckVar4,
                command = show_stats2).pack(anchor=W)

    
    root2 = Toplevel()
    root2.title("Microperspective")
    root2.configure(background = "lightblue")
    root2.minsize(500,500)

    title_micro = Label(root2, bg = "yellow", fg="red", width = 50, text = "Individual Lifestyles")
    title_micro.pack(pady=(0,30))
 
    person = StringVar()
    
    names_list = get_names(person_list)
    

    person.set(names_list[0])
    
    person_button = OptionMenu(root2, person, *names_list, command = display)
    person_button.config(bg="gray")
    person_button.pack()
    

    canvas = Canvas(root2, width = 200, height = 200, background="#ffcccb")
    canvas.pack(pady=60)

    person_label = Label(root2, width = 50, height=3, bg="#ffcccb")
    

    person_label.configure(text=person_list[0].first_name + " "+ person_list[0].last_name)
    person_label.pack()
    

    display(person_list[0].first_name + " "+ person_list[0].last_name)
    

############## Make your call to the main function below here ##############
#main("Sample_Population_1.csv")

