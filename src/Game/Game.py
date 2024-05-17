import pygame
import sys
from src.HardwareManagement import PhoneManager
import src.Game.Levels as L


class Game:
	def __init__(self, screen: pygame.surface.Surface):
		self.screen = screen
		self.clock = pygame.time.Clock()
		
		self.phone_manager = PhoneManager()
		
		self.levels: [L.Level] = [" ", " ", " "]
		self.current_level_index = 0
		
	def start(self):
		self.tutorial_loop()
		self.main_loop()
	
	def tutorial_loop(self):
		print("Tutorial Loop")
		# self.phone_manager.ring("A")
	
	def main_loop(self):
		print("Main Loop")
		# pygame.mixer.stop()
		# self.BACKGROUND_MUSIC.play(1)
		while True:
			self.manage_input()
			self.update()
			
			if self.player_has_lost() or self.current_level_index > len(self.levels):
				break
				
			self.clock.tick(30)  # Frame-Rate
		self.game_over()
	
	def manage_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				
		self.phone_manager.get_dialed_number()
		
	def update(self):
		pass
	
	def game_over(self):
		print("Game Over")

	def player_has_lost(self):
		return False
