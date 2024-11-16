#Task-1 (Understanding Python Data types)


# Creating a list in python

def handle_list_operations():
    products = ["Laptop", "Mouse", "Keyboard"] 
    
    #Adding an item to the list
    products.append("Headphones")  
    
    #Removing an item from the list
    products.remove("Mouse")  
    
    #AModifying an item in the list
    products[1] = "Mechanical Keyboard"  
    print("Updated list:", products)
    
    

# Creating  a dictionary in python

def handle_dict():
    orders = {"Alice": ["Laptop"], "Bob": ["Mouse", "Keyboard"]}  
    
    # Adding operation in dictionary
    orders["Alice"].append("Headphones") 
    
    #Removal operation in dictionary
    del orders["Bob"]  
    
    # Modification operation in dictionary
    orders["Charlie"] = ["Mouse"]  
    print("Updated orders:", orders)
    
    

# Creating a set in python


def handle_set_operations():
    categories = {"Electronics", "Accessories"}
   
   # Adding operation in set 
    categories.add("Gaming") 
    
    #Removal operation in set
    categories.remove("Accessories")  
    print("Updated categories:", categories)

