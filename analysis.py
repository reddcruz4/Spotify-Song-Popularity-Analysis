import sqlite3
import pandas as pd

conn = sqlite3.connect("spotify.db")

df = pd.read_sql_query(
    "SELECT DISTINCT * FROM songs",
    conn
)

conn.close()

features = df[
    [
        "track_popularity",
        "danceability",
        "energy",
        "valence",
        "tempo",
        "loudness"
    ]
]

corr = features.corr()

print(corr)