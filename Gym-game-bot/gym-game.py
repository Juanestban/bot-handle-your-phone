# *-* coding: utf-8 *-*
from ppadb.client import Client as ClientAdb
import time
import pygame
import sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
# from Torre import *

adb = ClientAdb(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print("has'nt any device connected")
    quit()

device = devices[0]
# result = device.screencap()
# with open('screen.png', 'wb') as fb:
#     fb.write(result)
#     print('screenshoot completed')

getFortuneRule = '540 1600 540 1600'
getClickedSeconds = '540 1470 540 1470'
GameRulete = False
GameClicked = False


def Rulete():
    while True:
        device.shell('input touchscreen swipe {} 1'.format(getFortuneRule))
        # time.sleep(0.05)


def ClickedBySeconds():
    while True:
        device.shell(
            'input touchscreen swipe {} 1'.format(getClickedSeconds))
        time.sleep(0.00001)


# ClickedBySeconds()
Rulete()


# pygame.init()
# winWidth = 720
# winHeight = 540
# gameStarted = True
# timerFrame = pygame.time.Clock()

# screen = pygame.display.set_mode((winWidth, winHeight))
# pygame.display.set_caption('Bot Handler Game')
# font = pygame.font.SysFont(None, 30)
# white = (204, 204, 204)
# blackColor = (0, 0, 0)
# greenColor = (67, 214, 16)
# redColor = (214, 37, 16)
# click = False
# isActived = 'OFF'
# currentColor = redColor


# def DrawText(text, font, color, surface, x, y):
#     textObj = font.render(text, 1, color)
#     textRect = textObj.get_rect()
#     textRect.topleft = (x, y)
#     surface.blit(textObj, textRect)


# def QuitGame():
#     pygame.quit()
#     sys.exit()


# def InitGame():
#     screen.fill((4, 9, 15))
#     widthScreen = screen.get_width()
#     heightScreen = screen.get_height()
#     centerX = widthScreen / 2
#     centerY = heightScreen / 2
#     statusRulete = False
#     clicksForSeconds = False
#     while True:
#         mx, my = pygame.mouse.get_pos()

#         if statusRulete:
#             isActived = 'STATUS'
#             currentColor = greenColor
#             GameRulete = True
#             Rulete()
#         if not statusRulete:
#             isActived = 'STATUS'
#             currentColor = redColor
#             GameRulete = False

#         DrawText('{}'.format(isActived), font, currentColor,
#                  screen, widthScreen - 150, 10)
#         buttonClick = pygame.Rect(centerX - 100, centerY - 25, 200, 50)
#         pygame.draw.rect(screen, (225, 220, 220), buttonClick)
#         DrawText('bot Gym Game', font, blackColor,
#                  screen, centerX - 70, centerY - 10)
#         if buttonClick.collidepoint((mx, my)):
#             if click:
#                 print('clicked')
#                 statusRulete = not statusRulete
#                 pass

#         if clicksForSeconds:
#             # GameClicked = True
#             ClickedBySeconds()
#         # if not clicksForSeconds:
#         #     GameClicked = False

#         btnClickForSeconds = pygame.Rect(centerX - 100, centerY + 70, 200, 50)
#         pygame.draw.rect(screen, (225, 220, 220), btnClickForSeconds)
#         DrawText('clicked fast Game', font, blackColor,
#                  screen, centerX - 90, centerY + 85)
#         if btnClickForSeconds.collidepoint((mx, my)):
#             if click:
#                 print('clicked')
#                 clicksForSeconds = not clicksForSeconds
#                 pass

#         click = False
#         for event in GAME_EVENTS.get():
#             # print(event.type)
#             if event.type == GAME_GLOBALS.QUIT:
#                 QuitGame()

#             if event.type == GAME_GLOBALS.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     click = True

#             pygame.display.update()
#             # if (event.type == KEYUP) or (event.type == KEYDOW):
#             #     print('keyPressed')
#             #     time.sleep(.1)

#         timerFrame.tick(60)
#         pygame.display.update()


# InitGame()
