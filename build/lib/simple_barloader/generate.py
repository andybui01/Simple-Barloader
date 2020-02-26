import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

''' PLATES INFO'''
PLATES = {
    'RED':{
        'WEIGHT':25.0,
        'RGB':(255,0,0),
        'POSITION':{
            'START':55,
            'WIDTH':13,
            'HEIGHT':90
        }},
    'BLU':{
        'WEIGHT':20.0,
        'RGB':(0,0,255),
        'POSITION':{
            'START':55,
            'WIDTH':11,
            'HEIGHT':90
        }},
    'YLW':{
        'WEIGHT':15.0,
        'RGB':(255,255,0),
        'POSITION':{
            'START':55,
            'WIDTH':9,
            'HEIGHT':90
        }},
    'GRN':{
        'WEIGHT':10.0,
        'RGB':(124,252,0),
        'POSITION':{
            'START':55,
            'WIDTH':7,
            'HEIGHT':90
        }},
    'WHT':{
        'WEIGHT':5.0,
        'RGB':(255,255,255),
        'POSITION':{
            'START':77,
            'WIDTH':5,
            'HEIGHT':46
        }},
    'mRED':{
        'WEIGHT':2.5,
        'RGB':(255,0,0),
        'POSITION':{
            'START':79,
            'WIDTH':4,
            'HEIGHT':42
        }},
    'mBLU':{
        'WEIGHT':2.0,
        'RGB':(0,0,255),
        'POSITION':{
            'START':81,
            'WIDTH':4,
            'HEIGHT':38
        }},
    'mYEL':{
        'WEIGHT':1.5,
        'RGB':(255,255,0),
        'POSITION':{
            'START':83,
            'WIDTH':4,
            'HEIGHT':34
        }},
    'mGRN':{
        'WEIGHT':1.0,
        'RGB':(124,252,0),
        'POSITION':{
            'START':84,
            'WIDTH':4,
            'HEIGHT':32
        }},
    'mWHT':{
        'WEIGHT':0.5,
        'RGB':(255,255,255),
        'POSITION':{
            'START':86,
            'WIDTH':3,
            'HEIGHT':28
        }}
}
''' COLLAR INFO '''
COLLAR = {
    'WEIGHT':2.5,
    'RGB':(128,128,128),
    'POSITION':{
        'START':82,
        'WIDTH':8,
        'HEIGHT':36
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

    if weight < loaded:
        raise ValueError

    loaded = weight - loaded

    while loaded != 0:
        for colour in PLATES:
            if loaded >= PLATES[colour]['WEIGHT']:
                loaded -= PLATES[colour]['WEIGHT']
                setup[colour] += 1
                break
    
    return setup


def generate(weight, isMale, **kwargs):
    ''' Generate image for barloading '''

    if len(kwargs) > 0:
        file_path = kwargs['file_path']
    else:
        file_path = ''

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

    # Render plates + collar
    for colour in setup:

        # Draw collar before drawing red microplate
        if colour == "mRED":
            pygame.draw.rect(screen,COLLAR['RGB'], (x, COLLAR['POSITION']['START'], COLLAR['POSITION']['WIDTH'], COLLAR['POSITION']['HEIGHT']))
            x+=COLLAR['POSITION']['WIDTH']+3

        # Draw plate, repeat if necessary
        for i in range(setup[colour]):
            pygame.draw.rect(screen, PLATES[colour]['RGB'], (x,PLATES[colour]['POSITION']['START'],PLATES[colour]['POSITION']['WIDTH'],PLATES[colour]['POSITION']['HEIGHT']))
            x+=PLATES[colour]['POSITION']['WIDTH']+3

    file_name=''
    if isMale: file_name+="M"
    else: file_name+="F"
    file_name+= str(weight)
    file_name+=".jpeg"

    pygame.image.save(screen, file_path+file_name)

    return file_name