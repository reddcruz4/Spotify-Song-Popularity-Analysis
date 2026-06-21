# Spotify-Song-Popularity-Analysis
A mini project data analysis about Spotify Songs and how audio features such as Danceability, Tempo, Energy, Loudness, and Valence affect its popularity.

## Overview

This project investigates whether Spotify audio features are associated with song popularity.

Using SQL and Python, I analyzed a Spotify dataset containing thousands of songs and compared audio characteristics such as danceability, energy, valence, tempo, and loudness against popularity scores.

The goal was to determine whether certain musical characteristics are common and determining factors among highly popular songs.

## Research Question

What audio features are associated with Spotify song popularity?

Specifically:

- Are popular songs more danceable?
- Are popular songs more energetic?
- Does loudness influence popularity?
- Does tempo influence popularity?
- Are happier songs more popular?


## Dataset

Source:
https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset

The dataset contains:

- Track Name
- Artist
- Popularity Score
- Danceability
- Energy
- Valence
- Tempo
- Loudness
- Genre

## Techstack

- Python
- Pandas
- SQLite
- Matplotlib
- DB Browser for SQLite

## Methodology

1. Loaded Spotify CSV datasets into SQLite.
2. Removed duplicate songs using SQL DISTINCT.
3. Compared high-popularity and low-popularity songs.
4. Performed genre-level analysis.
5. Calculated correlations between popularity and audio features.
6. Created scatter plots and boxplots to visualize relationships.

## Key Findings

### Correlation with Popularity

| Feature | Correlation |
|----------|------------|
| Loudness | 0.211 |
| Energy | 0.187 |
| Danceability | 0.128 |
| Valence | 0.093 |
| Tempo | 0.059 |

### Observations

- Loudness showed the strongest relationship with popularity but was considerably weak.
- Energy and danceability had weak positive relationships.
- Tempo and valence showed little relationship with popularity.
- No single audio feature strongly explained and determined the popularity of a song.


## Visualizations

### Popularity vs Loudness

![Loudness Scatter Plot](images/popularity_vs_loudness.png)

### Popularity vs Energy

![Loudness Scatter Plot](images/popularity_vs_energy.png)

### Loudness Distribution by Popularity Group

![Loudness Boxplot](images/loudness_by_popularity.png)


## Conclusion

The analysis found that audio features have only weak correlations with popularity. Loudness showed the strongest relationship, although the correlation remained low (0.21). Visualization revealed that highly popular songs tend to concentrate within a relatively narrow loudness range, whereas less popular songs exhibit a significantly greater variation. This suggests that popularity is associated not only with louder production, but also with greater standardization of audio characteristics. However, the weak correlations indicate that factors beyond the audio features in the dataset likely play a larger role in determining popularity. 

## Future Improvements

- Apply machine learning models to predict popularity.
- Perform clustering analysis on songs.
- Investigate artist popularity effects.
- Analyze trends by release year.



## What I Learned

- Importing and cleaning datasets using Pandas
- Loading data into SQLite
- Writing SQL aggregation queries
- Performing correlation analysis
- Creating visualizations with Matplotlib
- Interpreting statistical results critically
