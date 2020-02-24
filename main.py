import pygame


def main():
    black = (0,0,0)
    white = (255,255,255)

    (width, height) = (200, 200)
    screen = pygame.display.set_mode((width, height))
    screen.fill(black)

    pygame.display.flip()

    running = True
    while running:

        pygame.draw.rect(screen, white, (50,50,10,100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()

    return

PLATES = {
    'RED':25.0,
    'BLU':20.0,
    'YLW':15.0,
    'GRN':10.0,
    'WHT':5.0,
    'mRED':2.5,
    'mBLU':2.0,
    'mYEL':1.5,
    'mGRN':1.0,
    'mWHT':0.5
}

COLOURS = {
    'RED': (255,0,0),
    'BLU': (0,0,255),
    'YLW': (255,255,0),
    'GRN': (124,252,0),
    'WHT': (255,255,255),
    'mRED':(255,0,0),
    'mBLU':(0,0,255),
    'mYEL':(255,255,0),
    'mGRN':(124,252,0),
    'mWHT':(255,255,255)
}

def barload(weight, isMale):
    ''' Take arguments weight and isMale (True for Men's, False for Women's bar) '''

    ''' return dictionary indicating number of each coloured plate needed per side '''
    setup = {
        'RED': 0,
        'BLU': 0,
        'YLW': 0,
        'GRN': 0,
        'WHT': 0,
        'mRED': 0,
        'mBLU': 0,
        'mYEL': 0,
        'mGRN': 0,
        'mWHT': 0
    }

    weight = float(weight/2)

    if isMale:
        loaded = 12.5
    else:
        loaded = 10.0

    loaded = weight - loaded

    while loaded != 0:
        for colour in PLATES:
            if loaded >= PLATES[colour]:
                loaded -= PLATES[colour]
                setup[colour] += 1
                break
    
    return setup

def generate(weight, isMale):

    setup = barload(weight,isMale)

    black = (0,0,0)
    white = (255,255,255)

    (width, height) = (200, 200)
    screen = pygame.display.set_mode((width, height))
    screen.fill(black)

    pygame.display.flip()

   
    running = True
    while running:
        x = 50
        for colour in setup:
            for i in range(setup[colour]):
                pygame.draw.rect(screen, COLOURS[colour], (x,50,10,100))
                x+=15

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
    return

