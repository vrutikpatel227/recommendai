import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class CollaborativeRecommender:
    def __init__(self, ratings):
        """
        ratings: DataFrame with columns [userId, movieId, rating]
        """
        self.ratings = ratings
        self.user_movie_matrix = ratings.pivot_table(index="userId", columns="movieId", values="rating").fillna(0)
        self.similarity = cosine_similarity(self.user_movie_matrix)

    def recommend(self, user_id, n=10):
        if user_id not in self.user_movie_matrix.index:
            return []
        user_idx = self.user_movie_matrix.index.get_loc(user_id)
        sim_scores = self.similarity[user_idx]
        similar_users = sim_scores.argsort()[-n-1:-1][::-1]
        recommendations = self.user_movie_matrix.iloc[similar_users].mean().sort_values(ascending=False)
        return recommendations.head(n).to_dict()
