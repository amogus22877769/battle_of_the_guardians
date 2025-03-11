from frontend.src.battle_of_the_guardians.action import Action
from frontend.src.battle_of_the_guardians.controllers.front import leaderboard
from frontend.src.battle_of_the_guardians.defines import stage
from frontend.src.battle_of_the_guardians.sprites_loaders.leaderboard_sprites import LeaderboardSprites


class Leaderboard:
    def __init__(self):
        self.sprites: LeaderboardSprites = LeaderboardSprites()
        self.is_this_the_first_iteration: bool = True

    def handle_updates(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.sprites.return_button.collide_point(*action.value):
                        self.is_this_the_first_iteration = True
                        return 'menu'
                case "resize":
                    self.sprites.update(action.value)
        return "leaderboard"

    def draw(self, screen) -> None:
        screen.blits(blit_sequence=((self.sprites.background.image, self.sprites.background.rect),
                                    (self.sprites.leaderboard_string.image, self.sprites.leaderboard_string.rect),
                                    *[(leader.image, leader.rect) for leader in self.sprites.leaders],
                                    (self.sprites.return_button.image, self.sprites.return_button.rect)))

    def update(self, actions: list[Action]) -> stage:
        if self.is_this_the_first_iteration:
            self.sprites.fill(leaderboard())
            self.is_this_the_first_iteration = False
        return self.handle_updates(actions)
