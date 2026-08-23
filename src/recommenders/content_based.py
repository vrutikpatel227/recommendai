from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentRecommender:
    def __init__(self, movies):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(movies["genres"])
        self.movies = movies

    def get_similar_movies(self, movie_id, n=10):
        idx = self.movies.index[self.movies["movieId"] == movie_id][0]
        sim_scores = cosine_similarity(self.tfidf_matrix[idx], self.tfidf_matrix).flatten()
        top_indices = sim_scores.argsort()[-n-1:-1][::-1]
        return self.movies.iloc[top_indices]
