class HybridRecommender:
    def __init__(self, content_model, collab_model, content_weight=0.5, collab_weight=0.5):
        self.content_model = content_model
        self.collab_model = collab_model
        self.content_weight = content_weight
        self.collab_weight = collab_weight

    def recommend(self, user_id, n=10):
        collab_scores = self.collab_model.recommend(user_id, n)
        content_scores = {}  # placeholder until linked with content model

        hybrid_scores = {}
        for movie, score in collab_scores.items():
            hybrid_scores[movie] = self.collab_weight * score + self.content_weight * content_scores.get(movie, 0)

        return sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)[:n]
