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
            user "Let's ...."
    else:
        show screen gameUI
        if firsttime==False:
            scene black with dissolve #forrest2
            show sischar at left with moveinleft
            sis "Let's get this over with and go warm ourselves... I'm freezing out here"
            Pause(1000)
        else:
            scene black with dissolve #helps user be familiar with the map
            show brochar at right with moveinright
            bro "Pressing the Map Button accesses the Map, Convinent right!!"
            Pause(1000)
