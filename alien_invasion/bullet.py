import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): #定义子类的时候，父类必须在括号里面。
	"""docstring for Bullet"""
	def __init__(self, ai_settings, screen, ship):

		super(Bullet, self).__init__() #可以使用sprite里面所有的类。
		
		self.screen = screen

		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)

		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		
		self.y -= self.speed_factor

		self.rect.y = self.y

	def draw_bullet(self):
		
		pygame.draw.rect(self.screen, self.color, self.rect)
		