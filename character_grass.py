
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

is_rectangle = True  # 직사각형 토글

while True:  # 무한 반복
    if is_rectangle:
        x = 20
        y = 90
        while x < 780:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x = x + 2
            delay(0.01)
            
        while y < 550:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(780, y)
            y = y + 2
            delay(0.01)
            
        while x > 20:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 550)
            x = x - 2
            delay(0.01)
            
        while y > 90:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(20, y)
            y = y - 2
            delay(0.01)
        is_rectangle = False
    else:
        x = 400
        y = 560
        
        radius = 250
        center_x = 400
        center_y = 300
        angle = 0  # 각도
        while angle <= 360:   
            clear_canvas()
            grass.draw(400, 30)
            x = center_x + radius * math.sin(math.radians(angle))
            y = center_y + radius * math.cos(math.radians(angle))   
            character.draw_now(x, y)
            angle += 2
            delay(0.01)
        is_rectangle = True  

close_canvas()
