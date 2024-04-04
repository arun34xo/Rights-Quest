default la = False
default nothingcount = 0
label pro2:

    scene bg_forrest
    "As the merry band walks through the forest they come across a ruin"

    scene ruin3pillars

    show bro at right with moveinright
    bro "What do we do? We've reached the place the villagers were talking about..."

    label choice1:
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
        show bro at right with moveinright
        bro "That's a good idea"
        jump pro3

    label lookaround:
        if la==False:
            user "Lets look around and search for clues"
            jump mini1
            label foundhiddenitem:
                user "Hey check this drawing out...."
                show bro at right with moveinright
                bro "What do we do now?"
                $ la=True
                jump choice1

    label lookarounddone:
        show sis at left with moveinleft
        sis "There's nothing more to be found"
        jump choice1

    label donothing:
        if nothingcount==0 and la==False:
            show sis at left with moveinleft
            sis "Lets look around for a bit and check if we can find something"
            show bro at right with moveinright
            bro "Good thinking... Spread out"
            $ nothingcount=1
        elif nothingcount==1 and la==False:
            show bro at right with moveinright
            bro "Don't just stand and laze around all day. Lend us a hand..."
            $ nothingcount=2
        elif la==True:
            show sis at left with moveinleft
            sis "There must be something we can do with the clue..."
            $ nothingcount=2
        jump choice1
