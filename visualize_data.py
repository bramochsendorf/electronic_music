def vis_data(a,b,genre):

    from matplotlib import pyplot as plt

    fig = plt.figure(figsize=(10.5,8))
    font = {'size':9}
    plt.rc('font', **font)

    plt.subplots_adjust(left=0.2, bottom=0.2, right=0.875, top=0.85, wspace=0.35, hspace=0.35)

    plt.subplot(331)
    plt.hist(a['popularity_norm'])
    plt.title('Popularity')

    plt.subplot(332)
    plt.hist(b['tempo_norm'])
    plt.title('Tempo')

    plt.subplot(333)
    plt.hist(b['loudness_norm'])
    plt.title('Loudness')

    plt.subplot(334)
    plt.hist(b['instrumentalness'])
    plt.title('Instrumentalness')

    plt.subplot(335)
    plt.hist(b['danceability'])
    plt.title('Danceability')

    plt.subplot(336)
    plt.hist(b['valence'])
    plt.title('Valence')

    plt.subplot(337)
    plt.hist(b['speechiness'])
    plt.title('Speechiness')

    plt.subplot(338)
    plt.hist(b['key'])
    plt.title('Key')

    plt.subplot(339)
    plt.hist(b['mode'])
    plt.title('Mode')

    plt.savefig('output/'+genre+'_normality.pdf', dpi=150, bbox_inches='tight', pad_inches=0.2)