from pico2d import open_canvas, delay, close_canvas
import game_framework

import play_mode as start_mode

open_canvas(1600, 600)
game_framework.run(start_mode)
close_canvas()
#1픽셀 : 3cm
#새의 크기 : (75,75), 약 180cm x 145cm
#새 이동 속도 : 시속 40km
#새의 날개짓 속도 : 초당 3번
