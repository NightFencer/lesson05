import simple_draw as sd


def sun(center=sd.get_point(500, 300), radius=100):
    for r in range(2, radius // 2, 4):
        sd.circle(center, r, color=sd.COLOR_YELLOW, width=4)
    for angle in range(0, 361, 36):
        # sd.get_vector(center,angle,radius,4)
        sd.vector(center, angle, radius, width=4)
