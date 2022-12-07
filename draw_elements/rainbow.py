import simple_draw as sd
def rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    step=0
    for color in rainbow_colors:

        sd.circle(sd.get_point(150,00),radius=1300-step,color=color,width=30)
        step=step+30