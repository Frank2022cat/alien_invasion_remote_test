class GameStats():
	"""跟踪游戏的统计信息"""

	def __init__(self, ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings
		self.reset_stats()

		# 游戏刚启动时处于非活动状态
		self.game_active = False
		# 在任何情况下都不应重置最高得分
		self.read_high_score()

	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
		
	def read_high_score(self):
		"""加载时读取历史最高分"""
		filename = 'statssave/highscore_save.txt' 
		try:
			with open(filename) as file_object:
				self.high_score = int(file_object.read())
		except FileNotFoundError:
			self.high_score = 0
			
		
	def save_high_score(self):
		"""退出时保存最高分至文件"""
		filename = 'statssave/highscore_save.txt'
		
		with open(filename, 'w') as file_object:
			file_object.write(str(self.high_score))
		
