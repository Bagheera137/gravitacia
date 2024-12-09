import random

import wrap
wrap.add_sprite_dir("mysprite")
wrap.world.create_world(500,600)
grass=wrap.sprite.add("texstures",250,600,"grass")
pacman=wrap.sprite.add("pacman",150,50,"player2")

platform=wrap.sprite.add("mario-items",220,300,"moving_platform2")
platform1=wrap.sprite.add("mario-items",150,360,"moving_platform2")
platform2=wrap.sprite.add("mario-items",290,230,"moving_platform2")
platform3=wrap.sprite.add("mario-items",220,100,"moving_platform2")
platform_grass=wrap.sprite.add("mario-items",250,557,"moving_platform2",False)
wrap.sprite.set_width(platform_grass,500)

wrap.sprite.set_size(grass,500,500)
cacoyto_list=[platform,platform1,platform2,platform3,platform_grass]
decorations=[grass]
speed=0

@wrap.always()
def padenye(pos_x,pos_y,keys):
    global speed
    wrap.world.set_title(pos_y)


    wrap.sprite.move(pacman, 0, speed)
    speed = speed + 2

    if speed>=20:
        speed=20

    #if bottom>550:
    #   wrap.sprite.move_bottom_to(pacman,550)
    #   speed=0

    for i in cacoyto_list:
        check_platform(i,keys)
    move_pacman()
def check_platform(platform,keys):
    global speed
    top_platform = wrap.sprite.get_top(platform)
    bottom = wrap.sprite.get_bottom(pacman)
    if bottom>top_platform and wrap.sprite.is_collide_sprite(pacman,platform):
        wrap.sprite.move_bottom_to(pacman, top_platform)
        speed = -7
        if wrap.K_SPACE in keys:
            speed = -20
@wrap.on_key_always(wrap.K_LEFT,wrap.K_RIGHT)
def move(keys):
    global speed
    if wrap.K_LEFT in keys:
        wrap.sprite.move(pacman,-5,0)
    elif wrap.K_RIGHT in keys:
        wrap.sprite.move(pacman, 5, 0)


def move_camera(number):
    wrap.sprite.move(pacman,0,number)
    for i in cacoyto_list:
        wrap.sprite.move(i, 0, number)
    for i in decorations:
        wrap.sprite.move(i, 0, number)
def move_pacman():
    y=wrap.sprite.get_y(pacman)
    colpix=300-y
    move_camera(colpix)
