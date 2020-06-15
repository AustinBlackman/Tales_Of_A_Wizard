# Things to do
# [X] Extend story
# [X] Save/loading
# [X] Add current spells
# [X] Add almost always accessible menu
# [ ] Add spell info
# [ ] Make different save slots
# [X] Put import time
# [X] put \n instead of print
# [X] change all ans.lower into input().lower
# [ ] Give enemies more attack - lists
# [X] Are you sure you want to leave without Stunlock

#^Ran out of time couldn't complete the rest of the list^

# Country name: Achierhiel
# Town name: Arkala
# North Town name: Gatka


# FOR YOUR FIRST TIME PLAYING THE GAME, PLEASE RUN IT AS A PYTHON FILE, NOT IN IDLE OR ANY OTHER IDE AS IT WILL LOOK
# DIFFERENTLY THAN INTENDED

# Time to beat - With all longest options, I got 60 mins - Sorry for being so long, I know you said shorter was better

import random, os, pickle, time

prompt = '>' # Used during inputs to mark when the player can input text

# ____________________________________________PLAYER CLASS______________________________________________________________

class player():  # Create a class for the player used to store player related information
    def __init__(self,name):
        self.name = name
        self.maxhealth = 100 # 100
        self.health = self.maxhealth
        self.base_attack = 10 #10
        self.magic = 0
        self.spells = {'Mana Bolt': '--> 10DMG'}
        self.currentSpell = 'Mana Bolt'
        self.items = {'50hp potion': '--> A potion that restores 50hp'}
        self.gold = 35
        self.magicType = None
        # Below save where the player currently is, and what they have done
        self.currentInteraction = None
        self.Encounter_talktoMan = 0
        self.Encounter_path_leaveAcademy = 0
        self.Encounter_findGold = 0
        self.Encounter_path_continueIntoArkala = 0
        self.Encounter_path_itemshopArkala = 0
        self.Encounter_path_continueIntoArkala = 0
        self.Encounter_path_spellShopArkala = 0
        self.Encounter_Path_trainingCentreArkala = 0
        self.Encounter_path_northGateArkala = 0
        self.Encounter_path_northSouthArkala = 0
        self.Encounter_path_enterGatka = 0
        self.Encounter_path_goWest = 0
        self.Encounter_talkedtoDragon = 0
        self.Encounter_path_goToClearing = 0
        self.Encounter_askAboutDragon = 0
        self.Encounter_path_southGateArkala = 0
        self.Encounter_helpWoman = 0
        self.Encounter_path_continueSouth = 0
        self.Encounter_path_goToCave = 0
        self.Encounter_askhowwegothere = 0
        self.Encounter_whyhiding = 0
        self.WinDragon = 0
        self.WinWizard = 0

    @property
    def attack(self): # A property allows for this to be called like it was an attribute, but allows for the information
        attack = self.base_attack # to be updated.
        # Depending what spell, add that amount of damage
        if self.currentSpell == 'Mana Bolt':
            attack += 10
        elif self.currentSpell == 'Fire Ball':
            attack += 20
        elif self.currentSpell == 'Lightning Storm':
            attack += 35
        elif self.currentSpell == 'Stunlock':
            attack = 0
        elif self.currentSpell == 'Ultra Blast':
            attack += 60
        elif self.currentSpell == 'Tidal Wave':
            attack += 45
        else:
            pass
        if playerIG.magicType == 'Attack':
            global attackMagicBoost
            attackMagicBoost = round((attack * .30), 0) # Put in a variable for use in later code
            attack += attackMagicBoost
        else:
            pass
        return attack


freshCharacter = player('name') # Store the class in a variable called freshCharacter that does not change throughout
# the course of the game, this allows for the game to be started from the beginning even if a save file is loaded.
playerIG = player('name') # Store the player class in a variable that is used to access the player data.

# _____________________________________________SHOP CLASSES_____________________________________________________________

class itemshops(): # Saves what is in the shops
    def __init__(self):
        self.arkala_items = {'Amulet': '--> A shiny Amulet, in perfect condition - 25G',
                             'Diamond': '--> A sharp crystal clear diamond with a hint of blue - 50G',
                             '100hp potion': '--> A potion that restores 100hp - 50G'}
        self.arkala_spells = {'Stunlock': '--> 0DMG, STUNS ENEMY - 100G', 'Tidal Wave': '--> 45DMG - 100G',
                              'Ultra Blast': '--> 60DMG - 165G'}
itemshopsIG = itemshops()

# _____________________________________________ENEMY CLASSES____________________________________________________________
# Classes used to store data for enemies throughout the game

class masterWizard():
    def __init__(self,name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.currentAttack = ['Fire Ball']
        self.golddrop = 75
masterWizardIG = masterWizard('Master Wizard')

class baronParzival():
    def __init__(self,name):
        self.name = name
        self.maxhealth = 130
        self.health = self.maxhealth
        self.attack = 20
        self.currentAttack = ['Meteor']
        self.golddrop = 125
baronParzivalIG = baronParzival('Baron Parzival')

class WildBoar():
    def __init__(self,name):
        self.name = name
        self.maxhealth = 75
        self.health = self.maxhealth
        self.attack = 30
        self.currentAttack = ['Charge']
        self.golddrop = 45
WildBoarIG = WildBoar('Wild Boar')

class Theif():
    def __init__(self,name):
        self.name = name
        self.maxhealth = 120
        self.health = self.maxhealth
        self.attack = 20
        self.currentAttack = ['Stab']
        self.golddrop = 75
TheifIG = Theif('Theif')

class Dragon():
    def __init__(self,name):
        self.name = name
        self.maxhealth = 350
        self.health = self.maxhealth
        self.attack = 40
        self.currentAttack = ['Fire Breath']
        self.golddrop = 175
DragonIG = Dragon('Dragon')

class Anduwin():
    def __init__(self,name):
        self.name = name
        self.maxhealth = 250
        self.health = self.maxhealth
        self.attack = 45
        self.currentAttack = ['Mana Ball']
        self.golddrop = 200
AnduwinIG = Anduwin('Anduwin')

class Tybaut():
    def __init__(self,name):
        self.name = name
        self.maxhealth = 200
        self.health = self.maxhealth
        self.attack = 40
        self.currentAttack = ['Fire Fury']
        self.golddrop = 200
TybautIG = Tybaut('Tybaut')

class Launce():
    def __init__(self,name):
        self.name = name
        self.maxhealth = 260
        self.health = self.maxhealth
        self.attack = 45
        self.currentAttack = ['Summon Sword']
        self.golddrop = 200
LaunceIG = Launce('Launce')

# ____________________________________________STORY FUNCTIONS___________________________________________________________

def firstInteraction(): # First interaction with Master Wizard - Ask's name
    print("~~For your entire life you always wanted to be a great wizard. You've always heard the stories of Anduwin, "
          " Tybaut, and Launce, the three great wizards. Together they defeated the the dragon Dugon, an evil, evil"
          " being that plagued Achierhiel for many decades. You looked up to these wizards your whole life, wanted"
          " to be exactly like them, and maybe one day be as powerful as them. You spent your whole life trying to "
          " obtain that goal. Four years ago your determination payed off, you started your first semester at the grand"
          " Wizarding Acedemy. For all four of your semesters you placed top of your class, and have become more"
          " powerful than some of the professors. You have earned the respect of your peers, professors, and the Master"
          " Wizard himself, even though he has gone senile this past year. Today is your graduation~~\n")
    time.sleep(5) # This is used throughout the code to make it seem like the
    print('Master Wizard: Congratulations on graduating, Wizard! You have proven your self as a dedicated student, and'
          ' have made this Academy proud.')
    time.sleep(1)
    print('Master Wizard: Uh, What was your name again?')
    global playerIG
    playerIG = freshCharacter # Makes the Player data "fresh" incase the player restarts after loading a save file.
    playerIG = player(input(prompt))
    playerIG.name = playerIG.name.capitalize() # Capitalizes the players name
    time.sleep(1)
    print('\nMaster Wizard: ahh! Thats right, how could I have forgotten a name as powerful as %s\n' % playerIG.name)
    secondInteraction() # Goes to the second interaction in the story

def secondInteraction(): # Second interaction with Master Wizard - Ask's magic type
    time.sleep(1)
    print('~~At the Wizarding Academy, the students each chose one of the four magical elements to major in.'
          ' Attack, Defense, Speed, and Healing. During their time at the Academy, each student will learn how to use'
          ' one of the elements, by the end of their time at the Academy, an average student would only be able to'
          ' use 1/5 of their true power. You were able to use most of your power during your first year at the Academy.'
          '~~\n')
    print('Master Wizard: Hmmm, what element did you major in in again')
    choice = ["attack", "defense", "speed", "healing"]
    while True: # Loop for entering text
        print('*[Attack, Defense, Speed, Healing]*\n')
        ans = input(prompt).lower()
        checkInput(ans) # Fucntion to test for commands
        time.sleep(1)
        if ans in choice: # If input is valid continue, else re-loop
            if ans == 'attack':
                print('Master Wizard: Ah yes, you majored in Attack magic!')
                time.sleep(1)
                print('Master Wizard: Attack magic is wonderful, it allows your spells to do more damage!')
                playerIG.magicType = 'Attack'
            elif ans == 'defense':
                print('Master Wizard: Ah yes, you majored in Defense magic!')
                time.sleep(1)
                print('Master Wizard: Defense magic is truly amazing! It allows you to protect yourself during battle!')
                playerIG.magicType = 'Defense'
            elif ans == 'speed':
                print('Master Wizard: Ah yes, you majored in Speed magic!')
                time.sleep(1)
                print('Master Wizard: Speed magic is crazy! It increases your chance to dodge during battle!')
                playerIG.magicType = 'Speed'
            else:
                print('Master Wizard: Ah yes, you majored in healing magic!')
                time.sleep(1)
                print('Master Wizard: Healing magic is really something special, it allows you to heal during battle!')
                playerIG.magicType = 'Healing'
            print('Master Wizard: Are you sure that was you majored in?')
            if yesNo():  # if player says yes
                time.sleep(1)
                print('Master Wizard: Wonderful!')
                thirdInteraction()
            else:  # if player says no
                playerIG.magicType = None
                continue
        else:
            print('Master Wizard: That is not what I was asking!')



def thirdInteraction():
    #playerIG.spells['Stunlock'] = '--> 0DMG, STUNS ENEMY' # DELETE THIS AFTER THIS IS FOR TESTING PURPOSES
    time.sleep(1)
    print('Master Wizard: So ' + playerIG.name + ', as part of graduation you must fight me!')
    time.sleep(6)
    fightSetup(masterWizardIG) # Sets up the fight game play
    if fight(): # Calls the fight, and if you win it continues, else it starts this function again
        pass
    else:
        thirdInteraction()
    print('Master Wizard: Well done %s, you beat me! You have come really far in your learning!'% playerIG.name)
    print('Master Wizard: Here take these, you have earned them')
    print(' ')
    print('Master Wizard gave you the Fire Ball spell and Graduation Certificate')
    print(' ')
    playerIG.spells['Fire Ball'] = '--> 20DMG' # adds Fire ball to the players spells
    playerIG.items['Graduation Certificate'] = '--> A certificate showing your hard work and dedication' # adds Graduation
    # Certificate to player's items
    print('!! You may now use / commands while entering certain text !!')
    print('!! To equip your new spell please use /equip !!\n')
    helpcheck = '/help'
    checkInput(helpcheck) # used to check input to see if commands are entered, in this context it automatically calls
    # the help command
    fourthInteraction() # Brings player to next section

def fourthInteraction():
    playerIG.currentInteraction = 'fithInteraction' # sets the players current interaction.
    print('* You now have free roam over your actions *')
    choice = ['leave academy', 'talk to master wizard']
    while True: # loop for text input
        print('*[Leave academy, Talk to Master Wizard]*')
        ans = input(prompt).lower()
        checkInput(ans) # Fucntion to test for commands
        if ans in choice:
            if ans == 'leave academy':
                path_leaveAcademy()
                break
            else: # if the player talks to the wizard
                print('Master Wizard: %s what are you doing here still! Get on with your journey!'% playerIG.name)
        else:
            continue

def path_leaveAcademy():
    playerIG.currentInteraction = 'path_leaveAcademy' # sets the players current interaction
    if playerIG.Encounter_path_leaveAcademy == 0:
        print('You just exited through the gates of the Wizarding Academy!\n')
    else:
        pass
    print('There is a dirt path that leads for miles. It goes from the Gate of the Academy all the way down the '
          'mountain to the village of Arkala.\n')
    if playerIG.Encounter_path_leaveAcademy == 0: # If this is the first time here
        print('There is also a rough looking man standing near the main gate of the academy.')
        choice = ['look','talk to man', 'follow path']
        choice_print = '*[Look, Talk to man, Follow Path]*'
    else: # If the player has been here before, already talked to the man
        print('The man that was standing near the gate is no longer there.')
        choice = ['look', 'follow path']
        choice_print = '*[Look, Follow Path]*'
    while True: # loop for text input
        print(choice_print)
        ans = input(prompt).lower()
        checkInput(ans) # Fucntion to test for commands
        print('')
        if ans in choice: # if answer is valid, print an option, else
            if ans == 'look':
                print('The weather is beautiful, the birds are chirping, and you can slighly hear the novice wizards'
                      ' practising their spells in the Academy.')
                print('The Academy is situated on top of the largest mountain in Achierhiel, you can see across the '
                      'entire country from here.')
            elif ans == 'talk to man':
                playerIG.Encounter_talktoMan += 1
                print("The man is frail, and looks like he's about to collapse")
                print('He whispers to you:')
                print('')
                print('Man: You know, I use to be a great wizard at one time. Just as young as you.')
                print('Man: People respected me, loved me, feared me.')
                print("Man: If you give me some gold, I'll help you out.")
                choice2 = ['give gold','leave']
                while True: # loop for text input
                    print('*[Give gold, Leave]*')
                    ans2 = input(prompt).lower()
                    checkInput(ans2) # Fucntion to test for commands
                    if ans2 in choice2: # if answer is valid
                        if ans2 == 'give gold': # if player gave the man gold
                            playerIG.gold -= 10
                            print('You gave the man 10G')
                            print('Man: Thank you very much! Here take this!\n')
                            print('The man gave you a spell! Lighting storm!\n')
                            print('Man: Please, take care of it')
                            playerIG.spells['Lightning Storm'] = '--> 35DMG' # adds Lighting storm to players spells
                            playerIG.Encounter_path_leaveAcademy += 1
                            choice = ['look', 'follow path']
                            choice_print = '*[Look, Follow Path]*'
                            break
                        else: # If the player doesnt give the man gold
                            print('You left without giving the man any gold')
                            break
            else: # If the player follows the path
                if playerIG.Encounter_path_leaveAcademy <=1:
                    path_followPath() # Player follows the path
                    playerIG.Encounter_path_leaveAcademy += 2
                    break
                else:
                    path_continueIntoArkala()
                    break
        else: # If the player doesnt enter something valid
            continue

def path_followPath():
    playerIG.currentInteraction = 'path_followPath'# sets the players current interaction
    playerIG.Encounter_path_leaveAcademy += 2 # if player goes back to the academy, the man wont be there
    print('You followed the path, it was a long jouney, but you are finially at Arkala\n')
    time.sleep(1)
    print('You head into the town to find the town folk gathered around a fight.')
    time.sleep(1)
    print('Upon closer inspection you find a large Buff man fighting a much smaller man')
    time.sleep(1)
    print('You ask some of the crowd members what is going on')
    time.sleep(1)
    print('A lady replies:\n')
    time.sleep(1)
    print("Lady: The big guy, Baron Parzifal, is a local criminal. He uses his magic to beat people up and steal "
          "their money. None of us are strong enough to fight him so we're pretty much free money to him!")
    time.sleep(1)
    print('Lady: I see your wearing academy robes, would you be able to stop him?')
    time.sleep(1)
    choice = ['stop baron', 'do nothing']
    while True:
        print('*[Stop Baron, Do nothing]*')
        ans = input(prompt).lower()
        checkInput(ans) # Fucntion to test for commands
        if ans in choice:
            if ans == 'stop baron':
                path_stopBaron()
                break
            else:
                path_dontStopBaron()
                break
        else: # If the player doesnt enter something valid
            continue



def path_stopBaron():
    print('\nYou throw Baron off of the man hes savagely attacking.')
    time.sleep(1)
    print("Baron Parzifal: What do you think you're doing!")
    time.sleep(1)
    print("You'll pay for that")
    time.sleep(1)
    fightSetup(baronParzivalIG)
    if fight(): # If the player wins the fight
        path_winBaron()
    else: # if the player loses the fight
        path_stopBaron()


def path_dontStopBaron():
    print("You tell the lady that stopping this man isn't your job.\n")
    time.sleep(3)
    path_continueIntoArkala() # Go to arkala

def path_winBaron():
    print('The man that Baron was attacking comes up to you\n')
    print('Man: My name is Alderman Gylaw')
    time.sleep(1)
    print('Alderman Gylaw: I cannot thank you enough for helping me, please accept this coin as a token of my'
          ' appreciation. My family use to own the Largest bank in Achierhiel, this coin may come in use to you during'
          ' your journey! \n')
    playerIG.items['Gylaw coin'] = '--> A coin made by the Gylaw bank' # add the coin to the players inven
    time.sleep(1)
    print('Alderman Gylaw gave you a Glyaw Coin.\n')
    time.sleep(9)
    path_continueIntoArkala() # go to arkala

def path_continueIntoArkala():
        time.sleep(3)
        os.system('cls') # Clear the screen
        playerIG.currentInteraction = 'path_continueIntoArkala' # sets the players current interaction
        if playerIG.Encounter_path_continueIntoArkala == 0: # If the player hasnt been here before
            print('You continue to venture farther into Arkala.')
        else: # if the player has been here before
            pass
        playerIG.Encounter_path_continueIntoArkala += 1 # Shows that the player has been here
        time.sleep(1)
        print('The town is chaotic, yet calm.')
        time.sleep(1)
        print('There are so many people although, they are all minding their own business')
        time.sleep(1)
        print('There are many shops all around the town, such as an item shop, spell shop, and training center')
        time.sleep(1)
        choice = ['go to item shop','go to spell shop', 'go to training barracks', 'look around',
                  'go back to the academy','leave through south gate','leave through north gate']
        while True: # Loop for text entering
            print('*[Go to item shop, Go to spell shop, Go to training barracks, Look around, Go back to the academy'
                  ', Leave through north gate, Leave through south gate]*')
            ans = input(prompt).lower()
            checkInput(ans) # Fucntion to test for commands
            if ans in choice:
                if ans == 'go to item shop':
                    path_itemShopArkala() # Go to item shop
                elif ans == 'go to spell shop':
                    path_spellShopArkala() # go to spell shop
                elif ans == 'go to training barracks':
                    path_trainingCenterArkala() # go to training place
                elif ans == 'go back to the academy':
                    path_leaveAcademy() # go to the academy
                elif ans == 'leave through north gate':
                    if playerIG.Encounter_path_spellShopArkala == 0: # if the player hasnt been to the spell shop
                        print('You should probably visit the spell shop before you continue your journey')
                        continue
                    else: # if the player has been to spell shop
                        path_northGateArkala()
                elif ans == 'leave through south gate':
                    if playerIG.Encounter_path_spellShopArkala == 0: # if the player hasnt been to the spell shop
                        print('You should probably visit the spell shop before you continue your journey')
                        continue
                    else: # if the player has been to spell shop
                        path_southGateArkala()
                else: # Else look
                    time.sleep(1)
                    print('The town is vast, there are many homes, shops and taverns.')
                    print('The there is a large fountain in the town square where small children are running around'
                          ' while their mothers are shopping.')
                    if playerIG.Encounter_findGold == 0:
                        print('You notice some coins lying on the ground')
                        print('You find 20 Gold')
                        playerIG.gold += 20
                        playerIG.Encounter_findGold += 1
                        continue
                    else:
                        print('The gold is no longer there')
                        continue

def path_itemShopArkala():
    os.system('cls') # clear screen
    time.sleep(1)
    print('You entered the Arkala item shop!\n')
    time.sleep(1)
    if playerIG.Encounter_path_itemshopArkala == 0: # if the player hasnt been to the item shop
        clerkName = 'Clerk'
    else: # if the player has been to the item shop
        clerkName = 'Jerard'
    message = random.randint(0,2) # chooses a random message
    if message == 0:
        print('%s: Welcome adventurer!' % clerkName)
    elif message == 1:
        print('%s: Welcome to my item shop young man!' % clerkName)
    else:
        print('%s: I hope your able to find what your looking for at my shop!'% clerkName)
    print('%s: Please take a look at my stock!'% clerkName)
    time.sleep(1)
    if playerIG.Encounter_path_itemshopArkala == 0: # if the player hasnt been to the item shop
        print("%s: It's great to meet you, my name is Jerard. I see you're wearing Academy robes, you must a recent "
              " graduate! If there is anything I can help you with, feel free to ask!"% clerkName)
        playerIG.Encounter_path_itemshopArkala += 1
        clerkName = 'Jerard'
    else: # if the player has been to the item shop
        pass
    while True: # loop for text entering
        print('*[Buy items, Look around, Ask about shop, Leave]*\n')
        choice = ['buy items','look around','ask about shop','leave']
        ans = input(prompt).lower()
        checkInput(ans)
        if ans in choice:
            time.sleep(1)
            if ans == 'buy items' and itemshopsIG.arkala_items != {}: # if the player chooses to buy items and the shop
                # has items
                print("%s: These are my wares! "% clerkName)
                print(itemshopsIG.arkala_items) # prints the shop items
                print('%s: What would you like to purchase? (Case sensitive)'% clerkName)
                while True:
                    print('*[^Item^, back]*')
                    ans2 = input(prompt)
                    if ans2 in itemshopsIG.arkala_items:
                        time.sleep(1)
                        if ans2 == 'Amulet' and playerIG.gold >=25:
                            print('This Amulet is 25G, are you sure you want to purchase it?')
                            if yesNo(): # checks if the player says yes or no
                                playerIG.items['Amulet'] = '--> A shiny Amulet, in perfect condition' #adds to player
                                playerIG.gold -= 25
                                del itemshopsIG.arkala_items['Amulet'] # removes from shop
                                print('You have purchased the Amulet')
                                break
                        elif ans2 == 'Diamond' and playerIG.gold >= 50:
                            print('This Diamond is 50G, are you sure you want to purchase it?')
                            if yesNo():  # checks if the player says yes or no
                                playerIG.items['Diamond'] = '--> A sharp crystal clear diamond with a hint of blue' #adds to player
                                playerIG.gold -= 50
                                del itemshopsIG.arkala_items['Diamond'] # removes from shop
                                print('You have purchased the Diamond')
                                break
                        elif ans2 == '100hp potion' and playerIG.gold >= 50:
                            print('This potion is 50G, are you sure you want to purchase it?')
                            if yesNo():  # checks if the player says yes or no
                                playerIG.items['100hp potion'] = '--> A potion that restores 100hp' #adds to player
                                playerIG.gold -= 50
                                del itemshopsIG.arkala_items['100hp potion'] # removes from shop
                                print('You have purchased the potion')
                                break
                        else: # if the player does not have enough gold
                            print('You do not have enough gold for that item')
                            break
                    elif ans2 == 'back':
                        break
                    else: # if the player didnt input something from the shop
                        print('That is not a valid item')
                        break
            elif ans == 'look around':
                print('The building is in magnificent shape, the walls are made of stone, and the floors are brick.'
                      ' Throughout the entire shop there is not a scratch or a chip throughout, Jerard really keeps '
                      ' this place in good condition, you can tell he put his heart and soul into the shop.\n')
                continue
            elif ans == 'ask about shop':
                print("%s: So, you want to know about my shop! Your the first person to ask about it in a long time!"
                      " The shop was originally built 324 years ago when settlers from the capital first ventured out"
                      " to Arkala to settle, My great, great, great, great, great grandfather built this place with"
                      " his bare hands. Ever since than it has been one of the most popular shops in all of Arkala."
                      " For generations the shop has been passed down, it was only a year and a half ago when I"
                      " inherited it from father after he died. That's enough about me and my shop!"% clerkName)
                continue
            elif ans == 'leave':
                print('You have left the shop')
                path_continueIntoArkala() # go to arkala
            else: # if the player bought all the items from the store
                print('%s: You bought all my wares! I have nothing left to sell!'% clerkName)
        else: # if the player didnt input a correct choice
            continue



def path_spellShopArkala():
    os.system('cls') # clear the screen
    time.sleep(1)
    print('You enter the spell shop')
    time.sleep(1)
    if playerIG.Encounter_path_spellShopArkala == 0: # if the player hasnt been to the shop before
        print('A midget from behind the store counter shouts:')
        time.sleep(1)
        print('Man: Who goes there!')
        time.sleep(1)
        print('The midget steps onto a stool so he is able to see')
        time.sleep(1)
        print('Man: Ah! A wizard! Welcome, my name is Samson, its nice to meet you!')
        time.sleep(1)
        print('Samson: Here at "Samsons home of spells" we have many powerful spells')
        time.sleep(1)
        print('Samson: A favourite among Academy graduates is Stunlock, a spell that stuns the enemy. It is a powerful'
              ' spell that I RECOMMEND')
        playerIG.Encounter_path_spellShopArkala += 1
    else:
        print('Samson: Welcome wizard, how can I help you today')
    while True:
        print('*[Buy items, Look around, Ask about shop, Leave]*\n')
        choice = ['buy items', 'look around', 'ask about shop', 'leave']
        ans = input(prompt).lower()
        checkInput(ans)
        if ans in choice:
            if ans == 'buy items' and itemshopsIG.arkala_spells != {}:
                print("Samson: These are my wares!")
                print(itemshopsIG.arkala_spells)
                print('Samson: What would you like to purchase? (Case sensitive)')
                while True:
                    print('*[^Item^, back]*')
                    ans2 = input(prompt)
                    if ans2 in itemshopsIG.arkala_spells:
                        time.sleep(1)
                        if ans2 == 'Stunlock' and playerIG.gold >= 100:
                            print('This spell is 100G, are you sure you want to purchase it?')
                            if yesNo():
                                playerIG.spells['Stunlock'] = '--> 0DMG, STUNS ENEMY' # adds to player
                                playerIG.gold -= 100
                                del itemshopsIG.arkala_spells['Stunlock'] # removes from shop
                                print('You have purchased the spell, Stunlock')
                                break
                        elif ans2 == 'Tidal Wave' and playerIG.gold >= 100:
                            print('This spell is 100G, are you sure you want to purhcase it?')
                            if yesNo():
                                playerIG.spells['Tidal Wave'] = '--> 45DMG' # adds to player
                                playerIG.gold -= 100
                                del itemshopsIG.arkala_spells['Tidal Wave'] # removes from shop
                                print('You have purchased the spell, Tidal Wave')
                                break
                        elif ans2 == 'Ultra Blast' and playerIG.gold >= 165:
                            print('This spell is 165G, are you sure you want to purchase it?')
                            if yesNo():
                                playerIG.spells['Ultra Blast'] = '--> 60DMG' # adds to player
                                playerIG.gold -= 165
                                del itemshopsIG.arkala_spells['Ultra Blast'] # removes from shop
                                print('You have purchased the spell, Ultra Blast')
                                break
                        else: # dont have enough gold
                            print('You do not have enough gold for that item')
                    elif ans2 == 'back':
                        break
                continue
            elif ans == 'look around':
                time.sleep(1)
                print("\nThe shop is very... Intriguing. There are pantings of animals coating the walls. Not average"
                      " animals either. The paintings are of wolves, zebras, bobcats, angler fish, and moles. The "
                      " single room of the shop is littered with tombs, containing numerous spells, varying with power"
                      ". The shop feels cozy, and for some reason reminds you of home.")
                continue
            elif ans == 'ask about shop':
                print("\nSamson: My shop, eh. I built it my self, you may not believe it because of my size, but I used"
                      ". a type of magic that allowed me to use the strength of 100 men. I managed to build the whole"
                      " thing in 5 hours. That use to be in my prime, unfortunately I can no longer access that power"
                      " it saddens me everyday. ")
            elif ans == 'leave':
                print('You have left the shop')
                path_continueIntoArkala() # go to arkala
            else:
                print('You have bought all of my spells!')
        else:
            continue


def path_trainingCenterArkala():
    os.system('cls')
    time.sleep(1)
    print('You enter the barracks')
    time.sleep(1)
    if playerIG.Encounter_Path_trainingCentreArkala == 0: # if the player has not been here before
        print("Man: Hmm, I don't recognize you, must be new")
        time.sleep(1)
        print('Man: My name will remain unknown, maybe once you prove your self you man know, for now, you may call me'
              ' Master X')
        time.sleep(1)
        print('Master X: Now, how may I help you?')
        time.sleep(1)
        playerIG.Encounter_Path_trainingCentreArkala += 1 # shows the player has been here
    else:
        print('Master X: How may I help you?')
    while True:
        print('*[Train for Health, Train for Attack, Look around, leave]*')
        choice = ['train for health','train for attack','look around','leave']
        ans = input(prompt).lower()
        checkInput(ans)
        if ans in choice:
            if ans == 'train for health' and playerIG.gold >= 40 and playerIG.maxhealth < 200:
                time.sleep(1)
                print('Master X: This training will be intense, and it costs 40G')
                time.sleep(1)
                print('Master X: Are you sure you want to continue?')
                if yesNo(): # checks if the player says yes or no
                    playerIG.gold -= 40
                    room = random.randint(1,2) # creates a random room
                    time.sleep(1)
                    print('Master X: Please enter and complete the course in room %i'% room)
                    time.sleep(1)
                    print('You enter the room')
                    time.sleep(1)
                    if room == 1:
                        print('The room is dark and only lit by a single candle in the corner')
                        time.sleep(1)
                        print('There is only a single Sack of wheat hanging from the ceiling')
                        time.sleep(1)
                        print("A note left by Master X says to punch this bag and let it swing back and hit me, odd but I"
                              " won't question it. The note also says to continue doing this until told other wise")
                        time.sleep(2)
                        print('You continue to punch the bag')
                        time.sleep(2)
                        print('You continue to punch the bag')
                        time.sleep(2)
                        print('Master X: You may stop now')
                        time.sleep(1)
                        print('You feel tired and your body hurts, but you feel like you can take more')
                    elif room == 2:
                        print("The room is so hot, and bright. It's almost like the sun was right in front of you")
                        time.sleep(1)
                        print("There is a note left by Master X, it says to sit on the floor until told other wise")
                        time.sleep(2)
                        print('You continue to sit in the heat')
                        time.sleep(2)
                        print('You continue to sit in the heat')
                        time.sleep(2)
                        print('Master X: You may stop now')
                        time.sleep(1)
                        print('You feel dehydrated but stronger.')
                    else:
                        pass
                    increaseby = [10,20,30] # sets a number to increase by
                    randomnum = random.randint(0,2) # makes a random number to increase by
                    playerIG.maxhealth = playerIG.maxhealth + increaseby[randomnum] # increases health
                    print('Your Max health just increased by %i' % increaseby[randomnum])
                    if playerIG.maxhealth > 200:
                        playerIG.maxhealth = 200
                    else: # if the players max health isnt 200 or greater
                        pass
                    continue
                else: # if the player said no
                    continue
            elif ans == 'train for attack' and playerIG.gold >= 40 and playerIG.base_attack < 100:
                time.sleep(1)
                print('Master X: This training will be intense, and it costs 40G')
                time.sleep(1)
                print('Master X: Are you sure you want to continue?')
                if yesNo(): # if the player says yes or no
                    playerIG.gold -= 40
                    room = random.randint(3,4) # creates a random room
                    time.sleep(1)
                    print('Master X: Please enter and complete the course in room %i'% room)
                    time.sleep(1)
                    print('You enter the room')
                    time.sleep(1)
                    if room == 3:
                        print('The room is really small, your barely able to fit in')
                        time.sleep(1)
                        print('There is a note from Master X that says to not get claustrophobic')
                        time.sleep(1)
                        print('The walls start to close in, its compressing your body, your forced to use all your '
                              'strength to push it back')
                        time.sleep(2)
                        print('The walls stop, they expand again.')
                        time.sleep(1)
                        print('You feel like your about to collapse, but feel stronger')
                    elif room == 4:
                        print('The room is filled with small monsters, there are hundreds of them')
                        time.sleep(1)
                        print('They start swarming you. You have no choice but to attack them')
                        time.sleep(2)
                        print('Your still fighting them off')
                        time.sleep(1)
                        print("They're finally all gone, you feel much stronger.")
                    else:
                        pass
                    increaseby = [5, 10, 20] # random number to increase by
                    randomnum = random.randint(0, 2) # chooses what to increase by
                    playerIG.base_attack = playerIG.base_attack + increaseby[randomnum] # adds the attack
                    print('Your Max Attack just increased by %i' % increaseby[randomnum])
                    if playerIG.base_attack > 100:
                        playerIG.base_attack = 100
                    else: # if the attack isnt over 100
                        pass
                    continue
                else: # if the player enters no
                    continue
            elif ans == 'look around':
                print("The barracks is filled with different weapons, there are spell tombs, katanas, and great swords."
                      " The barracks is a decent size, quite large actually. The place was tidy, even with all the"
                      " weapons around. Its obvious that Master X cares about this place.")
                continue
            elif ans == 'leave':
                print('You have left the shop')
                path_continueIntoArkala()
            else: # if there was an error with training
                if playerIG.gold < 40:
                    print('You do not have enough gold')
                elif playerIG.maxhealth >= 200 and playerIG.base_attack >= 100:
                    print('Your health and attack is too high to train here')
                elif playerIG.maxhealth >= 200:
                    print('Your health is too high to train here')
                else:
                    print('Your attack is high to train here')
                continue
        else: # if the player enters something that wasnt a choice
            continue

def path_northGateArkala():
    playerIG.currentInteraction = 'northGateArkala' # sets the current place
    os.system('cls')  # clears screen
    helpGirl = False # create variable for helping girl
    time.sleep(1)
    if playerIG.Encounter_path_northGateArkala == 0: # if the player hasnt been here before
        print('You leave the north gate and are now on the path from Arkala to Gatka')
        time.sleep(1)
        print('There is a small child on the side of the path crying')
        time.sleep(1)
        print('You may be able to cheer her up if you have the correct item to give her')
        time.sleep(1)
        printt = '*[Talk to girl, Continue down path, Go back to Arkala, look]*'
        choice = ['talk to girl', 'continue down path', 'go back to arkala', 'look']
    else: # if they have been here before
        print('You are on the north path')
        time.sleep(1)
        print('The girl that use to be here is gone now')
        printt = '*[Continue down path, Go back to Arkala, look]*'
        choice = ['continue down path', 'go back to arkala', 'look']
    while True:
        print(printt)
        ans = input(prompt).lower()
        checkInput(ans)
        if ans in choice:
            if ans == 'talk to girl':
                if helpGirl == True:
                    print('You already helped the girl')
                    continue
                else: # if the girl hasnt been helped
                    pass
                time.sleep(1)
                print('You: Are you okay?')
                time.sleep(1)
                print("Girl: No my mommy didn't come home last night, she was suppose to bring me a amulet")
                if 'Amulet' in playerIG.items: # if the player has an amulet
                    while True:
                        print('*[Give amulet, leave]*')
                        choice2 = ['give amulet', ' leave']
                        ans2 = input(prompt).lower()
                        checkInput(ans2)
                        if ans2 in choice2:
                            if ans2 == 'give amulet':
                                time.sleep(1)
                                print('Girl: Wow! Thanks mister! Now when my mommy comes home I will have two!')
                                del playerIG.items['Amulet'] # remove amulet from inv
                                print('Attack +10')
                                playerIG.base_attack += 10
                                time.sleep(2)
                                helpGirl = True # set variable to true
                                break
                            else: # didnt give amulet
                                time.sleep(1)
                                print('You: I hope your mommy comes back')
                                time.sleep(2)
                                break
                        else: # if the player didnt give an amulet
                            continue
                else: # if the player doesnt have an amulet
                    print('You do not have the correct item to give the girl')
                    while True:
                        print('*[leave]*')
                        ans2 = input(prompt)
                        if ans2 == 'leave':
                            print('You: I hope your mommy comes back')
                            time.sleep(1)
                            break
                        else:
                            print('That is not valid')
                            continue
                    continue
            elif ans == 'continue down path':
                time.sleep(1)
                playerIG.Encounter_path_northGateArkala += 1 # shows if you've been here
                print('You continue north')
                time.sleep(1)
                path_continueNorth() # go north
            elif ans == 'go back to arkala':
                playerIG.Encounter_path_northGateArkala += 1  # shows if you've been here
                path_continueIntoArkala() # go back to arkala
            else: # if player entered look
                time.sleep(1)
                print('The path continuing north is dull, not much to be seen. Surrounding the path is a dense forest'
                      ' that continues along the path.')
                time.sleep(1)
                continue
        else: # if the player didnt enter a choice
            continue

def path_southGateArkala():
    playerIG.currentInteraction = 'southGateArkala'
    os.system('cls') # clears screen
    time.sleep(1)
    if playerIG.Encounter_path_southGateArkala == 0: # if the player has not been here before
        print('You exit the south gate of Arkala')
        time.sleep(1)
        print('There is a woman arguing with what seems to be her husband on the side of the path.')
        choice = ['continue down path', 'go back to arkala', 'look', 'talk to woman']
        printt = '*[Continue down path, Go back to Arkala, Look, Talk to woman]*'
    else: # if player has been here
        print('You on are the south path')
        time.sleep(1)
        print('The woman and her husband must have left')
        printt = '*[Continue down path, Go back to Arkala, Look]*'
        choice = ['continue down path', 'go back to arkala', 'look']
    while True:
        print(printt)
        ans = input(prompt).lower()
        checkInput(ans) # checks if the player enters a command
        if ans in choice:
            if ans == 'continue down path':
                print('You continue south')
                time.sleep(1)
                playerIG.Encounter_path_southGateArkala += 1 # shows that the player has been here
                path_continueSouth() # goes south
            elif ans == 'go back to arkala':
                print('You go back to Arkala')
                time.sleep(2)
                playerIG.Encounter_path_southGateArkala += 1
                path_continueIntoArkala()
            elif ans == 'look':
                time.sleep(1)
                print('The path is nothing special, surrounded by forest and made of dirt.')
                time.sleep(2)
                continue
            else:
                if playerIG.Encounter_helpWoman == 0: # if the player hasnt helped the woman
                    pass
                else: # if the player has helped the woman
                    time.sleep(1)
                    print('You already helped the woman')
                    continue
                time.sleep(1)
                print('Woman: WHAT DO YOU WANT WIZARD!')
                time.sleep(1)
                print('You: Woah, whats going on here?')
                time.sleep(1)
                print('Woman: MY HUSBAND LOST MY RING!')
                time.sleep(1)
                print("Husband: I'm so sorry honney")
                if 'Diamond' in playerIG.items: # if the player has a diamond
                    while True:
                        print('*[Give diamond, Leave]*')
                        choice2 = ['give diamond', 'leave']
                        ans2 = input(prompt).lower()
                        checkInput(ans2) # checks for commands
                        if ans2 in choice2:
                            if ans2 == 'give diamond':
                                time.sleep(1)
                                print('Woman: WOW THANK YOU SIR')
                                del playerIG.items['Diamond']
                                time.sleep(1)
                                print('Health +20')
                                playerIG.maxhealth += 20 # adds 20 health
                                playerIG.Encounter_helpWoman += 1 # shows you helped the woman
                                break
                            else: # didnt give diamond
                                print('You leave the lady alone')
                                break
                        else:
                            continue
                else: # if the player doesnt have a diamond
                    print('You do not have the correct item to give the woman')
                    while True:
                        print('*[Leave]*')
                        ans3 = input(prompt).lower()
                        checkInput(ans3)
                        if ans3 =='leave':
                            time.sleep(1)
                            print('You: I hope you find your ring')
                            time.sleep(1)
                            break
                        else:
                            continue
        else: # if the player didnt enter a choice
            continue

def path_continueSouth():
    playerIG.currentInteraction = 'continueSouth' # saves current location
    time.sleep(1)
    os.system('cls') # clears screen
    if playerIG.Encounter_path_continueSouth == 0: # if the player hasnt been here
        print('You can feel strong magical presence coming from a nearby cave')
        playerIG.Encounter_path_continueSouth += 1
    else: # if the player has been here
        print('You are still on the south path')
    time.sleep(1)
    print('The path seems to end here')
    time.sleep(1)
    print('A clearing near the end of the path is fulled with boars')
    time.sleep(1)
    if playerIG.WinWizard == 0: # if the player hasnt beaten the great wizards
        while True:
            print('*[Go to cave, Hunt boars, go back]*')
            choice = ['go to cave', 'hunt boars', 'go back']
            ans = input(prompt).lower()
            checkInput(ans) # checks for commands
            if ans in choice:
                time.sleep(1)
                if ans == 'go to cave':
                    path_goToCave()
                elif ans == 'hunt boars':
                    found = random.randint(0,1) # random choice
                    if found == 0:
                        print('The boar got away!')
                    else: # if the random number is 1
                        print('You caught a boar!')
                        time.sleep(3)
                        fightSetup(WildBoarIG) # sets up the fight
                        if fight(): # if the player wins the fight
                            print('You won your fight with the boar')
                            time.sleep(2)
                            continue
                        else: # if the player loses the fight
                            print('The boar beat you!')
                            time.sleep(4)
                            path_continueSouth()

                else: # go back
                    time.sleep(2)
                    path_southGateArkala()
            else: # if player didnt show a choice
                continue
    else: # if the player didnt win
        print('You can no longer visit the cave, you beat the Great Wizards.')
        while True:
            print('*[Hunt boars, go back]*')
            choice = ['hunt boars', 'go back']
            ans = input(prompt).lower()
            checkInput(ans) # checks if the player enters a command
            if ans in choice:
                if ans == 'hunt boars':
                    found = random.randint(0, 1) # same stuff as above
                    if found == 0:
                        print('The boar got away!')
                    else:
                        print('You caught a boar!')
                        time.sleep(3)
                        fightSetup(WildBoarIG)
                        if fight():
                            print('You won your fight with the boar')
                            time.sleep(2)
                            continue
                        else:
                            print('The boar beat you!')
                            time.sleep(4)
                            path_continueSouth()
                else:
                    time.sleep(2)
                    path_southGateArkala()

def path_goToCave():
    playerIG.currentInteraction = 'goToCave' # sets current location
    time.sleep(3)
    os.system('cls')
    if playerIG.Encounter_path_goToCave == 0: #if the player hasnt been here before
        print('You enter the cave, the magical presence is almost overwhelming, it is like nothing you have felt during'
              ' your time at the academy.')
        time.sleep(1)
        print('You can hear voices coming from somewhere in the cave')
        time.sleep(1)
        print("Voice: %s, I've been wondering when you would make it here"% playerIG.name)
        time.sleep(1)
        if playerIG.Encounter_talktoMan != 0: # if the player talked to the man at the start of the game
            print('The voice sounds oddly famillular')
            time.sleep(1)
        else: # if the player hasnt talked to the man
            pass
        print('Voice: Continue down into the cave')
        time.sleep(1)
        print('You continue walking deeper into the cave')
        time.sleep(2)
        print('You continue walking deeper into the cave')
        time.sleep(2)
        print('Suddenly there is a white flash, its all you can see for a few seconds')
        time.sleep(1)
        print('You now seem to be in a very nice house, but how did you get here?')
        time.sleep(1)
        print('There is an old man standing in front of you, and two more are walking in')
        time.sleep(1)
        print('Voice: I am Anduwin, that is Tybaut, and that is Launce.')
        time.sleep(2)
        print('THE THREE GREAT WIZARDS!')
        time.sleep(1)
        print('Anduwin: You may recognize me, I was the man standing outside of the Academy when you left.')
        time.sleep(1)
        print('How could I have been so foolish to not recognize him')
        time.sleep(1)
        print('Anduwin: We have been watching you.')
        time.sleep(1)
        print('Anduwin: You have great power, if you wish you may join us under one circumstance.')
        time.sleep(1)
        print('Anduwin: You must beat all three of us in a duel.')
        time.sleep(1)
        print('Anduwin: It is your choice though.')
        playerIG.Encounter_path_goToCave += 1 # shows the player has been here
    else: # if the player has been to the cave before
        print('You enter the cave and make your way down to the house')
    while True:
        print('*[Fight Wizards, leave cave, ask questions]*')
        choice = ['fight wizards', 'leave cave', 'ask questions']
        ans = input(prompt).lower()
        checkInput(ans) # checks for commands
        if ans in choice:
            if ans == 'fight wizards':
                print("Anduwin: I hope you're ready, %s"% playerIG.name)
                time.sleep(4)
                fightSetup(AnduwinIG) # sets up fight
                if fight(): # if player wins fight
                    time.sleep(1)
                    print('Anduwin: I wish you well in your next fight.')
                    time.sleep(3)
                    pass
                else: # if player loses
                    print('Anduwin: I thought you were stronger....')
                    time.sleep(4)
                    path_continueSouth() # go to south path
                time.sleep(1)
                print('Tybaut: When your ready, %s'% playerIG.name)
                time.sleep(4)
                fightSetup(TybautIG) # sets up fight
                if fight(): # if player wins
                    time.sleep(1)
                    print('Tybaut: You are doing well, one more')
                    time.sleep(4)
                    pass
                else: # if the player loses
                    print('Tybaut: Weak....')
                    time.sleep(4)
                    path_continueSouth() # go to south path
                time.sleep(1)
                print('Launce: Good luck, %s'% playerIG.name)
                time.sleep(3)
                fightSetup(LaunceIG) # sets up fight
                if fight(): # if win fight
                    time.sleep(1)
                    print('Launce: Well done, Wizard')
                    time.sleep(4)
                    pass
                else: # if lose fight
                    print('Launce: Horrible, Pathetic, You are worthless')
                    time.sleep(4)
                    path_continueSouth() # go to south path
                print('Anduwin: You are very reputable wizard, we will be in touch.')
                time.sleep(3)
                playerIG.WinWizard += 1 # shows if player beat wizards
                if playerIG.WinWizard != 0 and playerIG.WinDragon != 0: #if player beat wizards and dragon
                    win() # win game
                else: # if player didnt beat game
                    pass
                print('I should go check the North Gate of Arkala')
                time.sleep(5)
                path_continueSouth() # go to south path
            elif ans == 'leave cave':
                time.sleep(1)
                path_continueSouth() # go to south path
            else: # ask questions
                while True:
                    print('*[How did we get here?, Why have you been in hiding?, Back]*')
                    choice = ['how did we get here?', 'why have you been in hiding?', 'back']
                    ans2 = input(prompt).lower()
                    checkInput(ans2) # checks for commands
                    if ans2 in choice:
                        if ans2 == 'how did we get here?':
                            if playerIG.Encounter_askhowwegothere == 0: # if the player has not asked this before
                                time.sleep(1)
                                print('You: How did we get here?')
                                time.sleep(1)
                                print('Anduwin: We are in a pocket dimension, I placed the entrance to it in the cave'
                                      ' you passed through')
                                time.sleep(1)
                                playerIG.Encounter_askhowwegothere += 1 # shows if the player asked this before
                            else: # if the player asked before
                                print('You have already asked that')
                                continue
                        elif ans2 == 'back':
                            break
                        else: # Why have you been in hiding
                            if playerIG.Encounter_whyhiding == 0: # if the player has not asked this before
                                time.sleep(1)
                                print('You: Why have you been in hiding?')
                                time.sleep(1)
                                print('Anduwin: We have not be hiding, merely training')
                                playerIG.Encounter_whyhiding += 1 # shows if the player asked this before
                            else: # if the player asked before
                                print('You have already asked that')
                                continue
        else: # if the player didnt enter a choice
            continue




def path_continueNorth():
    playerIG.currentInteraction = 'continueNorth' # sets current place
    os.system('cls') # clears screen
    time.sleep(1)
    TheifEncounter = random.randint(0,2) # chance for a theif to appear
    if TheifEncounter == 0:
        time.sleep(1)
        print('You encounter a theif!')
        time.sleep(1)
        print('Theif: GIVE ME YOUR GOLD')
        time.sleep(2)
        fightSetup(TheifIG) # sets up fight
        if fight(): # if player wins
            pass
        else: # if player loses
            print('You have lost')
            time.sleep(4)
            path_continueNorth()
    else: # if theif doesnt appear
        pass
    time.sleep(1)
    print("You're almost at the end of the path")
    time.sleep(1)
    print('You can see the northern town of Gatka')
    print('*[Continue to Gatka, look, go back toward Arkala]*')
    choice = ['continue to gatka', 'look', 'go back toward arkala']
    while True:
        ans = input(prompt).lower()
        checkInput(ans) # checks for commands
        if ans in choice:
            if ans == 'continue to gatka':
                time.sleep(1)
                print('You continue on')
                time.sleep(1)
                path_enterGatka() # go to gatka
            elif ans == 'look':
                print('The path looks the exact same; The path is dull, not much to be seen. Surrounding '
                      'the path is a dense forest that continues along the path.')
            else:
                time.sleep(1)
                print('You head back toward Arkala')
                time.sleep(3)
                path_northGateArkala() # go to north gate
        else: # if player didnt input a choice
            continue

def path_enterGatka():
    playerIG.currentInteraction = 'enterGatka'
    if playerIG.Encounter_path_enterGatka == 0: # checks if player has been here before, if not
        time.sleep(1)
        print('You enter the town of Gatka\n')
        time.sleep(1)
        print('The town is on fire, and everybody is running around frantically')
        time.sleep(1)
        print('You ask one of the people what had happened here')
        time.sleep(1)
        print("Lady: WE WERE ATTACKED! IT WAS A GIANT DRAGON! IT SHOT FIRE FROM OUT OF ITS MOUTH, HOTTER THAN ANY"
              " BLACKSMITHS KILN. HE FLEW OFF TO THE WEST")
        time.sleep(2)
        print('You think to yourself:')
        time.sleep(1)
        print('It must be Dugon, thats the only dragon that had been seen before, how is he alive? I thought the three'
              ' great wizards killed him?')
        time.sleep(1)
        print('I should go investigate')
        playerIG.Encounter_path_enterGatka += 1
    else: # if player has been here
        time.sleep(1)
        print('You enter the ruined town of Gatka')
    if playerIG.Encounter_path_goToClearing != 0: # if player defeated the dragon
        time.sleep(2)
        print('Lady: Thank you for defeating that dragon!\n')
        print('Maybe you should visit the South gate of Arkala')
    else: # if the player didnt defeat the dragon
        pass
    while True:
        print('*[Go to the west path, go to the south, look]*')
        choice = ['go to the west path', 'go to the south', 'look']
        ans = input(prompt).lower()
        checkInput(ans) # checks for commands
        if ans in choice:
            if ans == 'go to the west path':
                time.sleep(1)
                print('You go down the west path')
                time.sleep(1)
                path_goWest() # go to the west
            elif ans == 'go to the south':
                path_continueNorth() # go north
            else:
                print('The town is in ruin, the dragon really destroyed everything. The town use to be filled with life,'
                      ' now there is just death. Nothing but death is left.')
        else: # if player didnt enter a choice
            continue

def path_goWest():
    playerIG.currentInteraction = 'goWest'
    time.sleep(1)
    os.system('cls') # clears screen
    time.sleep(1)
    if playerIG.Encounter_path_goWest == 0: # if player hasnt been here before
        print('The path is charred, the dragon obviously came this way')
        playerIG.Encounter_path_goWest += 1 # show if player has been here
    else: # if player has been here
        print('You are on the west path')
    if playerIG.Encounter_path_goToClearing == 0: # if player hasnt killed dragon
        time.sleep(1)
        print('The dragon seems to have landed in the clearing upahead')
        time.sleep(1)
        print('You think to yourself')
        time.sleep(1)
        print("I should only enter if I'm ready to fight the dragon")
        while True:
            print('*[Go back to Gatka, Go to the clearing]*')
            choice = ['go back to gatka', 'go to the clearing']
            ans = input(prompt).lower()
            if ans in choice:
                if ans == 'go back to gatka':
                    path_enterGatka()
                else:
                    path_goToClearing()
            else:
                continue
    else: # if player killed dragon
        time.sleep(1)
        print('You have defeated the dragon, the only way to go is back.')
        while True:
            print('*[Go back to Gatka]*')
            ans = input(prompt).lower()
            if ans == 'go back to gatka':
                path_enterGatka()
            else:
                continue
def path_goToClearing():
    playerIG.currentInteraction = 'goToClearing'
    time.sleep(1)
    print('You enter the clearing. There is a large dragon standing there, it must be the dragon that destroyed Gatka.')
    time.sleep(1)
    print('The dragon turns around and looks at you')
    time.sleep(1)
    print('You stare at each other for a good while')
    time.sleep(1)
    print('Dragon: What are you doing HUMAN')
    time.sleep(1)
    while True:
        choice = ['you can talk?', 'you cant destroy the town']
        print('*[You can talk?, you cant destroy the town]*')
        ans = input().lower()
        checkInput(ans) # checks for commands
        if ans in choice:
            if ans == 'you can talk?':
                if playerIG.Encounter_talkedtoDragon != 0:
                    print("Dragon: We've been over this already")
                    continue
                else: # if player didnt ask this yet
                    pass
                print('You: You can talk?')
                time.sleep(1)
                print('Dragon: Of course I can talk!')
                time.sleep(1)
                print('You: How?')
                time.sleep(1)
                print("Dragon: Why wouldn't I?")
                time.sleep(1)
                print('You: Your a dragon')
                time.sleep(1)
                print('Dragon: Have you forgot Human? Dragons have been on this world longer than you have. This is'
                      ' rightfully our world that you have RUINED')
                playerIG.Encounter_talkedtoDragon += 1
                time.sleep(1)
            else: # if player confronts dragon
                time.sleep(1)
                print("You: You can't destroy the town, there are hundreds of people who live there.")
                time.sleep(1)
                print('Dragon: I will do as I please, who are you to stop me, peasant')
                break
    while True:
        print('*[Challenge, Ask about dragon]*')
        choice2 = ['challenge', 'ask about dragon']
        ans2 = input(prompt).lower()
        checkInput(ans2)
        if ans2 in choice2:
            if ans2 == 'challenge':
                fightSetup(DragonIG) # sets up fight
                if fight(): # if player wins fight
                    playerIG.WinDragon += 1 # shows player defeated dragon
                    break
                else: # if player doesnt win fight
                    time.sleep(2)
                    print('You lost to the Dragon... Going back to the west path')
                    path_goWest()
            else: # if player asks about dragon
                if playerIG.Encounter_askAboutDragon != 0: # if player asked this before
                    print('You already asked that')
                    continue
                else: # if player didnt ask this
                    pass
                time.sleep(1)
                print('Dragon: I am Elgoron, the son of the Great Dugon. I was born shortly before the three great'
                      ' wizards killed him. It was tragic, but he was a fool for losing to such inferior beings')
                DragonIG.name = 'Elgoron'
                playerIG.Encounter_askAboutDragon += 1
                continue
    playerIG.Encounter_path_goToClearing += 1 # shows player defeated the dragon
    print("The town will be happy to know that they don't have to worry about the dragon anymore")
    time.sleep(4)
    if playerIG.WinWizard != 0 and playerIG.WinDragon != 0: # if player defeated the wizards and dragon
        win() # win game
    else: # if player didnt win game
        pass
    path_goWest()

def win(): # function for winning game
    time.sleep(4)
    print('\nYou suddenly black out\n')
    time.sleep(4)
    print('You awake in a field that you do not recognize, what happened? I fought the dragon and won against the'
          ' Great Wizards, how did I end up here?')
    time.sleep(3)
    tobeContinuedArt()
    time.sleep(4)
    print('CREDITS:')
    credits() # shows credit graphic
    print('Basic fundamentals (Basic fighting, I modified heavily) - Vincent Gizzarelli')
    print('Graphic words - http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20')
    while True:
        print('Enter anything to exit')
        ans = input()
        exit()


# ____________________________________________OTHER FUNCTIONS___________________________________________________________

def fightSetup(whatEnemy): # sets up the fight function. They could be combined into one function but I'm keeping it
    # this way for the sake of organization.
    global enemy
    enemy = whatEnemy
    fightFlash()

def fight(): # fight function
    playerIG.health = playerIG.maxhealth
    stunAvailable = True # Sets the stun variable to true, this allows the player to use the stun attack if they have it
    # this was added so they player could not have the enemy in an infinite stun lock.
    print("// You are fighting %s //" % enemy.name)
    time.sleep(2)
    turn = 1 # Sets the turn to 1, if the turn is >= 1, it is the players turn.
    while True: # Fight loop
        os.system('cls') # Clears the terminal
        playerAttack = random.randint(round(playerIG.attack / 2, 0), playerIG.attack) # At the beginning of each turn
        # set the players attack randomly, within half the players attack and the players full attack
        enemyAttack = random.randint(round(enemy.attack / 2, 0), enemy.attack) # At the beginning of each turn
        # set the enemies attack random,y within half of their attack and their full attack
        print("// Your HP = %i/%i -- %s's HP = %i/%i //\n" % (playerIG.health, playerIG.maxhealth, enemy.name,
                                                              enemy.health, enemy.maxhealth))
        if winFight(): # If the enemies hp < 0
            enemy.health = enemy.maxhealth # Set the enemies hp to max, in case of a future fight
            playerIG.health = playerIG.maxhealth # set the players HP to max
            time.sleep(3)
            return True
        elif loseFight(): # If the players HP < 0
            enemy.health = enemy.maxhealth # Set the enemies hp to max as the fight will be re-run
            playerIG.health = playerIG.maxhealth # Set the players HP to max as the fight will be re-run
            print(' ')
            return False
        elif turn >=1: # If the turn variable is larger than one it is the players turn
            print(' // YOUR TURN //\n')
            print('What do you do?')
            if playerIG.magicType == 'Healing': # If the players magic type is healing, add the heal option to the fight
                print('*[Attack, Use item, Equip, Heal]*')
                choice = ['attack', 'use item','equip','heal']
            else: # if the players magic type is not healing, don't add the heal option to the fight.
                print('*[Attack, Use item, Equip]*')
                choice = ['attack', 'use item','equip']
            ans = input(prompt) # The user chooses an option
            if ans.lower() in choice: # If the option is valid, else loop again
                if ans.lower() == 'attack': # If the player chose attack
                    if playerIG.currentSpell != 'Stunlock': # if the players current attack is not Stunlock print how
                        # much damage you did, else pass
                        os.system('cls')
                        print('// You attacked %s with %s and did %i damage //' %(enemy.name, playerIG.currentSpell, playerAttack))
                    else:
                        pass
                    if playerIG.magicType == 'Attack': # if the players magic type is attack, print how much of the
                        # damage was acquired from that, else pass
                        print('%i of that damage was due to your Attack Magic!' % attackMagicBoost)
                    else:
                        pass
                    if playerIG.currentSpell == 'Stunlock': # if the player attacked with Stunlock
                        if stunAvailable: # if the player has a stun attack available
                            stunAmount = random.randint(2,3) # choose a random amount of turns the enemy is stunned for
                            print('Your opponent has been stunned for %i turns! '% stunAmount)
                            turn += stunAmount # add the stun amount to your turn count, recall that if the turn
                            # is greater than 0, it is the players turn.
                            stunAvailable = False
                            #time.sleep(2)
                            pass
                        else: # if the player does not have a stun available
                            print('%s is already stunned, this spell did nothing'% enemy.name)
                            time.sleep(2)
                            continue
                    enemy.health -= playerAttack # deal the damage to the enemy
                    turn -= 1 # remove a turn
                    time.sleep(3)
                    continue # start the loop again
                elif ans.lower() == 'heal': # if the player chose heal
                    heal = random.randint(playerIG.maxhealth * .2, playerIG.maxhealth *.35 ) # heal for a random number
                    # between %20 and %35 of the players max HP
                    print('// You healed for %i of your max health! //' % heal)
                    playerIG.health += heal # add the heal amount to the players HP
                    if playerIG.health >= playerIG.maxhealth: # if the players HP exceeds their max health during the
                        # heal, than set their HP to max, else pass.
                        playerIG.health = playerIG.maxhealth
                    else:
                        pass
                    turn -=1 # remove a turn
                    time.sleep(3)
                    continue # start the fight loop again.
                elif ans.lower() == 'equip': # if the player chose to equip a new spell
                    equip() # call the equip function
                    time.sleep(1)
                    continue # restart the loop without removing a turn, keeping it the players turn
                else: # if use item
                    while True: # loop for text input
                        if playerIG.items != {}: # if the player has items
                            print('You have %s, what would you like to use?' % playerIG.items)
                            print('*[^Item(s)^, Back]*')
                            ans2 = input(prompt)
                            if ans2.lower() in playerIG.items: # if the item the player selected is in the players inventory
                                if ans2.lower() == '50hp potion':
                                    if playerIG.health == playerIG.maxhealth:
                                        print('You cannot use a potion at max health!')
                                    else:
                                        pass
                                    playerIG.health += 50 # adds health to player
                                    turn -= 1 # adds a turn
                                    del playerIG.items['50hp potion']
                                    if playerIG.health > playerIG.maxhealth:
                                        playerIG.health = playerIG.maxhealth
                                    break
                                elif ans2.lower() == '100hp potion':
                                    if playerIG.health == playerIG.maxhealth:
                                        print('You cannot use a potion at max health!')
                                    else:
                                        pass
                                    playerIG.health += 100
                                    turn -= 1
                                    del playerIG.items['100hp potion']
                                    if playerIG.health > playerIG.maxhealth:
                                        playerIG.health = playerIG.maxhealth
                                    break
                                else: # A useless item not used in fight
                                    print('That item is not use-able in fights!')
                                    continue
                            elif ans2.lower() == 'back': # if the player selected back, break the loop
                                break
                        else: # if the player has no items, break
                            print('You have no items\n')
                            break
                    continue # when broken in the while loop stated above, it comes here and continues the fight loop
            else: # if the users initial input is not valid, continue
                continue
        elif turn == 0: # if the enemies turn
            print("// %s's TURN //\n" % enemy.name.upper())
            print('// %s attacked you with %s and did %i damage //' %(enemy.name, enemy.currentAttack, enemyAttack))
            time.sleep(3)
            if playerIG.magicType == 'Defense': # if the players magic type is defense
                beforeAttack = enemyAttack # set a variable that keeps track of the enemy attack before damage
                # is reduced.
                percentOff = (enemyAttack * .3) # finds the percent the player avoids from damage
                enemyAttack = enemyAttack - percentOff # takes that damage
                print('Although, you blocked %i of the %i damage due to your Defense Magic!' % (percentOff, beforeAttack))
            elif playerIG.magicType == 'Speed': # If the players magic type is speed
                dodgeChance = random.randint(0,10) # Set the dodge chance to a random number between 0 and 10
                #print(dodgeChance) # REMOVE THIS, IT IS FOR TESTING PURPOSES
                if dodgeChance <=2: # If the dodgechance value is less than 2, else pass
                    print('Although, you dodged it and took no damage!')
                    turn += 1 # add a turn
                    time.sleep(3)
                    stunAvailable = True # Allow the user to stun again
                    continue # restart the loop before the user takes damage.
                else:
                    pass
            else: # if the users magic doesnt have an effect pass
                pass
            playerIG.health -= enemyAttack # deal damage to the player
            turn += 1 # add a turn
            time.sleep(3)
            stunAvailable = True # allow the player to stun the enemy
            continue # restart the loop

def winFight(): # Function for fight, allows code to be read easier
    if enemy.health <= 0:
        print('Great job! you defeated %s ' % enemy.name)
        print('You gained %i gold from winning this battle!\n' % enemy.golddrop)
        playerIG.gold += enemy.golddrop
        return True

def loseFight(): # function for fight, allows code to be read easier
    deathMessage = random.randint(0,3) # chooses a random death message
    if playerIG.health <= 0:
        if deathMessage == 0:
            print('You: UGHHHHHHH')
        if deathMessage == 1:
            print('You: ARGGHGHGGG')
        if deathMessage == 2:
            print('You: OOF')
        if deathMessage == 3:
            print('You: AHHHHHHHHH')
        print('You have died')
        time.sleep(4)
        return True

def yesNo(): # function for yes and no questions
    while True: # loop for user input
        print('*[Yes, No]*')
        ans = input(prompt)
        if ans.lower() == 'yes':
            return True
        elif ans.lower() == 'no':
            return False
        else: # if the user enters something other than yes or no, start the loop again
            continue

def checkInput(ans): # function to check the users input for commands
    commands = ['/menu', '/inventory','/equip','/pinfo','/help','/playerinfo','/inv','/h'] # creates a list of inputs
    if ans in commands: # if the player enters a valid input, else, pass
        if ans == '/menu':
            menu() # calls the menu function
        elif ans == '/inventory' or ans == '/inv':
            print('Your items include: ' + str(playerIG.items))
            print('Your spells include: ' + str(playerIG.spells))
            print('If you would like to equip a new spell, use /equip')
        elif ans == '/equip':
            equip() #calls the equip function
        elif ans == '/playerinfo' or ans == '/pinfo':
            print('Name - %s'% playerIG.name)
            print('Health - %i'% playerIG.maxhealth)
            print('Attack - %i'% playerIG.base_attack)
            print('Gold - %i' % playerIG.gold)
            print('Equipped spell - %s'% playerIG.currentSpell)
            print('Magic Type - %s'% playerIG.magicType)
        elif ans == '/help' or ans == '/h':
            print('Commands\n')
            print('/menu --> Goes to the menu\n')
            print('/inventory or /inv --> Shows your inventory\n')
            print('/equip --> Brings you to the equip menu\n')
            print('/playerinfo or /pinfo --> Shows you the player info\n')
            print('/help or /h --> Shows you this menu\n')
            return True
        else: # Will never happen, although good to have
            pass
    else: # if the user didnt enter a command, pass
        pass

def fightFlash(): # Function for the fight flash "animation"
    os.system('cls')
    for i in range(0,7): # prints the fight animation 7 times
        fightArt()
        fightArt()
        fightArt()
        time.sleep(.15)
        os.system('cls') # clears screen
        fightArt2()
        fightArt2()
        fightArt2()
        time.sleep(.05)
        os.system('cls')

def menu(): # Menu function
    while True: #loop for the menu
        menuArt() # calls the menu art function, showing the user what they can option
        choice = ['start game', 'start', 'save game', 'save', 'load game', 'load', 'continue game', 'continue',
                  'override']
        while True: # loop for text input, reason for another loop is that I do not want the menu art called again
            ans2 = input(prompt)
            if ans2.lower() in choice: # if the input is valid
                if ans2.lower() == 'start game' or ans2.lower() == 'start':
                    firstInteraction() # start the game
                elif ans2.lower() == 'save game' or ans2.lower() == 'save':
                    global playerIG
                    with open('player_save.dat', 'wb') as f: # using the pickle library, the game gets saved
                        pickle.dump(playerIG, f)
                    global itemshopsIG
                    with open('shop_save.dat','wb') as g:
                        pickle.dump(itemshopsIG, g)
                    print('You have saved the game!')
                elif ans2.lower() == 'load game' or ans2.lower() == 'load': # using the pickle library, the game gets
                    # loaded
                    if os.path.exists('player_save.dat') is True and os.path.exists('shop.save.dat') is True:
                        with open('player_save.dat', 'rb') as f:
                            playerIG = pickle.load(f)
                        with open('shop_save.dat', 'rb') as g:
                            itemshopsIG = pickle.load(g)
                            print('Your game save has been loaded')
                    else:
                        print('There is nothing to be loaded.')
                elif ans2.lower() == 'override':  # Part of the menu that allows testers to go to a part of the game.
                                                    # Normal players wouldn't be able to go here, as they wouldn't
                                                    # know to type override.
                    path_continueIntoArkala()
                else:
                    goto()
            else:
                continue

def equip(): # Function for equiping weapons
    print('What spell would you like to equip (Case Sensitive) ? These are your spells: ')
    for spell in playerIG.spells: # Lists each spell in the players inventory
        print(spell)
    print('If you wish to leave this menu without equipping a new weapon, enter "back"')
    while True: # While loop for text input
        equip = input(prompt)
        if equip in playerIG.spells: # if the player has the spell
            if equip == playerIG.currentSpell: # if the player tries to equip the spell that they are currently using.
                print('%s is already equipped, try again.' % playerIG.currentSpell)
                continue
            else: #else, equip the spell that they entered
                playerIG.currentSpell = equip
                print('%s has just been equipped!' % equip)
                break
        elif equip.lower() == 'back':
            break
        else:
            print('That is not valid')
            continue

def goto(): # function used for continue option in menu, it looks at where the player is and loads that instance.
    if playerIG.currentInteraction == 'fithInteraction':
        fourthInteraction()
    elif playerIG.currentInteraction == 'path_leaveAcademy':
        path_leaveAcademy()
    elif playerIG.currentInteraction == 'path_followPath':
        path_followPath()
    elif playerIG.currentInteraction == 'path_continueIntoArkala':
        path_continueIntoArkala()
    elif playerIG.currentInteraction == 'northGateArkala':
        path_northGateArkala()
    elif playerIG.currentInteraction == 'continueNorth':
        path_continueNorth()
    elif playerIG.currentInteraction == 'enterGatka':
        path_enterGatka()
    elif playerIG.currentInteraction == 'goWest':
        path_goWest()
    elif playerIG.currentInteraction == 'goToClearing':
        path_goToClearing()
    elif playerIG.currentInteraction == 'southGateArkala':
        path_southGateArkala()
    elif playerIG.currentInteraction == 'continueSouth':
        path_continueSouth()
    elif playerIG.currentInteraction == 'goToCave':
        path_goToCave()
    else:
        print('There is nothing to continue to.')


#______________________________________________Art Functions____________________________________________________________
def credits():
    print('______          ___            _   _        ______ _            _                          ')
    print('| ___ \        / _ \          | | (_)       | ___ \ |          | |                         ')
    print('| |_/ /_   _  / /_\ \_   _ ___| |_ _ _ __   | |_/ / | __ _  ___| | ___ __ ___   __ _ _ __  ')
    print("| ___ \ | | | |  _  | | | / __| __| | '_ \  | ___ \ |/ _` |/ __| |/ / '_ ` _ \ / _` | '_ \ ")
    print("| |_/ / |_| | | | | | |_| \__ \ |_| | | | | | |_/ / | (_| | (__|   <| | | | | | (_| | | | |")
    print("\____/ \__, | \_| |_/\__,_|___/\__|_|_| |_| \____/|_|\__,_|\___|_|\_\_| |_| |_|\__,_|_| |_|")
    print("        __/ |                                                                              ")
    print("       |___/                                                                               ")


def title():
    print('/$$$$$$$$ /$$$$$$  /$$       /$$$$$$$$  /$$$$$$         /$$$$$$  /$$$$$$$$        /$$$$$$        /$$      /$$ /$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$$ ')
    print('|__  $$__//$$__  $$| $$      | $$_____/ /$$__  $$       /$$__  $$| $$_____/       /$$__  $$      | $$  /$ | $$|_  $$_/|_____ $$  /$$__  $$| $$__  $$| $$__  $$')
    print('   | $$  | $$  \ $$| $$      | $$      | $$  \__/      | $$  \ $$| $$            | $$  \ $$      | $$ /$$$| $$  | $$       /$$/ | $$  \ $$| $$  \ $$| $$  \ $$')
    print('   | $$  | $$$$$$$$| $$      | $$$$$   |  $$$$$$       | $$  | $$| $$$$$         | $$$$$$$$      | $$/$$ $$ $$  | $$      /$$/  | $$$$$$$$| $$$$$$$/| $$  | $$')
    print('   | $$  | $$__  $$| $$      | $$__/    \____  $$      | $$  | $$| $$__/         | $$__  $$      | $$$$_  $$$$  | $$     /$$/   | $$__  $$| $$__  $$| $$  | $$')
    print('   | $$  | $$  | $$| $$      | $$       /$$  \ $$      | $$  | $$| $$            | $$  | $$      | $$$/ \  $$$  | $$    /$$/    | $$  | $$| $$  \ $$| $$  | $$')
    print('   | $$  | $$  | $$| $$$$$$$$| $$$$$$$$|  $$$$$$/      |  $$$$$$/| $$            | $$  | $$      | $$/   \  $$ /$$$$$$ /$$$$$$$$| $$  | $$| $$  | $$| $$$$$$$/')
    print('   |__/  |__/  |__/|________/|________/ \______/        \______/ |__/            |__/  |__/      |__/     \__/|______/|________/|__/  |__/|__/  |__/|_______/ ')

def fightArt():
    print('FFFFFFFFFFFFFFFFFFFFFFIIIIIIIIII      GGGGGGGGGGGGGHHHHHHHHH     HHHHHHHHHTTTTTTTTTTTTTTTTTTTTTTT')
    print('F::::::::::::::::::::FI::::::::I   GGG::::::::::::GH:::::::H     H:::::::HT:::::::::::::::::::::T')
    print('F::::::::::::::::::::FI::::::::I GG:::::::::::::::GH:::::::H     H:::::::HT:::::::::::::::::::::T')
    print('FF::::::FFFFFFFFF::::FII::::::IIG:::::GGGGGGGG::::GHH::::::H     H::::::HHT:::::TT:::::::TT:::::T')
    print('  F:::::F       FFFFFF  I::::I G:::::G       GGGGGG  H:::::H     H:::::H  TTTTTT  T:::::T  TTTTTT')
    print('  F:::::F               I::::IG:::::G                H:::::H     H:::::H          T:::::T        ')
    print('  F::::::FFFFFFFFFF     I::::IG:::::G                H::::::HHHHH::::::H          T:::::T        ')
    print('  F:::::::::::::::F     I::::IG:::::G    GGGGGGGGGG  H:::::::::::::::::H          T:::::T        ')
    print('  F:::::::::::::::F     I::::IG:::::G    G::::::::G  H:::::::::::::::::H          T:::::T        ')
    print('  F::::::FFFFFFFFFF     I::::IG:::::G    GGGGG::::G  H::::::HHHHH::::::H          T:::::T        ')
    print('  F:::::F               I::::IG:::::G        G::::G  H:::::H     H:::::H          T:::::T        ')
    print('  F:::::F               I::::I G:::::G       G::::G  H:::::H     H:::::H          T:::::T        ')
    print('FF:::::::FF           II::::::IIG:::::GGGGGGGG::::GHH::::::H     H::::::HH      TT:::::::TT      ')
    print('F::::::::FF           I::::::::I GG:::::::::::::::GH:::::::H     H:::::::H      T:::::::::T      ')
    print('F::::::::FF           I::::::::I   GGG::::::GGG:::GH:::::::H     H:::::::H      T:::::::::T      ')
    print('FFFFFFFFFFF           IIIIIIIIII      GGGGGG   GGGGHHHHHHHHH     HHHHHHHHH      TTTTTTTTTTT      ')

def fightArt2():
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')
    print('/////////////////////////////////////////////////////////////////////////////////////////////////')

def menuArt():
    print('|-------------------------------------------------------------------------------------------------------------------------------------------------------------|')
    print('|                                                                                                                                                             |')
    print('|                                                                    START GAME                                                                               |')
    print('|                                                                    SAVE GAME                                                                                |')
    print('|                                                                    LOAD GAME                                                                                |')
    print('|                                                                  CONTINUE GAME                                                                              |')
    print('|                                                                                                                                                             |')
    print('|_____________________________________________________________________________________________________________________________________________________________|')

def tobeContinuedArt():
    print(' _____        _                      _   _               _ ')
    print('|_   _|___   | |_ ___    ___ ___ ___| |_|_|___ _ _ ___ _| |')
    print('  | | | . |  | . | -_|  |  _| . |   |  _| |   | | | -_| . |')
    print('  |_| |___|  |___|___|  |___|___|_|_|_| |_|_|_|___|___|___|')







title()
print('')
menu()

