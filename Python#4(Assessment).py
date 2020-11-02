while True:
    points = 1
    in_game = True
    while in_game == True and points > 0:
        guess = str(input("How many doors can fit around the sun?"))#this is the question
        if guess == "more than one":#this is the answer
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()#you only get one life, if you get it wrong it exits

    while in_game == True and points > 0:
        guess = str(input("How many penguins can fit around the sun?"))
        if guess == "alot":
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    while in_game == True and points > 0:
        guess = str(input("What is 2+2?"))
        if guess == "fish":
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    while in_game == True and points > 0:
        guess = str(input("What is 7+7?"))
        if guess == "Triangle":
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    while in_game == True and points > 0:
        guess = float(input("What is 3+3?"))
        if guess == 8:
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    while in_game == True and points > 0:
        guess = float(input("What is the volume of Erian's skull?"))
        if guess == 0:
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    while in_game == True and points > 0:
        guess = str(input("What is pythagoras?"))
        if guess == "Triangles":
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    while in_game == True and points > 0:
        guess = str(input("Jimmy is walking down the road. He has a mass of 156, and a height of 1.4. Now calculate the mass of the sun."))
        if guess == "About 333000 times the mass of the Earth.":
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    while in_game == True and points > 0:
        guess = str(input("Who is the best at Among Us?"))
        if guess == "Forensics":
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    while in_game == True and points > 0:
        guess = str(input("Who is Jacks Girlfriend?"))
        if guess == "CleaverBot":
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    while in_game == True and points > 0:
        guess = str(input("What is Wimbledon commonly known as?"))
        if guess == "Wimbledon":
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    while in_game == True and points > 0:
        guess = float(input("If the Hypotenuce is 81, and the adjacent is 72, then what is the opposite?"))
        if guess == 37.11:
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    while in_game == True and points > 0:
        guess = str(input("What is the best colour?"))
        if guess == "█████":
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()

    print("You Win!(But do you.....)")
    
    import time
    time.sleep(5)

    while in_game == True and points > 0:
        guess = str(input("Do you win?"))
        if guess == "NON":
            print("{} is the correct answer" .format(guess))
            points += 1
            print("Correct")
            break
        else:
            print("Wrong")
            exit()
            
    while in_game == True and points > 0:
        print("U Win")
        exit()
        
    
