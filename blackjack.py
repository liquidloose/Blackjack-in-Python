import random
import time
import sys 

######CREATES A LIST OF CARDS, THIS LIST SERVES AS KEYS TO SEARCH IN MAIN DECK AND ALSO SERVES AS A WAY TO SHUFFLE MAIN DECK######
def create_key_index():    
    key_index = []
    for x in range(1,14):
        for i in ['Hearts','Diamonds', 'Clubs','Spades']:        
            if x == 11:
                key_index.append(f"Jack of {i}")         
            elif x == 12:
                key_index.append(f"Queen of {i}")
            elif x == 13:
                key_index.append(f"King of {i}")
            elif x == 1:
                key_index.append(f"Ace of {i}")
            else:
                key_index.append(f"{x} of {i}")  
    #card_value(key_index)    
    return key_index 

###### Creates dictionary of deck to get values from cards ####    
def card_value(key_index):   
    main_deck = {} 
    value_of_cards = []
    for i in range(1,14):
        for _ in range(4):
            if i > 10:
                n = i 
                s = n - 10 
                t = n - s
                value_of_cards.append(t)
            else:
                value_of_cards.append(i)    
     
    n = 0
    while n < 52:             
        main_deck[key_index[n]] = value_of_cards[n]   
        n += 1
    random.shuffle(key_index) # => after main_deck is created, this shuffles the key_index to create a shuffled order to pull from main deck
    #game_engine(key_index,main_deck) 
    return main_deck

def hand_stats(human_card_values,human_hand,computer_hand,key_index,main_deck,computer_card_values,hidden):  
        
    print(f""" 
************************************************************************************************************************************************************************************************************
Your hand: {human_hand}        Your hand total: {sum(human_card_values)}         Dealer's hand: {hidden}     Dealer's Hand Total: {computer_card_values}
************************************************************************************************************************************************************************************************************ """)

def game_input_prompt():
    print("Enter number for desired game action:  1: Hit      2: Stand          ")       
    
def game_engine(player_name):
    key_index = create_key_index()
    main_deck = card_value(key_index) 
    human_card_values = [main_deck[key_index[-1]], main_deck[key_index[-2]]] 
    human_hand = [key_index[-1] , key_index[-2]] 
    computer_hand = [key_index[-3] , key_index[-4]]
    hidden = f"'[{computer_hand[0]}]'" + ', HIDDEN'
    computer_card_values = 'HIDDEN'
    hand_stats(human_card_values,human_hand,computer_hand,key_index,main_deck,computer_card_values,hidden)    
    #computer_card_values is reassigned here because it no longer needs to be seen as 'HIDDEN'. Value is revealed after above instance 
    computer_card_values = [main_deck[key_index[-3]], main_deck[key_index[-4]]]   
                                                                
    def humans_turn():
            game_prompt = input()
            
            if game_prompt == '1':     
                human_card_values.append(main_deck[key_index[-1]])
                human_hand.append(key_index[-1])          
                del main_deck[key_index[-1]]
                del key_index[-1]
                hidden = f"'[{computer_hand[0]}]'" + ', HIDDEN'
                #hidden_total = 'HIDDEN'   
                computer_card_values = 'HIDDEN'                      
                hand_stats(human_card_values,human_hand,computer_hand,key_index,main_deck,computer_card_values,hidden) 
                if sum(human_card_values) > 21:
                    print("BUST! YOU LOSE! TRY AGAIN, SUCKER!!!")
                    play_again(player_name)
                elif sum(human_card_values) <=21:
                    game_input_prompt()
                    humans_turn()                    
            elif game_prompt == '2':                
                computers_turn()             
            else:
                print('INVALID INPUT; PLEASE TRY AGAIN!!!')
                humans_turn()     

    def computers_turn():

        while sum(computer_card_values) < 18 or sum(computer_card_values) < 22:
            if sum(computer_card_values) < 18:
                print("Dealer chooses to hit") 
                time.sleep(1)           
                computer_card_values.append(main_deck[key_index[-1]])
                computer_hand.append(key_index[-1])          
                del main_deck[key_index[-1]]
                del key_index[-1]                       
            else:
                print("Dealer stands")
                game_tally(human_card_values,computer_card_values,player_name,computer_hand,human_hand,key_index,main_deck)                           
                break

        if sum(computer_card_values) > 21:
            game_tally(human_card_values,computer_card_values,player_name,computer_hand,human_hand,key_index,main_deck)

    def first_deal():   
        for x in range(-4,0):
            del main_deck[key_index[x]]
    
        for x in range(-4,0):
            del key_index[x] 
            
    first_deal()  
    game_input_prompt()
    humans_turn()

def game_tally(human_card_values,computer_card_values,player_name,computer_hand,human_hand,key_index,main_deck): 
    
    hidden = f"'{computer_hand}'"
    
    if sum(human_card_values) > sum(computer_card_values):
        hand_stats(human_card_values,human_hand,computer_hand,key_index,main_deck,sum(computer_card_values),hidden)
        print(f"{player_name} wins!!!")                
    elif sum(human_card_values) == sum(computer_card_values):                
        hand_stats(human_card_values,human_hand,computer_hand,key_index,main_deck,sum(computer_card_values),hidden)
        print("It's a tie! Bummer.")
    elif(sum(computer_card_values) > 21):
        hand_stats(human_card_values,human_hand,computer_hand,key_index,main_deck,sum(computer_card_values),hidden)
        print(f"Dealer busted!!! {player_name}, you won!!!")     
    else:         
        hand_stats(human_card_values,human_hand,computer_hand,key_index,main_deck,sum(computer_card_values),hidden)
        print("Dealer wins!!! You lose!!!")
         

    play_again(player_name)

def play_again(player_name):    
    start_loop = 0
    while start_loop == 0:
        print(f"\nWould you like to play another hand, {player_name}? Press 'Y' for yes or 'N' for no.")
        answer = input()
        if answer == "Y" or answer == "y":
            game_engine(player_name)
            start_loop = 1
        elif answer == "N" or answer == "n":
            print("Ok, whatever. It's cool, I didn't want to play with you anyway.")    
            sys.exit() 
        else:
            time.sleep(1) 
            print("Please enter input that's valid!")

def game_start():
    print("What's your name?")
    player_name = input()      
    print(f"Thanks {player_name}, lets get started!") 
    time.sleep(1) 
    game_engine(player_name)

game_start()



