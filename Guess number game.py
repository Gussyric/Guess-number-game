import sys
import random



def guess_number(name='PLayerOne'):
    game_count = 0
    player_wins = 0
    

    def play_guess_number():
            nonlocal name
            nonlocal player_wins
           
            
                
            playerchoice = input(
                f"\n{name}, please guess which number I am thinking...\n1 for 1, \n2 for 2, or \n3 for 3\n\n")

            if playerchoice not in ["1", "2", "3"]:
                print(f"{name}, please enter 1, 2, or 3.")
                return play_guess_number()
                
            player = int(playerchoice)

            computerchoice = random.choice("123")

            computer= int(computerchoice)

            print(f"\n{name}, you chose {str(guess_number(player)).replace ('guess_number.','').title()}.")
            print(f"\nPython chose {str(guess_number(computer)).replace ('guess_number.','').title()}.\n")
            def decide_winner(player, computer):
                nonlocal name, player_wins
                if player == computerchoice:
                    player_wins += 1
                    return f"🎉 {name}, You win!"
                else:
                    return f"🐍 Python Wins!\nSorry, {name}..😢"

                
            game_result = decide_winner(player, computer)

            print(game_result)
                
            nonlocal game_count
            
            game_count += 1

            print(f"\nGame count: {game_count}") 
            print(f"\n{name}'s wins: {player_wins}")
              

            print(f"\nPlay again, {name}?")

            while True:
                playagain = input("\nY for Yes or \nQ to Quit \n")
                if playagain.lower() not in ["y", "q"]:
                    continue
                else:
                    break

            if playagain.lower() == "y":
                    return play_guess_number()
            else:
                    print("\n🎉🎉🎉🎉")
                    print("Thank you for playing!\n")
                    sys.exit("Bye {name}! 👋🏿")
                
    return play_guess_number