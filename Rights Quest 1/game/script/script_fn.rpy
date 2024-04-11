#blinking transition
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
#auto-blurring
define sprite_focus = {}
default speaking_char = None

transform sprite_highlight(sprite_name):
    function SpriteFocus(sprite_name)

init -10 python:
    import math

    def name_callback(event, interact=True, name=None, **kwargs):
        global speaking_char
        if event == "begin":
            speaking_char = name

    class SpriteFocus(object):
        def __init__(self, char_name):
            self.char_name = char_name

        def __call__(self, trans, start_time, anim_time):
            def get_ease(t):
                return .5 - math.cos(math.pi * t) / 2.0

            global sprite_focus, speaking_char
            char_name = self.char_name

            if char_name not in sprite_focus:
                sprite_focus[char_name] = False
            anim_length = 0.2       # How long (in seconds) the animation will last
            bright_change = 0.5   # How much the brightness changes
            sat_change = 0.2        # How much the saturation changes
            zoom_change = 0.0025    # How much the zoom changes
           
            y_change = 1

            is_talking = speaking_char == char_name

            if isinstance(sprite_focus[char_name], (int, float)) and anim_time < sprite_focus[char_name]:
                sprite_focus[char_name] = is_talking
            if sprite_focus[char_name] != is_talking and isinstance(sprite_focus[char_name], bool):
                sprite_focus[char_name] = anim_time
                if renpy.is_skipping() or renpy.in_rollback():
                    sprite_focus[char_name] = is_talking

            curr_time = max(anim_time - sprite_focus[char_name],0) 
            curr_ease = 1.0
            if curr_time < anim_length and not isinstance(sprite_focus[char_name], bool):
                curr_ease = get_ease(curr_time/anim_length)
            else:
                sprite_focus[char_name] = is_talking
            if is_talking:
                trans.matrixcolor = SaturationMatrix((1.0-sat_change) + curr_ease * sat_change) * BrightnessMatrix(-bright_change + curr_ease * bright_change)
                trans.zoom = min(curr_ease * zoom_change + (1.0-zoom_change), 1.0)
                trans.yoffset = y_change - curr_ease * y_change 
            else:           
                trans.matrixcolor = SaturationMatrix(1.0 - curr_ease * sat_change) * BrightnessMatrix(curr_ease * -bright_change)
                trans.zoom = max(1.0 - curr_ease * zoom_change, (1.0-zoom_change))
                trans.yoffset = y_change * curr_ease            
            return 0

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

label call_mapUI:
    call screen MapUI

screen MapUI:
    add "map/bg_map.png"

    imagebutton:
        xpos 671
        ypos 316
        idle "map/santa_idle.png"
        hover "map/santa_hover.png"
        action Jump("end")

    imagebutton:
        xpos 1448
        ypos 746
        if L1complete==False:
            idle "map/L1_idle.png"
            hover "map/L1_hover.png"
        else:
            idle "map/L1_idle.png"
            hover "map/L1_hover.png"
        action Jump("L1")
        
    imagebutton:
        xpos 1475
        ypos 232
        if L2complete==False:
            idle "map/L2_idle.png"
            hover "map/L2_hover.png"
        else:
            idle "map/L2_idle.png"
            hover "map/L2_hover.png"
        action Jump("L2")

    imagebutton:
        xpos 415
        ypos 754
        if L3complete==False:
            idle "map/L3_idle.png"
            hover "map/L3_hover.png"
        else:
            idle "map/L3_idle.png"
            hover "map/L3_hover.png"
        action Jump("L3")

#######################################################################################################################################
#
