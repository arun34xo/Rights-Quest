# The script of the game goes in this file.

init python:
    res = False

default gender = "none"
default p1 = "none"
default p2 = "none"
default p3 = "none"
default child = True
# name of the character.

define dev = Character("Dev",alpha=1.0)
define gran = Character("Granny",alpha=1.0)
define sis = Character("Eileen",alpha=1.0)
define bro = Character("Keith",alpha=1.0)
define user = Character("Me")
define bear = Character("Guardian Bear")
define owl = Character("Guardian Owl")
define unicorn = Character("Guardian Unicorn")

label start:

    scene bg dev
    show dev with moveinright
    dev "Oh, Hey there. Welcome to Rights Quest"
    dev "Before we begin, mind answering some question?"
    show dev at right with move
    
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