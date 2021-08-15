import pygame
from config import *
import random
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("Times New Roman,Arial",24,True)
class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
		self.run = True
		self.player = Player(self.screen)
		self.clock = pygame.time.Clock()
		self.listZombie = []
	def Run(self):
		while self.run:
			self.clock.tick(60)
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					self.run = False
			self.screen.fill((0,255,0))
			self.addZombie()
			self.checkCollision()
			self.player.Controller()
			self.player.Draw()
			
			self.text = myfont.render(str(self.player.score),True,BLACK)
			self.screen.blit(self.text,(0,0))
			pygame.display.update()			
		pygame.display.quit()
	def addZombie(self):
		tmp = 0
		for i in self.listZombie:
			if i.die == True:
				tmp += 1
		if tmp == len(self.listZombie):
			for i in range(1):
				zombie = Zombie(self.screen,random.randrange(0,700),random.randrange(0,500))
				self.listZombie.append(zombie)

	def checkCollision(self):
		for i in self.listZombie:
			if i.die == False:
				if self.player.x + 70 >= i.x and self.player.y +  69 >= i.y and self.player.x + 70 <= i.x + 70 and self.player.y + 69 <= i.y + 70:
					self.player.die = True
				if self.player.x + 70 >= i.x and self.player.x + 70 <= i.x + 70 and self.player.y + 100 >= i.y and self.player.y + 100 <= i.y + 70:
					self.player.die = True
		for i in self.player.ammo:
			if i.posX  > 750 or i.posX < 0:
				self.player.ammo.remove(i)
			if i.posY >550 or i.posY < 0:
				self.player.ammo.remove(i)
		for i in self.listZombie:
			for j in self.player.ammo:
				if len(self.listZombie) > 0:
					if i.die == False:
						if i.left == True:
							if j.posY +5 > i.y and j.posY + 5  < i.y + 69 and j.posX > i.x and j.isRun == True:
								# self.listZombie.remove(i)
								i.die = True
								self.player.score += 1
								self.player.ammo.remove(j)
						elif i.right == True:
							if j.posY +5 > i.y and j.posY + 5  < i.y + 69 and j.posX < i.x and j.isRun == True:
								# self.listZombie.remove(i)
								i.die = True
								self.player.score += 1
								self.player.ammo.remove(j)
						elif i.up == True:
							if j.posX + 5 > i.x and j.posX + 5 < i.x + 70 and j.posY > i.y and j.isRun == True:
								# self.listZombie.remove(i)
								i.die = True
								self.player.score += 1
								self.player.ammo.remove(j)
						elif i.down == True:
							if j.posX + 5 > i.x and j.posX + 5 < i.x + 70 and j.posY < i.y and j.isRun == True:
								# self.listZombie.remove(i)
								i.die = True
								self.player.score += 1
								self.player.ammo.remove(j)
			if len(self.listZombie) > 0:
				i.Draw(self.player.x,self.player.y)
		print(self.player.die)
		print(self.player.score)
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
		self.die = False
		self.score = 0
		# self.bullet = pygame.draw.circle(self.screen,(255,255,255),(self.posX,self.posY))
		for i in range(len(ImageChar)):
			self.image.append(pygame.image.load("images/{}".format(ImageChar[i])))
	def Draw(self):
		if self.fire == True:
			for i in self.ammo:
				i.Draw()
		if self.die == True:
			self.screen.blit(pygame.image.load("images/dead.png"),(self.x,self.y))
		else:	
			self.screen.blit(self.image[self.frame],(self.x,self.y))
	def Controller(self):
		keys = pygame.key.get_pressed()
		if self.die == False:
			if keys[pygame.K_a]:
				self.frame = 0
				self.x -= 5
				# print(1)
				self.setFalse("left")
			elif keys[pygame.K_d]:
				# self.x += 1
				self.frame = 1
				self.x += 5
				self.setFalse("right")
			elif keys[pygame.K_w]:
				self.frame = 2
				self.y -= 5
				self.setFalse("up")
			elif keys[pygame.K_s]:
				self.frame = 3
				self.y += 5
				self.setFalse("down")
			if keys[pygame.K_k]:
				# self.ammo.clear()
				# print(self.right)
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
		# print(tmp[s])
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
		self.left = False
		self.right = False
		self.up = False
		self.down = False
		self.screen = screen
		self.die = False
		for i in range(len(ImageZombie)):
			self.images.append(pygame.image.load("images/{}".format(ImageZombie[i])))
	def Draw(self,cX,cY):
		if self.die == True:
			self.screen.blit(pygame.image.load("images/dead.png"),(self.x,self.y))
		else:
			if self.x < cX:
				self.x += 1
				self.setFalse("right")
				self.screen.blit(self.images[1],(self.x,self.y))
			elif self.y < cY:
				self.y += 1
				self.setFalse("down")
				self.screen.blit(self.images[3],(self.x,self.y))
			elif self.x > cX:
				self.x -= 1
				self.setFalse("left")
				self.screen.blit(self.images[0],(self.x,self.y))
			elif self.y > cY:
				self.y -= 1
				self.setFalse("up")
				self.screen.blit(self.images[2],(self.x,self.y))
		# self.screen.blit(self.images[0],(self.x,self.y))
	def setFalse(self,s:str):
		tmp = {
			"left" : 0,
			"right" : 1,
			"up" : 2,
			"down" : 3
		}
		listCheck = [False,False,False,False]
		listCheck[tmp[s]] = True
		# print(tmp[s])
		self.left = listCheck[0]
		self.right = listCheck[1]
		self.up = listCheck[2]
		self.down = listCheck[3]
class Bullet:
	def __init__(self,screen,x,y,sX,sY):
		self.posX = x
		self.posY = y
		self.sX = sX
		self.sY = sY
		self.screen = screen
		self.isRun = False
	def Draw(self):
		self.isRun = True
		self.posX = self.posX + self.sX
		self.posY = self.posY + self.sY
		pygame.draw.circle(self.screen,(255,255,255),(self.posX,self.posY),5)
game = Game()
game.Run()
