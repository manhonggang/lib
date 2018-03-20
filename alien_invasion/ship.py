import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
	"""docstring for Ship"""
	def __init__(self, ai_settings, screen):
		
		super(Ship, self).__init__()

		self.screen = screen #跟屏幕有关，所以

		self.ai_settings = ai_settings #把外面的设置引入到船里面来，然后变成船的变量一部分，在调用变量里的一部分。

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect() #获取图像的矩形
		self.screen_rect = screen.get_rect() #获取屏幕的矩形,把这个信息带进来，以后有用。

		self.rect.centerx = self.screen_rect.centerx #把屏幕中心位置赋给飞船中心位置
		self.rect.bottom = self.screen_rect.bottom #把屏幕底部位置赋给飞船底部位置

		self.center = float(self.rect.centerx)

		self.bottom = float(self.rect.bottom)
		
		self.moving_right = False # 默认静止的时候为假。
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		
		if self.moving_right and self.rect.right < self.screen_rect.right:#如果为真，则执行下面的向右移动。
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.bottom -= self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center #更新自身的中心位置
		self.rect.bottom = self.bottom #更新自身底部位置		

	def blitme(self):

		self.screen.blit(self.image, self.rect) #把ship的图片load到rect的位置。

	def center_ship(self):
		
		self.center = self.screen_rect.centerx

	def bottom_ship(self):
		
		self.bottom = self.screen_rect.bottom