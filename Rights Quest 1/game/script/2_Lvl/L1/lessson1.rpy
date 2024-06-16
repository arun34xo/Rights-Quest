label protection:
    if L1complete:
        #game over
        scene black with fade
    scene bg_living with dissolve
    show grannychar at right with moveinright
    gran "Remeber, you children have the Right to Protection. Which means that adults or anyone capable must help you in cases where you are in trouble"
    gran "Adults will only know how to help you when they know you need help"
    gran "Thus, in order to protect ones-self they must also learn to ask for help when required." 
    hide grannychar with dissolve
    if L1complete:
        jump d8
    else:
        jump d7