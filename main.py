import random

import wrap
wrap.add_sprite_dir("mysprite")
wrap.world.create_world(500,600)
grass=wrap.sprite.add("texstures",250,600,"grass")
pacman=wrap.sprite.add("pacman",200,-100,"player2")

platform=wrap.sprite.add("mario-items",220,300,"moving_platform2")
platform1=wrap.sprite.add("mario-items",150,360,"moving_platform2")
wrap.sprite.set_size(grass,500,500)
cacoyto_list=[platform,platform1]
speed=0

@wrap.always()
def padenye(pos_x,pos_y):
    global speed
    wrap.world.set_title(pos_y)
    bottom=wrap.sprite.get_bottom(pacman)


    if bottom<550:
        wrap.sprite.move(pacman,0,speed)
        speed=speed+2
        bottom = wrap.sprite.get_bottom(pacman)
        if bottom>550:
            wrap.sprite.move_bottom_to(pacman,550)
            speed=0
    for i in cacoyto_list:
        check_platform(i)

def check_platform(platform):
    global speed
    top_platform = wrap.sprite.get_top(platform)
    bottom = wrap.sprite.get_bottom(pacman)
    if bottom>top_platform and wrap.sprite.is_collide_sprite(pacman,platform):
        wrap.sprite.move_bottom_to(pacman, top_platform)
        speed=-speed*0.8

@wrap.on_key_always(wrap.K_LEFT)
def move():
    wrap.sprite.move(pacman,-1,0)