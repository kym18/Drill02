from pico2d import *

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas_now()
grass.draw_now(400, 30)
character.draw_now(400, 90)
delay(1)

def run_circle():
    print('CIRCLE')

    r = 200
    #0도부터 360도까지 5도TLr
    for deg in range(0, 360, 5):
        x = r * math.cos(math.radians(deg))
        y = r * math.sin(math.radians(deg))       
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
            
    pass  #아무것도 안한다. 근데 실행 ㄱㄴ 아무것도 하지않는 함수의 기능 함.(뼈대 만들기)

def run_rectangle():
    print('RECTANGLE')
    pass


while True:
    #먼저 함수 호출 -> 정의도 안됐는데? ->이게 무슨 코드인지 보이게
    run_circle()
    run_rectangle()
    break

close_canvas()
    
