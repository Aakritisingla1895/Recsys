from keras.models import Sequential
from keras.layers import Conv1D, GlobalMaxPooling1D, Embedding, LSTM
from keras.layers.core import Dense, Dropout, Activation
from keras.preprocessing.text import Tokenizer
from keras import metrics, regularizers
from keras.preprocessing import sequence
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer


data = pd.read_csv('bio_clean.csv', header = 0, names = ['affliations', 'Description'])
#data = pd.read_csv('../../Results/Cleaned_JobsNonIT.csv', header = 0, names = ['Query', 'Description'])