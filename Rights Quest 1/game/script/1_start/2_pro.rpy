default shouted = False
default knocked = False
default AskedForReward = False

label pro2:

    scene bg_santa_field with fade
    show snow1
    show snow2
    "As they go to the address on the tag, they reach a field filled with Reindeers and in the middle, a house with smoke coming out of the chimney is spotted"

    show brochar at right with moveinright
    bro "Is this the right location?"

    show sischar at left with moveinleft
    sis "It must be, it's magical."

    scene bg_santahouse with fade
    show snow1
    show snow2
    show brochar at right with moveinright
    bro "Shall we knock?"

    menu:
        user "hmm...."
        "Knock at the door":
            hide brochar
            hide sischar
            with dissolve
            show santachar_shadow at right with moveinright
            santa "Who is it at this time of the day?"
            $ knocked = True
            pass
        "Scream":
            user "IS ANYONE IN THERE??"
            show sischar at left with moveinleft
            sis "Nooo... Why are you shouting?"
            hide brochar
            hide sischar
            with dissolve
            show santachar_shadow at right with moveinright
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
            show santachar_shadow at right with moveinright
            santa "Who is it at this time of the day?"
            pass        

    show brochar at left with moveinleft
    bro "We found your bag lying around in the forest, Mister."

    hide brochar with dissolve
    show sischar at left with moveinleft
    sis "We thought we might as well as return it to the owner."

    "As the door opens, a large figure steps out with a pleasant smile"

    hide santachar_shadow with dissolve
    show santachar at right with dissolve
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

    menu:
        "What would you like to do?"
        "Accept the request":
            user "Of course, we don't mind helping at all"
            santa "Such a kind child, Very well!"
            pass

        "Ask for the reward" if AskedForReward==False:
            user "Do we get a reward?"
            santa "Such an eager child. Yes, I've prepared a series of challenges for you to overcome. The reward shall remain a surprise."
            $AskedForReward=True
            jump d2
        
        "{s}Ask for the reward{/s}" if AskedForReward==True:
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
    jump hidden2

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

    jump pro3
