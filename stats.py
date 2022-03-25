class Stats():
    """отслеживание статистики"""
    
    def __init__(self):
        """иницилизирует статистику"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())
        
        
    def reset_stats(self):
        """стистика изменяющаяся во времуя игнры"""
        
        self.guns_left = 2
        self.score = 0