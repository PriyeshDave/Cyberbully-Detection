import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tensorflow
import joblib
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences

sw = stopwords.words('english')
lm = joblib.load('./Models/Lemmatizer.pkl')
model = tensorflow.keras.models.load_model('./LSTM/Callbacks 3/model.02-0.42.h5')
mapper = {False: 'Not Toxic', True:'Toxic'}

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
  # One hot representation of words
  onehot_repr = [one_hot(sentence,voc_size)] 
  # Embedding the sentences
  embedded_docs = pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)
  return embedded_docs

def get_predictions(sentence):
  sentence = cleanData(sentence)
  data_lstm = word_embedding(sentence)
  prediction = model.predict(data_lstm)
  prediction = (prediction >= 0.5)

  return mapper[prediction[0][0]]
  




