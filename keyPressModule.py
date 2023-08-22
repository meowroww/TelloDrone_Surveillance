# Packages
import pygame

# Initialize window for pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


# Function to tell whether the key has been pressed or not


def getKey(keyName):
    # if not pressed then it's False
    ans = False
    for eve in pygame.event.get():
        pass
    # create input
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()

    return ans


def main():
    if getKey('LEFT'):
        print('Left key pressed')
    if getKey('RIGHT'):
        print('Right key pressed')


if __name__ == '__main__':
    init()
    while True:
        main()
