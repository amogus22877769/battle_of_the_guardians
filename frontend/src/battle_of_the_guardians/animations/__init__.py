from frontend.src.battle_of_the_guardians.animations.animation import Animation, _running

are_animations_running: bool = False

def update_animations() -> None:
    anim: Animation
    global are_animations_running
    if not _running:
        are_animations_running = False
    else:
        are_animations_running = True
    for anim in _running:
        anim.update()
