# The evolution of house, techno, and electro music.

When I moved to Amsterdam (~2005) I discovered electronic music. Particularly popular in the Amsterdam club scene during that time was Electro/Electro House (because of the likes of Boys Noize, Tiefschwarz, Digitalism, Justice, MSTRKRFT etc.), which was followed up by waves of Minimal, Tech House, Dub Step, Deep House, you name it. 

Looking back, it strikes me how fast these particular music genres went in and out of fashion, as there are major differences between e.g. Electro and Deephouse (although this may not appear so obvious to the untrained ear). To see what may drive particular mood-swings in the electronic music scene I explored how different genres of electronic music have evolved over time. Which music characteristics determine how popular (or 'mainstream') a given genre is (and will be)? 

## Conclusion ##
My main conclusion is that popular electronic music is becoming louder, not particular danceable, and full of negative energy. Therefore, a good bet for record labels or aspiring DJs is to produce ear-splitting house/techno tracks (as exemplified by the popularity of artists like, e.g., Skrillex). Be sure to warn your neighbors beforehand, though. 

## Analysis ## 
To come to this interesting conclusion, I queried the Spotify API to obtain tracks of a given music genre during the 1980-2016 timespan. For every track, I use the following metrics:

(1) Popularity --> parameterized from 0 (least popular) to 1 (most popular). Based on Spotify's magic algorithm (read: black box) on total playcount and how recent these are 

(2) Tempo --> in Beats Per Minute (BPM).

(3) Loudness --> in dB.

(4) Danceability --> parameterized from 0 to 1 through one of Spotify's magic algorithms.

(5) Instrumentalness --> parameterized from 0 to 1 through one of Spotify's magic algorithms. Gives a measure on the amoun vocal in a song (a song without any vocals would have Instrumentalness = 1).

(6) Valence --> parameterized from 0 to 1 through one of Spotify's magic algorithms. Gives a measure of 'positive' (value 1) or 'negative' energy (value 0) embedded in a song.

These parameters give us some insight into how different music genres have evolved over time, and may predict which genres will be hottest in the coming years. Results are plotted for each genre separately (spotify_evolution_plot.ipynb), and combined sets (spotify_combined_evolution_plot.ipynb). Be sure to check out both plots.

## Some thoughts on the data ## 
- House and Techno are getting more popular since the early and mid 2000's, respectively (caused by the surgence of laptop DJ's?). Electro has a more constant fan-base, with perhaps a small lingering obsession for mid-to-late 80's electro music.

- as a sanity check, I compared the 'House' genre with its younger subgenres 'Electro House' and 'Deep House', which are showing the same trends in music characteristics. 

- the House and Electro House seem to be the most evolving music genres throughout the last decade, with significant changes in their loudness, danceability, and instrumentalness, which go hand-in-hand with an increased popularity. The techno and electro charts are more difficult to quantify, as the spread amongst individual songs is larger. 
