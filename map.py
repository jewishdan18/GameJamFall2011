from __future__ import division
import math, random, os
import pygame

from item import Item


corner_image          = pygame.image.load(os.path.join("Art","wallcorner.png"))
side_image            = pygame.image.load(os.path.join("Art","wallside.png"))
floor_image           = pygame.image.load(os.path.join("Art","floortile.png"))
shelf_image           = pygame.image.load(os.path.join("Art","shelf.png"))
red_floor_image       = pygame.image.load(os.path.join("Art","tile_red.png"))
green_floor_image     = pygame.image.load(os.path.join("Art","tile_green.png"))
blue_floor_image      = pygame.image.load(os.path.join("Art","tile_blue.png"))
purple_floor_image    = pygame.image.load(os.path.join("Art","tile_purple.png"))
yellow_floor_image    = pygame.image.load(os.path.join("Art","tile_yellow.png"))

images = {
          0.1 :                          corner_image,
          0.2 : pygame.transform.rotate( corner_image, 90 ),
          0.3 : pygame.transform.rotate( corner_image, 180 ),
          0.4 : pygame.transform.rotate( corner_image, 270 ),
          
          1.1 :                          side_image,
          1.2 : pygame.transform.rotate( side_image, 90 ),
          1.3 : pygame.transform.rotate( side_image, 180 ),
          1.4 : pygame.transform.rotate( side_image, 270 ),
          
          2.1 : green_floor_image,
          2.2 : red_floor_image,
          2.3 : blue_floor_image,
          2.4 : yellow_floor_image,
          2.5 : purple_floor_image,
          
          3.1 : shelf_image,
          3.2 : shelf_image,
          3.3 : shelf_image,
          3.4 : shelf_image
        }
        
shelf_maps = [
              [
                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.2, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.3, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.4, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0, 3.1, 0.0, 0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,3.1 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ],
                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ]
              ]
            ]


maps = [
        [
          [ 0.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1 ,1.1 ,1.1 ,1.1 ,1.1 ,1.1 ,1.1 ,1.1 ,1.1 ,1.1 ,1.1 ,1.1 ,1.1 ,0.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 1.4, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,2.1 ,1.2 ],
          [ 0.4, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3 ,1.3 ,1.3 ,1.3 ,1.3 ,1.3 ,1.3 ,1.3 ,1.3 ,1.3 ,1.3 ,1.3 ,1.3 ,0.3 ]
        ]
      ]
          
    
def generateFloor(num_points,xLim,yLim):
  m = {}
  queue = []
  pos = 0
  for i in range(num_points):
    p = (random.randint(0,xLim-1),random.randint(0,yLim-1) )
    while p in queue:
      p = (random.randint(0,xLim-1),random.randint(0,yLim-1) )
    queue.append( (p,i) )
  while pos < len(queue):
    (x,y),c = queue[pos]
    if (x,y) in m:
      pos += 1
      continue
    m[ (x,y) ] = c
    if (x+1,y) not in queue and (x+1,y) not in m and x+1 < xLim:
      queue.append( ((x+1,y), c) )
    if (x-1,y) not in queue and (x-1,y) not in m and x-1 >= 0:
      queue.append( ((x-1,y), c) )
    if (x,y+1) not in queue and (x,y+1) not in m and y+1 < yLim:
      queue.append( ((x,y+1), c) )
    if (x,y-1) not in queue and (x,y-1) not in m and y-1 >= 0:
      queue.append( ((x,y-1), c) )
  return m

def floorPatternToKey(n):
  if n == 0:
    return 2.1
  if n == 1:
    return 2.2
  if n == 2:
    return 2.3
  if n == 3:
    return 2.4
  if n == 4:
    return 2.5



class Map:
  
  def __init__(self, level):
    #self.tiles = maps[level]
    self.shelves = shelf_maps[level]
    self.tiles = {}
    floor_pattern = generateFloor(20,25,25)
    for x in range(25):
      self.tiles[x]={}
      for y in range(25):
        
        if   x is 0 and y is 0:
          self.tiles[x][y] = 0.1
        elif x is 0 and y is 24:
          self.tiles[x][y] = 0.2
        elif x is 0:
          self.tiles[x][y] = 1.1
        
        elif x is 24 and y is 0:
          self.tiles[x][y] = 0.4
        elif x is 24 and y is 24:
          self.tiles[x][y] = 0.3
        elif x is 24:
          self.tiles[x][y] = 1.3
        
        elif y is 0:
          self.tiles[x][y] = 1.4
        elif y is 24:
          self.tiles[x][y] = 1.2
        else:
          self.tiles[x][y] = floorPatternToKey(floor_pattern[ (x,y) ]%5 ) 
    
    self.items = {}
    for x in range(25):
      for y in range(25):
        if   self.shelves[x][y] == 3.2:
          self.items[ (x,y) ] = Item(0)
        elif self.shelves[x][y] == 3.3:
          self.items[ (x,y) ] = Item(1)
        elif self.shelves[x][y] == 3.4:
          self.items[ (x,y) ] = Item(2)
    
  def walkable(self,x,y,color):
    return int(self.tiles[x][y]) == 2 and self.shelves[x][y] == 0.0
  
  def hit(self,x,y):
    if not (x,y) in self.items:
      return -1
    dead = self.items[ (x,y) ].hit()
    if not dead:
      return -1
    return self.items[ (x,y) ].color
        
  
  def getShelfImage(self,x,y):
    if self.shelves[x][y] != 0.0:
      return images[self.shelves[x][y]]
    return None
    
  def getTileImage(self,x,y):
    return images[self.tiles[x][y]]
    
  def getDrawPos(self,x,y):
    return (x*40,y*40)
    
  def draw(self,screen):
    for x in range(25):
      for y in range(25):
        screen.blit(self.getTileImage(x,y),self.getDrawPos(x,y))
        shelf_image = self.getShelfImage(x,y)
        if shelf_image:
          screen.blit(shelf_image,self.getDrawPos(x,y))
        if (x,y) in self.items:
          self.items[ (x,y) ].draw(screen, (x*40,y*40) )
          
  