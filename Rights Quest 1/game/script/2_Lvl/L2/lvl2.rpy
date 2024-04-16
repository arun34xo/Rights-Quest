label L2:
    #The Right against discrimination.
    scene town_bg with fade
    "The kids approach the town and find their way to a complex of restaurants."

    show brochar at left with moveinleft
    bro "Sighhh… I’m starving."

    show sischar at right with moveinright
    sis "Me too! Let’s get something to eat!"

    show brochar at left 
    bro "Look! I see a restaurant! Let’s get ourselves a bowl of noodles!"

    hide brochar
    hide sischar

    scene restaurant_bg with fade

    "The kids approach the restaurant."

    show ownerchar at left 
    storeowner "Hello there, how can I help you kids?"

    show sischar at right with moveinright
    sis "Hi Mister! We’d like a bowl of noodles each!"

    show ownerchar at left
    storeowner "Alright! What kind of noodles would you kids like?"

    hide ownerchar

    show sischar at right with moveinright
    sis "I’d like a bowl of chicken noodles!"

    show brochar at left with moveinleft
    bro "I'd like a bowl of egg noodles."

    menu:
        "Ramen noodles":
            user "I’d like a bowl of Ramen noodles!"
            hide brochar
            hide sischar
            show ownerchar at left with moveinleft
            storeowner "That's a fine choice you've chosen, child!"
            pass
        "Egg noodles":
            user "I'd like a bowl of egg noodles!"
            hide brochar
            hide sischar
            show ownerchar at left with moveinleft
            storeowner "That's a fine choice you've chosen, child!"
            pass
        "Egg noodles":
            user "I'd like a bowl of Chow mein noodles"
            hide brochar
            hide sischar
            show ownerchar at left with moveinleft
            storeowner "That's a fine choice you've chosen, child!"
            pass

    hide ownerchar

    show sischar at right with moveinleft
    sis "That will be all, Mister!"

    show brochar at left with moveinleft
    bro "We will be waiting, Mister!"

    hide brochar
    hide sischar

    show ownerchar at left with moveinleft
    storeowner "Delightful! I’ll get your food ready in jiffy!"

    hide ownerchar

    show mrsgraychar at right with moveinright
    mrsgray "Hello there, I’d like to get a bowl of noodles?"

    show ownerchar at left with moveinleft
    storeowner "I shall not serve you. We don’t serve your kind of people."   

    hide ownerchar

    show brochar at left with moveinleft
    bro "Excuse me? What do you mean by "your kind of people"?"

    show mrsgraychar at right
    mrsgray "I believe he's referring to my color. It seems he's discriminating against me because of it."

    menu:
        "Stay Silent":
            hide brochar
            hide mrsgraychar
            show sischar at left with moveinleft
            sis "We can't let this go!"
        "Speak up against discrimination":
            hide brochar
            hide mrsgraychar
            user "That's not fair! Everyone deserves to be treated equally!"

    hide mrsgraychar

    show brochar at left with moveinleft
    bro "Yeah, you can't just refuse to serve someone because of who they are or what they have."

    show ownerchar at right with moveinright
    storeowner "I have the right to refuse service to anyone I want!"

    show brochar at left
    bro "Actually, you don't. Discrimination based on color is against the law"

    hide brochar

    show sischar at left with moveinleft
    sis "That's right! We have the right against discrimination!"

    show ownerchar at right with moveinright
    storeowner "Fine! I'll serve her this time, but I don't have to like it."

    hide sischar
    hide ownerchar
    
    "The store owner reluctantly serves Mrs.Gray her noodles"
    
    show mrsgraychar at right with moveinright
    mrsgray "Thank you for standing up for me, kids. It's important to fight against discrimination whenever we encounter it."

    show brochar at left with moveinleft
    bro "No problem, Mrs. Gray. We believe everyone deserves to be treated withrespect and fairness."

    menu:
        "Glad we could help, Ma'am!":
            hide mrsgraychar
            show sischar at right with moveinright
            sis "Let's eat our noodles together and continue our quest!"

        "Speak up against discrimination":
            hide mrsgraychar
            show sischar at right with moveinright
            sis "Let's eat our noodles together and continue our quest!"

    hide brochar
    hide sischar

    "The kids and Mrs. Gray enjoy their noodles together before setting of on their next adventure"

    #scene somewhere with fade
    #"trial"
    $ L2complete = True
    $ c = c+1
    #jump pro3