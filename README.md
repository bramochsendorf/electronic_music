# The evolution of house, techno, and electro music.

When I moved to Amsterdam (~2005) I discovered electronic music. Particularly popular in the Amsterdam club scene during that time was Electro/Electro House (because of the likes of Boys Noize, Tiefschwarz, Digitalism, Justice, MSTRKRFT etc.), which was followed up by waves of Minimal, Tech House, Dub Step, Deep House, you name it. 

Looking back, it strikes me how fast these particular music genres went in and out of fashion, as there are major differences between e.g. Electro and Deephouse (although this may not appear so obvious to the untrained ear). To see what may drive particular mood-swings in the electronic music scene I explored how different genres of electronic music have evolved over time. Which music characteristics determine how popular (or 'mainstream') a given genre is (and will be)? 

## Conclusion ##
My main conclusion is that popular electronic music is becoming louder, full of negative energy, and for the house genre, not particularly danceable. Therefore, a good bet for record labels or aspiring DJs is to produce ear-splitting house tracks (as exemplified by the popularity of artists like, e.g., Skrillex), or dark techno tracks. Be sure to warn your neighbors beforehand, though. 

## Analysis ## 
To come to this interesting conclusion, I queried the Spotify API to obtain tracks of a given music genre during the 1980-2016 timespan (spotify_query.py). 

### Music characteristics ###
For every track, I parsed the following metrics (music characteristics):

(1) Popularity --> parameterized from 0 (least popular) to 1 (most popular). Based on Spotify's magic algorithm (read: black box) on total playcount and how recent these are 

(2) Tempo --> originally 24-200 BPM, normalized to 0 to 1.

(3) Loudness --> originally in -60 dB to 60 dB, normalized -1 to 1.

(4) Danceability --> parameterized from 0 to 1 through one of Spotify's magic algorithms.

(5) Instrumentalness --> parameterized from 0 to 1 through one of Spotify's magic algorithms. Gives a measure on the amoun vocal in a song (a song without any vocals would have Instrumentalness = 1).

(6) Valence --> parameterized from 0 to 1 through one of Spotify's magic algorithms. Gives a measure of 'positive' (value 1) or 'negative' energy (value 0) embedded in a song.

These parameters give us some insight into how different music genres have evolved over time, and may predict which genres will be hottest in the coming years. Complete analysis are given for each genre separately (music_evolution_plot.ipynb), and combined sets (spotify_combined_evolution_plot.ipynb). Be sure to check out both plots. 

### First peek into the data ###
I first looked at the distributions of the different music characteristics for a given sample of tracks in a 'test year'. From here I realized that some variables are (roughly) normally distributed (such as Popularity, Tempo, Loudness, Danceability, Valence), others are not. Offcourse, this depence on your sample size.

### Plotting the evolution accross 1980-2016 ###
Next thing was to calculate the 25th, median, and 75th percentile of the music characteristics within each year, and plot them as a function of year to visualize their evolution. 

### Regression analysis: model selection + evaluation ###
To model the evolution of the music characteristics I use a simple polynomial regression model, where the degree of the polynomial is left as a free parameter.

Some of the features are noisy with a lot of variation in a given year. To speed up the training process, I perform the regression on the median feature values for each year. The best-performing model (i.e., the order of the polynomial) is chosen through a gridsearch in Scikit-learn together with a 10-fold cross validation. Persisting outliers are cleaned out using a median filter approach, where the threshold to flag an outlier is set high to incorporate as much 'original' data as possible.

With the best-performing model in hand, I proceed to estimate the uncertainty of my performance estimate: the R2 score. To this end, I use a bootstrap method, resampled my data 1000 times with replacement, and calculate the 95% confidence interval of the R2 score. 

The complete analysis (model selection + evaluation) is performed and plotted in spotify_regression_analysis.ipynb

Note that in some cases, the R2 scores are skewed with the lower bound of the confidence interval yielding negative numbers. This in practice means that in some cases, my fits are performing worse than a simple, horizontal line (...). This has to do with the intrinsic variations in the data, but also partly because of the pessimistic bias coming from the bootstrap: only ~63% of the original datapoints will eventually be chosen through the classical bootstrap method. 

Lastly, I combine the models and plot them together in the spotify_combined_evolution_plot.ipynb for easy comparison.

### Observation ### 

- House and Techno are getting more popular since the early and mid 2000's, respectively (caused by the surgence of laptop DJ's?). Electro has a more constant fan-base, with perhaps a small lingering obsession for mid-to-late 80's electro music.

- as a sanity check, I compared the 'House' genre with its younger subgenres 'Electro House' and 'Deep House', which are showing the same trends in music characteristics (data to be included in the repo). 

- For House and Techno (the genres with a clear increase in popularity) one can observe the following: increasing loudness, decreasing valence, and decreasing/increasing danceability for house/techno. These parameters may play an important role in determining a track's popularity.

### The significance of the variations ###
Given the large variation of some of the music features, one may ask how significant these changes are. For this, I grouped together tracks from the 1990's, 2000's, and 2010's, and did a simple Independant Samples t-test, which basically compares means of two distributions, quantifies their difference, and how significant these differences are. It assumes normality, so I performed this on the music characteristics that appear to be normally distributed: 'Tempo', 'Loudness', 'Danceability', and 'Valence'. Resulting p-values are calculated, showing that all genres and the aforementioned characteristics are significantly evolving (for 'significance' I choose p < 0.05), except the 'Danceability' of electro between the 2000's and 2010's.
