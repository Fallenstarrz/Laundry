#######################################################################################################################################################################################################################
# You assignment is to create an algorithm and a flowchart for doing laundry.                                                                                                                                         #
#                                                                                                                                                                                                                      #
# The following items will be available:                                                                                                                                                                              #
#                                                                                                                                                                                                                      #
# A pile (multiple loads) of dirty laundry                                                                                                                                                                            #
# Detergent                                                                                                                                                                                                           #
# Bleach                                                                                                                                                                                                              #
# Fabric softener                                                                                                                                                                                                     #
# One washing machine                                                                                                                                                                                                 #
# One dryer                                                                                                                                                                                                           #
# The following rules must be followed:                                                                                                                                                                               #
#                                                                                                                                                                                                                      #
# The algorithm will start with a multi-load pile of dirty laundry                                                                                                                                                    #
# Whites must be washed separately from colors                                                                                                                                                                        #
# Colors must be washed with one cup of detergent                                                                                                                                                                     #
# Whites must be washed with one cup of detergent and one cup of bleach                                                                                                                                               #
# The washer can only hold one load of laundry at a time                                                                                                                                                              #
# The dryer can only hold one load of laundry at a time                                                                                                                                                               #
# Colors must be dried with one fabric softener                                                                                                                                                                       #
# Laundry must be folded after it is dry                                                                                                                                                                              #
# The algorithm will end when the last load is folded                                                                                                                                                                 #
# Your flowchart must accurately reflect your algorithm. You may use any Microsoft tools for your algorithm and flowchart (Word, Visio, PowerPoint). Your submission will be graded according to the following rubric.#
#######################################################################################################################################################################################################################

import time
import random
from math import ceil                                       # This calls "ceiling" from math to round numbers up when called later in the algorithm
Dark = 0                                                    # This is the number of dark articles of clothes
White = 0                                                   # This is the number of white articles of clothes
Choice = input('Would you like to do laundry? \n')          # Get the yes or no choice

if (Choice.casefold().startswith('y')):                     # If Y (not case sensitive) is at start of the variable then = true, otherwise go else.
                                                            # Sort starts here
    Choice = input('Do you need to sort your laundry? \n')  #Get the yes or no choice
    
    if (Choice.casefold().startswith('y')):                 # If Y (not case sensitive) is at start of the variable then = true, otherwise go else.
        Articles = int(input('How many articles of clothes do you have to do? \n')) #This finds out how many clothes you have to wash
        
        for Articles in range(Articles, 1 -1, -1):          # This looks for articles to equal 1 instead of 0, so the computer doesn't count 0 and add an extra item of clothing.                                                  
                                                            
                                                            # Next we choose if it is white or dark.
            if ((int(random.uniform(1,6)))/1==1):           # Randomly selects an interger between 1 and 5 then divides it by 1. If the result of the division is 1 then its true, it it is true then its white
                White = White + 1                           # This adds 1 to the Whites variable to keep track of how many white articles of clothes we have now
                print('This article was White.')
            else:
                Dark = Dark + 1                             # This adds 1 to the Whites variable to keep track of how many white articles of clothes we have now
                print('This article was Dark.')
            print(Articles)
            print('Remaining')
        print('########## Done Sorting ##########')
        print('There were',(White),'White articles of clothing and',(Dark),'Dark','Articles of clothing!')
        LoadsWhite = float(White) / 15                      # This is where the White articles of clothing are sorted into how many loads it will take.
        LoadsDark = float(Dark) / 15                        # This is where the Dark articles of clothing are sorted into how many loads it will take.
                                                            # This will produce a decimal if White and Dark aren't divisible by 15, so next we use ceiling from math to round it up
        LoadsWhite = ceil(LoadsWhite)                       # This is where the LoadsWhite variable gets rounded up
        LoadsDark = ceil(LoadsDark)                         # This is where the LoadsWhite variable gets rounded up
        print('This means there will be',(LoadsWhite),'White Loads and',(LoadsDark),'Dark Loads.')
        print('##################################')
        print('Now we are ready to wash our clothes!')
    else:                                                   # This is used if you have already sorted your own laundry
        print('How many loads of whites do you have to do?')
        LoadsWhite = int(input())                           # This puts the number of white loads you have to do in the LoadsWhite variable
        print('How many loads of darks do you have to do?')
        LoadsDark = int(input())                            # This puts the number of white loads you have to do in the LoadsWhite variable
                                                            # Now we start washing darks.
    while LoadsDark > 0:
                                                            # Wash Darks
        print('There are',(LoadsDark),'more loads of dark laundry to go.')
        print('You now load 1 load of dark laundry to the washing machine.')
        print('You now deposit 1 unit of Detergent.')
        print('You now start the washing machine.')
        
        time.sleep(3)                                       # This is a 3s timer
        print('**Washing machine is done**')
        while True:                                         # This simulates a Do Loop
                                                            # Dry Darks
            print('You now remove the load from the washer and put it into the dryer.')
            print('You now add a dryer sheet to the dryer.')
            print('You now start the dryer.')
            while True:                                     # This simulates a Do Loop
                                                            # Fold Darks
                time.sleep(3)                               # This is a 3s timer
                print('**Dryer is done**')
                print('You now remove the load from the dryer and begin to fold it.')
                time.sleep(3)                               # This is a 3s timer
                print('**You are done folding this load.**')
                if not(LoadsDark == 0): break               # Breaks loop when LoadsDark reaches 0
            if not(LoadsDark == 0): break                   # Breaks loop when LoadsDark reaches 0
        LoadsDark = LoadsDark - 1                           # Takes 1 away from LoadsDark so keep track of how many loads remaining
                                                            # Start Washing Whites Now
    while LoadsWhite > 0:
                                                            # Wash Whites
        print('You now load 1 load of white laundry to the washing machine.')
        print('You now deposit 1 unit of Detergent.')
        print('You now deposit 1 unit of bleach.')
        print('You now start the washing machine.')
        
        time.sleep(3)                                       # This is a 3s timer
        print('**Washing machine is done**')
        while True:                                         # This simulates a Do Loop
                                                            # Dry Whites
            print('There are',(LoadsWhite),'more loads of white laundry to go.')
            print('You now remove the load from the washer and put it into the dryer.')
            print('You now add a dryer sheet to the dryer.')
            print('You now start the dryer.')
            time.sleep(3)                               # This is a 3s timer
            print('**Dryer is done**')
            while True:                                     # This simulates a Do Loop
                                
                print('You now remove the load from the dryer and fold it.')
                time.sleep(3)                               # This is a 3s timer
                print('**You are done folding this load.**')
                if not(LoadsWhite == 0): break              # Breaks loop when LoadsWhite reaches 0
            if not(LoadsWhite == 0): break                  # Breaks loop when LoadsWhite reaches 0
        LoadsWhite = LoadsWhite - 1                         # Takes 1 away from LoadsDark so keep track of how many loads remaining
    print('Congradulations, You are done doing laundry!')
else:                                                       # This is the else to the beginning if statement
    print('Okay maybe later')
