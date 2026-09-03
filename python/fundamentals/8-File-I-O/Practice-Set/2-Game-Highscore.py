import random
import os

def game():
    print("Welcome you are playing the game!")
    score = random.randint(0, 100)
    
    # Fetch the highscore from the file
    if os.path.exists("highscore.txt"):
        with open("highscore.txt") as f:
            highscore = f.read().strip()
            if highscore.isdigit():
                highscore = int(highscore)
            else:
                highscore = 0
    else:
        highscore = 0
    
    print(f"Your score: {score}")
    if score > highscore:
        # Write this score to the file
        with open("highscore.txt", "w") as f:
            f.write(str(score))
        print("New high score!")
    else:
        print("Try again to beat the high score!")

    return score

game()