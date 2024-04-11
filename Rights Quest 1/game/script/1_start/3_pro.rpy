########################################################################################################
default completed=False
default L1complete=False
default L2complete=False
default L3complete=False
default recentcomplete=False
default firsttime=True
default c=0

label completedD:
    if c<3:
        show brochar at right with moveinright
        bro "Pretty sure we found the Present from that region, right?"
        show sischar at left with moveinleft
        sis "Yes, I believe that we have searched that area. Let's look else where."
    else:
        show brochar at right with moveinright
        bro "Pretty sure we found all the presents that were lost, right?"
        show sischar at left with moveinleft
        sis "Yes, I believe that we have found all 3 of the missing present. Let's go meet Santa Clause."
    jump pro3


label pro3:
    if child==True:
        scene black with dissolve
        show brochar at right with moveinright
        bro "What's the next plan of action"
        menu:
            "Use map to find next present":
                jump call_mapUI
            "Go to Mr. Santa's home":
                jump end
            "------------------"
    else:
        show screen gameUI
        if firsttime==False
            scene black with dissolve
            show sischar at left with moveinleft
            sis "Let's get this over with and go warm ourselves... I'm freezing out here"
        else
            scene black with dissolve #helps user be familiar with the map
            show brochar at right with moveinright
            bro "Pressing the Map Button helps access the Map, Convinent right!!"
        




















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