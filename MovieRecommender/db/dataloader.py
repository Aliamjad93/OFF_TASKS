# Import the pandas library and alias it as 'pd'
import pandas as pd

# Define a class for loading data
class DataLoader:
    def __init__(self):
        # Initialize the class by reading two CSV files into DataFrames

        # Load movie data from a CSV file into a 'movies' DataFrame
        self.movies = pd.read_csv(r'C:\Users\farha\.spyder-py3\Task1\MovieRecommender\db\tmdb_5000_movies.csv')
        
        # Load credits data from a CSV file into a 'credits' DataFrame
        self.credits = pd.read_csv(r'C:\Users\farha\.spyder-py3\Task1\MovieRecommender\db\tmdb_5000_credits.csv')

# Create an instance of the 'DataLoader' class to load data into DataFrames
dataLoader = DataLoader()
