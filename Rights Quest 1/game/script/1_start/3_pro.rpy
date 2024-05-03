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
        bro "Pretty sure we found the Present from that area, right?"
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
        show snow1
        show snow2  
        show brochar at right with moveinright
        bro "What's the next plan of action"
        label d4:
            pass
        menu:
            "Let's go ..."
            "Find the 1st present":
                if L1complete == True:
                    show sischar at left with moveinleft
                    sis "We found that present, let's search else where"
                    jump d4
                else:
                    show sischar at left with moveinleft
                    sis "Very well, let's be on our way then!!"
                    jump L1
            "Find the 2nd present":
                if L2complete == True:
                    show sischar at left with moveinleft
                    sis "We found that present, let's search else where"
                    jump d4
                else:
                    show sischar at left with moveinleft
                    sis "Onwards we go!!"
                    jump L2
            "Find the 3rd present":
                if L3complete == True:
                    show sischar at left with moveinleft
                    sis "We found that present, let's search else where"
                    jump d4
                else:
                    show sischar at left with moveinleft
                    sis "Let's go, it's freezing out here!!"
                    jump L3
            "To Mr. Santa's home":
                jump end
    else:
        scene black with dissolve
        show snow1
        show snow2
        show screen gameUI
        if firsttime==False:
            scene black with dissolve #forest2
            show sischar at left with moveinleft
            sis "Let's get this over with and go warm ourselves... I'm freezing out here"
            $ renpy.pause(100, hard=True)
        else:
            scene black with dissolve #helps user be familiar with the map
            show brochar at right with moveinright
            bro "Pressing the Map Button accesses the Map, Convinent right!!"
            $ renpy.pause(100, hard=True)
