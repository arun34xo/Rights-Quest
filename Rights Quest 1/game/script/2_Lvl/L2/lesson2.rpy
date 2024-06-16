label discrimination:
    if L2complete:
        #game over
        scene black with fade
    scene bg_living with dissolve
    show grannychar at right with moveinright
    gran "That's not really the right thing to do, Whats important is that one must stand against discrimination, be it you who is the target or another person."
    gran "No one deserves to suffer just because they are a bit different from others"
    gran "Especially if it is something they can not control"
    hide grannychar with dissolve
    if L2complete:
        jump d9
    else:
        jump d3