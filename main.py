import pygame

''' PLATES INFO'''
PLATES = {
    'RED':{
        'weight':25.0,
        'rgb':(255,0,0),
        'position':{
            'start':55,
            'width':13,
            'height':90
        }},
    'BLU':{
        'weight':20.0,
        'rgb':(0,0,255),
        'position':{
            'start':55,
            'width':11,
            'height':90
        }},
    'YLW':{
        'weight':15.0,
        'rgb':(255,255,0),
        'position':{
            'start':55,
            'width':9,
            'height':90
        }},
    'GRN':{
        'weight':10.0,
        'rgb':(124,252,0),
        'position':{
            'start':55,
            'width':7,
            'height':90
        }},
    'WHT':{
        'weight':5.0,
        'rgb':(255,255,255),
        'position':{
            'start':77,
            'width':5,
            'height':46
        }},
    'mRED':{
        'weight':2.5,
        'rgb':(255,0,0),
        'position':{
            'start':79,
            'width':4,
            'height':42
        }},
    'mBLU':{
        'weight':2.0,
        'rgb':(0,0,255),
        'position':{
            'start':81,
            'width':4,
            'height':38
        }},
    'mYEL':{
        'weight':1.5,
        'rgb':(255,255,0),
        'position':{
            'start':83,
            'width':4,
            'height':34
        }},
    'mGRN':{
        'weight':1.0,
        'rgb':(124,252,0),
        'position':{
            'start':84,
            'width':4,
            'height':32
        }},
    'mWHT':{
        'weight':0.5,
        'rgb':(255,255,255),
        'position':{
            'start':86,
            'width':3,
            'height':28
        }}
}
''' COLLAR INFO '''
COLLAR = {
    'weight':2.5,
    'rgb':(128,128,128),
    'position':{
        'start':82,
        'width':8,
        'height':36
}}


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
            if loaded >= PLATES[colour]['weight']:
                loaded -= PLATES[colour]['weight']
                setup[colour] += 1
                break
    
    return setup


def generate(weight, isMale):
    ''' Generate image for barloading '''

    setup = barload(weight,isMale)

    black = (0,0,0)

    (width, height) = (200, 200)
    screen = pygame.Surface((width, height))
    screen.fill(black)

    # Starting x position
    x = 50

    # Render grip section
    pygame.draw.rect(screen, (220,220,220), (0, 97, 44, 6))

    # Render separation piece
    pygame.draw.rect(screen, (220,220,220), (44, 93, 6, 14))

    # Render outer sleeve
    # pygame.draw.rect(screen, (128,128,128), (50, 95, 83, 10))

    for colour in setup:
        if colour == "mRED":
            pygame.draw.rect(screen,COLLAR['rgb'], (x, COLLAR['position']['start'], COLLAR['position']['width'], COLLAR['position']['height']))
            x+=COLLAR['position']['width']+3

        for i in range(setup[colour]):
            pygame.draw.rect(screen, PLATES[colour]['rgb'], (x,PLATES[colour]['position']['start'],PLATES[colour]['position']['width'],PLATES[colour]['position']['height']))
            x+=PLATES[colour]['position']['width']+3

    pygame.image.save(screen, "M"+str(weight)+".jpeg")

    return