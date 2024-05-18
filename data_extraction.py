import librosa
import numpy as np
import pandas as pd
import deeplake

dataset_path = 'hub://activeloop/gtzan-genre'
ds = deeplake.load(dataset_path)

features = []
filenames = []
genres = []

for i, audio_blob in enumerate(ds['audio']):
    audio_data = audio_blob.numpy().flatten()
    filename = f'file_{i}'
    genre = ds['genre'][i].numpy().item()
    
    sr = 22050
    
    feature_vector = {
        'chroma_stft': np.mean(librosa.feature.chroma_stft(y=audio_data, sr=sr)),
        'rmse': np.mean(librosa.feature.rms(y=audio_data)),
        'spectral_centroid': np.mean(librosa.feature.spectral_centroid(y=audio_data, sr=sr)),
        'spectral_bandwidth': np.mean(librosa.feature.spectral_bandwidth(y=audio_data, sr=sr)),
        'rolloff': np.mean(librosa.feature.spectral_rolloff(y=audio_data, sr=sr)),
        'zero_crossing_rate': np.mean(librosa.feature.zero_crossing_rate(y=audio_data)),
        'mfcc': np.mean(librosa.feature.mfcc(y=audio_data, sr=sr), axis=1).tolist()
    }
    
    features.append(feature_vector)
    filenames.append(filename)
    genres.append(genre)

features_df = pd.DataFrame(features)
features_df['filename'] = filenames
features_df['genre'] = genres

features_df.to_csv('audio_features.csv', index=False)

print("Features extracted for all audio files.")