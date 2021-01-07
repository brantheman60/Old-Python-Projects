def colorBlender(rgb1, rgb2, midpoints, n):
    # 123123123
    if n<0 or n>midpoints:
        return None
    
    r1 = rgb1 // 1000000
    g1 = (rgb1 // 1000) % 1000
    b1 = rgb1 % 1000
    
    r2 = rgb2 // 1000000
    g2 = (rgb2 // 1000) % 1000
    b2 = rgb2 % 1000
    
    rStep = (r2 - r1) / (midpoints + 1)
    r3 = round(r1 + rStep*n);
    gStep = (g2 - g1) / (midpoints + 1)
    g3 = round(g1 + gStep*n);
    bStep = (b2 - b1) / (midpoints + 1)
    b3 = round(b1 + bStep*n);
    
    return (r3 * 1000000) + (g3 * 1000) + b3


print(colorBlender(220020060, 189252201, 3, 1))
print(colorBlender(220020060, 189252201, 2, 3))
print(colorBlender(100100100, 200200200, 4, 2))
print(colorBlender(100100100, 200200200, 4, -1))

# 220020060, 189252201, 3, 1 returns 212078095