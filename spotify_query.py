import pandas as pd
import spotipy
from spotipy import util
import numpy as np
from sys import exit

username = "bramochsendorf"

# This script queries the Spotify API and return the top tracks of a given music genre within a specific timeframe
def _get_features_df(sp, track_ids):
    """
    Get track features and return a pandas dataframe
    """

    feature_list = []
    i = 0
    while track_ids:
        print("Audio features #{}".format(i + 1))
        features_results = sp.audio_features(track_ids[:limit])

        feature_list += features_results
        
        track_ids = track_ids[limit:]
        i += 1

    df_features = pd.DataFrame(feature_list)[["id", "analysis_url", "duration_ms", "acousticness", "danceability", 
                                              "energy", "instrumentalness", "liveness", "loudness", "valence", 
                                              "speechiness", "key", "mode", "tempo", "time_signature"]]

    return df_features

# Get token
scope = 'playlist-modify-public'
spotify_token = util.prompt_for_user_token(username, scope)

# Create client
sp = spotipy.Spotify(auth=spotify_token)

# Spotify API limit
limit = 50
number_of_tracks = 500

# Define amount of API queries
runs = int(number_of_tracks/limit)

# Open lists
search_list = []
release_list = []

# Define timeframe (here: 1980, 2017) to query tracks
year_ = np.arange(1980,2017,1)
years = year_.astype(str)

# Now loop over years. Define the music genre here, use the offset parameter to go down the list of results
for year in years:
    num = 0
    for i in range(runs):
        print("Tracks #{}".format(i + 1))
        search_results = sp.search(q='genre:house year:'+year, type="track", limit=limit, offset=limit*i)
        
        for t in search_results['tracks']['items']:
            num = len(search_results['tracks']['items'])
            search_list += [[t["id"], t["name"], t["artists"][0]["id"], t["artists"][0]["name"], t["album"]["id"], t["popularity"],sp.album(t["album"]["id"])['release_date'][0:4]]]
    
    # Save to pandas dataframe; add normalized popularity            
    df_search = pd.DataFrame(search_list, columns=["id", "song_name", "artist_id", "artist_name", "album_name", "popularity","release_year"])
    df_search["popularity_norm"] = df_search["popularity"] / 100.
    track_ids = df_search["id"].unique().tolist()
    
    # check if we found some results, if not we skip the feature finding.
    if num > 0:
        df_features = _get_features_df(sp, track_ids)

# option to save 
# df_search.to_pickle('data/deep_house_'+year)
# df_features.to_pickle('data/deep_house_features_'+year)