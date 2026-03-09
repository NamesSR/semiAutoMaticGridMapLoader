import cv2
import pyautogui

map_data = ""
map = ""
m = 0
Ax_start = 3
Ay = 2

img = cv2.imread('image/Screenshot 2026-03-09 204813.png')

for y in range(17):

    Ax = Ax_start

    for x in range(31):

        pixel_color = img[Ay][Ax]
        b, g, r = pixel_color

        print(f"Pixel color at ({x},{y}): {pixel_color}")

        if y in (0, 16) or x in (1,30):
            s = "#"
        else:
            s = "T"

        if s not in ("w", "B"):

            if 65 <= r <= 80 and 150 <= g <= 160 and 80 <= b <= 95:
                map_data += s + "g"

            elif 35 <= r <= 45 and 100 <= g <= 115 and 245 <= b <= 255:
                print("enemy Color")
                p = input() 
                map_data += f"P{p}"

            elif 35 <= r <= 48 and 95 <= g <= 108 and 40 <= b <= 55:
                map_data += s + "gd"

            elif 40 <= r <= 50 and 40 <= g <= 50 and 40 <= b <= 50:
                map_data += s + "b"

            elif 130 <= r <= 140 and 130 <= g <= 140 and 130 <= b <= 140:
                map_data += s + "y"

            elif 60 <= r <= 75 and 60 <= g <= 75 and 60 <= b <= 75:
                map_data += "Fyd"

            elif 95 <= r <= 110 and 95 <= g <= 110 and 95 <= b <= 110:
                map_data += s + "yy"

            elif 165 <= r <= 180 and 50 <= g <= 65 and 50 <= b <= 65:
                map_data += s + "r"
            elif 250 <= r <= 255 and 0 <= g <= 5 and 0 <= b <= 5: 
                print("enemy Color")
                p = input() 
                print("Which Enemy")
                l = input() 
                map_data += f"E{p}{l}" 
                print(map_data)
            elif 250 <= r <= 255 and 250 <= g <= 255 and 250 <= b <= 255:
                print("waipoint Color")
                p = input() 
                print("waiPoint of Which Enemy ")
                l = input() 
                print("WaiPointCount start At 0")
                i = input()
                
                map_data += f"W{p}{l}{i}" 
                print(map_data)
            elif 0 <= r <= 5 and 0 <= g <= 5 and 0 <= b <= 5:
                map_data += "#d" 
            elif 250 <= r <= 2555 and 0 <= g <= 5 and 0 <= b <= 255:
                print("powerOrb Color")
                p = input() 
                map_data += f"B{p}"
            else:
                print("Unknown color:", pixel_color)

        Ax += 17

    Ay += 17

for c in map_data:
    if c in ("#", "T"):
        m += 1
        if m == 31:
            map += ","
            m = 0
    map += c
   
    



print(map)