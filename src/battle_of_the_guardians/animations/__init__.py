from src.battle_of_the_guardians.animations.animation import Animation, _running


def update_animations() -> None:
    anim: Animation
    for anim in _running:
        anim.update()
