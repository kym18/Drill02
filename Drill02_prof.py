from pico2d import *

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')


def render_frame(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

def run_circle():
    print('CIRCLE')
    cx, cy = 400, 300
    r = 200
    
    for deg in range(0, 360, 5):   #0도부터 360도까지 5도씩
        x = r * math.cos(math.radians(deg)) + cx
        y = r * math.sin(math.radians(deg)) + cy   
        render_frame(x, y)
            
    #pass :아무것도 안한다. 근데 실행 ㄱㄴ 아무것도 하지않는 함수의 기능 함.(뼈대 만들기)


def run_rectangle():
    print('RECTANGLE')

    #bottom line
    for x in range(20, 780+1, 5):  # +1해주는 이유 780까지 가서 정확하게 실행
        render_frame(x, 90) #x,y 위치에 캐릭터 그려줄 수 있는 함수

    #right line
    for y in range(90, 550+1, 5):
        render_frame(780, y)

    #top line
    for x in range(780, 20-1, -5):
        render_frame(x, 550)


    #left line
    for y in range(550, 90-1, -5):
        render_frame(20, y)


while True:
    #먼저 함수 호출 -> 정의도 안됐는데? ->이게 무슨 코드인지 보이게
    run_circle()
    run_rectangle()
    

close_canvas()
    
