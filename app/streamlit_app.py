import streamlit as st
import librosa
import numpy as np
import pickle
import pandas as pd

st.set_page_config(page_title="Music Recommendation System")

with open('knn_model.pkl', 'rb') as model_file:
    knn = pickle.load(model_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('filenames_train.pkl', 'rb') as f:
    filenames_train = pickle.load(f)
with open('y_train.pkl', 'rb') as f:
    y_train = pickle.load(f)

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
st.title('Music Recommendation System')
st.write('Upload an audio file to get recommendations.')

uploaded_file = st.file_uploader("Choose an audio file...", type=["wav", "mp3", "ogg"])

if uploaded_file is not None:
    audio_data, sr = librosa.load(uploaded_file, sr=None)
    
    chroma_stft = np.mean(librosa.feature.chroma_stft(y=audio_data, sr=sr))
    rmse = np.mean(librosa.feature.rms(y=audio_data))
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=audio_data, sr=sr))
    spectral_bandwidth = np.mean(librosa.feature.spectral_bandwidth(y=audio_data, sr=sr))
    rolloff = np.mean(librosa.feature.spectral_rolloff(y=audio_data, sr=sr))
    zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y=audio_data))
    mfcc = np.mean(librosa.feature.mfcc(y=audio_data, sr=sr), axis=1)
    
    feature_vector = [chroma_stft, rmse, spectral_centroid, spectral_bandwidth, rolloff, zero_crossing_rate]
    feature_vector.extend(mfcc)
    
    feature_vector = np.array(feature_vector).reshape(1, -1)
    feature_vector_scaled = scaler.transform(feature_vector)
    
    distances, indices = knn.kneighbors(feature_vector_scaled)
    
    st.write('Recommendations:')
    for i in range(len(indices[0])):
        genre_index = y_train[indices[0][i]]
        genre_name = genre_mapping[genre_index]
        audio_col, button_col = st.columns([4, 1], gap = "small")
        with audio_col:
            st.audio(f"https://mlsaproject.blob.core.windows.net/audios/{filenames_train[indices[0][i]]}.wav")
        with button_col:
            container = st.container(border=True)
            container.write(genre_name)