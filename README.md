# Music Recommendation System based on item-to-item based collaborative filtering in Python 3.7

This repository contains a proof of concept (POC) implementation of a music recommendation system using item-to-item based collaborative filtering. The system is implemented in Python 3.7.

## Overview
The recommendation system is designed to provide song recommendations based on user preferences and similarities between songs. It utilizes the item-to-item collaborative filtering technique to identify similar songs and recommend them to users.

## Files
- `SongRecommender.py`: This file contains the code for the recommendation system. It reads sample data from two sources: [https://static.turi.com/datasets/millionsong/10000.txt](https://static.turi.com/datasets/millionsong/10000.txt) and [https://static.turi.com/datasets/millionsong/song_data.csv](https://static.turi.com/datasets/millionsong/song_data.csv). The code is tested on a dataset of a million songs.
- `Recommenders.py`: This module contains the recommendation algorithm that uses a co-occurrence matrix. It is imported and used in the `SongRecommender.py` file.

## Usage
To use the music recommendation system, follow these steps:
1. Clone the repository: `git clone https://github.com/gargmegham/MusicRecommendationEngine.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the `SongRecommender.py` file: `python SongRecommender.py`

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Make sure to follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).


## Contact

For any questions or inquiries, please contact [meghamgarg@gmail.com](mailto:meghamgarg@gmail.com).
