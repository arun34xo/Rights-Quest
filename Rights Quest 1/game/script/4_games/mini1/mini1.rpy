#incomplete

label mini1:
    scene bg room
    # fill the game screen with objects
    $ InitGame("bg forest", 1.0, (902, 595), "figure")

    # show the game screen as a simple background
    $ GameAsBG()
    with dissolve

    user "Lets find a 'RED' object"

    # launch the game and play
    $ res = StartGame()

    # show as background again
    # (but without items found during the game)
    $ GameAsBG()

    # check the game results and play them in the scenario    
    if oRes:
        scene black with dissolve:
            pause(1.0)
        scene close with dissolve
        user "Hmm, it is unusual for a bag to be out here..."
        scene blank
        jump redbag
    else:
        "{i}Hint : Look by the trees{/i}"
        jump mini1