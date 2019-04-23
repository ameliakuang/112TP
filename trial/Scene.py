import pygame

# The general idea of the code below was adopted from this link, but I added a few changes.
# Citation: https://stackoverflow.com/questions/14700889/pygame-level-menu-states
class Scene(object):
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError

class SceneManager(object):
    def __init__(self):
        pass

# Show Win/Loss
class CustomScene(object):
    def __init__(self, state):
        self.state = state

    def redrawAll(self, screen):
        # Win
        if(self.state == True):
            image = pygame.image.load('You Win.png').convert()
            rect = image.get_rect()
            rect.center = (screen.get_rect().centerx, screen.get_rect().centery)
        # Lose
        else:
            image = pygame.image.load('game-over.png').convert()
            rect = image.get_rect()
            rect.center = (screen.get_rect().centerx, screen.get_rect().centery)
        screen.blit(image, rect.center)




