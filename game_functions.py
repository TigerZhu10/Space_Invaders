import pygame, sys
from bullet import Bullet
from alien import Alien
from time import sleep


reset_numbers = 3

def Key_up(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def Key_down(ship, event, bullet_group, screen, game_settings):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True 

    if event.key == pygame.K_SPACE:
        lunch_bullet(bullet_group, game_settings, screen, ship)

def check_mouse_key_events(ship, screen, bullet_group, game_settings, button):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()

        elif ev.type == pygame.KEYDOWN and game_settings.game_active:
            Key_down(ship, ev, bullet_group, screen, game_settings)
        elif ev.type == pygame.KEYUP and game_settings.game_active: 
            Key_up(ship, ev)
        # if click the button down, get a position of the mouse cursor where 
        # mouse_x is the x coordinate of the mouse... And then check if the mouse is click on the area of the button
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button.rect.collidepoint(mouse_x, mouse_y):
                game_settings.game_active = True

def update_screen(screen, ship, game_settings, bullet_group, alien_group, button, score, lives, round):
    screen.fill(game_settings.bg_color)
    
    if game_settings.game_active:
        ship.moving_ship()
        ship.display_ship()

        alien_group.draw(screen)
        alien_group.update()
        
        update_bullet(bullet_group, alien_group)
        check_collisions(ship, alien_group, game_settings, screen, bullet_group, lives)
        check_bullet_alien_collisions(bullet_group, alien_group, score, game_settings, screen, ship)

        score.display_score()
        lives.display_lives()
        round.display_round()
        
    else:
        button.draw_buttons()
        button.display_text()
    
    pygame.display.flip()

def check_bullet_alien_collisions(bullet_group, alien_group, score, game_settings, screen, ship):
    collisions = pygame.sprite.groupcollide(bullet_group, alien_group, True, True)
    if collisions:
        game_settings.score += 50
        score.display_score()
    # When you kill all the aliens then recreate alien group
    if len(alien_group) == 0:  
        bullet_group.empty()
        create_alien_group(game_settings, screen, alien_group, ship, bullet_group)
        speed_increase(game_settings)
    
        
def check_collisions(ship, alien_group, game_settings, screen, bullet_group, lives):
    # When the ship hit the alien you lose a life and reset the game
    if pygame.sprite.spritecollideany(ship, alien_group):
        alien_group.empty()
        # game_settings.reset_number -= 1
        game_settings.lives -= 1
        lives.display_lives()
        if len(alien_group) == 0:
            game_reset(ship, game_settings, screen, alien_group, bullet_group)

def game_reset(ship, game_settings, screen, alien_group, bullet_group):
    bullet_group.empty()
    ship.position = game_settings.WINDOW_WIDTH // 2
    create_alien_group(game_settings, screen, alien_group, ship, bullet_group)
    # if you die 3 times than you reset the game and display the button again
    if game_settings.lives <= 0:
        game_settings.game_active = False
        game_settings.lives = 3
        game_settings.score = 0

# change the speed everytime when you kill one group of alien
def speed_increase(game_settings):
    game_settings.alien_velocity *= 1.1
    game_settings.alien_drop_speed *= 1.1
    game_settings.bullet_velocity *= 1.1
    game_settings.ship_velocity *= 1.1




def get_aliens_in_a_row(game_settings, alien_width):
    available_space_x = game_settings.WINDOW_WIDTH - 2 * alien_width
    alien_number = available_space_x // (2 * alien_width)
    return alien_number

def get_aliens_in_more_rows(game_settings, ship, alien_height):
    available_space_y = game_settings.WINDOW_HEIGHT - (alien_height * 3 + ship.rect.height)
    alien_rows = available_space_y // (2 * alien_height)
    return alien_rows

def create_alien(screen, game_settings, alien_group, alien_width, alien_num, alien_height, alien_r, bullet_group, ship):
    alien_position_x = alien_width + 2 * alien_width * alien_num
    alien_position_y = alien_height + alien_r * (2 * alien_height)
    
    alien = Alien(screen, alien_group, game_settings, alien_position_x, alien_position_y, bullet_group, ship)
    alien_group.add(alien)
    
def create_alien_group(game_settings, screen, alien_group, ship, bullet_group):
    alien = Alien(screen, alien_group, game_settings, alien_position_x=0, alien_position_y=0, bullet_group=bullet_group, ship=ship)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien_number = get_aliens_in_a_row(game_settings, alien_width)
    alien_rows = get_aliens_in_more_rows(game_settings, ship, alien_height)
    for alien_r in range(alien_rows):
        for alien_num in range(alien_number):
            create_alien(screen, game_settings, alien_group, alien_width, alien_num, alien_height, alien_r, bullet_group, ship)

def lunch_bullet(bullet_group, game_settings, screen, ship):
    if len(bullet_group) < game_settings.bullet_num_allowed:
        bullet_group.add(Bullet(screen, ship, game_settings))

def update_bullet(bullet_group, alien_group):
    for bullet in bullet_group.sprites():
        bullet.draw_bullet()
        bullet.display_bullet()
        
    for bullet in bullet_group.copy():
        if bullet.rect.bottom <= 0:
            bullet_group.remove(bullet)
