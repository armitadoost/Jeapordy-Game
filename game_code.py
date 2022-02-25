import intro
from threading import Timer
import time

class Player: #Used this class to have a saved variable for names and points of multiple players
    def __init__(self,name,points,):
        self.name = name
        self.points = points

while True: #Used this while loop to make sure that the number of players is within the range of 2 - 4, once the a number in the range is entered, the loop ends
    print " "
    players_n = input("Enter number of players (2-4): ")
    print " "
    if players_n > 4:
        print "Please enter a number in the range of 2 to 4."
    if players_n <= 4:
        break
            
if players_n >= 2: #Had this as >= because players entered will always be either bigger than or equal to 2
    player_1 = Player((raw_input("Player 1: Enter your name: ")),0, )
    player_2 = Player((raw_input("Player 2: Enter your name: ")),0, )
    
if players_n >= 3: #Had this as >= because if 3 or 4 players is entered, I wouldn't have to repeat the writing player 3
    player_3 = Player((raw_input("Player 3: Enter your name: ")),0, )

if players_n == 4:
    player_4 = Player((raw_input("Player 4: Enter your name: ")),0, )

players = [player_1.name,player_2.name] #This list will help determine whose turn it is
if players_n >= 3:
    players += [player_3.name]
if players_n == 4:
    players += [player_4.name]
    

def drawTable(table): #This function creates the table of values for the game
    output = ""
    for item in table[0]: #This is the categories for the game
        space = 24 - len(item) #This helps center the categories
        
        output += ": " + space/2 * " " + str(item) + space/2 * " " #This puts all the categories in one line
    print output
    
    for i in range(1,4): #This helps print the values, since there are 3 types of values, I have a range of 4 which becomes 3
        items = ""
        for x in table[i]: #Goes through each list of values defined
            items += ":" + 8 * " " + x + 8 * " " #This puts all the values that are suppose to be in one line together
        print items 

value_1 = ["1. $200 ","1. $200 ","1. $200 ","1. $200 "] #These are all the values
value_2 = ["2. $400 ","2. $400 ","2. $400 ","2. $400 "]
value_3 = ["3. $600 ","3. $600 ","3. $600 ","3. $600 "]

table = [["1 - Music","2 - Science","3 - Geography","4 - Capitals"],value_1, value_2 , value_3]


#These are all the questions and their answers
category_1 = ["This Chained To The Rhythm singer is a judge on the 2018 version of American idol" , "This mechanical device is used by musicians to keep time.", "What was the first music video on MTV?"]
answer_1 = [("a. Selena Gomez","b. Katy Perry","c. Miley Cyrus","d. Adam Levine"),("a. Reduction thread","b. Mic Looper","c. Baton","d. Metronome"),("a. Video Killed The Radio Star","b. You Better Run","c. Too Late","d. Sailing")]
correct_answer_1 = ["b", "d","a"]

category_2 = ["What part of a plant transports food and water?" , "What pigment makes plants green?", "In the food chain, plants are known as ______?"]
answer_2 = [("a. roots","b. leaves","c. stem","d. Node"),("a. Anthocyanin","b. Chlorophyll","c. Heme","d. Cytochrome"),("a. Primary Consumers","b. Secondary Consumers","c. Decomposer","d. Producers")]
correct_answer_2 = ["c", "b","d"]

category_3 = ["What is Earth's largest continent?" , "What is the driest place on Earth?", "What river runs through Baghdad?"]
answer_3 = [("a. Asia","b. Europe","c. Antarctica","d. Africa"),("a. Kufra, Libya","b. Sahara desert","c. McMurdo, Antarctica","d. Atacama desert"),("a. Jordan","b. Euphrates","c. Karun","d. Tigris")]
correct_answer_3 = ["a", "c","d"]

category_4 = ["What is the capital of Cuba?" , "What is the capital of Iran?", "What is the capital of Egypt?"]
answer_4 = [("a. Varadero","b. Havana","c. Santa Clara","d. Cienfuegos"),("a. Shiraz","b. Kabul","c. Istanbul","d. Tehran"),("a. Alexandria","b. Cairo","c. Giza","d. Luxor")]
correct_answer_4 = ["b", "d","b"]


#This function determines which players turn it is
def turn_f(list):
    time.sleep(1)
    print " "
    print "It is" , list[0] + "'s turn!!"
    list += [list.pop(0)]

#This function contains the question and answering of the game
def table_questions(category, value):

    if category == 1: #The functions goes through each if statement depending on the category entered
        if category_1[value-1] == 0: #I set each part in the questions in the category list to equal to 0 if it had been answered correctly
            print "This question has already been answered" 
            
        elif category_1[value-1] != 0:  
            print category_1[value-1] #Prints the question
            for i in answer_1[value-1]: #Prints the answer options vertically
                print "\t" , i
            start_time = time.time() #Counts time from the moment the answering is printed
            answer = raw_input("\nYou have 30 seconds \nEnter your answer: (a,b,c,d): ")  
            #Lets them know they have 30 seconds to answer
               
            elapsed_time = time.time() - start_time # Total time from the seconds since the epoch
            if int(time.strftime("%S", time.gmtime(elapsed_time))) > 30: #Converts the elapsed_time to normal seconds and into an integer as the milliseconds do not matter in this case
                print "You did not answer the question in time"
            
            elif int(time.strftime("%S", time.gmtime(elapsed_time))) <= 30: #Enters this if statement if they entered the answer in 30 seconds
                if answer == correct_answer_1[value-1]:
                    print "You are right!"
                    
                    
                    if value == 1: #This prints the value, adds the money to the player who got it right and prints their money balance
                        if players[-1] == str(player_1.name):
                            player_1.points += 200
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 200
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points +=200
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 200
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        
                        value_1[0] = '        ' #Replaces the value in the chart so it clears showing it had already been answered
                    
                    
                    if value == 2:
                        if players[-1] == str(player_1.name):
                            player_1.points += 400
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 400
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points +=400
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 400
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        
                        value_2[0]  = '        '
                    
                    if value == 3:
                        if players[-1] == str(player_1.name):
                            player_1.points += 600
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 600
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points += 600
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 600
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        
                        value_3[0] = '        '
                    
                    category_1[value-1] = 0
                    
                else: #If answer was not right, it enters this part
                    print "You are wrong :("
       
    
    elif category == 2: #Same as category 1, but applies to different parts of the list
        if category_2[value-1] == 0:
            print "This question has already been answered" 
        
        
        elif category_2[value-1] != 0:
            print category_2[value-1]
            for i in answer_2[value-1]:
                print "\t" , i
                
            start_time = time.time()
            answer = raw_input("\nYou have 30 seconds \nEnter your answer: (a,b,c,d): ")  
    
            elapsed_time = time.time() - start_time
            if int(time.strftime("%S", time.gmtime(elapsed_time))) > 30:
                print "You did not answer the question in time"
            
            elif int(time.strftime("%S", time.gmtime(elapsed_time))) <= 30:
                
                if answer == correct_answer_2[value-1]:
                    print "You are right!"
                     
                    
                    if value == 1:
                        if players[-1] == str(player_1.name):
                            player_1.points += 200
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 200
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points +=200
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 200
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        
                        value_1[1] = '        '
  
  
                    if value == 2:
                        if players[-1] == str(player_1.name):
                            player_1.points += 400
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 400
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points +=400
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 400
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        
                        
                        value_2[1] = '        '
                    
                    
                    if value == 3:
                        if players[-1] == str(player_1.name):
                            player_1.points += 600
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 600
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points += 600
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 600
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        
                        value_3[1] = '        '
                    
                    category_2[value-1] = 0
                
                else:
                    print "You are wrong :("
            
            
    elif category == 3:
        if category_3[value-1] == 0:
            print "This question has already been answered" 
        
        elif category_3[value-1] != 0:
            print category_3[value-1]
            for i in answer_3[value-1]:
                print "\t" , i
            
            start_time = time.time()
            answer = raw_input("\nYou have 30 seconds \nEnter your answer: (a,b,c,d): ")  
            
            elapsed_time = time.time() - start_time
            if int(time.strftime("%S", time.gmtime(elapsed_time))) > 30:
                print "You did not answer the question in time"
            
            elif int(time.strftime("%S", time.gmtime(elapsed_time))) <= 30:
                
                if answer == correct_answer_3[value-1]:
                    print "You are right!"
        
        
                    if value == 1:
                        
                        if players[-1] == str(player_1.name):
                            player_1.points += 200
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 200
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points +=200
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 200
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        value_1[2] = '        '
        
                    if value == 2:
                        
                        if players[-1] == str(player_1.name):
                            player_1.points += 400
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 400
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points +=400
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 400
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        
                        value_2[2] = '        '
                
                    
                    if value == 3:
                        
                        if players[-1] == str(player_1.name):
                            player_1.points += 600
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 600
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points += 600
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 600
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        
                        value_3[2] = '        '          
                
                    category_3[value-1] = 0
                
                else:
                    print "You are wrong :("
            
        
    elif category == 4:
        if category_4[value-1] == 0:
            print "This question has already been answered" 
        
        elif category_4[value-1] != 0:
            print category_4[value-1]
            for i in answer_4[value-1]:
                print "\t" , i
            
            start_time = time.time()
            answer = raw_input("\nYou have 30 seconds \nEnter your answer: (a,b,c,d): ")  
            
            elapsed_time = time.time() - start_time
            if int(time.strftime("%S", time.gmtime(elapsed_time))) > 30:
                print "You did not answer the question in time"
            
            elif int(time.strftime("%S", time.gmtime(elapsed_time))) <= 30:
                    
                if answer == correct_answer_4[value-1]:
                    print "You are right!"
                    if value == 1:
                        if players[-1] == str(player_1.name):
                            player_1.points += 200
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 200
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points +=200
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 200
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        
                        value_1[3] = '        '
                    
                    if value == 2:
                        if players[-1] == str(player_1.name):
                            player_1.points += 400
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 400
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points +=400
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 400
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        
                        value_2[3] = '        '
                    
                    
                    if value == 3:
                        if players[-1] == str(player_1.name):
                            player_1.points += 600
                            time.sleep(1)
                            print "Player 1: You have $" + str(player_1.points)
                        if players[-1] == str(player_2.name):
                            player_2.points += 600
                            time.sleep(1)
                            print "Player 2: You have $" + str(player_2.points)
                        if players_n >= 3:
                            if players[-1] == player_3.name:
                                player_3.points += 600
                                time.sleep(1)
                                print "Player 3: You have $" + str(player_3.points)
                            if players_n == 4:
                                if players[-1] == player_4.name:
                                    player_4.points += 600
                                    time.sleep(1)
                                    print "Player 4: You have $" + str(player_4.points)
                        
                        value_3[3 ]= '        '
  
                    category_4[value-1] = 0
                    
                    
                else:
                    print "You are wrong :("
    
while True: #Used a while loop to bring it all together
    
    #If all the values are gone from the list, the game ends by going through these if statements
    if value_1[0] ==  '        ' and value_1[1] ==  '        ' and value_1[2] ==  '        ' and value_1[3] ==  '        ':
        if value_2[0] ==  '        ' and value_2[1] ==  '        ' and value_2[2] ==  '        ' and value_2[3] ==  '        ':
            if value_3[0] == '        ' and value_3[1] ==  '        ' and value_3[2] ==  '        ' and value_3[3] ==  '        ':
                print "\n\nThank you for playing Jeapordy.\nThe winner of this round is:"
                if players_n == 2:
                    highest = max(player_1.points,player_2.points) #Finds out which player had the most points in there were 2 players
                    if highest == player_1.points:
                        print "Player 1 -" , player_1.name , "with $" + str(player_1.points) 
                    elif highest == player_2.points:
                        print "Player 2 -", player_2.name , "with $" + str(player_2.points) 
                if players_n == 3: #Finds out which player had the most points in there were 3 players
                    highest = max(player_1.points,player_2.points, player_3.points)
                    if highest == player_1.points:
                        print "Player 1 -" , player_1.name , "with $" + str(player_1.points) 
                    elif highest == player_2.points:
                        print "Player 2 -", player_2.name , "with $" + str(player_2.points) 
                    elif highest == player_3.points:
                        print "Player 3 -", player_3.name , "with $" + str(player_3.points) 
                if players_n == 4: #Finds out which player had the most points in there were 4 players
                    highest = max(player_1.points,player_2.points, player_3.points)
                    if highest == player_1.points:
                        print "Player 1 -" , player_1.name , "with $" + str(player_1.points) 
                    elif highest == player_2.points:
                        print "Player 2 -", player_2.name , "with $" + str(player_2.points) 
                    elif highest == player_3.points:
                        print "Player 3 -", player_3.name , "with $" + str(player_3.points) 
                    elif highest == player_4.points:
                        print "Player 4 -", player_4.name , "with $" + str(player_4.points) 
                
                exit() #Used this function to end the game
    
    turn_f(players)

    drawTable(table)
    while True: #Process used to make sure that the category and value entered are in range
        category = input("\nPick Category (1-4): ")
        value = input("Enter values (1-3): ")
    
        if category > 4 or value > 3:
            print "Enter a valid category and value"
        elif category <= 4 and value <= 3:
            break
    print " "
    table_questions(category,value) 
    #Prints the function and then re-loops for the next player



