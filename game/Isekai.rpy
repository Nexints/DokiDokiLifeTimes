label isekai_start:
    # The start of the Isekai.

    # Not finished.
    $ console_history = []
    $ run_input(input="print(isekai)", output="You will be kicked out.") # Stats printed
    $ run_input(input="print()", output="Achievement gained! - Isekai Route")
    $ pause(3)
    hide screen console_screen
    return