def calc_pvalues(a,b):

        from scipy import stats
        import pandas as pd    
    
        t1, p1 = stats.ttest_ind(a['tempo_norm'], b['tempo_norm'])
        t1, p2 = stats.ttest_ind(a['loudness_norm'], b['loudness_norm'])
        t1, p4 = stats.ttest_ind(a['danceability'], b['danceability'])
        t1, p5 = stats.ttest_ind(a['valence'], b['valence'])

        p = [p1,p2,p4,p5]
        
        return p
    