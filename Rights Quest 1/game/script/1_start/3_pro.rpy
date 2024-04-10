########################################################################################################
default completed=False
default L1complete=False
default L2complete=False
default L3complete=False
default c=0

label pro3:

    scene black with dissolve
    show screen gameUI

    show brochar at right with moveinright
    bro "Very well, we shall victoriously be back, Santa!"

    show sischar at left with moveinleft
    sis "We won't let you down!"

    return




















#######################################################################################################################################
'''
    #hide all
    scene ruin3pillars
    "As the children stand next to the 3 pillars, the ground shakes and there appears 3 magical beast"

    show owl with moveinleft
    owl "Welcome young ones"
    show bear at left with moveinleft    
    bear "We shall be your guide to the jewels"
    show unicorn at right with moveinright
    unicorn "After collecting all the jewels you may go to the temple to get your wish"

    hide owl
    hide bear
    hide unicorn
    with dissolve
    show bro at right with moveinright
    bro "Shall we undertake the trials?"
    show sis at left with moveinleft
    sis "Can we? Can we please?"

    #hide all
    scene black with dissolve
    label menu2:
        menu:
            "Lets do this!!":
                pass
            "No, lets go back home...":
                bro "We've come this far, lets push on a bit more?"
                jump menu2

    scene ruin3pillars with dissolve

    show owl with moveinleft
    owl "I hold the jewel of Knowledge"

    show bear at left with moveinleft
    bear "I protect the jewel of Protection"
    
    show unicorn at right with moveinright
    unicorn "I posses the jewel of Survival"

    label choice2:
        if c==3:
            $ completed = True
        if firsttime==False:
            show owl with moveinleft
            show bear at left with moveinleft
            show unicorn at right with moveinright
        menu:
            "{i}What would you like to do?{/i}"
            "Choose Bear - Knowledge":
                if bearcomplete == False:
                    $ firsttime = False
                    jump Bear
                elif bearcomplete == True:
                    bear "You have passed my trail children..."
                    jump choice2
            "Choose Owl - Protection":
                if owlcomplete == False:
                    $ firsttime = False
                    jump Owl
                elif owlcomplete == True:
                    owl "You posses the jewel of Knowledge already..."
                    jump choice2
            "Choose Unicorn - Survival":
                if unicorncomplete == False:
                    $ firsttime = False
                    jump Unicorn
                elif unicorncomplete == True:
                    unicorn "Go on, I acknowledge you children..."
                    jump choice2
            "Go to Temple" if completed == True:
                jump temple
'''