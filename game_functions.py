import pygame, sys
from bullet import Bullet
from alien import Alien
from time import sleep


def Key_up(ship, event):

    #When the button is released, change the flag back to false to stop moving.
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def Key_down(ship, event, bullet_group, screen, game_settings):

    # When the button is pressed, change the flag to True to continuously move the spacecraft
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True 

    if event.key == pygame.K_SPACE:
        lunch_bullet(bullet_group, game_settings, screen, ship)


def check_mouse_key_events(ship, screen, bullet_group, game_settings):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()

        elif ev.type == pygame.KEYDOWN:
            Key_down(ship, ev, bullet_group, screen, game_settings)
        elif ev.type == pygame.KEYUP:
            Key_up(ship, ev)     

def update_screen(screen, ship, game_settings, bullet_group, alien_group):
    screen.fill(game_settings.bg_color)

    ship.moving_ship()
    ship.display_ship()

    alien_group.draw(screen)

    update_bullet(bullet_group, alien_group)

    check_collisions(ship, alien_group, game_settings, screen, bullet_group)

    #If there is no more Alien than create again.
    if len(alien_group) == 0:  
        bullet_group.empty()
        create_alien_group(game_settings, screen, alien_group, ship, bullet_group)

    alien_group.update()

    # Update every thing on the screen
    pygame.display.flip()




def check_collisions(ship, alien_group, game_settings, screen, bullet_group):
    if pygame.sprite.spritecollideany(ship, alien_group):
        alien_group.empty()
        if len(alien_group) == 0:
            game_reset(ship, game_settings, screen, alien_group, bullet_group)
            
def game_reset(ship, game_settings, screen, alien_group, bullet_group):
    bullet_group.empty()
    ship.position = game_settings.WINDOW_WIDTH//2
    create_alien_group(game_settings, screen, alien_group, ship, bullet_group)

# get aliens in one row(获取一行能放下多少外星人)
def get_aliens_in_a_row(game_settings, alien_width):
    # calculate the available space for x coordinate, which you subtract two alien from each end.
    available_space_x = game_settings.WINDOW_WIDTH - 2 * alien_width
    # calculate the number of aliens, which one alien should be remove between two aliens. 
    alien_number = available_space_x // (2 * alien_width)
    return alien_number

#get alien numbers in more rows(获取多行能放下多少外星人)
def get_aliens_in_more_rows(game_settings, ship, alien_height):
    # calculate the available space for y coordinate
    available_space_y = game_settings.WINDOW_HEIGHT - (alien_height * 3 + ship.rect.height)
    # calculate the available rows in the screen, which is the same way as before.  
    alien_rows = available_space_y // (2 * alien_height)
    return alien_rows

#create alien to alien group every single time when column number 76 and 77 calls him(创建一个外星人当第76和第77行呼叫他的时候)
def create_alien(screen, game_settings, alien_group, alien_width, alien_num, alien_height, alien_r, bullet_group, ship):
    # calculate the space between the alien which is 2 * alien_width * alien_num(第几个)
    alien_position_x = alien_width + 2 * alien_width * alien_num
    # calculate the space between aliens in y coordinate using the same method as x.
    alien_position_y = alien_height + alien_r * (2 * alien_height)
    
    alien = Alien(screen, alien_group, game_settings, alien_position_x, alien_position_y, bullet_group, ship)

    alien_group.add(alien)
    

def create_alien_group(game_settings, screen, alien_group, ship, bullet_group):
    # get alien's width and height 
    alien = Alien(screen, alien_group, game_settings, alien_position_x = 0, alien_position_y = 0, bullet_group = bullet_group, ship = ship)
    # alien_width and alien_height 是固定值
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien_number = get_aliens_in_a_row(game_settings, alien_width)
    alien_rows = get_aliens_in_more_rows(game_settings, ship, alien_height)
    for alien_r in range(alien_rows):
        for alien_num in range(alien_number):
            create_alien(screen, game_settings, alien_group, alien_width, alien_num, alien_height, alien_r, bullet_group, ship)

        
def lunch_bullet(bullet_group, game_settings, screen, ship):
    # give the user a limit for lunching bullets
    if len(bullet_group) < game_settings.bullet_num_allowed:
        bullet_group.add(Bullet(screen, ship, game_settings))

def update_bullet(bullet_group, alien_group):
    for bullet in bullet_group.sprites():
        bullet.draw_bullet()
        bullet.display_bullet()
        pygame.sprite.groupcollide(bullet_group, alien_group, True, True)
        
    # bullet remove after it got out of the screen   
    for bullet in bullet_group.copy():
        if bullet.rect.bottom <= 0:
            bullet_group.remove(bullet)