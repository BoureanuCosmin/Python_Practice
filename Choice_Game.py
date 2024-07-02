print(r'''
       ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^
      /|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\
      /|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\
      /|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# Write your code below this line 👇
choice1 = input(
    'You\'re at a crossroad, where do you want to go? Type "left" or "right" \n'
)

if choice1 == "right":
    print("You came across a deer. What do you do?")
    print(r"""

                          ,/  \.
                         |(    )|
                    \`-._:,\  /.;_,-'/
                     `.\_`\')(`/'_/,'
                         )/`.,'\(
                         |.    ,|
                         :6)  (6;
                          \`\ _(\
                           \._'; `.___...---..________...------._
                            \   |   ,'   .  .     .       .     .`:.
                             \`.' .  .         .   .   .     .   . \\
                              `.       .   .  \  .   .   ..::: .    ::
                                \ .    .  .   ..::::::::''  ':    . ||
                                 \   `. :. .:'            \  '. .   ;;
                                  `._  \ ::: ;           _,\  :.  |/(
                                     `.`::: /--....---''' \ `. :. :`\`
                                      | |:':               \  `. :.\
                                      | |' ;                \  (\  .\
                                      | |.:                  \  \`.  :
                                      |.| |                   ) /  :.|
                                      | |.|                  /./   | |
                                      |.| |                 / /    | |
                                      | | |                /./     |.|
                                      ;_;_;              ,'_/      ;_|
                                     '-/_(              '--'      /,'/
                  """)
    choice2 = input('Type "run" or "pet" \n')
    if choice2 == "run":
        print("You saw a house in the distance. What do you do? \n")
        choice3 = input('Type "enter" or "keep running" \n')
        if choice3 == "keep running":
            print('A snake bit you. Game over.')
            print(r'''
                              .--.--.
       `'.'.                .'`__ o  `;__.      
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
              ''')

        elif choice3 == "enter":
            print('You saw a chest. What do you do? \n')
            print(r'''
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/[TomekK]
            *******************************************************************************
            ''')
            choice4 = input('Type "open" or "leave it" \n')
            if choice4 == "open":
                print("You found the treasure. You win!")
                print(r'''

                      __________________
                    .-'  \ _.-''-._ /  '-.
                  .-/\   .'.      .'.   /\-.
                 _'/  \.'   '.  .'   './  \'_
                :======:======::======:======:  
                 '. '.  \     ''     /  .' .'
                   '. .  \   :  :   /  . .'
                     '.'  \  '  '  /  '.'
                       ':  \:    :/  :'
                         '. \    / .'
                           '.\  /.'    
                             '\/'
                ''')
            else:
                print('You decided to leave the chest alone. Game over.')
    else:
        print('You are blessed to death. Game over.')
else:
    print("A bear killed you. Game over.")
    print(r'''
           .--.              .--.
          : (\ ". _......_ ." /) :
           '.    `        `    .'
            /'   _        _   `\
           /     X}      {X     \
          |       /      \       |
          |     /'        `\     |
           \   | .  .==.  . |   /
            '._ \.' \__/ './ _.'
            /  ``'._-''-_.'``  \
                    `--`
     ''')
