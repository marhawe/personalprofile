'''
Project 3 - Fast Food 
Author: <your name and VT pid here>

This program <describe your program here>.

I have neither given or received unauthorized assistance on this assignment.
Signed:  <Marhawe Asmerom>

'''

def read_file(filename):
    menu = {}
    file = open(filname, 'r')
    
    line = file.readline()
    line = file.readline()
    while(line):
        line = line.rstrip()
        entries = line.split(',')
        menu[entries[0]]=(float(entries[1]),int(entries[2]), entries[3])
        line = file.readline
        
        
    return menu


def alphabetical_menu(carte):
    items = carte.keys()
    return sorted(items)

def count_type(carte):
    count = {"Entrees": 0, "Salads": 0, "Sides": 0, "Kid's Meals": 0, "Desserts": 0, "Drinks": 0}
    for i in carte.values:
        count[i[2]] += 1    
    return count

def 
        
        
    