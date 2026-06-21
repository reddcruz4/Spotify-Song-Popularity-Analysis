import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("spotify.db")

df = pd.read_sql_query(
    "SELECT DISTINCT * FROM songs",
    conn

#SCATTERPLOT
)

conn.close()

plt.scatter(
    df["energy"],
    df["track_popularity"]
)

plt.xlabel("Energy")
plt.ylabel("Popularity")
plt.title("Popularity vs Energy")



# Boxplot
df["pop_group"] = df["track_popularity"].apply(
    lambda x: "High" if x >= 68 else "Low"
)

df.boxplot(
    column="loudness",
    by="pop_group"
)

plt.title("Loudness by Popularity Group")
plt.suptitle("")
plt.show()