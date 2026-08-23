import pandas as pd

def load_movielens(data_path="data/raw/"):
    # Ratings file (u.data → ratings.csv)
    ratings = pd.read_csv(
        f"{data_path}ratings.csv",
        sep="\t",
        names=["userId", "movieId", "rating", "timestamp"]
    )

    # Movies file (u.item → movies.csv)
    movies = pd.read_csv(
        f"{data_path}movies.csv",
        sep="|",
        encoding="latin-1",
        names=[
            "movieId","title","release_date","video_release_date","IMDb_URL",
            "unknown","Action","Adventure","Animation","Children","Comedy","Crime",
            "Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery",
            "Romance","Sci-Fi","Thriller","War","Western"
        ]
    )

    # Combine binary genre flags into a single text column
    genre_columns = ["unknown","Action","Adventure","Animation","Children","Comedy","Crime",
                     "Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery",
                     "Romance","Sci-Fi","Thriller","War","Western"]

    movies["genres"] = movies[genre_columns].apply(
        lambda row: " ".join([col for col in genre_columns if row[col] == 1]),
        axis=1
    )

    return ratings, movies
