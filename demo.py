from src.data.loader import load_movielens
from src.preprocessing.cleaner import preprocess
from src.recommenders.content_based import ContentRecommender
from src.recommenders.collaborative import CollaborativeRecommender
from src.recommenders.hybrid import HybridRecommender

# Load dataset
ratings, movies = load_movielens("data/raw/")

# Preprocess ratings
ratings_clean = preprocess(ratings)

# Content-based recommender
content_model = ContentRecommender(movies[["movieId", "title", "genres"]])
print("\n🎬 Content-based similar movies to Toy Story:")
print(content_model.get_similar_movies(movie_id=1, n=5))

# Collaborative recommender
collab_model = CollaborativeRecommender(ratings_clean[["userId", "movieId", "rating"]])
print("\n👥 Collaborative recommendations for user 1:")
print(collab_model.recommend(user_id=1, n=5))

# Hybrid recommender
hybrid_model = HybridRecommender(content_model, collab_model)
print("\n⚡ Hybrid recommendations for user 1:")
print(hybrid_model.recommend(user_id=1, n=5))

def id_to_title(movie_ids, movies):
    return movies[movies["movieId"].isin(movie_ids)][["movieId", "title"]]

# Collaborative recommendations
collab_recs = collab_model.recommend(user_id=1, n=5)
print("\n👥 Collaborative recommendations for user 1:")
print(id_to_title(list(collab_recs.keys()), movies))

# Hybrid recommendations
hybrid_recs = hybrid_model.recommend(user_id=1, n=5)
print("\n⚡ Hybrid recommendations for user 1:")
print(id_to_title([m[0] for m in hybrid_recs], movies))
