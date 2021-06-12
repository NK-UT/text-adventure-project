# global functions---------------------------------------------------------------
import random
import time
items = []

def print_pause(message):
    print(message)
    time.sleep(.5)


def valid_input_var(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("Try again dumb dumb.")

# Add a random chance that the elevator will break and crash to the ground, then the player is magically
# transported to safety and takes another elevator.

def elevator():
    items = []
    print("--------------------")
    menu()
    print_pause("--------------------")
    options = (["lobby", "human resources", "engineering department", "engineering"])
    response = valid_input_var("Which floor, please?.\n--------------------\n", options)
    if "lobby" in response:
        lobby()
    elif "human resources" in response:
        human_resources()
    elif "engineering department" in response:
        engineering_department()
    elif "engineering" in response:
        engineering_department()
    print_pause("")
    print_pause("")


#Chapter 1 Functions-------------------------------------------------------------


def chapter_1_intro():
    print_pause("")
    print_pause("")
    print_pause("                               ~~The Elevator~~")
    print_pause("")
    print_pause("")
    print_pause("Hi!")
    print_pause("")
    print_pause("^o^")
    print_pause("")
    print_pause("Welcome to your first day at the slave facto... SuperMegaCorpTM!")
    print_pause("You will need a few things before you can give up your sou- I mean...")
    print_pause("... begin work.")
    print_pause("You'll need your prison tag... I mean ID card,")
    print_pause("And the Book of Transgress... Employee Handbook.")
    print_pause("")
    print_pause("Head to the lobb... I mean the... Wait. That was right. The lobby. Yes. The lobby.")
    print_pause("Head to the lobby and pick up your pri... ID card.")
    print_pause("Then head to Human Traffi... Human Resources and get the Book of...")
    print_pause("Employee handgu... Handbook. Your Employee Handbook.")
    print_pause("You'll need all of these before going to the Hall of Indentured Servi... Engineering.")
    print_pause("Trust us. You DON'T want to go to Engineering without that stuff.")
    print_pause("")
    print_pause("*shudder*")
    print_pause("")
    print_pause("Good luck! #^_^#")
    print_pause("")


def menu():
    print("Lobby")
    print("Human Resources")
    print("Engineering Department")


def lobby():  #first floor
    print_pause("")
    print("~~")
    print_pause("You press the button for the lobby.")
    print_pause("There is a loud metallic clang inside the door. Strange.")
    print_pause("After a moment, the elevator begins to rumble as it goes up.")
    print_pause("The elevator dings and there is the lobby.")
    print("~~")
    print("")
    if "ID_Card" in items:
        print_pause("")
        print_pause("~~")
        print_pause("The clerk looks at you like you have slugs on your face.")
        print_pause("        'I already gave you your ID, creep.'")
        print_pause("You back away slowly, nodding and not turning your back to her.")
        print_pause("~~")
        print_pause("")
        elevator()
    elif "ID_Card" not in items:
        print_pause("")
        print_pause("~~")
        print_pause("You approach the clerk. She's filing her nails.")
        print_pause("       'Hello. I'm new here. May I please have my ID?' You ask.")
        print_pause("The clerk looks you up and down, and flicks your ID card on to the floor.")
        print_pause("You pick it up and leave, shooting the rude clerk a pouty glare.")
        items.append("ID_Card")
        print_pause("")
        print_pause("**You acquired: ID CARD!!! YAY!**")
    print_pause("~~")
    print_pause("")
    elevator()


def human_resources(): #second floor
    print_pause("")
    print_pause("~~")
    print_pause("You press the button for Human Resources.")
    print_pause("The elevator rumbles again.")
    print_pause("The elevator comes to a stop and dings.")
    print_pause("The doors slide halfway open, close, then open again and the digital display flickers.")
    print_pause("You step out. The lights are off. The entire floor is silent.")
    print_pause("~~")
    print_pause("")
    if "ID_Card" in items:
        print_pause("~~")
        print_pause("""The room explodes into illumination. Beskirtted office ladies pop confetti
and blow little kazoos.""")
        print_pause("They whistle and clap as a door bursts open and the head of HR cartwheels out.")
        print_pause("        'I see you have your ID Card!' she shouts, doing a backflip and landing in front of you.")
        print_pause("        'Here is your copy of the Employee Handbook!'")
        print_pause("You take the book, bewildered and befuddled, then leave.")
        print_pause("You scratch your head confusedly with a corner of the book as you get back on the elevator.")
        items.append("employee_handbook")
        print_pause("")
        print_pause("**You acquired: Book of Transgressio... EMPLOYEE HANDBOOK!!! YAY!**")
        print_pause("~~")
        print_pause("")
    if "ID_Card" not in items:
        print_pause("~~")
        print_pause("There is the faint smell of brimstone.")
        print_pause("As you edge your way into the area, a door bursts open.")
        print_pause("""Standing there, wreathed in flame is the shadowy outline of a woman in a sensible, 
businesslike skirt staring at you with hands on hips and a look of purest abhorrence 
in her eyes.""")
        print_pause("       'Who defiles my floor with their un-ID-Cardedness?!' She bellows.")
        print_pause("You nope out of there and flee back into the elevator, arms flapping behind you as you go.")
        print_pause("You jab the 'CLOSE DOOR' button like a madman.")
    print("~~")
    print_pause("")
    elevator()


def engineering_department(): #third floor
    print_pause("")
    print_pause("~~")
    options = (["scan my card", "leave"])
    response2 = valid_input_var("""There is a black rectangle on the elevator wall. A green light blinks on it.\n
What do you do?\n--------------------\n  Scan my card\n  Leave\n--------------------\n""", options)
    print_pause("")
    if response2 == "scan my card":
        if "ID_Card" in items:
            print_pause("The elevator door opens.")
            print_pause("A voice says; 'Engineering department. You made it! Yay!'")
            print_pause("~~")
            print_pause("")
            if "employee_handbook" in items:
                print_pause("")
                print_pause("~~")
                print_pause("""The card reader beeps and the door hisses open on pneumatic pistons.
A figure robbed in purest white light emerges to greet you. 
    'I see you have your ID card as well as the sacred Book of Transgre... 
Employee handbook.' It says. 'Long has it been since a worthy challenger has 
approached this door with all of the required items.' 
You look around and see row after row of nerdy guys in glasses clacking away on 
ergonomic mechanical keyboards. 
    'K,' you say.""")
                print_pause("        'There is, however, one more challenge!' he says")
                print_pause("""The figure steps aside, and the door transforms into a wall of 
shimmering light. He laughs maniacally as you're sucked bodily into the portal.""")
                print_pause("~~")
            else:
                print_pause("")
                print_pause("~~")
                print_pause("Wait... What?! Where's your handbook?!")
                print_pause("Come back when you have the book you worm!")
                print_pause("You are mysteriously transported out of the building.")
                print_pause("""You materialize in the dumpster behind that
Chinese restaurant next door.""")
                print_pause("You make your way back inside. You're just inside the main entrance.")
                print_pause("~~")
                print_pause("")
                elevator()
        else:
            print_pause("")
            print_pause("~~")
            print_pause("A voice booms in the elevator:") 
            print_pause("        'Piss off!'")
            print_pause("        'Come back when you have the Book of Tra... Employee Handbook and your ID!'")
            print_pause("You are mysteriously transported out of the building.")
            print_pause("""You materialize in the dumpster behind that Chinese restaurant next door. 
Gross.""")
            print_pause("")
            print_pause("You make your way back inside, stinky and covered in noodles.") 
            print_pause("""You're in the elevator. Other people look at you with a mixture of 
disgust and a sudden hankering for lunch.""")
            print_pause("~~")
            print_pause("")
            elevator()
    if response2 == "leave":
        print_pause("""        'Ya big wuss!' a voice complains over a loudspeaker. Following it is much
grumbling and something about a Chinese restaurant.""")
        elevator()


def chapter_1():
    chapter_1_intro()
    elevator()


#chapter 2 functions--------------------------------------------------------------
def end_game():
    elevator()


def chapter_2_intro():
    print_pause("")
    print_pause("                               ~~Chapter 2: The Pit~~")
    print_pause("")
    print_pause("")
    print_pause("~~")
    print_pause("""You materialize, this time not in a dumpster behind a Chinese restaurant.
Your eyes adjust to the dark and you begin to make out shapes. 
There is a doorway. Above it is written:
        'Abandon ALGOL all who enter!'""")
    print_pause("        'ALGOL? WTH is ALGOL?' you think to yourself, and approach the door.")
    print_pause("~~")
    print_pause("")


def entrance():
    print_pause("")
    print_pause("~~")
    options_3 = (["face my challenge", "flee"])
    response_3 = valid_input_var("What do you do?\n Face my challenge!\n Flee!\n", options_3)
    if "flee" in response_3:
        print_pause("You turn tail and run. Your arms fail wildly and comically.")
        print_pause("As you run, you feel yourself de-materializing once again.")
        print_pause("You materialize in an all-too-familiar dumpster behind that Chinese restaurant.")
        print_pause("You once again make your way back into the elevator.")
        end_game()
    elif "face my challenge" in response_3:
        print_pause(""""You boldly step through the doorway. The moment you cross
the threshhold, everything goes black. A voice speaks to you and says:
    'This concludes the Nick Kay Intro to Python Adventure Game Project: Shareware Edition!'
    To continue your exciting adventures as a new developer at SuperMegaCorpTM, 
    give Nick a passing score and visit https://www.facebook.com/ElectrotechUSA !""")
        end_game()
    else:
        print_pause("That is NOT an acceptable reply!")
        entrance()

# extend the scenario to include a boss fight utilizing the random.choice function 
# from the random module. This will generate a random monster for the player to do code battle with.

def chapter_2():
    chapter_2_intro()
    entrance()
#game--------------------------------------------------------------------------


chapter_1()
chapter_2()

#----------------
#                                  ~~ELEVATOR RANDOM ENCOUNTER TEST CODE~~
# import random
# import time
#
# events = ['The elevator rumbles.', 'The elevator jerks.', 'The elevator crashes.', "That didn't work. Try again."]
#
# def variable_input(prompt, options):
#    while True:
#        response = input(prompt).lower()
#        if response in options:
#            return response
#        else:
#            print("That didn't work. Try again.")
#            return variable_input()
#
# def print_pause(message):
#    print(message)
#    time.sleep(.5)
#
# def menu():
#    print_pause("\nWelcome!")
#    print_pause("-----------------------\n1")
#    print_pause("2")
#    print_pause("3\n----------------------")
#
# def random_event():
#    event = None
#    if random.uniform(0, 1) < .25:
#        event = random.choice(events)
#    if event:
#        return event
#        elevator()
#
# def elevator():
#    menu()
#    options = (["1", "2", "3"])
#    selection = variable_input("Please choose a floor.\n", options)
#    if "1" in selection:
#        print_pause(random_event()) or print("Floor 1")
#    elif "2" in selection:
#        print_pause(random_event()) or print("Floor 2")
#    elif "3" in selection:
#        print_pause(random_event()) or print("Floor 3")
#    elevator()
#
# elevator()