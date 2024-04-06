transform blink:
    "eye_half.png"
    .1
    "eye_close.png" 
    .1
    "eye_open.png"
    .2
    "eye_half.png"
    .1
    "eye_close.png"
    .1
    "eye_open.png"
    .2
    "eye_half.png"
    .1
    "eye_close.png"
    .1
    "eye_open.png"
    alpha 0.0

#######################################################################################################################################

image granny_blurred = im.Blur("granny.png", 5)

#######################################################################################################################################
#interactable map

screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump ("call_mapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")
        # This was the same code used in the vlog.

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.

label call_mapUI:
    call screen MapUI

screen MapUI:
    add "map/bg_mapOG.jpg"

    imagebutton:
        xpos 794
        ypos 353
        idle "map/santa_idle.png"
        hover "map/santa_hover.png"
        action Jump("Santa_home")

    imagebutton:
        xpos 1448
        ypos 746
        idle "map/present1_idle.png"
        hover "map/present1_hover.png"
        action Jump("L1")
        
    imagebutton:
        xpos 1475
        ypos 232
        idle "map/present2_idle.png"
        hover "map/present2_hover.png"
        action Jump("L2")

    imagebutton:
        xpos 415
        ypos 754
        idle "map/present3_idle.png"
        hover "map/present3_idle hover.png"
        action Jump("L3")

#######################################################################################################################################