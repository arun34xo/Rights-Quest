label find1:
    scene inside_locker
    # fill the game screen with objects
    $ InitGame("inside_locker", 1.0, (935, 490), "present2")

    # show the game screen as a simple background
    $ GameAsBG()
    with dissolve

    user "Let's find the missing present!"
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
        user "We found it!"
        jump foundhiddenitem3
    else:
        "{i}Hint : Check on one of the racks.{/i}"
        jump find1