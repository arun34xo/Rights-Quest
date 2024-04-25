# The script of the game goes in this file.
init python:
    res = False

#arg used in game
default gender = "none"
default p1 = "none"
default p2 = "none"
default p3 = "none"
default child = True


#starting splash screen
label splashscreen:
    scene black
    with Pause(1)

    show text "Team 8 Interactive Prodcutions Presents" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "Rights-Quest" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    return


#blur fn
image devchar = At('dev', sprite_highlight('dev'))

image grannychar = At('granny', sprite_highlight('granny'))

image sischar main= At('sis main', sprite_highlight('eileen'))
image sischar = At('sis', sprite_highlight('eileen'))

image brochar main= At('bro main', sprite_highlight('keith'))
image brochar = At('bro', sprite_highlight('keith'))

image userchar = At('no_char', sprite_highlight('me'))

image santachar = At('santa', sprite_highlight('santa'))

#char intro
define dev = Character("Dev",image='devchar',callback=name_callback, cb_name='dev')
define gran = Character("Granny",image='granchar',callback=name_callback, cb_name='granny')
define sis = Character("Eileen",image='sischar',callback=name_callback, cb_name='eileen')
define bro = Character("Keith",image='brocahr',callback=name_callback, cb_name='keith')
define user = Character("Me",image='userchar',callback=name_callback, cb_name='me')
define santa = Character("Santa",image='santachar',callback=name_callback, cb_name='santa')
define bully = Character("Bully", image='bullychar',callback=name_callback, cb_name='bully')
define storeowner = Character("StoreOwner", image='storeownerchar',callback=name_callback, cb_name='storeowner')
define mrsgray = Character("Gray", image='graychar',callback=name_callback, cb_name='mrsgray')


label start:

    #jump pro3

    scene bg dev
    show devchar with moveinright
    dev "Oh, Hey there. Welcome to Rights Quest"
    dev "Before we begin, mind answering some question?"
    show devchar at right with move
    
    menu:
        dev "User's gender is :"

        "Male":
            $gender = "male" #setting gender
            $p1 = "he" #setting pronoun
            $p2 = "him"
            $p3 = "his"

        "Female":
            $gender = "female"
            $p1 = "she"
            $p2 = "her"
            $p3 = "her"

        "Prefer Not To Say":
            $gender = "none"
            $p1 = "they"
            $p2 = "them"
            $p3 = "them"

    menu:
        dev "User's age is :"

        "4-6":
            $child=True
        "7-12+":
            $child=False

    dev "Game has been customized to suit the user.\nEnjoy Little One!!"

    jump pro1