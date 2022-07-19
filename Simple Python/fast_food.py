'''
Project 3 - Fast Food (Template)

< Looking through a text file as menu that sorts alphabetical through a carte
counts item types , find meal price , compare prices and calories usind 2D list of tables

@author: Marhawe Asmerom
@pid: @howie18
@date: 4/14/20

I have neither given or received unauthorized assistance on this assignment.
Signed:  < Marhawe Asmerom > 
'''

# Note: A call to the pass statement has been added to any function that
# does not yet contain other statements. This avoids errors that would
# otherwise be produced by having "empty" methods.

def read_file(filename): #read file that is inputted
    menu = {}
    file = open(filename, 'r') 
    file.readline()
    for line in file:
        line = line.rstrip('/n')
        entries = line.split(',')
        menu[entries[0]]=(float(entries[1]),int(entries[2]), entries[3].strip())
       
    file.close()    
    return menu

def alphabetical_menu(carte): # sorts menu in alphabetical order
    items = carte.keys()
    return sorted(items)

def count_type(carte): # counts the type of different items in carte
    count = {"Entrees": 0, "Salads": 0, "Sides": 0, "Kid's Meals": 0, "Desserts": 0, "Drinks": 0}
    for i in carte.values():      
        count[i[2]] += 1    
    return count
    

def calculate_meal_price(carte, food_order, discount = 0 , totalprice = 0): # calculates meal using food_order    
    for order in food_order: # searching thorough food order and finds the meal price 
        if order in carte.keys():  
            totalprice += carte[order][0]
    totalprice -= discount * totalprice * 0.01 # accounts for discount
    totalprice += (0.053 * totalprice) # accounts for tax 
    
    return round(totalprice,2)

def print_table(results): 
    for i in range(3):
        print("{:^30}".format(results[0][i]), end='   ')   
    print()
    barrier = "-" * 100
    print(barrier)
    for i in range(1, len(results)):
        for j in range(len(results[i])):
            print("{:^30}".format(results[i][j]), end='   ')
        print()

def prices_extrema(carte, item_type): # finds the min / max price for in carte for each item type
    min_price = 100 # declaring variables
    max_price = 0
    items = ["",""]
    maxitems = ""
    minitems = ""
    for y in carte.keys(): # looping through function to find min and max prices
        if carte[y][2] == item_type:
            if max_price < carte[y][0]:
                max_price = carte[y][0]
                maxitems = y # finding max price
            if min_price > carte[y][0]:
                min_price = carte[y][0]
                minitems = y # finding min item
    items[0] = minitems
    items[1] = maxitems
    
    return items
    
def prices_table(carte): 
    #setup
    rows, columns = (7, 3)
    results = [["_"] * columns for j in range(rows) ]
    item_types = ["Type","Entrees", "Salads", "Sides", "Kid's Meals", "Desserts", "Drinks"]
    
    for i in range(0, len(item_types)):
        results[i][0] = item_types[i]
        if i > 0 : # finds the min / max price for each item type and makes table from these values 
            p = prices_extrema(carte , item_types[i])
            results[i][1] = p[0]
            results[i][2] = p[1]

            
    results[0][1] = "Cheapest Item"
    results[0][2] = "Most Expensive Item"
    
    return results

def calories_extrema(carte, item_type): # finds the min / max calories for each item type 
    min_calories = 100000 
    max_calories = 0
    items = ["",""]
    maxcal = ""
    mincal = ""
    for y in carte.keys():
        if carte[y][2] == item_type:
            if max_calories < carte[y][1]:
                max_calories = carte[y][1]
                maxcal = y
            if min_calories > carte[y][1]:
                min_calories = carte[y][1]
                mincal = y
    items[0] = mincal
    items[1] = maxcal
    
    return items

def calories_table(carte): 
    rows, columns = (7, 3)
    results = [["_"] * columns for j in range(rows) ]
    item_types = ["Type","Entrees", "Salads", "Sides", "Kid's Meals", "Desserts", "Drinks"]
    
    for i in range(0, len(item_types)):
        results[i][0] = item_types[i]
        if i > 0: # find what fast has the most and least calories using calories extrema and puts it into a table
            x = calories_extrema(carte , item_types[i])
            results[i][1] = x[0]
            results[i][2] = x[1]
   
    
    results[0][1] = "Least Calories"
    results[0][2] = "Most Calories"
    
    return results
   
    

def main(filename, food_order, discount = 0): # main function that runs all functions and makes tables 
    carte = read_file(filename)
    print(alphabetical_menu(carte))
    print(count_type(carte))
    print("My meal includes: ")
    for i in food_order: # loops through food order to calculate meal price
        print(i)
    print ('The cost of the meal is ' + str(calculate_meal_price(carte, food_order, discount))) 
    print_table(prices_table(carte))
    print("        ")
    print_table(calories_table(carte))
    
main("menu1.csv",  ["Spicy Chicken Sandwich", "Chick-fil-A Waffle Potato Fries", "Chic-fil-A Lemonade", "Chocolate Chunk Cookie"] , 10 )

