import time
import random
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def users_selection(keyword):
    if keyword.lower() == "r":
        return "Rock"
    elif keyword.lower() == "s":
        return "Scissor"
    elif keyword.lower() == "p":
        return "Paper"
    else:
        return None

def game_condition(user_choose:str,name:str,user_score,bot_score):
    words = ["Rock", "Paper", "Scissor"]
    bot_choose = random.choice(words)
    
    if user_choose is None:
        print(Fore.YELLOW + "Invalid selection. No points awarded.")
        print(f"Bot chose {bot_choose}")
    elif user_choose.lower() == "rock" and bot_choose.lower() == "scissor" or user_choose.lower() == "paper" and bot_choose.lower() == "rock" or user_choose.lower() == "scissor" and bot_choose.lower() == "paper":
        print(Fore.GREEN + "You Win 🏆")
        print(Fore.CYAN + f"Bot chose {bot_choose}")
        user_score+=1
    elif user_choose.lower() == bot_choose.lower():
        print(Fore.YELLOW + "You Both Selected Same the game is DRAW 😄")
    else:
        print(Fore.RED + "You Lose 🤓")
        print(Fore.CYAN + f"Bot chose {bot_choose}")
        bot_score+=1
    
    print(Fore.MAGENTA + f"\t\t\t{name} score is {user_score}\n\t\t\tCyberCoder Score is {bot_score}")
    return bot_score, user_score

def main():
    user_score = 0
    bot_score = 0
    print(Fore.CYAN + Style.BRIGHT + "\n\tWelcome to Rock (🥌), Paper(📄), Scissor(✂) Game 🎯")
    user_name:str = input(Fore.GREEN + "Enter your Name 📛: " + Fore.RESET)
    time.sleep(1)
    print(Fore.CYAN + f"Nice to Meet you {Fore.YELLOW + user_name + Fore.CYAN}, \n\t I am your game friend CyberCoder")
    time.sleep(1)
    no_of_rounds:int = int(input(Fore.GREEN + "Enter the Number of rounds 🔁 (Each round contain 3 games): " + Fore.RESET))
    print(Fore.CYAN + f"Okay you want to play {Fore.YELLOW + str(no_of_rounds) + Fore.CYAN} rounds hmmm Interesting 😃 \n\n\tOkay let's Start")
    no_of_games = no_of_rounds * 3
    if no_of_rounds > 0:
        for round in range(no_of_rounds):
            time.sleep(1)
            print(Fore.BLUE + Style.BRIGHT + f"\n\tRound {round+1}")
            for game in range(3):
                print(Fore.BLUE + f"\nGame {game+1}")
                time.sleep(1)
                user_choose:str = input(Fore.GREEN + "Select your Weapon\nFor Rock(r)\nFor Paper(p)\nFor Scissor(s)\t: " + Fore.RESET)
                selection = users_selection(user_choose)
                if selection:
                    print(Fore.CYAN + "You Selected " + Fore.YELLOW + selection)
                else:
                    print(Fore.RED + "Invalid keyword entered. Please select r, p, or s.")
                    continue
                no_of_games -= 1
                time.sleep(0.5)
                bot_score, user_score = game_condition(selection, name=user_name, user_score=user_score, bot_score=bot_score)
                print(f"\t\t\t{Fore.RED}The numbers of games left is: {no_of_games}")
    else:
        print(Fore.RED + "Please enter a positive number of rounds")
        exit()
        
    print(Fore.WHITE+"\n\n\t=== FINAL RESULTS ===")
    if bot_score > user_score:
        print(Fore.RED + f"Cyber Coder Won 🎉 with a score of {bot_score} to {user_score}")
    elif user_score > bot_score:
        print(Fore.GREEN + f"{user_name} Won 🎉 with a score of {user_score} to {bot_score}")
    else:
        print(Fore.YELLOW + f"It's a tie! Both players scored {user_score} points")
if __name__ == "__main__":
    main()