#incomplete

label hidden1:
    play music "Game.mp3"
    scene bg_forest
    show snow1
    show snow2
    # fill the game screen with objects
    $ InitGame("bg_forest", 1.0, (1500, 926), "figure")

    # show the game screen as a simple background
    $ GameAsBG()
    with dissolve

    user "Lets find a {color=#FF0000}'Red'{/color} object"
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
        show snow1
        show snow2
        user "Hmm, it is unusual for a bag to be out here..."
        play music "main-menu-music.mp3"
        jump redbag
    else:
        "{i}Hint : Look on the right side by the trees{/i}"
        jump hidden1