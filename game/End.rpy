# Endings for DDLT.
# Stored seperatly from the actual acts.
# End of demo.

label end_demo:
    scene black
    with wipeleft
    window hide
    scene breakdown
    with wipeleft
    play music m1
    $ console_history = []
    $ run_input(input="print(actEnding)", output="Act 0 demo has concluded.")
    $ run_input(input="print(message)", output="This mod has a lot left to go, so please stick around for development!")
    $ run_input(input="print(thankYou)", output="Thank you for playing through what's available. This instance will now quit.")
    window show
    "Continue by clicking anywhere."
    window hide
    hide screen console_screen
    return

# End of DDLT - Act 0
label end:
    scene black
    with wipeleft
    window hide
    scene breakdown
    with wipeleft
    play music m1
    $ console_history = []
    $ run_input(input="print(actEnding)", output="Act 0 has concluded.")
    $ run_input(input="print(thankYou)", output="Thank you for playing through Act 0.")
    $ run_input(input="print(thankYouTwo)", output="I hope to see you in Act 1, as Act 1 isn't out yet!")
    window show
    "Continue by clicking anywhere."
    window hide
    hide screen console_screen
    return