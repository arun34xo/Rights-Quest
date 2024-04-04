

label mini1:
    scene bg room
    # fill the game screen with objects
    $ InitGame("bg ruin", 1.0, (902, 595), "figure1")

    # show the game screen as a simple background
    $ GameAsBG()
    with dissolve

    user "Lets find a clue"

    # launch the game and play
    $ res = StartGame()

    # show as background again
    # (but without items found during the game)
    $ GameAsBG()

    # check the game results and play them in the scenario    
    if oRes:
        scene black with dissolve:
            pause(1.0)
        scene HintOg with dissolve
        user "Such a peculiar drawing"
        scene blank
        jump foundhiddenitem
    else:
        "{i}Hint : Search on the Walls of the ruins{/i}"
        jump mini1