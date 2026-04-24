import random

countries_words=[]
animals_words=[]
fruits_words=[]
matrix=[ ['','','','','','','','','','']
        ,['','','','','','','','','','']
        ,['','','','','','','','','','']
        ,['','','','','','','','','','']
        ,['','','','','','','','','','']
        ,['','','','','','','','','','']
        ,['','','','','','','','','','']
        ,['','','','','','','','','','']
        ,['','','','','','','','','','']
        ,['','','','','','','','','','']]


def get_words(which):            # Get words from files
    c=open("countries.txt","r")  # Open the file in read mode
    countries=c.readlines()      # variable that read lines
    for i in countries:          #Iterates over the lines
        countries_words.append(i.strip())       #appending each line to the list
    c.close()                                   #Close file

    a = open("animals.txt", "r") # Open the file in read mode
    animals = a.readlines()      # variable that read lines
    for i in animals:            #Iterates over the lines
        animals_words.append(i.strip())        #appending each line to the list
    a.close()                                  #Close file

    f = open("fruits.txt", "r") # Open the file in read mode
    fruits = f.readlines()      # variable that read lines
    for i in fruits:            #Iterates over the lines
        fruits_words.append(i.strip())         #appending each line to the list
    f.close()                                  #Close file

    random_countries = random.sample(countries_words,10) # Used to select 10 random names from the list
    random_animals = random.sample(animals_words, 10)    # Used to select 10 random names from the list
    random_fruits = random.sample(fruits_words, 10)      # Used to select 10 random names from the list


    if which == 'c':                                    # if letter is Letter Condition
        return random_countries

    elif which =='a':
        return random_animals
    elif which =='f':
        return random_fruits
    else :
        return "No word category is selected"


def gridy(words):
    for word in words:
        word_length = len(word)
        placed = False  # To check if the word has been placed

        while not placed:  # Keep trying until the word is successfully placed

            direction = random.choice(['v', 'h', 'd'])  # Add diagonal direction 'd'

            if direction == "h":  # Horizontal placement
                row = random.randint(0, 9)
                col = random.randint(0, 10 - word_length)

                # Check and place the word horizontally
                for i in range(word_length):
                    if matrix[row][col + i] != '':
                        break
                else:
                    for i in range(word_length):
                        matrix[row][col + i] = word[i]
                    placed = True

            elif direction == "v":  # Vertical placement
                row = random.randint(0, 10 - word_length)
                col = random.randint(0, 9)

                # Check and place the word vertically
                for i in range(word_length):
                    if matrix[row + i][col] != '':
                        break
                else:
                    for i in range(word_length):
                        matrix[row + i][col] = word[i]
                    placed = True

            elif direction == "d":  # Diagonal placement
                row = random.randint(0, 10 - word_length)
                col = random.randint(0, 10 - word_length)

                # Check and place the word diagonally
                for i in range(word_length):
                    if matrix[row + i][col + i] != '':
                        break
                else:
                    for i in range(word_length):
                        matrix[row + i][col + i] = word[i]
                    placed = True

    # Fill remaining empty cells with random letters
    for row in range(10):
        for col in range(10):
            if matrix[row][col] == '':
                matrix[row][col] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    for p in matrix:  # Print the resulting matrix
        print(p)
def player_mode(words,sorm):
    score = 0
    if sorm == "s":
        na = input("Enter Your name")
        while score != 10 :
            inp=input("Enter word you found ").upper()
            if inp in words :
                print (f"Correct !! {inp} is removed from the list")
                words.remove(inp)
                print (words)
                score +=1
                print (f"Your score is {score}")
                s = input(" Would you like to save or continue ? (s,n)").lower()
                if s == "s":
                    print("Game is Saved ")
                    save_s(na,words,score)
                    break

            else:
                print ("False ,Try Again")
        print(f"Nice jop !! you Finished the game with a score = {score}")




    if sorm == "m":
        corp=input("1v1(1) or vs pc (2)")
        if corp =="1" :
            sc1=0
            sc2=0
            n1 = input("Enter palyer 1 name")
            n2 = input("Enter palyer 2 name ")
            while sc1 + sc2 != 10 :
                u1=input(f"{n1} ,Enter the word you found : ").upper()
                if u1 in words :
                    sc1 +=1
                    print (f"{n1}'s score is {sc1}")
                    words.remove(u1)
                    print(words)
                    s = input(" Would you like to save or continue ? (s,n)").lower()
                    if s == "s":
                        print("Game is Saved ")
                        save_m(sc1,sc2 , words , n1,n2)
                        break
                else:
                    print(f"wrong ! {n2}'s turn")
                u2=input(f"{n2} ,Enter the word you found : ").upper()
                if u2 in words:
                    sc2 += 1
                    print(f"{n2}'s score is {sc2}")
                    words.remove(u2)
                    print(words)
                    s = input(" Would you like to save or continue ? (s,n)").lower()
                    if s == "s":
                        print("Game is Saved ")
                        save_m(sc1,sc2 , words , n1,n2)
                        break
                else:
                    print(f"wrong ! {n1} turn")
                    s = input(" Would you like to save or continue ? (s,n)").lower()
                    if s == "s":
                        print("Game is Saved ")
                        save_m(sc1,sc2 , words , n1,n2)
                        break


            if sc1 > sc2  :
                print (f"{n1} score : {sc1} \n {n2} score : {sc2} \n so {n1} is the winner congrats !!")
            else :
                print(f"{n1} score : {sc1} \n {n2} score : {sc2} \n so {n2} is the winner congrats !!")

        if corp == "2":
            scp=0
            scc=0
            nc = input("Enter your name")
            while scp + scc != 10 :
                up = input(f"{nc} ,Enter the word you found : ").upper()
                if up in words :
                    scp+=1
                    print(f"Your score is {scp}")
                    words.remove(up)
                    print (words)
                    s = input(" Would you like to save or continue ? (s,n)").lower()
                    if s == "s":
                        print("Game is Saved ")
                        save_c(scp,scc, words, nc )
                        break
                else:
                    print("wrong ! computer's turn")
                torf = random.randint(0, 1)
                if torf == 1 :
                    random_word = random.choice(words)
                    print(f"Computer has found the word {random_word}")
                    words.remove(random_word)
                    scc +=1
                    print(f"Your score is {scc}")
                    print(words)
                elif torf == 0 :
                    print ("Computer didn't get the word")
            if scp > scc :
                print(f"{nc} score : {scp} \nComputer score : {scc} \nso {nc} is the winner congrats !!")
            else:
                print(f"{nc} score : {scp} \nComputer score : {scc} \nso the computer is the winner !")

def save_s (na, words,score):
    with open('single_save.txt', 'w') as sin_file:
        sin_file.write(na + '\n')
        sin_file.write(str(score) + '\n')
        sin_file.write(','.join(words) + '\n')
        for row in matrix:
            sin_file.write(''.join(row) + '\n')





def save_m (sc1,sc2 , words , n1,n2):
    with open('mult_save.txt', 'w') as mul_file:
        mul_file.write(n1 + '\n')
        mul_file.write(n2 + '\n')
        mul_file.write(str(sc1) + '\n')
        mul_file.write(str(sc2) + '\n')
        mul_file.write(','.join(words) + '\n')
        for row in matrix:
            mul_file.write(''.join(row) + '\n')

def save_c(scp,scc, words, nc):
    with open('comp_save.txt', 'w') as com_file:
        com_file.write(nc + '\n')
        com_file.write(str(scp) + '\n')
        com_file.write(str(scc) + '\n')
        com_file.write(','.join(words) + '\n')
        for row in matrix:
            com_file.write(''.join(row) + '\n')

def load_s(name_save):
    with open('single_save.txt', 'r') as ss:
        lines = ss.readlines()
        if lines[0].strip() == name_save:
            s1=name_save
            s2 = int(lines[1].strip())
            s3= lines[2].strip().split(',')
            matrix = [list(lines[3 + i].strip()) for i in range(10)]
            score =s2
            words=s3
            na = s1
            for i in matrix :
                print (i)
            print (f"Hello back {na}")
            print(words)
            while score != 10:

                inp = input("Enter word you found ").upper()
                if inp in words:
                    print(f"Correct !! {inp} is removed from the list")
                    words.remove(inp)
                    print(words)
                    score += 1
                    print(f"Your score is {score}")
                    s = input(" Would you like to save or continue ? (s,n)").lower()
                    if s == "s":
                        print("Game is Saved ")
                        save_s(na, words, score)
                        break

                else:
                    print("False ,Try Again")
            print(f"Nice jop !! you Finished the game with a score = {score}")

        else:
            print(f"No saved data found for the name: {name_save}")
            return None



def load_m(name_save):
    with open('mult_save.txt', 'r') as ms:
        lines = ms.readlines()
        if lines[0].strip() == name_save:
            m1=name_save
            m2= str(lines[1].strip())
            m3= int(lines[2].strip())
            m4 = int(lines[3].strip())
            m5 = lines[4].strip().split(',')
            sc1 = m3
            sc2 = m4
            n1 = m1
            n2 = m2
            words = m5
            matrix = [list(lines[5 + i].strip()) for i in range(10)]
            for i in matrix:
                print (i)
            print(words)
            print(f"Welcome back {n1} and {n2} ")
            while sc1+sc2 != 10:
                u1 = input(f"{n1} ,Enter the word you found : ").upper()
                if u1 in words:
                    sc1 += 1
                    print(f"{n1}'s score is {sc1}")
                    words.remove(u1)
                    print(words)
                    s = input(" Would you like to save or continue ? (s,n)").lower()
                    if s == "s":
                        print("Game is Saved ")
                        save_m(sc1, sc2, words, n1, n2)
                        break
                else:
                    print(f"wrong ! {n2}'s turn")
                u2 = input(f"{n2} ,Enter the word you found : ").upper()
                if u2 in words:
                    sc2 += 1
                    print(f"{n2}'s score is {sc2}")
                    words.remove(u2)
                    print(words)
                    s = input(" Would you like to save or continue ? (s,n)").lower()
                    if s == "s":
                        print("Game is Saved ")
                        save_m(sc1, sc2, words, n1, n2)
                        break
                else:
                    print(f"wrong ! {n1} turn")
                    s = input(" Would you like to save or continue ? (s,n)").lower()
                    if s == "s":
                        print("Game is Saved ")
                        save_m(sc1, sc2, words, n1, n2)
                        break

            if sc1 > sc2:
                print(f"{n1} score : {sc1} \n{n2} score : {sc2} \n so {n1} is the winner congrats !!")
            else:
                print(f"{n1} score : {sc1} \n{n2} score : {sc2} \n so {n2} is the winner congrats !!")

        else:
            print(f"No saved data found for the name: {name_save}")
            return None

def load_c(name_save):
    with open('comp_save.txt', 'r') as cs:
        lines = cs.readlines()
        if lines[0].strip() == name_save:
            s1=name_save
            s2= int(lines[1].strip())
            s3= int(lines[2].strip())
            s4 = str(lines[3].strip())
            scp = s2
            scc = s3
            nc = s1
            words = s4.split(',')
            matrix = [list(lines[4 + i].strip()) for i in range(10)]
            for i in matrix:
                print(i)
            print(f"Welcome back {nc}")
            print (words)
            while scp + scc != 10:
                up = input(f"{nc} ,Enter the word you found : ").upper()
                if up in words:
                    scp += 1
                    print(f"Your score is {scp}")
                    words.remove(up)
                    print(words)
                    s = input(" Would you like to save or continue ? (s,n)").lower()
                    if s == "s":
                        print("Game is Saved ")
                        save_c(scp, scc, words, nc)
                        break
                else:
                    print("wrong ! computer's turn")
                torf = random.randint(0, 1)
                if torf == 1:
                    random_word = random.choice(words)
                    print(f"Computer has found the word {random_word}")
                    words.remove(random_word)
                    scc += 1
                    print(f"Your score is {scc}")
                    print(words)
                elif torf == 0:
                    print("Computer didn't get the word")
            if scp > scc:
                print(f"{nc} score : {scp} \nComputer score : {scc} \nso {nc} is the winner congrats !!")
            else:
                print(f"{nc} score : {scp} \nComputer score : {scc} \nso the computer is the winner !")
        else:
            print(f"No saved data found for the name: {name_save}")
            return None




def load():
    name_save=input("Who was playing (Enter player 1 name)?")
    mode_save=input("which mode?\nsingle(1)\nversus pc (2)\nversus a player(3)")
    if mode_save == '1':
        load_s(name_save)



    if mode_save == '2':
        load_c(name_save)


    if mode_save == '3':
        load_m(name_save)



def main():
    l=input("would you like to load a game (y,n) ?").lower()
    if l == "y":
        load()
        player_mode(l,load)
    if l=="n":
        which = input("Choose words category \n(c for Countries)\n(a for Animals)\n(f for Fruits)  : ").lower() # user input a letter to choose a category
        sorm = input("Do you want to play (s) single player mode or (m) multi player mode?").lower()
        words=get_words(which)
        gridy(words)
        print(words)
        player_mode(words, sorm)

main()