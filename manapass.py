from pystyle import Colors, Colorate, Center
# from discord_webhook import DiscordWebhook
import json
import time

print(
    Colorate.Diagonal(
        Colors.red_to_black,
        Center.XCenter("""
888b     d888        d8888 888b    888        d8888 8888888b.     d8888  .d8888b.   .d8888b.  
8888b   d8888       d88888 8888b   888       d88888 888   Y88b   d88888 d88P  Y88b d88P  Y88b 
88888b.d88888      d88P888 88888b  888      d88P888 888    888  d88P888 Y88b.      Y88b.      
888Y88888P888     d88P 888 888Y88b 888     d88P 888 888   d88P d88P 888  "Y888b.    "Y888b.   
888 Y888P 888    d88P  888 888 Y88b888    d88P  888 8888888P" d88P  888     "Y88b.     "Y88b. 
888  Y8P  888   d88P   888 888  Y88888   d88P   888 888      d88P   888       "888       "888 
888   "   888  d8888888888 888   Y8888  d8888888888 888     d8888888888 Y88b  d88P Y88b  d88P 
888       888 d88P     888 888    Y888 d88P     888 888    d88P     888  "Y8888P"   "Y8888P"\n
""")))

print(Colors.red, Center.XCenter("[1] Save password   [2] Find password"))

userChoiceLoop = -1

while userChoiceLoop == -1:
    try:
        userChoice = int(input())
        if userChoice == 1 or userChoice == 2:
            userChoiceLoop = 0
        else:
            print("Erreur ! Ce n'est pas un chiffre entre 1 et 2")
    except:
        print("Erreur ! Ce n'est pas un chiffre")

if userChoice == 1:
    print("Enter website :")
    userWebsite = input()
    print("Enter email / username :")
    userEmail = input()
    print("Enter password :")
    userPassword = input()
    # webhook = DiscordWebhook(
    #     url=
    #     'IF YOU WANT TO USE A WEBHOOK',
    #     content=
    #     f'Website : {userWebsite} | Mail / Username : {userEmail} | Password : {userPassword}'
    # )
    # response = webhook.execute()
    new_data = {userWebsite: {'email': userEmail, 'password': userPassword}}
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            data.update(new_data)
    except FileNotFoundError:
        with open('data.json', 'w') as data_file:
            json.dump(new_data, data_file, indent=4)

else:
    print("Enter a website")
    userWebsite = input()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            userEmail = data[userWebsite]['email']
            userPassword = data[userWebsite]['password']
            print(f"Username : {userEmail} | Password : {userPassword}")
            time.sleep(60)
    except KeyError as error_msg:
        print("This website isn't registered")
        time.sleep(5)
    except FileNotFoundError as error_msg:
        print("File does not exist")
        time.sleep(5)
