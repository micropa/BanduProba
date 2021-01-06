Banduka = 0
def KIBE():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        """)
def zizi():
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        # . # . .
        . # # # #
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        . . # . .
        . # # # #
        # . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        # # . # .
        . . . . #
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        # . . . #
        """)

def on_gesture_logo_down():
    pass
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_a():
    zizi()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Banduka
    Banduka = input.light_level()
    for index in range(7):
        KIBE()
    basic.show_leds("""
        . . # . .
        # # # # #
        # # # # #
        . . # . .
        . . # . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # # # # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # # # #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . # # #
        . . . . #
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . # #
        . . . . #
        . . . . #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . #
        . . . . #
        . . . . #
        . . . . #
        . . . . .
        """)
    basic.show_leds("""
        . . . . #
        . . . . #
        . . . . #
        . . . . #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . #
        . . . . #
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . #
        . . . . #
        . . . # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . #
        . . # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . # # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        # # # . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # . . . .
        # . . . .
        # # . . .
        """)
    basic.show_leds("""
        . . . . .
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        """)
    basic.show_leds("""
        . . . . .
        # # . . .
        # . . . .
        # . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        # # # . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        # # # # .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . # # # .
        . . . # .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . # # .
        . . . # .
        . . . # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . # .
        . . . # .
        . . # # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . # .
        . # # # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . # . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . # . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        """)
    basic.show_leds("""
        # # # # #
        # # . # #
        # . . . #
        # # . # #
        # # # # #
        """)
    basic.show_leds("""
        # # . # #
        # . # . #
        . # . # .
        # . # . #
        # # . # #
        """)
    basic.show_leds("""
        # # . # #
        # # . # #
        . . # . .
        # # . # #
        # # . # #
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        # # # # #
        . . # . .
        . . # . .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        . . # . #
        # # # # .
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        . . # . .
        # # # # .
        . . # . #
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # #
        # . . . .
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        # . . . #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
