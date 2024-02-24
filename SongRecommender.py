from sklearn.model_selection import train_test_split
import pandas
import Recommenders as Recommenders
 
def load_data():
    """
    Load and preprocess data.
    """
    df1 = pandas.read_csv('https://static.turi.com/datasets/millionsong/10000.txt', header=None, sep='\t')
    df1.columns = ['user_id', 'song_id', 'listen_count']
    df2 = pandas.read_csv('https://static.turi.com/datasets/millionsong/song_data.csv')
    df = pandas.merge(df1, df2.drop_duplicates(['song_id']), on="song_id", how="left")
    
    # Decrease the dataframe length to 10000 just to test the data
    df = df.head(10000)
    
    # Merge song title and artist_name columns to make a merged column
    df['song'] = df['title'].map(str) + " - " + df['artist_name']
    return df

def main():
    """
    Main function to demonstrate recommendation process.
    """
    df = load_data()

    song_grouped = df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
    grouped_sum = song_grouped['listen_count'].sum()
    song_grouped['percentage'] = song_grouped['listen_count'].div(grouped_sum) * 100
    most_popular_songs = song_grouped.sort_values(['listen_count', 'song'], ascending=[0, 1])

    users = df['user_id'].unique()
    songs = df['song'].unique()

    train_data, test_data = train_test_split(df, test_size=0.2, random_state=0)

    is_model = Recommenders.item_similarity_recommender_py()
    is_model.create(train_data, 'user_id', 'song')

    # Echo the songs for the user in training data
    user_id = users[5]
    user_items = is_model.get_user_items(user_id)

    print("**********Training data songs for the user userid: {}**********".format(user_id))
    for user_item in user_items:
        print(user_item)
    print("****************Recommendation process going on****************")
    # Top 10 Recommended songs for the user using personalized model
    recommended = is_model.recommend(user_id)
    print(recommended[['song', 'score', 'rank']])

if __name__ == "__main__":
    main()
