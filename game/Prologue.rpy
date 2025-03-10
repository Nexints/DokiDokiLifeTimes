
label prologue:
    stop music fadeout 0.5

    $ syncGlobalToAct()

    # MC in his bedroom.
    scene mcpov
    $ pause(0.01)
    scene black
    with dissolve_cg
    play music t2
    scene bg bedroom
    with dissolve_scene_half
    window show
    "Alarm" "BSST!!!!"
    mc "5 more minutes... Please."
    "Alarm" "BSST!!!!"
    mc "Fine... I'll wake up."
    "It's the first day of school, and I'm already dreading it."
    "Honestly, I would rather be playing games instead of going to school."
    "However, I should probably get to school though, otherwise my mom and Sayori will both have a word with me."

    # MC meeting Sayori.
    scene black
    with wipeleft
    scene bg residential_day
    with wipeleft
    $ s_name = "Sayori"
    s "Heeeeeeeyyy!!"
    "That girl over there is Sayori, my close childhood friend who I've known for many years."
    "Since we go to the same school, we both generally walk to school together."
    "Honestly, it's slightly tiring having to deal with Sayori all the time."
    "We're so close that people sometimes call us lovers, but it's not like that."
    "But hey, it's better than not having anyone to talk to."
    $ sref()
    $ mpt_af_mouth_auto = True
    $ af_enabled = True
    show sayori base afm happ om at f11
    s "Come on, let's get to school!~"
    show sayori cm at t11
    mc "Fine, but I just wanna play video games."
    mc "Besides, why do you hang around me so often?"
    show sayori om lup rup at hf11
    s "Because you're fun to be around!"
    show sayori cm ldown rdown at t11
    mc "Whatever you want. Let's just go to school."
    show sayori om ce at t11
    s "Sure! Ehe~"
    
    # MC talking about highschools with Sayori.
    scene black
    with wipeleft
    scene street
    with wipeleft
    "We make our way to our school."
    "The streets are filled with people commuting to work or just walking around."
    show sayori 1b zorder 2 at f11
    s "By the way,"
    s "Are you interested in any highschools?"
    show sayori at t11
    mc "As I have said already, I just wanna play video games. It's not that deep."
    show sayori 1h zorder 2 at h11
    s "You've gotta go to highschool!"
    s "I mean, it's our last year here..."
    show sayori at t11
    mc "That's true, but I'm just not interested."
    show sayori 2g zorder 2 at s11
    s "You promised though!"
    show sayori 2l zorder 2 at f11
    s "I want to go to the same highschool as you!"
    s "Besides, I genuinely care about you."
    show sayori at t11
    mc "Fine, I'll see what I can do. No promises though."
    show sayori 2r zorder 2 at hf11
    s "Yay!~"
    "Sayori's skipping along on the sidewalk, unable to contain her excitement."
    "She's a strange one, but I like her for that."
    "Otherwise, I wouldn't have stayed friends with her."

    # MC at school.
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene bg class_day
    with wipeleft
    play music t5
    play sound sfxBell
    "I'm finally here."
    "School is honestly such a drag."
    "If it wasn't for the insane amount of work they gave us, I would have been fine with it."
    "But I just want to go home and play games, especially when my first period is Math."
    $ w_name = "Teacher"
    show wallace 1bb at f11
    w "Hello, everyone."
    $ w_name = "Wallace"
    w "I'm Wallace, and I will be your teacher for the next year."
    w "I hope that we will have a great class together."
    show wallace 1ba at t11
    "That's your standard teacher introduction."
    "I'm honestly just going to tune out for the rest of class."
    show wallace at thide
    hide wallace
    "At least I know some friends here, so this class is a lot more bearable than I thought."
    "As class progresses, Sayori whispers into my ear."
    $ sref()
    show sayori base afm curi om at f11
    s "Psst..."
    s "Wanna get lunch later?"
    show sayori cm at t11
    mc "Sure."
    show sayori lsur om at f11
    s "Pleasee- Wait, you said yes?"
    show sayori cm at t11
    mc "I'll most likely be alone anyways, so why not."
    show sayori happy om at f11
    s "Yay!~"
    show sayori flustered lup rup cm at t21
    show wallace 1bj at f22
    w "Sayori and [player], be quiet."
    w "Students are actually trying to learn, and you are disrupting class."
    show wallace 1bp at t22
    $ sref()
    show sayori tap nerv om oe uniform afm at s21
    s "Alright..."
    show sayori cm at t21
    mc "Fine."
    show sayori at thide
    show wallace at thide
    hide wallace
    hide sayori
    "I typically don't go to lunch with Sayori, but this time I decided to go."
    "Sayori's always asking me to go, and I always end up going with her since I don't talk to anyone else."
    "Honestly though, I kind of enjoy hanging out with her. It's refreshing every once in a while."

    # Transition to lunch time with Sayori.
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene bg class_day
    with wipeleft
    play music t2
    play sound sfxBell
    "Bell" "RIING!"
    "It's finally lunchtime, and I had to sit through 3 other boring classes."
    "I'd rather not be here, but my parents wanted me to go to school."
    $ sref()
    show sayori base afm happy oe om at f11
    s "Come on, [player]! Let's go~"
    show sayori cm at t11
    mc "Sure, whatever. Where are we eating?"
    show sayori ce om at f11
    s "The rooftop!"
    show sayori cm at t11
    mc "Hold on, isn't the rooftop off limits?"
    $ sref()
    show sayori tap nerv om oe uniform afm at f11
    s "Ehe...~"
    $ sref()
    show sayori base afm happy oe mo at f11
    s "I got permission from the principal!"
    show sayori ce at f11
    s "Let's go~"
    show sayori at thide
    hide sayori
    mc "Wait, how did you-"
    mc "Alright, I guess."
    "I wonder how Sayori got permission on the first day of school."
    "Oh well, at least we can go to the rooftop."
    "I've been eyeing that spot ever since we came to school."

    # Lunch time with Sayori.
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene roof
    with wipeleft
    play music t8
    "I packed a lot of lunch today - almost too much."
    "My mom was insistent... She wanted me to cook and bring a lot on the first day."
    "\"You'll never know when you need it!\""
    "Honestly, I didn't want to bring a big lunch today."
    "But it might have been worth it."
    $ sref()
    show sayori base afm lsur lup rup oe om at hf11
    s "Woahh!"
    s "This looks sooo delicious!"
    show sayori ldown rdown sedu at f11
    s "Can I try?"
    show sayori cm at t11
    mc "No."
    show sayori pout om at f11
    s "Come on..."
    show sayori cm at t11
    mc "I'm kidding. Take some if you'd like."
    show sayori anno om at f11
    s "Stop teasing me!-"
    "Sayori takes a bite out of my lunch."
    show sayori lup rup lsur at hf11
    s "Uwaaaa-"
    show sayori ldown rdown at f11
    s "So delicious!"
    s "Did you cook this?"
    show sayori cm at t11
    mc "Yeah, I cooked it."
    mc "That's not important though."
    show sayori om happ at f11
    s "Thank you for the food~"
    show sayori nerv at f11
    s "I... might've forgotten to bring my lunch..."
    s "Ehe~"
    show sayori cm at t11
    mc "So that's why you wanted my lunch."
    mc "Don't forget your lunch next time. Please."
    show sayori om at f11
    s "Alright, alright. I get it~"
    show sayori cm at t11
    mc "Good."
    show sayori at thide
    hide sayori
    "She always does things like this."
    "Why she forgets things so often, I have no idea."
    "Pretty soon, she's going to forget when to wake up and go to school..."
    "But that won't happen, I'll make sure it doesn't."

    # Lunch time ending, transition back to classes.
    scene black
    with wipeleft
    scene roof
    with wipeleft
    play sound sfxBell
    "Bell" "RIING"
    "That signifies the end of lunch, and the start of another 4 periods of pain."
    $ sref()
    show sayori base afm happy oe cm at t11
    mc "We should head back now."
    show sayori om at f11
    s "Yeah~"
    s "Honestly, lunch flew by so fast... I wish we could talk more like this!"
    show sayori cm at t11
    mc "Yeah... ..."
    show sayori at thide
    hide sayori
    "Honestly, she's slightly annoying at times, but it's better than not talking to anyone."
    "We head back to the classroom, preparing ourselves for another world of hurt."

    # Classes
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene bg class_day
    with wipeleft
    play music t5
    play sound sfxBell
    "Classes are as boring as ever, and it's time to leave school."
    "Honestly, I'm just so tired from school that I just want to sleep."
    "But I'm suddenly jolted awake by a blue-eyed girl"
    $ sref()
    show sayori base afm anno om oe at f11
    s "[player]!"
    show sayori cm at t11
    mc "... Just let me sleep here..."
    show sayori base happy ce om at f11
    s "Come on, let's walk home together!"
    show sayori at thide
    hide sayori
    "To be honest, I don't really want to walk home with Sayori."
    "I'm slightly busy, as I have things to do outside of school."

    # Option menu - Do you want to walk home with Sayori, or ignore her?
    if story_mode == True:
        "But might as well go with Sayori this time."
        "She'll probably like it."
        call day1Walk
    else:
        menu:
            "Should I walk home with Sayori?"
            "You should":
                "Well, there's nothing bad that can come from walking with Sayori, I guess."
                call day1Walk from _call_day1Walk
            "You shouldn't":
                call day1NoWalk from _call_day1NoWalk
        return

label day1Walk:

    # Confirmation of walking with Sayori.
    $ route = 1
    mc "Alright, sure."
    $ sref()
    show sayori base afm laug oe om at hf11
    s "Let's go then! Ehe~"
    show sayori cm at t11
    mc "Fine, fine, just give me a second."
    if story_mode == False:
        $ console_history = []
        $ run_input(input="", output="+1 affection (Sayori)")
        $ pause(1)
        hide screen console_screen

    # The actual walk.
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene street
    with wipeleft
    play music t8
    "We walk together to our homes, admiring the roads and walking side-by-side."
    "Might as well, since we both live close to each other anyways."
    "I kind of wish she would stop clinging onto me though - as if I'm her only friend"
    $ sref()
    show sayori base afm lsur oe om at hf11
    s "Uwoaaa!"
    show sayori cm at t11
    mc "What is it?"
    show sayori om at f11
    s "There's so many people here!"
    show sayori cm at t11
    mc "Yeah, since everyone's leaving school."
    mc "I just wanted to play games and watch anime, to be honest."
    show sayori anno lup rup om at f11
    s "Come on!-"
    s "There's more to life than anime and video games though.."
    show sayori ldown rdown cm at t11
    mc "Like what?"
    show sayori happy om at f11
    s "Talking with friends, going to the park, there's so much to do!"
    show sayori cm at t11
    "Come to think of it, I haven't been to the park in a solid while."
    "I'll probably go there later though."
    mc "Like you're one to talk."
    mc "You're always clinging onto me, as if I'm your only friend."
    show sayori curi om at f11
    s "But we're childhood friends!"
    show sayori worr at f11
    s "I'm just worried about you."
    show sayori cm at t11
    mc "On the contrary, why haven't you tried playing games yet?"
    mc "I just enjoy playing games a lot, more than going out."
    show sayori at thide
    hide sayori
    "Sayori remains quiet for a bit, thinking about her response."
    "We walk a little bit more as she thinks of her answer."

    # Choice: Go out with Sayori, or don't?
    scene black
    with wipeleft
    scene street_sunset
    with wipeleft
    $ sref()
    show sayori base anno lup om at f11
    s "Becoming a NEET is not good for you!"
    s "Besides, it's more fun hanging around together!"
    show sayori worr at f11
    s "You haven't even gone outside in the past 3 months-"
    show sayori ldown cm at t11
    mc "Uhh..."
    mc "I swear I have though-"
    show sayori nerv om at f11
    s "We should go out together sometime!"
    show sayori cm at t11
    "Honestly, I don't really feel like going outside."
    "I honestly wanted to play video games and enjoy myself."
    if story_mode == True:
        "But, might as well anyway."
        call day1WalkCont
    else:
        menu:
            "Should I go out with Sayori?"
            "Yes":
                $ isekai_flag = True
                call day1WalkCont from _call_day1WalkCont
            "No":
                $ isekai_flag = False
                call day1WalkContTwo from _call_day1WalkContTwo
    return

label day1WalkCont:

    # Confirmation of going out with Sayori
    $ route = 2
    mc "Fine, but I don't see much of a reason to go out."
    if story_mode == False:
        $ console_history = []
        $ run_input(input="", output="+1 affection (Sayori)")
        $ pause(1)
        hide screen console_screen

    # Discussion with Sayori
    $ sref()
    show sayori happ om at f11
    s "Yess~"
    s "Meet me at the park next weekend!"
    show sayori cm at t11
    mc "Sure...?"
    "I have no idea why she's so ecstatic to meet with me..."
    "But if that's what makes her happy, I guess I'll meet with her."
    show sayori curi om at f11
    s "By the way, what are we doing tomorrow?"
    show sayori cm at t11
    mc "It's the second day of school."
    show sayori laug om at f11
    s "We'll be seeing each other more often then!"
    show sayori cm at t11
    mc "Well, yeah, because I'm forced to go to school instead of playing games."
    show sayori anno at t11
    mc "Due to a certain someone..."
    show sayori anno at hf11
    s "Meanie!"
    show sayori at thide
    hide sayori
    "We continue to banter like this, all the way back home."

    # Going home
    scene black
    with wipeleft
    scene intersection_sunset
    with wipeleft
    $ sref()
    show sayori base afm happ oe cm at t11
    mc "Welp, my house is on the right from here."
    mc "I'll see you tomorrow."
    show sayori happ om at f11
    s "See you [player]!"
    show sayori at thide
    hide sayori
    "I make my way home, as the sun sets in the background."
    if story_mode == True:
        $ console_history = []
        $ run_input(input="Story mode is enabled.", output="Skipping open-worlded parts.")
        $ pause(1)
        hide screen console_screen
        call day1WalkEnd
    $ actions = 3
    call day1WalkEnd from _call_day1WalkEnd
    return

label day1WalkContTwo:

    # Deny going out with Sayori.
    $ route = 3
    mc "No, I've been really busy lately."
    $ console_history = []
    $ run_input(input="", output="-1 affection (Sayori)")
    $ pause(1)
    hide screen console_screen

    # Discussion with Sayori about going outside.
    $ sref()
    show sayori dist om at f11
    s "Alright then..."
    show sayori worr om at f11
    s "I just wanted you to go outside though."
    show sayori cm at t11
    mc "As I've said, I'm really busy recently. I have my dailies in IdleCraft Simulator and the next episode of TerraAnime to watch."
    show sayori om at f11
    s "But I really care about you~"
    show sayori cm at t11
    mc "I'm sorry, but no is no."
    show sayori dist om at f11
    s "Aww..."
    show sayori nerv om at f11
    s "Maybe next time then~"
    show sayori nerv cm at t11
    mc "Maybe, if there even is one."
    "I feel bad rejecting Sayori like this, but I gotta do what I gotta do."
    "Besides, you only live once, right?"
    $ console_history = []
    $ run_input(input="print(disclaimerThree)", output="PS: dont follow the MC here lol") # Disclaimer 3
    $ pause(0.25)
    hide screen console_screen
    show sayori at thide
    hide sayori
    "We continue discussing about random topics all the way home, but Sayori seems less cheerful than before."
    "Maybe I should check up on Sayori later."

    # Going home
    scene black
    with wipeleft
    scene intersection_sunset
    with wipeleft
    $ sref()
    show sayori base afm dist oe om at t11
    mc "Welp, my house is on the right from here."
    mc "I'll see you tomorrow."
    show sayori om at f11
    s "See you, [player]."
    show sayori at thide
    hide sayori
    "I make my way home, as the sun sets in the background."
    $ actions = 3
    call day1WalkEnd from _call_day1WalkEnd
    return

label day1NoWalk:

    # Deny the walk with Sayori.
    $ route = 4
    "I'm going to deny the walk with Sayori this time."
    "I need to finish my dailies quickly."
    mc "I'm slightly busy, so I can't walk with you today."
    $ sref()
    show sayori base dist om at f11
    s "Alright..."
    show sayori at thide
    hide sayori
    $ console_history = []
    $ run_input(input="", output="-1 affection (Sayori)")
    $ pause(1)
    hide screen console_screen

    # Open World starting point
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene street
    with wipeleft
    play music t8
    "I end up leaving school on my own, while Sayori goes home herself."
    "I feel bad for Sayori, but she seemed to understand that I wanted to be by myself today."
    "Maybe I'll hang out with her later on."
    "Honestly, there's a lot I want to do at home, but there's also a lot of things to do outside."
    $ actions = 5
    call day1ResetScene from _call_day1ResetScene
    return

label day1ResetScene:

    # Resets the scene for the open world aspect
    scene black
    with wipeleft
    stop music fadeout 0.5
    if actions < 4:
        scene street_sunset
        with wipeleft
    else:
        scene street
        with wipeleft
    play music t4 # Placeholder for actual music.
    call day1WhatToDo from _call_day1WhatToDo
    return

label day1WhatToDo:

    # Open World Option menu - What to do?
    menu:
        "What should I do? ([actions] actions left.)"
        "Go back home":
            call day1WalkEnd from _call_day1WalkEnd_1
        "Work out (Jog)" if actions > 3:
            call day1WorkOut from _call_day1WorkOut
        "Read at the Library (Locked)" if actions > 3:
            "This option is currently locked today."
            call day1WhatToDo from _call_day1WhatToDo_1
    return

label day1WorkOut:
    "I ended up working out by going for a light jog."
    $ strength = (0 if strength is None else strength) + 1
    $ actions -= 1
    $ console_history = []
    $ run_input(input="", output="+1 Strength (Total: [strength])")
    $ pause(1)
    hide screen console_screen
    "As I jogged around, I saw plenty of people and animals roaming the streets."
    "Not that it matters anyway."
    "I can feel myself getting stronger by the second."
    # Resets the scene without the music stopping
    scene black
    with wipeleft
    if actions < 4:
        scene street_sunset
        with wipeleft
    else:
        scene street
        with wipeleft
    call day1WhatToDo from _call_day1WhatToDo_2
    return


label day1WalkEnd:
    # End the walk with Sayori.
    "I end up going home to play games, watch anime and do homework."
    "Honestly, there's nothing better here than playing games late at night."
    "I still have some of my dailies to go through, as I didn't have enough time this morning."
    $ homework = 0;
    call day1gaming from _call_day1gaming
    return

label day1gaming:
    # Home session for the night of day 1. This piece of code is reused and slightly modified over the days.
    # This is a merge point of 3 routes.
    # Route 2 - Walk and go out
    # Route 3 - Walk and no going out
    # Route 4 - No walk
    scene black
    with wipeleft
    if actions < 2:
        scene bedroom_night
        with wipeleft
    else:
        scene bg bedroom
        with wipeleft

    # Open World Option menu - What to do?
    if story_mode == True: # Skip options if story mode is enabled.
        call day1StoryMode
    else: # Don't skip options.
        if actions > 0:
            menu:
                "What should I do at home? ([actions] actions left.)"
                "Read a book":
                    call day1Read from _call_day1Read
                "Do my homework" if homework == 0:
                    call day1Homework from _call_day1Homework
                "Play IdleCraft Simulator":
                    call day1IdleCraft from _call_day1IdleCraft
                "Watch TerraAnime":
                    call day1TerraAnime from _call_day1TerraAnime
                "Sleep":
                    call day1Sleep from _call_day1Sleep
        else:
            call day1Sleep from _call_day1Sleep_1
    return

label day1Read:
    "I ended up reading a book alone."
    "This book's title is very interesting."
    $ intel = (0 if intel is None else intel) + 1
    $ actions -= 1
    $ console_history = []
    $ run_input(input="", output="+1 Intelligence (Total: [intel])")
    $ pause(1)
    hide screen console_screen
    "This book was quite entertaining to read!"
    "I should read another book from my bookshelf sometime."
    "I can feel myself getting smarter by the second."
    call day1gaming from _call_day1gaming_1
    return

label day1Homework:
    "I ended up doing my homework"
    "I'd rather not do my homework, but I have to do it to keep my grades high."
    $ intel = (0 if intel is None else intel) + 1
    $ homework = 1
    $ actions -= 1
    $ console_history = []
    $ run_input(input="", output="+1 Intelligence (Total: [intel])")
    $ pause(1)
    hide screen console_screen
    "My homework wasn't very interesting to be honest."
    "At least it's over with."
    call day1gaming from _call_day1gaming_2
    return

label day1IdleCraft:
    "I ended up playing IdleCraft with a couple of my gaming buddies."
    $ gameSkill = (0 if gameSkill is None else gameSkill) + 1
    $ actions -= 1
    $ console_history = []
    $ run_input(input="", output="+1 Gaming Skill (Total: [gameSkill])")
    $ pause(1)
    hide screen console_screen
    "I'm not that great right now at gaming."
    "I can feel myself getting better though..."
    call day1gaming from _call_day1gaming_3
    return

label day1TerraAnime:
    "I ended up watching TerraAnime alone."
    $ isekai_flag = True
    $ actions -= 1
    $ console_history = []
    $ run_input(input="", output="Nothing changed.")
    $ pause(1)
    hide screen console_screen
    "I feel absolutely nothing different about me."
    "Honestly, I'm not sure what I'm doing with my life."
    call day1gaming from _call_day1gaming_4
    return

label day1StoryMode:
    "I first decided to do my homework."
    "Homework was exhausting to do, but I did it anyway."
    "I still can't wrap my head around several questions, so I'll probably ask the teacher tomorrow."
    "I'm now bored, so I'll probably play some games and check up on my dailies and head to bed soon."
    scene black
    with wipeleft
    scene bedroom_night
    with wipeleft
    "Phew!"
    "That was a nice round of gaming."
    "I managed to log into IdleCraft and collect some dailies."
    "I'll quickly head to sleep now, as I'm tired."
    call day2Intro
    return

label day1Sleep:

    # Sleeping dialogue
    scene black
    with wipeleft
    if actions < 2:
        scene bedroom_night
        with wipeleft
        "I'll quickly head to sleep now, before it gets too late."
    else:
        scene bg bedroom
        with wipeleft
        "I'll sleep, since it's late and I'm going to be late for school tomorrow."
    $ console_history = []
    $ run_input(input="print(stats)", output="Strength: [strength], Intelligence: [intel], ") # Stats printed
    $ run_input(input="print(stats2)", output="Game Skill: [gameSkill], Tardiness: [tardy]")
    $ run_input(input="print(stats3)", output="(Debug) Route: [route]")
    $ pause(0.25)
    "Continue by clicking anywhere."
    hide screen console_screen
    call day2Intro
    return
    