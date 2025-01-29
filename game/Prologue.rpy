# Start of Act 0.
# Details the background behind the MC.

label prologue:
    stop music fadeout 0.5

    # Introduction. The console and the intro video is introduced.
    scene black
    with dissolve_scene_half
    play music m1
    $ console_history = []
    $ run_input(input="print(currentAct)", output="Current Act: Prologue (0).")
    $ run_input(input="print(currentDate)", output="Date: April 8, 2011.")
    $ run_input(input="print(disclaimer)", output="This is a multi-part mod. Playing through Act 0 is recommended before playing other parts.")
    "Continue by clicking anywhere."
    $ console_history = []
    $ run_input(input="print(disclaimerTwo)", output="Characters may not be perfectly accurate from the original game.")
    $ run_input(input="print(haveFun)", output="Have fun!")
    "Continue by clicking anywhere."
    window hide
    hide screen console_screen
    $ renpy.movie_cutscene("mod_assets/videos/DDLT_Act_0.avi")

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
    "I just wanted to play video games..."
    "It's the first day of school, and I already hate it."
    "I should probably get to school though, otherwise my mom will have a word with me."

    # MC meeting Sayori.
    scene black
    with wipeleft
    scene bg residential_day
    with wipeleft
    $ s_name = "Sayori"
    s "Heeeeeeeyyy!!"
    "That girl over there is Sayori, my close neighbor and childhood friend."
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

    # Lunch time has ended.
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
    return