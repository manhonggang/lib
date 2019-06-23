import sys

import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from alien import Alien

from game_stats import GameStats 

from button import Button 

from scoreboard import Scoreboard 

def run_game():
	
	pygame.init() #初始化模块

	ai_settings = Settings() #把设置里的内容作为一个变量引入

	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	
	pygame.display.set_caption("Alien Invasion")

	stats = GameStats(ai_settings)

	sb = Scoreboard(ai_settings, screen, stats)

	play_button = Button(ai_settings, screen, "Play")

	ship = Ship(ai_settings, screen)

	alien = Alien(ai_settings, screen)

	bullets = Group()

	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)

	while True:
		gf.check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb)	
		gf.update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,sb)
		if stats.game_active:
			ship.update()
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)

run_game()