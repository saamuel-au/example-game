import pygame
from settings import Settings
from button import Button
from player import Player
from bubble import Bubble
from scoreboard import Scoreboard
from game_stats import GameStats
import game_functions as gf
def run_game():
    pygame.init()
    gm_settings = Settings()
    
    #Set up drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)
    
    play_button = Button(gm_settings, screen, "Play")
    
    stats = GameStats()
    
    sb = Scoreboard(gm_settings, screen, stats)
    
    clock = pygame.time.Clock()
    
    # Institate a player
    player = Player(screen)
    
    # Creates groups to hold bubbles
    bubbles = pygame.sprite.Group()
    
    # Run until user asks to quit
    while True:
        gf.check_events(gm_settings, screen, player, bubbles, stats, play_button)
        if stats.game_active:
            player.update()
            gf.update_bubbles(player, bubbles, stats, sb)
            gf.update_bubbles(player, bubbles, stats, sb, gm_settings)
            bubbles.update()
        else:
            bubbles.empty()
