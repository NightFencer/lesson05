import simple_draw as sd




def house(x0, y0, x1, y1):
    #wall parameters
    step_x = (x1-x0)//10
    step_y = (y1-y0)//20
    color = (255, 255, 255)
    width = 2
    row_stown = 0
    #walls
    sd.line(sd.get_point(x0, y0), sd.get_point(x0, y1), color, width)
    sd.line(sd.get_point(x1, y0), sd.get_point(x1, y1), color, width)
    sd.line(sd.get_point(x0, y1), sd.get_point(x1, y1), color, width)
    for y in range(y0, y1 , step_y):
        sd.line(sd.get_point(x0, y), sd.get_point(x1, y), color, width)

        if row_stown // 2 == row_stown / 2:
            shear = step_x // 2
        else:
            shear = 0
        for x in range(x0 + shear, x1 + 1, step_x):
            sd.line(sd.get_point(x, y), sd.get_point(x, y + step_y), color, width)
        row_stown = row_stown + 1
    # roof
    left_point = sd.get_point(x0-20,y1)
    right_point = sd.get_point(x1+20,y1)
    top_point = sd.get_point((x1-x0)//2+x0,(y1-y0)//4+y1)
    sd.line(left_point,right_point,sd.COLOR_RED,3)
    sd.line(left_point, top_point, sd.COLOR_RED, 3)
    sd.line(top_point, right_point, sd.COLOR_RED, 3)
    #window
    left_bottom = sd.get_point((x1-x0)//3+x0,(y1-y0)//3+y0)
    right_top = sd.get_point(x1-(x1 - x0) // 3 ,y1- (y1 - y0) // 3)
    sd.rectangle(left_bottom,right_top,sd.COLOR_YELLOW)
    sd.vector(left_bottom,90,(y1 - y0) // 3+1,color,2)
    sd.vector(left_bottom, 0,(x1 - x0) // 3+1, color, 2)
    sd.vector(right_top,180,(x1 - x0) // 3+1, color, 2)
    sd.vector(right_top, 270, (y1 - y0) // 3+1, color, 2)


#house(100, 100, 300, 300)
# TODO здесь ваш код\
row = 0
# for y0 in range(0, 301, step_y):
#     if row / 2 == row // 2:
#         shear = 25
#     else:
#         shear = 0
#     for x0 in range(0 - shear, 401, step_x):
#         point_list = [sd.get_point(0 + x0, 0 + y0), sd.get_point(50 + x0, 0 + y0),
#                       sd.get_point(50 + x0, 25 + y0), sd.get_point(0 + x0, 25 + y0)]
#         sd.lines(point_list=point_list, width=4, color=sd.COLOR_ORANGE)
#     row = row + 1

#sd.pause()
