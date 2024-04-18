#incomplete

label mini1:
    scene bg_forest
    # fill the game screen with objects
    $ InitGame("bg_forest", 1.0, (1500, 926), "figure")

    # show the game screen as a simple background
    $ GameAsBG()
    with dissolve

    user "Lets find a 'RED' object" #change red to red colour
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
        scene bg_forest with dissolve
        user "Hmm, it is unusual for a bag to be out here..."
        jump redbag
    else:
        "{i}Hint : Look on the right side by the trees{/i}"
        jump mini1