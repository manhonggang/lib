import sys

import pygame

from bullet import Bullet

from alien import Alien

from time import sleep

def get_number_aliens_x(ai_settings, alien_width):
	
	available_space_x = ai_settings.screen_width - 2*alien_width
	number_aliens_x = int(available_space_x/(2*alien_width))
	return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
	
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows


def create_alien(ai_settings, screen, aliens, alien_number,row_number):
	
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width*alien_number # 计算出每个飞船的x位置，并返还给飞船的坐标，循环画出来
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens): #参数顺序很重要
	
	alien = Alien(ai_settings, screen)
	
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	for row_number in range(number_rows):
	
		for alien_number in range(number_aliens_x): #顺带定义了alien_number

			create_alien(ai_settings, screen, aliens, alien_number,row_number)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
	
	if event.key == pygame.K_RIGHT: #按键都应该是平级的。
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	if event.key == pygame.K_DOWN:
		ship.moving_down = True
	if event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_q: #普通按键都是小写
		sys.exit()
	elif event.key == pygame.K_SPACE:

		fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
	
	if len(bullets) < ai_settings.bullet_allowed:
			new_bullet = Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)


def check_keyup_events(event,ship):
	
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
	if event.key == pygame.K_DOWN:
		ship.moving_down = False
	if event.key == pygame.K_UP:
		ship.moving_up = False	


def check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb): #跟船有关，不用再额外设计，直接传正确的值就好了。
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos() #x,y值不需要在上面标记变量的原因主要是因为
			check_play_button(ai_settings, screen, ship, aliens, bullets, stats, play_button,mouse_x, mouse_y, sb)

def check_play_button(ai_settings, screen, ship, aliens, bullets, stats, play_button,mouse_x, mouse_y, sb):
	
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

	if button_clicked and not stats.game_active:
		stats.reset_stats()
		stats.game_active = True
		pygame.mouse.set_visible(False)

		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()

		ai_settings.initialize_dynamic_settings()

		aliens.empty()
		bullets.empty()

		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		ship.bottom_ship()

def update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,sb):

	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()

	sb.show_score()

	aliens.draw(screen)

	if not stats.game_active:

		play_button.draw_button()

	pygame.display.flip() #绘制最近的屏幕

def update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb):
	
	bullets.update()

	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets,stats,sb)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets,stats,sb):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats,sb)

	if len(aliens) == 0:

		bullets.empty()
		ai_settings.increase_speed()
		stats.level += 1
		create_fleet(ai_settings, screen, ship, aliens)

	for bullet in bullets.copy(): # 为什么用副本
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites(): #group里的每个都是精灵。aliens是个group
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship, aliens):
		print("Ship hit!!!")
		ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
	check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
	
	if stats.ships_left > 0:
		stats.ships_left -= 1
		sb.prep_ships()
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

	aliens.empty()
	bullets.empty()

	create_fleet(ai_settings, screen, ship, aliens)
	
	ship.center_ship()
	ship.bottom_ship()

	sleep(0.5)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
	
	screen_rect = screen.get_rect()

	for alien in aliens.sprites():
		
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
			break

def check_high_score(stats, sb):

	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score
	