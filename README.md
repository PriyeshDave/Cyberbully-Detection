# Cyberbully-Detection🚨
<img width="957" alt="image" src="https://user-images.githubusercontent.com/81012989/164934713-058d82a2-6c44-4b92-a29f-de0ecdbd5a95.png">

## Introduction
Cyberbully detector is an application that classifies whether a comment is toxic or not. 

## 🧭 Problem Statement: 
This is a binary classification problem where we are predicting if the given coment is toxic or not:
* Toxic => Contains text with hate speech, aggression, insults, and toxicity.
* Non Toxic 

## 🧾 Description: 
This dataset is a collection of datasets from different sources related to the automatic detection of cyber-bullying. The data is from different social media platforms like Kaggle, Twitter, Wikipedia Talk pages, and YouTube. The data contains text and are labeled as bullying or not. The data contains different types of cyber-bullying like hate speech, aggression, insults, and toxicity.

### :bar_chart: Exploratory Data Analysis:
* Exploratory Data Analysis is the first step of understanding your data and acquiring domain knowledge. 

### :hourglass: Data Preprocessing:
* The given data was cleaned & preprocessed by first removing the unwanted special characters and numbers from text.
* Next I removed the stop words from the sentences.
* Now I used **WordNetLemmatizer** for converting each of the tokens to their root words.
* Once the data is cleaned, I used **WordEmbedding** technique to convert words into vectors.

### ⚙ Model Training:
* The model is trained using **BidirectionalLSTM** with a vocabulary size of 16K and each word reprented by a vector of length 300.
* My trained model gives an accuracy of **91%** on train data while of **81%** on test data.
* As per the problem statement I used **F1 Score** as the evaluation metric for my model.
