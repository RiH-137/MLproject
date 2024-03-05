import pickle

# Specify the path to your .pkl file
file_path = "artifacts/model.pkl"

# Open the .pkl file in binary read mode
with open(file_path, "rb") as f:
    # Load the data from the file
    data = pickle.load(f)
