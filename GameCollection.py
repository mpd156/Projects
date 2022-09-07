#Game 3 currently breaks with string input
#menu() returns restart function loop when user tries to exit
def menu():
    print('                                                         Welcome!')
    print("\n\t\t\tto Maxwell D'Angelo's game collection. The following games are available:")
    print('\n\t\t\tMadLibs (1), Rock Paper Scissors (2), Number Guessing Game (3), Exit (4)')
    x = input('\n\t\t\t\tEnter the number of the game you would like to play:')
    while True:
        if x == "1":
            game1()
        elif x == "2":
            game2()
        elif x == "3":
            game3()
        elif x == "4":
            break
        else: 
            menubreak()


def menubreak():
    print("\n\t\t\t\tYou've entered an invalid choice. Please try again.")
    menu()
        

def game1():
    print('                                        Madlibs')
    print('\n\t\t\t\tWelcome to Madlibs! Please choose a story to fill out')
    choice = str(input('\n\t\t\t\tAction Story (1), My Cubicle (2), Superhero Movie(3):'))
    if choice == '1':
        name11= str(input('\n\t\t\t\tEnter a man\'s name:'))
        job11= str(input('\n\t\t\t\tEnter an occupation:'))
        noun11= str(input('\n\t\t\t\tPick a noun:'))
        noun12= str(input('\n\t\t\t\tPick a noun:'))
        noun13= str(input('\n\t\t\t\tPick a noun:'))
        shape11= str(input('\n\t\t\t\tChoose a shape:'))
        verb11= str(input('\n\t\t\t\tPick a verb:'))
        name13= str(input('\n\t\t\t\tEnter a woman\'s name:'))
        bodypart11= str(input('\n\t\t\t\tPick a body part:'))
        verb12= str(input('\n\t\t\t\tPick a verb:'))
        noun14= str(input('\n\t\t\t\tPick a noun:'))
        restaurant11= str(input('\n\t\t\t\tEnter the name of a restaurant:'))
        monument11= str(input('\n\t\t\t\tPick a historical monument:'))
        verb13= str(input('\n\t\t\t\tPick a verb:'))
        noun16= str(input('\n\t\t\t\tPick a noun:'))
        noun17= str(input('\n\t\t\t\tPick a noun:'))
        verb14= str(input('\n\t\t\t\tPick a verb:'))
        adj11= str(input('\n\t\t\t\tEnter an adjective:'))
        adj12= str(input('\n\t\t\t\tEnter an adjective:'))
        emotion11= str(input('\n\t\t\t\tChoose an emotion:'))
        verb15= str(input('\n\t\t\t\tPick a verb:'))
        noun20= str(input('\n\t\t\t\tPick a noun:'))
        

        print(f"""{name11} is a normal {job11}. Then one day, a {noun11} explodes, causing a
        {noun12} to blow up as a nearby {noun13} erupts into a {shape11} of flames. {name11} realizes
        that he's being chased by the government, who's trying to {verb11} him. While on the run, he teams
        up with an incredibly attractive woman named {name13}, who has an incredible {bodypart11}. She may be
        from the streets, but she can {verb12} like nobody\'s business. The duo decide to turn the 
        tables on their pursuers by blowing up a {noun14}, which triggers a chain reaction, causing the local
        {restaurant11} and {monument11} to explode. Then, the bad guys' helicopter gets {verb13} by a pice of
        {noun16} from when the {restaurant11} exploded. The helicopter exploded and falls onto a {noun17} causing it to
        {verb14} which shoots a fireball straight into the heart of the bad guy leader. Everything is {adj11} and the
        two decide that such a {adj12} ordeal has caused them to fall in {emotion11} with each
        other. They decide to celebrate by {verb15}ing on the {noun20}.
        """)

        restart1()
    

    elif choice == '2':
        adj21= str(input('\n\t\tPick an adjective:'))
        superlative21 = str(input("\n\t\tEnter a superlative:"))
        singularnoun21= str(input('\n\t\tEnter a singular noun:'))
        adj22= str(input("\n\t\tPick an adjective:"))
        singularnoun22= str(input('\n\t\tEnter a singular noun:'))
        adj23 = str(input("\n\t\tPick an adjective:"))
        singularnoun23= str(input('\n\t\tEnter a singular noun:'))
        presenttenseverb21 = str(input("\n\t\tEnter verb in the present tense:"))
        singularnoun24= str(input('\n\t\tEnter a singular noun:'))
        presenttenseverb22= str(input("\n\t\tEnter verb in the present tense:"))
        singularnoun25= str(input('\n\t\tEnter a singular noun:'))
        adj24= str(input("\n\t\tPick an adjective:"))
        adj25 = str(input("\n\t\tPick an adjective:"))
        pluralnoun21= str(input("\n\t\tEnter a plural noun:"))
        city21= str(input("\n\t\tEnter the name of a city:"))
        singularnoun26= str(input('\n\t\tEnter a singular noun:'))
        singularnoun27= str(input('\n\t\tEnter a singular noun:'))


        print(f"""\n\t\tMy cubicle is {adj21}. It is the {superlative21} cubicle in 
        the office. I have a {singularnoun21} on my desk next to a(n) {adj22} {singularnoun22}.
        In my drawer, I also have a(n){adj23} {singularnoun23}. One time, a coworker
        tried to {presenttenseverb21} a {singularnoun24} on my desk. I said to him,
        'Hey! How would you like it if I {presenttenseverb22} your {singularnoun25}? I'll
        do it if you don\'t leave.' My one complaint about my cubicle is that it is 
        {adj24}. I think everyone here at the office complains about this. We also complain
        that our cubicles are {adj25}. If we had money in our budget, my boss would purchase 
        some {pluralnoun21} to help alleviate this problem. Our boss doesn\'t understand.
        His office is the size of {city21}. He has enough room in his office to put a {singularnoun26}
        and a {singularnoun27} in there.""")
        
        restart1()


    elif choice == '3':
        sillyname31= str(input('\n\t\tPick a silly name (male):'))
        unrealisticprofession31 = str(input("\n\t\tEnter an unrealistic profession:"))
        country31= str(input('\n\t\tPick a country:'))
        sillyname32= str(input("\n\t\tPick another silly name:"))
        color31= str(input('\n\t\tPick a color:'))
        adj31 = str(input("\n\t\tPick an adjective:"))
        adverb31= str(input('\n\t\tEnter an adverb:'))
        sillyname33 = str(input("\n\t\tPick a third silly name (female):"))
        sillyname34= str(input('\n\t\tPick a fourth silly name:'))
        facialfeature31= str(input("\n\t\tEnter a distinguishing facial feature:"))
        Uscity31= str(input('\n\t\tChoose a city in the Unites States:'))
        sillyname35= str(input("\n\t\tPick one final silly name:"))
        verb31 = str(input("\n\t\tChoose a verb ending in '-ing':"))
        noun31= str(input("\n\t\tEnter a noun:"))
        actor31= str(input("\n\t\tEnter the name of an actor:"))
        noun32= str(input('\n\t\tEnter a noun:'))
        color32= str(input('\n\t\tPick a color:'))
        noun32=str(input('\n\t\tEnter a noun:'))
        planet31= str(input('\n\t\tPick a planet:'))


        print(f"""Meet our hero {sillyname31}, a super-intelligent {unrealisticprofession31}. A run-in
        with the {country31} military leads him to create his alter-ego '{sillyname32}', a {color31} {adj31}
        giant capable of great destruction. He {adverb31} battles the military with his girlfriend
        {sillyname33}. Eventually, it\'s discovered that our hero\'s long-time colleague {sillyname34}, distinguished
        by his {facialfeature31} is trying to turn {sillyname32} into a living weapon, leading to a 
        climactic (if pointless) battle in downtown {Uscity31} with an evil version of the same giant
        alter-ego called {sillyname35}. Eventually, the enemy is subdued by {verb31} with a {noun31}.
        In the final reel, {actor31} appears to propose joining our hero in a fight against {color32} {noun32} from the planet {planet31}.""")


        restart1()


    else:
        gamebreak1()


def restart1():
    while True:
        ask = str(input("\n\t\t\t\tWould you like to play MadLibs again?:"))
        if ask == "yes":
            game1()
        elif ask == "no":
            menu()
        else:
            gamebreak1()


def gamebreak1():
    while True:
        ask = input("\n\t\t\t\tYou have entered an invalid choice. Would you like to play MadLibs again?:")
        if ask == "yes":
            game1()
        elif ask == "no":
            menu()
        else:
            gamebreak1()



import random
def game2():
    list = ['rock', 'paper', 'scissors']
    user_choice = str(input('''\n\t\t\tWelcome to Rock Paper Scissors! You will be playing against the computer.
    \n\t\t\t\t\tWill you choose rock, paper, or scissors?:'''))
    comp = random.choice(list)

# Rock
    if user_choice == 'rock' and comp == 'rock':
        print('\n\t\t\t\tYour opponent chose', comp)
        print("\n\t\t\t\tIt's a draw")
        restart2()

    elif user_choice == 'rock' and comp == 'scissors':
        print('\n\t\t\t\tYour opponent chose', comp)
        print("\n\t\t\t\tRock crushes scissors. You win!")
        restart2()

    elif user_choice == 'rock' and comp == 'paper':
        print('\n\t\t\t\tYour opponent chose', comp)
        print('\n\t\t\t\tPaper covers rock. You lose.')
        restart2()

# Paper
    elif user_choice == 'paper' and comp == 'paper':
        print('\n\t\t\t\tYour opponent chose', comp)
        print("\n\t\t\t\tIt's a draw.")
        restart2()

    elif user_choice == 'paper' and comp == 'scissors':
        print('\n\t\t\t\tYour opponent chose', comp)
        print("\n\t\t\t\tScissors cuts paper. You lose.")
        restart2()

    elif user_choice == 'paper' and comp == 'rock':
        print('\n\t\t\t\tYour opponent chose', comp)
        print('\n\t\t\t\tPaper covers rock. You win.')
        restart2()

#Scissors
    elif user_choice == 'scissors' and comp == 'scissors':
        print('\n\t\t\t\tYour opponent chose', comp)
        print("\n\t\t\t\tIt's a draw.")
        restart2()

    elif user_choice == 'scissors' and comp == 'rock':
        print('\n\t\t\t\tYour opponent chose', comp)
        print('\n\t\t\t\tRock crushes scissors. You lose.')
        restart2()

    elif user_choice == 'scissors' and comp == 'paper':
        print('\n\t\t\t\tYour opponent chose', comp)
        print('\n\t\t\t\tScissors cuts paper. You win!')
        restart2()
    
    else:
        gamebreak2()


def restart2():
    while True:
        ask = str(input("\n\t\t\t\tWould you like to play Rock Paper Scissors again?:"))
        if ask == "yes":
            game2()
        elif ask == "no":
            menu()
        else:
            gamebreak2()


def gamebreak2():
    while True:
        ask = input("\n\t\t\t\tYou have entered an invalid choice. Would you like to play Rock Paper Scissors again?:")
        if ask == "yes":
            game2()
        elif ask == "no":
            menu()
        else:
            gamebreak2()



import random
def game3():
    guess_count= 0
    guess_limit= 3
    answer = random.randint(1,10)
# number of guesses has to be less than the limit
    while guess_count < guess_limit:
        print("\n\t\tWelcome to Guess the Number! You have three chances to correctly guess a randomly chosen number")
        user= int(input("\n\t\t\t\t\tI'm thinking of a number between 1 and 10:"))
    # updates variable with every attempt
        guess_count += 1

        if answer == user:
            print("\n\t\t\t\t\t\tCongratulations! You guessed correctly!")
            restart3()
    
        elif answer < user:
            print("\n\t\t\t\t\t\tToo high. Try again:")
    
        elif answer > user:
            print("\n\t\t\t\t\t\tToo low. Try again:")
        
    
        if guess_count == 3:
            print("\n\t\t\t\tYou are out of chances. The number that I was thinking of was", answer)
            restart3()


def restart3():
    while True:
        ask = input("\n\t\t\t\t\t\tWould you like to play Guess the Number again?:")
        if ask == "yes":
            game3()
        elif ask == "no":
            menu()
        else:
            gamebreak3()


def gamebreak3():
    while True:
        ask = input("\n\t\t\t\tYou have entered an invalid choice. Would you like to play Guess the Number again?:")
        if ask == "yes":
            game3()
        elif ask == "no":
            menu()
        else:
            gamebreak3()


menu()