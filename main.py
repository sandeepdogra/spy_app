from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime
STATUS_MESSAGES = ["My name is Bond, James Bond", "Shaken, not stirred"]

print "Hello! Let's get started"  #message first display

choice = raw_input("Do you want to continue as a default user. Press Y/N: ") #start

def add_status():
   updated_status_message = None
   if spy.current_status_message != None:
       print "Your current status message is %s \n" % (spy.current_status_message)
   else:
       print "You don't have any status message currently \n"
       default = raw_input("Do you want to select from the older status (Y/N)? ")
       if default.upper() == "N":
           new_status_message = raw_input("What status message do you want to set? ")
           if len(new_status_message) > 0:
               STATUS_MESSAGES.append(new_status_message)
               updated_status_message = new_status_message
       elif default.upper() == "Y":
           item_position = 1
           for message in STATUS_MESSAGES:
               print "%d %s" % (item_position, message)
               item_position = item_position + 1
           message_selection = int(raw_input("\nChoose from the above messages "))
           if len(STATUS_MESSAGES) >= message_selection:
               updated_status_message = STATUS_MESSAGES[message_selection - 1]
       else:
            print " The option you chose is not valid.Press either Y or N."
       if updated_status_message:
           print "Your updated status message is: %s" % (updated_status_message)
       else:
           print "You current don't have a status update"
       return updated_status_message


def add_friend():
    new_friend = Spy('','',0,0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = int(raw_input("Age?"))
    new_friend.rating = float(raw_input("Spy rating?"))

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print "Friend Added"
    else:
        print "Sorry! Invalid entry. We can't add friend with the details you provided"
    return len(friends)

def select_a_friend():
    item_number = 0
    for friend in friends:
        print "%d %s %s aged %d with rating %.2f is online" % (item_number +1, friend.salutation, friend.name ,friend.age, friend.rating)
        item_number = item_number + 1
    friend_choice = raw_input("Choose from your friends")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position

def send_message():
    friend_choice = select_a_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say?")
    if len(text) > 0:
        Steganography.encode(original_image, output_path, text)
        new_chat = ChatMessage(text,True)
        friends[friend_choice].chats.append(new_chat)
        print "Your secret message image is ready!"
    else:
        print"Please,provide text for secret message"


def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text,False)
    friends[sender].chats.append(new_chat)
    print "Your secret message has been saved!"


def read_chat_history():
    read_for = select_a_friend()
    print '\n6'
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print "[%s] %s: %s" % (chat.time.strftime("%d %B %Y"), "You said:", chat.message)
        else:
            print "[%s] %s said: %s" % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name
    print "Authentication complete. Welcome %s %d %.2f Proud to have you onboard" %(spy.name,spy.age,spy.rating)
    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
        menu_choice = int(raw_input(menu_choices))
        if menu_choice == 1:
            spy.current_status_message = add_status()
        elif menu_choice == 2:
             number_of_friends = add_friend()
             print "You have %d friends" %(number_of_friends)
        elif menu_choice == 3:
              send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice == 5:
            read_chat_history()
        elif menu_choice == 6:
            show_menu = False
        else:
            print"Invalid choice,provide valid please!"

if choice.upper() == "Y":           #deafult user
    start_chat(spy)
elif choice.upper() == "N":         #new user
    spy = Spy('','',0,0.0)
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy.name) > 0:
        spy.salutation = raw_input("enter M or F for Mr. or Ms.?: ")
        if spy.salutation.upper()== "M":
            spy_salutation = "Mr"
            spy.salutation = spy_salutation
        elif spy.salutation.upper() == "F":
            spy_salutation = "Ms."
            spy.salutation = spy_salutation
        else:
            print"Please enter valid M/F"
            exit(0)
        print"Hi " +spy.salutation+" "+ spy.name + " I want to know more about you"
        spy.age = int(raw_input("What is your age?"))
        if (spy.age >= 12 and spy.age <= 50):
            spy.rating = float(raw_input("what is your spy rating"))
            if (spy.rating >= 4.5):
                print"Great ace!"
            elif (spy.rating >= 3.5 and spy.rating <= 4.5):
                print "You are good one spy"
            elif (spy.rating >= 2.5 and spy.rating <= 3.5):
                print "You can always do better"
            else:
                print "We provider helper to you in the office"
            start_chat(spy)
        else:
            print "Sorry you are not of valid age to be a spy"
    else:
        print "Please enter a valid spy name"
else:
    print "enter valid choice"

