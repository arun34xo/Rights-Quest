label hidden4:
    scene inside_shed
    # fill the game screen with objects
    $ InitGame("safe_room", 1.0, (825, 720), "present1")

    # show the game screen as a simple background
    $ GameAsBG()
    with dissolve

    user "Let's find the key!"
    window hide
    # launch the game and play
    $ res = StartGame()

    # show as background again
    # (but without items found during the game)
    $ GameAsBG()

    # check the game results and play them in the scenario    
    if oRes:
        scene black with dissolve:
            pause(1.0)
        scene safe_room with dissolve
        user "Look at that! We found Santa's first missing present!"
        jump foundhiddenitem2
    else:
        "{i}Hint : On of the shelves below the lantern.{/i}"
        jump hidden4