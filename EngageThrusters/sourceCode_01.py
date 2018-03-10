# A simple script for animating a sprite's "thruster flame" using
# the pygame module.

import pygame, sys
import numpy as np
from pygame.locals import *

FPS = 60
fpsClock = pygame.time.Clock()

# Setting up "viewing window"
winWidth = 400*4
winHeight = 300*4
DISPLAYSURF = pygame.display.set_mode((winWidth,winHeight), 0, 32)
pygame.display.set_caption('Basic Animation')
backGndColor = (255,0,255)





class playerSprite:

    def __init__(self, imgWidth, imgHeight, spriteFolder):

        self.width = imgWidth
        self.height = imgHeight
        self.spriteFolder = spriteFolder

        # loading sprite images...

            # Thruster flame: #
        self.flameStep_1 = pygame.image.load(self.spriteFolder + 'thrusterFlame_01.png')
        self.flameStep_2 = pygame.image.load(self.spriteFolder + 'thrusterFlame_02.png')
        self.flameStep_3 = pygame.image.load(self.spriteFolder + 'thrusterFlame_03.png')
        self.flameStep_4 = pygame.image.load(self.spriteFolder + 'thrusterFlame_04.png')
        self.flameStep_5 = pygame.image.load(self.spriteFolder + 'thrusterFlame_05.png')
        self.flameStep_6 = pygame.image.load(self.spriteFolder + 'thrusterFlame_06.png')

            # Car body: #
        self.carBody = pygame.image.load(self.spriteFolder + 'car_body.png')


        # placing sprite in center of screen...

        self.xCoord = winWidth/2 - self.width/2
        self.yCoord = winHeight/2 - self.height/2

        self.theta = 0


        # variable for storing flame animation FSM state-value.

        self.flameState = 0

        # Variable for setting-up "DriveCar" method.

        self.fwd = 0

    #########################################
    # Method for transforming sprite assets #
    #########################################

    def TransformAsset(self, thatWhichMoves):
        spinner = pygame.transform.rotate(thatWhichMoves, self.theta)

        rotatedRect1 = spinner.get_rect()
        rotatedRect1.center = (self.xCoord + self.width/2, self.yCoord + self.height/2) # want to rotate about center of sprite (which just happens to be in the middle of the screen!)
        DISPLAYSURF.blit(spinner, rotatedRect1)


    #############################################
    # Methods for producing outputs for FSM ... #
    #############################################

        # fs(n+1) : fs(n) & fs(n-1) & ... & fs(2) & fs(1)

    def fs1(self):
        self.TransformAsset(self.flameStep_1)
    def fs2(self):
        self.fs1()
        self.TransformAsset(self.flameStep_2)
    def fs3(self):
        self.fs2()
        self.TransformAsset(self.flameStep_3)
    def fs4(self):
        self.fs3()
        self.TransformAsset(self.flameStep_4)
    def fs5(self):
        self.fs4()
        self.TransformAsset(self.flameStep_5)
    def fs6(self):
        self.fs5()
        self.TransformAsset(self.flameStep_6)

    ########################################
    # FSM for animating the thruster flame #
    ########################################

    def animateflame(self):

            # Flame-animation FSM ... #

        if self.flameState == 0:
            #Do nothing
            self.flameState+=1

        elif self.flameState == 1:
            # Flame-layer 1
            self.flameState += 1
            self.fs1()

        elif self.flameState == 2:
            # Flame-layer 2
            self.flameState += 1
            self.fs2()

        elif self.flameState == 3:
            # Flame-layer 3
            self.flameState += 1
            self.fs3()

        elif self.flameState == 4:
            # Flame-layer 4
            self.flameState += 1
            self.fs4()

        elif self.flameState == 5:
            # Flame-layer 5
            self.flameState += 1
            self.fs5()

        elif self.flameState == 6:
            # Flame-layer 6; recycle to initial state when done.
            self.flameState = 0
            self.fs6()



    #################################
    # Functions for controlling car #
    #################################


    def terminal_vel(self, fwdStep):
        return fwdStep*5

    def accelerate(self, factor=4.0):
        self.fwd += self.fwd*(factor/100)

    def tooFast(self, fwdStep):
        return self.fwd > self.terminal_vel(fwdStep)

    def tooSlow(self, fwdStep):
        return self.fwd < fwdStep

    def DriveCar(self, angleStep, fwdStep):

        # Check for key-presses.
        pressed = pygame.key.get_pressed()


        if pressed[K_LEFT]:
            self.theta += angleStep
        if pressed[K_RIGHT]:
            self.theta -= angleStep

        # Conditions for going forward: Up-arrow pressed, or speed is above increment value.
        if pressed[K_UP] or self.fwd > fwdStep:

            # Sanity check: has makes "self.fwd" equal fwdStep when it hasn't been assigned yet (check __init__).
            self.fwd = fwdStep if (self.fwd == 0) else self.fwd


            # If thruster is ON!
            if pressed[K_LSHIFT]:

                # Turn on thruster!
                self.animateflame()

                if self.tooFast(fwdStep):

                    self.fwd = self.terminal_vel(fwdStep)
                else:
                    self.accelerate()

            # If thruster is Off, decelerate if too fast.
            else:

                if self.tooSlow(fwdStep):
                    self.fwd = fwdStep
                else:
                    self.accelerate(factor=-2.0)





            self.xCoord -= self.fwd*np.sin(self.theta*np.pi/180)
            self.yCoord -= self.fwd*np.cos(self.theta*np.pi/180)

            print(self.fwd)

        # if pressed[K_DOWN]:
        #     self.xCoord += self.fwd*np.sin(self.theta*np.pi/180)
        #     self.yCoord += self.fwd*np.cos(self.theta*np.pi/180)

        if pressed[K_ESCAPE]:
            pygame.quit()
            sys.exit()

            # Thruster! #

        # if pressed[K_LSHIFT]:
        #
        #     myCar.animateflame()
        #     self.fwd = self.fwd*1.02
        #
        #     # Setting Terminal velocity
        #     if self.fwd >= fwdStep*3:
        #         self.fwd = fwdStep*3
        #
        # else:
        #
        #     if self.fwd > fwdStep :
        #         self.fwd = self.fwd*0.98
        #     else:
        #         self.fwd = fwdStep



        #print(self.theta)
        #print('[{},{}]'.format(self.xCoord, self.yCoord))









#####################
# INITIALIZE ASSETS #
#####################

myCar = playerSprite(100,100,'./Sprites/')

#############
# GAME LOOP #
#############

while True:


    DISPLAYSURF.fill(backGndColor)
    myCar.TransformAsset(myCar.carBody)
    #myCar.animateflame()
    #
    # pressed = pygame.key.get_pressed()
    # if pressed[K_UP]:
    myCar.DriveCar(5,5)


    # CONDITIONS FOR EXITING GAME LOOP.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    # UPDATE GRAPHICS AND INDUCE FPS DELAY.
    pygame.display.update()
    fpsClock.tick(FPS)
