import wrap
wrap.add_sprite_dir("mysprite")
wrap.world.create_world(500,600)
grass=wrap.sprite.add("texstures",250,600,"grass")
pacman=wrap.sprite.add("pacman",200,-100,"player2")

wrap.sprite.set_size(grass,500,500)

speed=0
@wrap.always()
def padenye(pos_x,pos_y):
    global speed
    wrap.world.set_title(pos_y)
    y=wrap.sprite.get_y(pacman)
    bottom=wrap.sprite.get_bottom(pacman)
    if bottom<540:
        wrap.sprite.move(pacman,0,speed+2)
        speed=speed+2
