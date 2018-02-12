# The evolution of house, techno, and electro.

When I moved to Amsterdam (~2005) I discovered electronic music. Particularly popular in the Amsterdam club scene during that time was Electro/Electro House (because of the likes of Boys Noize, Tiefschwarz, Digitalism, Justice, MSTRKRFT etc.), which was followed up by waves of Minimal, Tech House, Dub Step, Deep House, you name it. 

Looking back, it strikes me how fast these particular music genres went in and out of fashion (there are major differences between Electro and Deephouse...!). To see what may drive particular mood-swings in the electronic music scene I explored how different genres of electronic music have evolved over time: which music characteristics determine how popular (or 'mainstream') a given genre is (and will be)? 

For this project, I queried the Spotify API to obtain a number of tracks during the 1980-2016 timespan. For every track, I use the:

(1) Popularity --> parameterized from 0 (least popular) to 1 (most popular). Based on Spotify's magic algorithm (read: black box) on total playcount and how recent these are.
(2) Tempo --> in Beats per minute (BPM).
(3) Loudness --> in dB.
(4) Danceability --> parameterized from 0 to 1 through one of Spotify's magic algorithms.
(5) Instrumentalness --> parameterized from 0 to 1 through one of Spotify's magic algorithms. Gives a measure on the amount of vocals in a song.
(6) Valence --> parameterized from 0 to 1 through one of Spotify's magic algorithms. Gives a measure of 'positive' (value 1) or 'negative' energy (value 0)

These parameters give us some insight into how different music genres have evolved over time, and may predict which genres will be hottest in the coming years.
