label protection:
    if L1complete==False:
        scene black with fade
        stop music
        play sound "Game Over.ogg"
        $ renpy.pause(3, hard=True)
        scene bg_gameover with fade
        $ renpy.pause(3, hard=True)
        "That did not end well, people have boo boos now"
        scene black with fade
    play music "Lesson.mp3"
    scene bg_living with dissolve
    show granny at right with moveinright
    play sound "audio/voice/lesson_1/lesson_1_line1.ogg"
    Granny "Remeber, you children have the Right to Protection. Which means that adults or anyone capable must help you in cases where you are in trouble"
    play sound "audio/voice/lesson_1/lesson_1_line2.ogg"
    Granny "Adults will only know how to help you when they know you need help"
    play sound "audio/voice/lesson_1/lesson_1_line3.ogg"
    Granny "Thus, in order to protect ones-self they must also learn to ask for help when required."
    stop sound
    hide granny with dissolve
    play music "main-menu-music.mp3"
    if L1complete:
        jump d8
    else:
        jump d7