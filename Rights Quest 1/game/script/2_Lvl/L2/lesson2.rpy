label discrimination:
    if L2complete==False:
        scene black with fade
        stop music
        play music "Game Over.ogg"
        $ renpy.pause(3, hard=True)
        scene bg_gameover with fade
        $ renpy.pause(3, hard=True)
        "That did not end well, the food doesn't taste great after what happened."
        scene black with fade
    play music "Lesson.mp3"
    scene bg_living with dissolve
    show granny at right with moveinright
    play sound "audio/voice/lesson_2/lesson_2_line1.ogg"
    Granny "That's not really the right thing to do, Whats important is that one must stand against discrimination, be it you who is the target or another person."
    play sound "audio/voice/lesson_2/lesson_2_line2.ogg"
    Granny "No one deserves to suffer just because they are a bit different from others"
    play sound "audio/voice/lesson_2/lesson_2_line3.ogg"
    Granny "Especially if it is something they can not control"
    stop sound
    hide granny with dissolve
    play music "main-menu-music.mp3"
    if L2complete:
        jump d9
    else:
        jump d3