label L3:
    play music "main-menu-music.mp3"
    #The Right to Survival gave the power of healing and nourishment
    if L3complete==True:
        jump completedD
    else: 
        pass
    scene bg_dev with fade
    show devchar with moveinright
    dev "This part is to show the game can be Extended as much as required"
    dev "Thus being a demo level, the present is awarded to the user, please proceed..."

    $ L3complete = True
    $ c = c+1
    jump pro3