import simple_draw as sd



def smiling_circle(x0, y0, color =sd.COLOR_YELLOW):
    point_list = [sd.get_point(-20 + x0, 0 + y0), sd.get_point(-10 + x0, -15 + y0), sd.get_point(10 + x0, -15 + y0),
                  sd.get_point(20 + x0, 0 + y0)]
    sd.lines(point_list=point_list, width=2, color=color)
    sd.circle(center_position=sd.get_point(x0, y0), color=color, radius=25)
    sd.circle(center_position=sd.get_point(x0 - 10, y0 + 10), color=color, radius=5)
    sd.circle(center_position=sd.get_point(x0 + 10, y0 + 10), color=color, radius=5)
    sd.circle(center_position=sd.get_point(x0, y0), color=color, radius=2)

def man(x,y,size):
    smiling_circle(x,y)
    point = sd.get_point(x,y-25)
    body_vector = sd.get_vector(point,270,size)
    body_vector.draw()
    sd.vector(body_vector.end_point,225,30)
    sd.vector(body_vector.end_point, 315, 30)
    point = sd.get_point(x, y - 45)
    while True:
        if sd.user_want_exit():
            break
        sd.vector(point, 225, 30)
        sd.vector(point, 315, 30)
        sd.sleep(0.2)
        sd.vector(point, 225, 30,sd.background_color)
        sd.vector(point, 315, 30,sd.background_color)
        sd.vector(point, 135, 30)
        sd.vector(point, 45, 30)
        sd.sleep(0.2)
        sd.vector(point, 135, 30, sd.background_color)
        sd.vector(point, 45, 30, sd.background_color)
