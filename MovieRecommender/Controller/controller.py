#importing required Modules

from db import dataloader
import pandas as pd
import ast
import nltk
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
import pickle
ps=PorterStemmer()
class collection:
    
    # Merges data from dataloader.dataLoader.movies and dataloader.dataLoader.credits based on the title.
    def merge(self):
        
        self.movies = dataloader.dataLoader.movies.merge(dataloader.dataLoader.credits,on='title')
    
    # Selects only required columns ('movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew') from the merged data.
    def NeededColumns(self):
        self.movies = self.movies[['movie_id','title','overview','genres','keywords','cast','crew']]
        
    # Drops rows with missing values from the data.
    def MissingDrop(self):
        self.movies.dropna(inplace=True)
        
    # Converts text data in a specific format to a list of names.
    def convert(self,text):
        L = []
        for i in ast.literal_eval(text):
            L.append(i['name']) 
        return L
    
    # Applies the convert method to the 'genres' and 'keywords' columns. to fetch only these names
    
    def FetchNameofGenresKeywords(self):
        self.movies['genres'] = self.movies['genres'].apply(self.convert)
        self.movies['keywords'] = self.movies['keywords'].apply(self.convert)
        
    
    # Applies the convert method to the 'cast' column and keeps only the first three names.
    
    def fetchNameofCast(self):
        self.movies['cast'] = self.movies['cast'].apply(self.convert)
        self.movies['cast'] = self.movies['cast'].apply(lambda x:x[0:3])
        
    # Extracts the names of director from a given text 
    
    def fetch_director(self,text):
        L = []
        for i in ast.literal_eval(text):
            if i['job'] == 'Director':
                L.append(i['name'])
        return L 
    
    # Applies the fetch_director method to the 'crew' column.
    def FetchDirectorOnly(self):
        self.movies['crew'] = self.movies['crew'].apply(self.fetch_director)
        
        
        # Removes spaces from a list of strings.
    
    def RemoveSpaceFromColumns(self,L):
        L1 = []
        for i in L:
            L1.append(i.replace(" ",""))
        return L1
    
    # Applies the RemoveSpaceFromColumns method to multiple columns.
    
    def RemovingSpace(self):
        self.movies['cast'] = self.movies['cast'].apply(self.RemoveSpaceFromColumns)
        self.movies['crew'] = self.movies['crew'].apply(self.RemoveSpaceFromColumns)
        self.movies['genres'] = self.movies['genres'].apply(self.RemoveSpaceFromColumns)
        self.movies['keywords'] = self.movies['keywords'].apply(self.RemoveSpaceFromColumns)
    
    
    # Splits the 'overview' text into a list of words.
    def ConvertList(self):
        self.movies['overview'] = self.movies['overview'].apply(lambda x:x.split())
    
        # Merge all the columns into a single Tag column
    def MergeintoTags(self):
        self.movies['tags'] = self.movies['overview'] + self.movies['genres'] + self.movies['keywords'] + self.movies['cast'] + self.movies['crew']
        
    #dropping the other columns except tags and title and id
    def NewData(self):
        self.new = self.movies.drop(columns=['overview','genres','keywords','cast','crew'])
        self.new['tags'] = self.new['tags'].apply(lambda x: " ".join(x))
        
    # convert text into lowercase
        
    def ConvertTagintoLwerForm(self):
        self.new['tags']=self.new['tags'].apply(lambda x:x.lower())
        
    # Getting only one keyword not all keyword whom related to one: Like Love,Loving only will get love
    def strem(self,text):
        y=[]
        for i in text.split():
            y.append(ps.stem(i))
            
        return " ".join(y)
    
    def RemoveRelativeWords(self):
        self.new['tags']=self.new['tags'].apply(self.strem)
        
    # Creating Model Cosine similarity. Firslty convert text into vectors and pass these vectors to cosine which will return 
    # the nearest other movies according to the input value
        
    def CreatingModel(self):
        self.cv = CountVectorizer(max_features=5000,stop_words='english')
        self.vector = self.cv.fit_transform(self.new['tags']).toarray()
        self.similarity = cosine_similarity(self.vector)
        
    #Getting some recommendations
    def Recommend(self,movie):
        self.index = self.new[self.new['title'] == movie].index[0]
        self.distances = sorted(list(enumerate(self.similarity[self.index])),reverse=True,key = lambda x: x[1])
        for i in self.distances[1:6]:
            
            return (self.new.iloc[i[0]].title)
        
        #Saving Model
    def SaveModel(self):
        
        pickle.dump(self.similarity,open(r'C:\Users\farha\.spyder-py3\Task1\MovieRecommender\Controller\similarity.pkl','wb'))
        pickle.dump(self.new.to_dict(),open(r'C:\Users\farha\.spyder-py3\Task1\MovieRecommender\Controller\similarity_dict.pkl','wb'))
        
    # Make Predictions
    def Predict(self,movie):
        self.similarity=pickle.load(open(r'C:\Users\farha\.spyder-py3\Task1\MovieRecommender\Controller\similarity.pkl','rb'))
        self.data=pickle.load(open(r'C:\Users\farha\.spyder-py3\Task1\MovieRecommender\Controller\similarity_dict.pkl','rb'))
        self.NewData=pd.DataFrame(self.data)
        
        self.index = self.NewData[self.NewData['title'] == movie].index[0]
        self.distances = sorted(list(enumerate(self.similarity[self.index])),reverse=True,key = lambda x: x[1])
        
        movies_List=[]
        for i in self.distances[1:6]:
            movies_List.append(self.NewData.iloc[i[0]].title)
            
            
        return movies_List
    # Return All Titles in the dataset
    def Alldata(self):
        self.data=pickle.load(open(r'C:\Users\farha\.spyder-py3\Task1\MovieRecommender\Controller\similarity_dict.pkl','rb'))
        self.NewData=pd.DataFrame(self.data)
        titles = self.NewData['title'].values  # Assuming each item has a 'title' attribute
        Title=[]
        for j in titles:
            Title.append(j)
        return Title
            
        
        
        
        
Controller=collection()



    
    
        

