import json


# Data to be written
character_info = {
    "name": "",
    "sex": "",
    "age": ""
}

try:
    test = open('save_character.json', 'r')
    test.close()
except:
    test = False

if test == False:
    # String Variable
    str1 = "Hello, I'm Zabb-g'wosh \nIs your universal translater working? \n"
    # Print to console
    print(str1)

    input("[I think so?]")

    # get user input
    character_info['name'] = input("Great, great, nothing to be concerned but...we don't really know anything about you. \n Can you fill in the blanks?\n Let's start with an easy one...What is your name?\n")

    print("Nice to meet you, \n" + character_info['name'])

    character_info['sex'] = input("We don't understand your species body parts...are you a [male] or [female]?")

    l = len(character_info['name'])
    print("Your name is "+str(l)+" letters long.\n Is that how old you are? Do you get a letter for every one of your people's years?")
    c = character_info['name'].count("s")
    character_info['age']=input("That seems like a lot, just how old are you really?:")

    cfile = open('save_character.json', 'w')
    save_data = json.dumps(character_info, indent=4)
    cfile.write(save_data)
    cfile.close() 
else:

    print("And it has "+" instances of the letter s! Isn't that cool! \n")
    a2 = input("no/yes\n")

    rfile = open('save_character.json', 'r')
    char_data = json.load(rfile)
    print(char_data['name'])
    # you only live to 100, and you now only have 67 years left. Do things that increase or decrease your life.
    if a2 == "no":
        print("Well thats not nice, your not cool!")
    elif a2 == "yes":
        print("Dope we should be friends, let's go!")
    else:
        print("That wasn't an option!")

s = '''\
          \ /
          oVo
      \___XXX___/
       __XXXXX__
      /__XXXXX__\\
      /   XXX   \\
           V\
'''.format(length='multi-line', ordinal='second')

print(s)













