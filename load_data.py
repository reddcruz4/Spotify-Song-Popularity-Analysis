from pathlib import Path
import pandas as pd
import sqlite3

BASE_DIR = Path(__file__).parent

high = pd.read_csv(BASE_DIR / "high_popularity_spotify_data.csv")
low = pd.read_csv(BASE_DIR / "low_popularity_spotify_data.csv")


# Step 2: Combine them into one dataset
df = pd.concat([high, low], ignore_index=True)

# Step 3: Keep only needed columns
df = df[[
    "track_name",
    "track_artist",
    "track_popularity",
    "danceability",
    "energy",
    "valence",
    "tempo",
    "loudness",
    "playlist_genre"
]]

# Step 4: Connect to SQLite database
conn = sqlite3.connect(BASE_DIR / "spotify.db")

# Step 5: Load data into SQL table
df.to_sql("songs", conn, if_exists="replace", index=False)

# Step 6: Close connection
conn.close()