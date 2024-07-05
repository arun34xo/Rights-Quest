label hidden4:
    play music "Game.mp3"
    scene inside_shed
    # fill the game screen with objects
    $ InitGame("safe_room", 1.0, (230, 770), "key1")

    # show the game screen as a simple background
    $ GameAsBG()
    with advtrans5

    user "Let's find the key!"
    window hide
    # launch the game and play
    $ res = StartGame()

    # show as background again
    # (but without items found during the game)
    $ GameAsBG()

    # check the game results and play them in the scenario    
    if oRes:
        scene black with advtrans5:
            pause(1.0)
        scene safe_room with dissolve
        user "We found the key!"
        play music "main-menu-music.mp3"
        jump foundhiddenitem2
    else:
        "{i}Hint : On the stool next to the desk.{/i}"
        jump hidden4