import engine.stage as stage
import pygame
import spriteManager
import settingsManager
import os

def getStage():
    return Arena()

def getStageName():
    return "Arena"

def getStageIcon():
    return spriteManager.ImageSprite(os.path.join(os.path.dirname(__file__).replace('main.exe',''),"sprites","icon_treehouse.png"))

def getStagePreview():
    return None

def getMusicList():
    return [(settingsManager.createPath('music/Laszlo - Fall To Light.ogg'),1,"Laszlo - Fall To Light (NCS Release)"),
            (settingsManager.createPath('music/Autumn Warriors.ogg'),1,"Autumn Warriors")]

class Arena(stage.Stage):
    def __init__(self):
        stage.Stage.__init__(self)
        
        self.size = pygame.Rect(0,0,2160,1440)
        self.camera_maximum = pygame.Rect(48,32,2064,1376)
        self.blast_line = pygame.Rect(0,0,2160,1440)
        
        self.platform_list = [stage.Platform([self.size.centerx - 230,self.size.bottom-318], [self.size.centerx + 230,self.size.bottom-318],(True,True)),
                              stage.PassthroughPlatform([self.size.centerx - 540,self.size.bottom-434], [self.size.centerx - 348,self.size.bottom-434],(True,False)),
                              stage.PassthroughPlatform([self.size.centerx + 347,self.size.bottom-434], [self.size.centerx + 539,self.size.bottom-434],(False,True))
                              
                              ]
        
        
        self.spawn_locations = [[self.size.centerx - 77,1121],
                               [self.size.centerx + 153,1121],
                               [self.size.centerx - 445,1005],
                               [self.size.centerx + 445,1005]]
        
        
        bg_sprite = spriteManager.ImageSprite(os.path.join(os.path.dirname(__file__).replace('main.exe',''),"sprites","TreeHouseBack.png"))
        bg_sprite.rect.midbottom = self.size.midbottom
        self.addToBackground(bg_sprite)
        
        fg_sprite = spriteManager.ImageSprite(os.path.join(os.path.dirname(__file__).replace('main.exe',''),"sprites","TreeHouseFront.png"))
        fg_sprite.rect.midbottom = self.size.midbottom
        self.foreground_sprites.append(fg_sprite)
        
        
        self.getLedges()
