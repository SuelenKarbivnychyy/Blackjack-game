import art
import random


def deal_cards():  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  

  random_card = random.choice(cards)
  return random_card



def calculate_score(list_of_cards):    
  score = sum(list_of_cards)

  if 11 in list_of_cards and score > 21:
    list_of_cards.remove(11)
    list_of_cards.append(1) 
    score = sum(list_of_cards)
    return score
  elif 10 in list_of_cards and 11 in list_of_cards:  
    return 0    
  else:
    return score


 

def play_game():  
  
  play = True
  
  while play:
    wants_to_play = input("\nDo you wants to play a Blackjack game? type 'y' or 'n': ").lower()
  
    if wants_to_play == 'y':
      replit.clear()
      print(art.logo) 

      user_cards = []
      computer_cards = []      
        
      while len(user_cards) <= 1:
        user_cards.append(deal_cards())
      user_score = calculate_score(user_cards)      
      print(f"User {user_cards}, the score is: {calculate_score(user_cards)}")
        
      while len(computer_cards) <= 1:
        computer_cards.append(deal_cards())
      computer_score = calculate_score(computer_cards)
      print(f"Computer first card: {computer_cards[0]}") 
    
      if calculate_score(user_cards) == 0:
        print("user won")
        print(user_score)
        play_game()
        break
      elif calculate_score(computer_cards) == 0:
         print(f"computer wins {computer_score}")
         play_game()
        
     
      draw_a_card = True      
      # while game is not over
      while draw_a_card:
        draw_or_pass = input("\nType 'y' to get another card, type 'n' to pass: ")  
        
        if draw_or_pass == "y":
          user_cards.append(deal_cards())  
          user_score = calculate_score(user_cards)
          if user_score < 21:
            print(f"cards: {user_cards}, score:{user_score}")       
          else:           
            print(f"cards: {user_cards}, score: {user_score}") 
            print("Game over, the computer won.")
            break          
        else:       
          print(f"Computer turns, computer frst card: {computer_cards[0]}")
          while calculate_score(computer_cards) < 17:
            computer_cards.append(deal_cards()) 
            computer_score = calculate_score(computer_cards)
            # print(f"{computer_cards}, computer score: {computer_score}")
            
          compare_score(user_score = calculate_score(user_cards), computer_score = calculate_score(computer_cards)) 

            
          draw_a_card = False       
        
          # break     
    else:
      print("Goodbye")
      play =False 

      
def compare_score(user_score, computer_score):
  '''Function to decide who won the game.'''

  if computer_score > user_score and computer_score <= 21:
    print(f"\nComputer won with the score of: {computer_score}")
  elif user_score == computer_score:
      print(f"\nIt's a draw. user {user_score}, Computer: {computer_score}")              
  elif user_score > computer_score:
    print("\nUser won with the greatest score")           
  else:
    print(f"\nPc lost, Pc score is: {computer_score}")



play_game()    #main code