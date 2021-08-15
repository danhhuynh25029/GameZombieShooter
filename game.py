import pygame
from config import *
pygame.init()

class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
		self.run = True
		self.player = Player(self.screen)
		self.clock = pygame.time.Clock()
		self.zombie = Zombie(self.screen,100,200) 
	def Run(self):
		while self.run:
			self.clock.tick(60)
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					self.run = False
			self.screen.fill((0,0,0))
			self.player.Controller()
			self.player.Draw()
			self.zombie.Draw()
			pygame.display.update()
			
		pygame.display.quit()
class Player:
	def __init__(self,screen):
		self.x = WIN_WIDTH // 2
		self.y = WIN_HEIGHT //2
		self.image = []
		self.frame = 1
		self.ammo = []
		self.screen = screen
		self.posX = self.x
		self.posY = self.y
		self.fire = False
		self.left = False
		self.right = True
		self.up = False
		self.down = False
		# self.bullet = pygame.draw.circle(self.screen,(255,255,255),(self.posX,self.posY))
		for i in range(len(ImageChar)):
			self.image.append(pygame.image.load("images/{}".format(ImageChar[i])))
	def Draw(self):
		if self.fire == True:
			for i in self.ammo:
				i.draw()
		self.screen.blit(self.image[self.frame],(self.x,self.y))
	def Controller(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.frame = 0
			self.x -= 1
			# print(1)
			self.setFalse("left")
		elif keys[pygame.K_d]:
			# self.x += 1
			self.frame = 1
			self.x += 1
			self.setFalse("right")
		elif keys[pygame.K_w]:
			self.frame = 2
			self.y -= 1
			self.setFalse("up")
		elif keys[pygame.K_s]:
			self.frame = 3
			self.y += 1
			self.setFalse("down")
		if keys[pygame.K_k]:
			# self.ammo.clear()
			print(self.right)
			self.fire = True
			for i in range(1):
				if self.left == True:
					self.ammo.append(Bullet(self.screen,self.x,self.y+36,-10,0))
				if self.right == True:
					self.ammo.append(Bullet(self.screen,self.x+100,self.y+36,10,0))
				if self.up == True:
					self.ammo.append(Bullet(self.screen,self.x+38,self.y,0,-10))
				if self.down == True:
					self.ammo.append(Bullet(self.screen,self.x+38,self.y+100,0,10))
	def setFalse(self,s:str):
		tmp = {
		"left" : 0,
		"right" : 1,
		"up" : 2,
		"down" : 3
		}
		listCheck = [False,False,False,False]
		listCheck[tmp[s]] = True
		print(tmp[s])
		self.left = listCheck[0]
		self.right = listCheck[1]
		self.up = listCheck[2]
		self.down = listCheck[3]
		# print(self.frame)
	# def DrawBullet(self):
	# 	pygame.draw.circle(self.screen,(255,255,255),(self.posX+1,self.posY),30)
class Zombie:
	def __init__(self,screen,x,y):
		self.x = x
		self.y = y
		self.images = []
		self.screen = screen
		for i in range(len(ImageZombie)):
			self.images.append(pygame.image.load("images/{}".format(ImageZombie[i])))
	def Draw(self):
		self.screen.blit(self.images[0],(self.x,self.y))

class Bullet:
	def __init__(self,screen,x,y,sX,sY):
		self.posX = x
		self.posY = y
		self.sX = sX
		self.sY = sY
		self.screen = screen
	def draw(self):
		self.posX = self.posX + self.sX
		self.posY = self.posY + self.sY
		pygame.draw.circle(self.screen,(255,255,255),(self.posX,self.posY),5)
game = Game()
game.Run()
