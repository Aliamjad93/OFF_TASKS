import pandas as pd

class DataLoader:
    def __init__(self):
        self.movies = pd.read_csv(r'C:\Users\farha\.spyder-py3\Task1\MovieRecommender\db\tmdb_5000_movies.csv')
        self.credits = pd.read_csv(r'C:\Users\farha\.spyder-py3\Task1\MovieRecommender\db\tmdb_5000_credits.csv')
        
dataLoader=DataLoader()
         