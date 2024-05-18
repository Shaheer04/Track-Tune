import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import pickle

features_df = pd.read_csv('audio_features.csv')
model_path = 'knn_model.pkl'
scaler_path = 'scaler.pkl'

X = features_df.drop(['filename', 'genre'], axis=1).values
y = features_df['genre'].values
filenames = features_df['filename'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test, filenames_train, filenames_test = train_test_split(
    X_scaled, y, filenames, test_size=0.2, random_state=42)

knn = NearestNeighbors(n_neighbors=5, algorithm='auto').fit(X_train)

with open(model_path, 'wb') as model_file:
    pickle.dump(knn, model_file)
with open(scaler_path, 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

with open('filenames_train.pkl', 'wb') as f:
    pickle.dump(filenames_train, f)
with open('y_train.pkl', 'wb') as f:
    pickle.dump(y_train, f)

print(f"Model trained and saved to {model_path}. Scaler saved to {scaler_path}.")