# ECOR 1042 Lab 5 - Individual submission for sort_characters_health_insertion function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Rami Sabouni)
__author__ = "Emily Causi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101236902"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T055"

#==========================================#
# Place your sort_characters_health_insertion function after this line

def sort_characters_health_insertion(health: list[dict], order: str) -> list:
    """ Return providing dictionaries in acending or descending health orders, based on user defined input.
    order must be a string of value "A" or "D", health must be a dictionary
    
    >>> sort_characters_health_insertion([{'Occupation': 'EB','Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "A")
    [{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}]
    
    >>> sort_characters_health_insertion([{'Occupation': 'EB','Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "D")
    [{'Occupation': 'H', 'Health': 62.71}, {'Occupation': 'EB', 'Health': 62.37}]
    
    >>> sort_characters_health_insertion([{'Occupation':'EB'}, {'Occupation': 'M'}], "A")
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    """
    
    # Checking for an empty dictionary
    if health == []:
        return health  
    
    
    # Checking to see if "Health" is a valid key given
    for dictionary in health:
        for key, value in dictionary.items():
            if key == 'Health':
                #print(key)  
                print("")
        
    
    # Returning the dictionaries based on the specified order!
    health_key = 'Health' 
    
    # Initializing separate lists for dictionaries
    dicts_with_health = []
    dicts_without_health = []
    
    # Separate dictionaries based on the presence of the Health key
    for d in health:
        if health_key in d:
            
            # Converting the Health value to float, then adding to 'dicts_with_health'
            try:
                d[health_key] = float(d[health_key])
                dicts_with_health.append(d)
            
            except ValueError:
                # If float fails
                dicts_without_health.append(d)
        else:
            dicts_without_health.append(d)
    
    # Reversing the order if given decreasing as the string
    reverse = order.upper() == 'D'
    
    # Sort 'dicts_with_key' by the float values of 'key'
    dicts_with_health.sort(key = lambda d: d[health_key], reverse = reverse)
    
    # If order is ascending
    if order.upper() == 'A':
        sorted_list = dicts_with_health + dicts_without_health
        return sorted_list  
        
   # If order is descending
    else:
        sorted_list = dicts_without_health + dicts_with_health
        return sorted_list   
        
  
    # Printing each of the health values from each dictionary: ADD
    
    
    # Comparing healths: ADD
    

    # Other: How to print out index keys and values
    # How to print out lengths
    # How to compare indexed values    

           
     # Use the insert sort algorithm to sort characters by "Health" attribute
     # If "Health" is a key in the dictionary, will return sorted list
     # If "Health" is not a key, will print out a message stating the key is not in the dictionary
     
     
    
# Do NOT include a main script in your submission
