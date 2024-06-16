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

    show text "Team 8 Interactive Productions Presents" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "Rights-Quest" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    return

#movie bg fn
image snowy_field = Movie(size=(1920, 1080), channel="movie", play="images/snowy_field.ogv")

#snow--fall
image snow1 = Fixed(SnowBlossom("gui/snow1.png", 50, xspeed=(20, 50), yspeed=(100, 200), start=50))
image snow2 = Fixed(SnowBlossom("gui/snow2.png", 50, xspeed=(20, 50), yspeed=(100, 200), start=50))
image heavysnow1 = Fixed(SnowBlossom("gui/snow1.png", 2000, xspeed=(400, 1000), yspeed=(6000, 8000), start=2000))
image heavysnow2 = Fixed(SnowBlossom("gui/snow1.png", 3000, xspeed=(600, 800), yspeed=(3000, 4000), start=3000))
image heavysnow3 = Fixed(SnowBlossom("gui/snow1.png", 3000, xspeed=(500, 900), yspeed=(3000, 4000), start=3000))


#blur fn
image devchar = At('dev', sprite_highlight('dev'))
image grannychar = At('granny', sprite_highlight('granny'))

image sischar main= At('sis main', sprite_highlight('eileen'))
image sischar = At('sis', sprite_highlight('eileen'))

image brochar main= At('bro main', sprite_highlight('keith'))
image brochar = At('bro', sprite_highlight('keith'))

image userchar = At('no_char', sprite_highlight('me'))

image santachar = At('santa', sprite_highlight('santa'))
image santachar_shadow = At('santa_shadow', sprite_highlight('santa'))


image bullychar = At('bully', sprite_highlight('bully'))

image mrsgraychar = At('mrsgray', sprite_highlight('mrsgray'))

image storeownerchar = At('storeowner', sprite_highlight('storeowner'))

image mrwickchar = At('mrwick', sprite_highlight('mrwick'))

#char intro
define dev = Character("Dev",image='devchar',callback=name_callback, cb_name='dev')
define gran = Character("Granny",image='granchar',callback=name_callback, cb_name='granny')
define sis = Character("Eileen",image='sischar',callback=name_callback, cb_name='eileen')
define bro = Character("Keith",image='brocahr',callback=name_callback, cb_name='keith')
define user = Character("Me",image='userchar',callback=name_callback, cb_name='me')
define santa = Character("Santa",image='santachar',callback=name_callback, cb_name='santa')
define bully = Character("Bully", image='bullychar',callback=name_callback, cb_name='bully')
define storeowner = Character("Store Owner", image='storeownerchar',callback=name_callback, cb_name='storeowner')
define mrsgray = Character("Mrs.Gray", image='mrsgraychar',callback=name_callback, cb_name='mrsgray')
define mrwick = Character("Mr.Wick", image = 'mrwickchar', callback=name_callback, cb_name='mrwick')


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