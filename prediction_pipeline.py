import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tensorflow
import joblib
#from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences

nltk.download('stopwords')
nltk.download('wordnet')
sw = stopwords.words('english')
lm = joblib.load('./Models/Lemmatizer.pkl')
model = tensorflow.keras.models.load_model('./LSTM/Callbacks/model.02-0.43.h5')
one_hot_df = pd.read_csv('./Datasets/One Hot Encoded Data.csv').set_index('Word')

mapper = {0 : 'Not Toxic', 1 : 'Toxic'}

voc_size = 16000
sent_length = 25
embedding_vector_features = 300


def removeTags(sentence):
  return ' '.join([word for word in sentence.split(' ') if not word.__contains__('@')])

def cleanData(sentence):

  sentence = str(sentence)
  sentence = sentence.lower()

  # Removing @tags from sentences
  sentence = removeTags(sentence)

  # Removing twitter handles urls
  sentence = ' '.join([word if not word.__contains__('https:') else '' for word in sentence.split(' ')])

  # Removing twitter handles urls
  sentence = ' '.join([word if not word.__contains__('http:') else '' for word in sentence.split(' ')])

  # Removing #MKR from tweets
  sentence = ' '.join([word if not word.__contains__('#mkr') else '' for word in sentence.split(' ')])

  # Removing stopwords and lemmatizing 
  sentence = ' '.join([lm.lemmatize(word) for word in sentence.split(' ') if not word in sw])
  
  #Removing special characters
  sentence = re.sub("[^a-z ]", " ", sentence)

  # Removing single characters
  sentence = ' '.join([word if not len(word) == 1 else '' for word in sentence.split(' ')])

  # Removing extra spaces
  sentence = re.sub(" +", " ", sentence)
  return sentence.strip()

def word_embedding(sentence):
  sentence = sentence.split(' ')
  # One hot representation of words
  onehot_repr = [one_hot_df.loc[word][0] for word in sentence]
  # Embedding the sentences
  embedded_docs = pad_sequences([onehot_repr],padding='pre',maxlen=sent_length)
  return embedded_docs

def get_predictions(sentence):
  print('Sentence Length: ', len(sentence))
  sentence = cleanData(sentence)
  print('Sentence Length: ', len(sentence))
  print(sentence)
  data_lstm = word_embedding(sentence)
  print('Embeded Docs: ', data_lstm)
  predicted_probability = model.predict(data_lstm)[0][0]
  print('Predicted Probability: ', predicted_probability)
  prediction = (predicted_probability >= 0.5)

  return (mapper[int(prediction)], predicted_probability)
  




