def rgb(r, g, b):
    return "".join([hex(min(max(0, i), 255))[2:].zfill(2) for i in [r, g, b]]).upper()


print(rgb(0, 0, 0))  # 000000
print(rgb(0, 0, -20))  # 000000
print(rgb(300, 255, 255))  # FFFFFF
print(rgb(173, 255, 47))  # ADFF2F
