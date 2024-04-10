default shouted = False
default nothingcount = 0
label pro2:

    scene santa_field with fade
    "As they go to the address on the tag, they reach a field filled with Reindeers and in the middle, a house with smoke coming out of the chimney is spotted"

    show brochar at right with moveinright
    bro "Is this the right location?"

    show sischar at left with moveinleft
    sis "It must be, it's magical."

    scene bg_santahouse
    show brochar at right with moveinright
    bro "Shall we knock?"

    user "...."
    menu:
        "Knock at the door":
            hide brochar
            hide sischar
            with dissolve
            show santachar at right with moveinright:
                alpha 0.2
            santa "Who is it at this time of the day?"
            pass
        "Scream":
            user "IS ANYONE IN THERE??"
            sis "Nooo... Why are you shouting?"
            hide brochar
            hide sischar
            with dissolve
            show santachar at right with moveinright:
                alpha 0.3
            santa "Who is so rude enough to disturb a man and his reindeers like this?"
            $ shouted = True
            pass
        "Simply wait outside":
            bro "We'll be here for a while then..."
            show sischar at left with moveinleft
            sis "I'll just knock then..."
            hide brochar
            hide sischar
            with dissolve
            show santachar at right with moveinright:
                alpha 0.1
            santa "Who is it at this time of the day?"
            pass        

    show brochar at left with moveinleft
    bro "We found your bag lying around in the forest, Mister."

    hide brochar with dissolve
    show sischar at left with moveinleft
    sis "We thought we might as well as return it to the owner."

    "As the door opens, a large figure steps out with a pleasant smile"

    hide santachar with dissolve
    show santachar at right with moveinright
    sis "Oh my god it's Santa!!"
    santa "Oh my!! What a merry surprise. I was puzzled on what I should do ever since I lost the bag."
    santa "Come in children, welcome to my humble abode."

    scene bg_santa_workshop1 with fade

    show santachar at right with moveinright
    santa "I lost my bag as I was travelling back, Thank you young ones for finding the bag. You may have very well saved Christmas this year."
    
    show sischar at left with moveinleft
    sis "Really? It's an honour Mr. Santa Claus!"
    hide sischar with dissolve

    show brochar at left with moveinleft
    bro "We only did what had to be done."
    hide brochar with dissolve

    santa "If you children would like to help, I have a few missing presents around the area."

    label d2:
        pass

    "What would you like to do?"
    menu:
        "Accept the request":
            user "Of course, we don't mind helping at all"
            santa "Such a kind child, Very well!"
            pass

        "Ask for the reward":
            user "Do we get a reward?"
            santa "Such an eager child. Yes, I've prepared a series of challenges for you to overcome. The reward shall remain a surprise."
            jump d2

        "Stay silent":
            hide santachar with dissolve

            show brochar at right with moveinright
            bro "If presents missing, then someone won't have presents this Christmas"

            show sischar at left with moveinleft
            sis "I don't want people to be present-less this Christmas. Can we please help Santa?"

            menu:
                "Ok, Let's Help":
                    sis "Yayyy Thank You!!"
                    bro "Let's do this then!"
                    pass

    hide brochar
    hide sischar
    with dissolve
    show santachar at right with moveinright
    santa "I thank you again young ones, I've got a map with the locations of the presents I lost."
    santa "I kept it somewhere here... Where did I keep it now? Hmmm..."
    jump mini2

    label foundhiddenitem:
        pass

    scene bg_santa_workshop with dissolve
    show santachar at right with moveinright
    santa "Ahh!! There it is, good job for finding it!"
    scene bg_mapwpoint with fade
    santa "Yes, the presents that I've lost are located in these 3 areas"
    scene bg_santa_workshop with fade
    show santachar at right with moveinright
    santa "I wish you the best of luck on your adventure"
    hide santachar with dissolve
    show brochar at right with moveinright
    bro "Very well, we shall victoriously be back, Santa!"

    show sischar at left with moveinleft
    sis "We won't let you down!"
    jump L1








#######################################################################################################################################
'''    label choice1:
        menu:
            "Stand at each of the 3 pillars separately" if la==True:
                jump stand3pill
            "Look around a bit":
                if la==False:
                    jump lookaround
                elif la==True:
                    jump lookarounddone
            "Do nothing..." if nothingcount<2:
                jump donothing

    label stand3pill:
        user "Lets stand besides the 3 pillars and see what happens?"
        show brochar at right with moveinright
        bro "That's a good idea"
        jump pro3

    label lookaround:
        if la==False:
            user "Lets look around and search for clues"
            jump mini1
            label foundhiddenitem:
                user "Hey check this drawing out...."
                show brochar at right with moveinright
                bro "What do we do now?"
                $ la=True
                jump choice1

    label lookarounddone:
        show sischar at left with moveinleft
        sis "There's nothing more to be found"
        jump choice1

    label donothing:
        if nothingcount==0 and la==False:
            show sischar at left with moveinleft
            sis "Lets look around for a bit and check if we can find something"
            show brochar at right with moveinright
            bro "Good thinking... Spread out"
            $ nothingcount=1
        elif nothingcount==1 and la==False:
            show brochar at right with moveinright
            bro "Don't just stand and laze around all day. Lend us a hand..."
            $ nothingcount=2
        elif la==True:
            show sischar at left with moveinleft
            sis "There must be something we can do with the clue..."
            $ nothingcount=2
        jump choice1
'''