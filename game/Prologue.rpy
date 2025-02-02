
label prologue:
    stop music fadeout 0.5

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
    "That girl over there is Sayori, my close childhood friend from years in the past."
    "We're close friends, and since we go to the same school, we both walk to school with each other."
    "Honestly, it's slightly tiring having to deal with Sayori all the time."
    "We're so close that people sometimes call us lovers, but it's not like that."
    "But hey, it's better than not having anyone to talk to."
    s "Come on, let's get to school!~"
    mc "Fine, but I just wanna play video games."
    mc "Besides, why do you hang around me so often?"
    s "Because you're fun to be around!"
    mc "Whatever you want. Let's just go to school."
    s "Sure! Ehe~"
    
    # MC talking about highschools with Sayori.
    scene black
    with wipeleft
    scene street
    with wipeleft
    "We make our way to our school."
    "The streets are filled with people."
    s "By the way,"
    s "Are you interested in any highschools?"
    mc "As I have said already, I just wanna play video games. It's not that deep."
    s "You've gotta go to highschool!"
    s "I mean, it's our last year here..."
    mc "That's true, but I'm just not interested."
    s "You promised though!"
    s "I want to go to the same highschool as you!"
    s "Besides, I genuinely care about you."
    mc "Fine, I'll see what I can do. No promises though."
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
    "I'm finally here."
    "School is honestly such a drag."
    "If it wasn't for the insane amount of work they gave us, I would have been fine with it."
    "But I just want to go home and play games. Especially when my first period is Math."
    $ w_name = "Teacher"
    w "Hello."
    $ w_name = "Wallace"
    w "I'm Wallace, and I will be your teacher for the next year."
    w "I hope that we will have a great class together."
    "That's your standard teacher introduction."
    "I'm already uninterested in this class, and the teacher had to make it worse."
    "At least I'm seated next to Sayori, so the class is a lot more bearable than I thought."
    "As class progresses, Sayori whispers into my ear."
    s "Psst..."
    s "Wanna get lunch later?"
    mc "Sure."
    s "Pleasee- Wait, you said yes?"
    mc "Yeah, I have nothing to do in school anyways."
    s "Yay!~"
    w "Sayori and [player], be quiet."
    w "Students are actually trying to learn, and you are disrupting class."
    s "Alright..."
    mc "Fine."
    "I typically don't go to lunch with Sayori, but this time I decided to go."
    "Sayori's always asking me to go, and I always end up going with her since I don't talk to anyone else."
    "Honestly though, I kind of wish she didn't ask me so often."

    # Transition to lunch time with Sayori.
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene bg class_day
    with wipeleft
    play music t2
    "Bell" "RIING!"
    "It's finally lunchtime, and I had to sit through 3 other boring classes."
    "School is honestly such a drag."
    s "Come on, [player]! Let's go~"
    mc "Sure, whatever. Where are we eating?"
    s "The rooftop!"
    mc "Hold on, isn't the rooftop off limits?"
    s "I got permission from the principal! Let's go~"
    mc "Wait, how did you-"
    mc "Alright, I guess."
    "Well, I don't really have a choice."
    "Once she's set on something, it's really hard to convince her."

    # Lunch time with Sayori.
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene roof
    with wipeleft
    play music t8
    "I packed a lot of lunch today - almost too much."
    "My mom was insistent... She wanteed me to cook and bring a lot on the first day."
    "\"You'll never know when you need it!\""
    "Honestly, I didn't want to bring a big lunch today."
    "But it might have been worth it."
    s "Woahh!"
    s "This looks sooo delicious!"
    s "Can I try?"
    mc "No."
    s "Come on!"
    mc "I'm kidding. Take some if you'd like."
    s "Stop teasing me!-"
    "Sayori takes a bite out of my lunch."
    s "Uwaaaa-"
    s "So delicious!"
    mc "Yeah, it's quite good."
    s "Did you cook this?"
    s "I could have this every day!"
    mc "Yeah, I cooked it."
    mc "That's not important though."
    s "Thank you so much!"
    s "I... might've forgotten to bringg my lunch..."
    s "Ehe~"
    mc "So that's why you wanted my lunch."
    mc "Don't forget your lunch next time. Please."
    s "Alright, alright. I get it~"
    mc "Good."
    "She always does things like this."
    "Why she forgets things so often, I have no idea."
    "Pretty soon, she's going to forget when to wake up and go to school..."
    "Let's hope that doesn't happen."

    # Lunch time ending, transition back to classes.
    scene black
    with wipeleft
    scene roof
    with wipeleft
    "Bell" "RIING"
    "That signifies the end of lunch, and the start of another 4 periods of pain."
    mc "We should head back now."
    s "Yeah!"
    s "Honestly, lunch flew by so fast... I wish we could talk more!"
    mc "Yeah, sure."
    "Honestly, she's slightly annoying at times, but it's better than not talking to anyone."
    "We head back to the classroom, preparing ourselves for another world of hurt."

    # Classes
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene bg class_day
    with wipeleft
    play music t5
    "Classes are as boring as ever, and it's time to leave school."
    "Honestly, I'm just so tired from school that I just want to sleep."
    "But I'm suddenly jolted awake by a blue-eyed girl named Sayori."
    s "[player]!"
    mc "... Just let me sleep here..."
    s "Come on, let's walk home together!"
    "To be honest, I don't really want to walk home with Sayori."

    # Option menu - Do you want to walk home with Sayori, or ignore her?
    menu:
        "Should I walk home with Sayori?"
        "You should":
            call day1Walk from _call_day1Walk
        "You shouldn't":
            call day1NoWalk from _call_day1NoWalk
    return

label day1Walk:

    # Confirmation of walking with Sayori.
    $ route = 1
    "Well, there's nothing bad that can come from walking with Sayori, I guess."
    mc "Alright, sure."
    s "Let's go then! Ehe~"
    mc "Fine, fine, just give me a second."
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
    s "Uwoaaa!"
    mc "What is it?"
    s "There's so many people here!"
    mc "Yeah, since everyone's leaving school."
    mc "I just wanted to play games and watch anime, to be honest."
    s "Come on!-"
    s "There's more to life than anime and video games though.."
    mc "Like what?"
    s "Talking with friends, going to the park, there's so much to do!"
    "Come to think of it, I haven't been to the park in a solid while."
    "I'll probably go there later though."
    mc "Like you're one to talk."
    mc "You're always clinging onto me, as if I'm your only friend."
    s "But we're childhood friends!"
    s "I'm just worried about you."
    mc "Alright, but why haven't you considered playing games?"
    "Sayori remains quiet for a bit, thinking about her response."
    "We walk a little bit more as she thinks of her answer."

    # Choice: Go out with Sayori, or don't?
    scene black
    with wipeleft
    scene street_sunset
    with wipeleft
    s "Becoming a NEET is not good for you!"
    s "Besides, it's more fun hanging around together!"
    s "You haven't even gone outside in the past 3 months-"
    mc "Uhh..."
    mc "I swear I have though-"
    s "We should go out together sometime!"
    "Honestly, I don't really feel like going outside."
    "I honestly wanted to play video games and enjoy myself."
    menu:
        "Should I go out with Sayori?"
        "Yes":
            call day1WalkCont from _call_day1WalkCont
        "No":
            call day1WalkContTwo from _call_day1WalkContTwo
    return

label day1WalkCont:

    # Confirmation of going out with Sayori
    $ route = 2
    mc "Fine, but I don't see much of a reason to go out."
    $ console_history = []
    $ run_input(input="", output="+1 affection (Sayori)")
    $ pause(1)
    hide screen console_screen

    # Discussion with Sayori
    s "Yay~"
    s "Meet me at the park next weekend!~"
    mc "Sure...?"
    "I have no idea why she's so ecstatic to meet with me..."
    "But if that's what makes her happy, I guess I'll meet with her."
    s "By the way, what are we doing tomorrow?"
    mc "It's the second day of school."
    s "We'll be seeing each other more often then!"
    mc "Well, yeah, because I'm forced to go to school instead of playing games."
    mc "Due to a certain someone..."
    s "Meanie!"
    "We continue to banter like this, all the way back home."

    # Going home
    scene black
    with wipeleft
    scene intersection_sunset
    with wipeleft
    mc "Welp, my house is on the right from here."
    mc "I'll see you tomorrow."
    s "See you [player]!"
    "I make my way home, as the sun sets in the background."
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
    s "Alright then..."
    s "I just wanted you to go outside though."
    mc "As I've said, I'm really busy recently. I have my dailies in IdleCraft Simulator and the next episode of TerraAnime to watch."
    s "But I really care about you~"
    mc "I'm sorry, but no is no."
    s "Aww..."
    s "Maybe next time then~"
    mc "Maybe, if there even is one."
    "I feel bad rejecting Sayori like this, but I gotta do what I gotta do."
    "Besides, you only live once, right?"
    $ console_history = []
    $ run_input(input="print(disclaimerThree)", output="PS: dont follow the MC here lol") # Disclaimer 3
    $ pause(0.25)
    hide screen console_screen
    "We continue discussing about random topics all the way home, but Sayori seems less cheerful than before."
    "Maybe I should check up on Sayori later."

    # Going home
    scene black
    with wipeleft
    scene intersection_sunset
    with wipeleft
    mc "Welp, my house is on the right from here."
    mc "I'll see you tomorrow."
    s "See you, [player]."
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
    s "Alright..."
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
    call day1ResetScene
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
    call day1WhatToDo
    return

label day1WhatToDo:

    # Open World Option menu - What to do?
    menu:
        "What should I do? ([actions] actions left.)"
        "Go back home":
            call day1WalkEnd
        "Work out (Jog)" if actions > 3:
            call day1WorkOut
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
    # Resets the scene without the music stopping
    scene black
    with wipeleft
    if actions < 4:
        scene street_sunset
        with wipeleft
    else:
        scene street
        with wipeleft
    call day1WhatToDo
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
    if actions > 0:
        menu:
            "What should I do at home? ([actions] actions left.)"
            "Read a book":
                call day1Read
            "Do my homework" if homework == 0:
                call day1Homework
            "Play IdleCraft Simulator":
                call day1IdleCraft
            "Watch TerraAnime":
                call day1TerraAnime
            "Sleep":
                call day1Sleep
    else:
        call day1Sleep
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
    call day1gaming
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
    call day1gaming
    return

label day1IdleCraft:
    "I ended up playing IdleCraft with a couple of my gaming buddies."
    $ gameSkill = (0 if gameSkill is None else gameSkill) + 1
    $ actions -= 1
    $ console_history = []
    $ run_input(input="", output="+1 Gaming Skill (Total: [gameSkill])")
    $ pause(1)
    hide screen console_screen
    "I'm not that great, but I aspire to become one of the best at video games."
    call day1gaming
    return

label day1TerraAnime:
    "I ended up watching TerraAnime alone."
    $ actions -= 1
    $ console_history = []
    $ run_input(input="", output="Nothing changed.")
    $ pause(1)
    hide screen console_screen
    "I feel absolutely nothing different about me."
    "Honestly, I'm not sure what I'm doing with my life."
    call day1gaming
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
    $ run_input(input="print(stats)", output="Strength: [strength], Intelligence: [intel], Game Skill: [gameSkill], Tardiness: [tardy], Route: [route]") # Stats printed
    $ pause(0.25)
    "Continue by clicking anywhere."
    hide screen console_screen
    window hide
    return
    