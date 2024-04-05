

label mini1:
    scene bg room
    # fill the game screen with objects
    $ InitGame("bg ruin", 1.0, (902, 595), "figure1")

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
        scene HintOg with dissolve
        user "Hmm, this is unusual"
        scene blank
        jump redbag
    else:
        "{i}Hint : Search behind the trees{/i}"
        jump mini1