# train.py
import argparse
import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from loguru import logger

# Argument parser setup
parser = argparse.ArgumentParser()
parser.add_argument('--data_file', required=True, type=str, help='CSV file with training data')
parser.add_argument('--model_file', required=True, type=str, help='File to save the trained model')
parser.add_argument('--overwrite_model', default=False, action='store_true', help='Overwrite the model file if it exists')

args = parser.parse_args()

data_file = args.data_file
model_file = args.model_file
overwrite = args.overwrite_model

# Check if the model file exists
if os.path.isfile(model_file):
    if overwrite:
        logger.info(f"Overwriting existing model file {model_file}")
    else:
        logger.info(f"Model file {model_file} already exists. Use --overwrite_model option to overwrite.")
        exit(-1)

logger.info("Loading training data")
train = pd.read_csv(data_file)

# Features and target variable
X = train.drop('label', axis=1)
y = train['label']

# Data preprocessing
logger.info("Preprocessing data")
X = X / 255.0  # Normalizing the data

# Split the data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=99)

# Building the model
logger.info("Building the model")
model = RandomForestClassifier(n_estimators=100, random_state=99)

# Training the model
logger.info("Training the model")
model.fit(X_train, y_train)

# Evaluate the model
logger.info("Evaluating the model")
y_pred = model.predict(X_valid)
accuracy = accuracy_score(y_valid, y_pred)
logger.info(f"Validation Accuracy: {accuracy:.4f}")

# Saving the model
logger.info(f"Saving the model to {model_file}")
with open(model_file, 'wb') as f:
    pickle.dump(model, f)

logger.info("Training completed successfully")
