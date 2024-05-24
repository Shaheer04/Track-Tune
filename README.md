# Track Tune
This project implements a web application built with Python, Streamlit, Librosa, sckikitlearn and is deployed on Azure Web Services. It allows users to upload music files and receive genre classification along with recommendations for similar songs.

##Link to Presentation deck
Please visit the following link for presentation deck:

## Azure Web Services
We have utilized Microsoft's Azure Web services to host our project. This streamlined the workload by making it easier for the changes to be deployed while the code is being experimented upon. You can visit the following link to get to the Track Tune app:
https://tracktune.azurewebsites.net/ 

## Problem Statement
Music lovers often struggle to discover new songs with similar vibes to their favorites. Traditional music streaming services might not provide detailed genre breakdowns or personalized recommendations that capture the essence of a particular song.

## Solution
This app addresses this challenge by offering the following functionalities:
###Genre Classification: Uploads an audio file, and the app leverages a machine learning model trained on the GTZAN Genre Dataset (https://datasets.activeloop.ai/docs/ml/datasets/) to identify the genre (e.g., pop, rock, EDM). The genre mapping is as follows:

```
genre_mapping = {
    0: 'pop',
    1: 'metal',
    2: 'classical',
    3: 'rock',
    4: 'blues',
    5: 'jazz',
    6: 'hiphop',
    7: 'reggae',
    8: 'disco',
    9: 'country'
}
```
### Similar Song Recommendations
Based on the predicted genre, the app suggests five songs from the dataset that share a similar style, potentially introducing users to new favorites with a familiar feel.

## How to Use
Upload Your Music: We created a webapp for this project, where you can easily uploadyour music files.
https://tracktune.azurewebsites.net/

## Get Results
The app processes the uploaded audio, predicts the genre, and presents you with the result. Additionally, it suggests five similar songs from the dataset based on the predicted genre.

## Running the App Locally (Optional)
Install Dependencies: Create a virtual environment and install the required dependencies using:
```pip install -r requirements.txt.```
Navigate to the project directory in your terminal and execute:
```streamlit run .py```
This will launch the app on your local machine (usually at http://localhost:8501 by default).

## Dependencies
Python (tested with version 3.12)
Streamlit (tested with version 1.25.0): Refer to https://docs.streamlit.io/ for the latest version.
librosa (tested with version 0.11.0): Refer to https://github.com/librosa/librosa for the latest version.
numpy (tested with version 1.24.3): Refer to https://numpy.org/ for the latest version.
pandas (tested with version 1.5.3): Refer to https://pandas.pydata.org/ for the latest version.
scikit-learn (tested with version 1.2.2): Refer to https://scikit-learn.org/ for the latest version.
  
## Next Steps
Enhance the recommendation engine by incorporating additional factors like tempo, mood, and artist information.
Expand the dataset to encompass a broader range of genres and musical styles.
Integrate with music streaming services to allow users to directly add recommended songs to their playlists.

## Disclaimer
This project is for educational purposes only. The GTZAN Genre Dataset is used for illustration, and you might need to acquire appropriate licenses for commercial use of music data.
