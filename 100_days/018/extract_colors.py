import colorgram

colors = colorgram.extract('image.jpg', 30)

def extract_colors(colors_palette, ):
    palette = []
    for i in colors_palette:
        r = i.rgb.r
        g = i.rgb.g
        b = i.rgb.b
        new_color = (r, g, b)
        palette.append(new_color)
    return palette

print(extract_colors(colors))

color_list = [(204, 164, 107), (155, 73, 46), (235, 238, 244), (52, 92, 123), (224, 201, 135), (171, 153, 40), (138, 31, 21), (132, 162, 185), (200, 91, 71), (48, 122, 87), (14, 99, 73), (95, 73, 75), (146, 178, 147), (72, 47, 38), (163, 142, 158), (234, 175, 165), (55, 46, 50), (184, 206, 172), (19, 85, 90), (144, 21, 24), (41, 62, 74), (82, 145, 128), (181, 87, 89), (41, 66, 90), (13, 71, 68), (213, 178, 183), (179, 191, 207)]
