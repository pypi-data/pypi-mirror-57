import tensorflow as tf
from tensorflow.python import keras
from tensorflow.python.keras import preprocessing
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, LSTM, Reshape
import pickle
import numpy as np
import pandas as pd
from keras_preprocessing import text

np.random.seed(10)
data_1 = pd.read_csv('color2vec/src/data/colors_1.csv')
data_2 = pd.read_csv('color2vec/src/data/basic.csv')
del data_2['Hex']
data_3 = pd.read_csv('color2vec/src/data/advanced.csv')
del data_3['Hex']
data_4 = pd.read_csv('color2vec/src/data/pantone.csv')
del data_4['Hex']
data_5 = pd.read_csv('color2vec/src/data/ultra_basic.csv')
del data_5['Hex']
data = pd.concat([data_1, data_2, data_3, data_4, data_5])
# data.head()
data = data.reset_index()
names = data["name"]

print(len(names))

# Visualize the name string length distribution

h = sorted(names.str.len().as_matrix())
import numpy as np
import scipy.stats as stats
# import pylab as plt

# fit = stats.norm.pdf(h, np.mean(h), np.std(h))  # this is a fitting indeed
# plt.plot(h, fit, '-o')
# plt.hist(h, normed=True)  # use this to draw histogram of your data
# plt.xlabel('Chars')
# plt.ylabel('Probability density')
# plt.show()

# Tokenize, char level
maxlen = 41
import pickle

# t = Tokenizer(char_level=True)
# loading
# t = pd.read_pickle("color2vec/src/model/tokenizer.pickle")
#
# t.fit_on_texts(names)

import json
with open('color2vec/src/model/tokenizer.json') as f:
    tokenizer_data = json.load(f)
    t = text.tokenizer_from_json(tokenizer_data)




# t = text.tokenizer_from_json("color2vec/src/model/tokenizer.json")
tokenized = t.texts_to_sequences(names)
padded_names = preprocessing.sequence.pad_sequences(tokenized, maxlen=maxlen)

# One-hot encoding
from keras.utils import np_utils

one_hot_names = np_utils.to_categorical(padded_names)
num_classes = one_hot_names.shape[-1]
print(num_classes)


# The RGB values are between 0 - 255
# scale them to be between 0 - 1
def norm(value):
    return value / 255.0


normalized_values = np.column_stack([norm(data["red"]), norm(data["green"]), norm(data["blue"])])

model = Sequential()
model.add(LSTM(256, return_sequences=True, input_shape=(maxlen, num_classes)))
model.add(LSTM(128))
model.add(Dense(128, activation='relu'))
model.add(Dense(3, activation='sigmoid'))
model.compile(optimizer='adam', loss='mse', metrics=['acc'])

model.load_weights("color2vec/src/model/string_to_rgb_model.h5")
model.summary()


# history = model.fit(one_hot_names, normalized_values,
#                     epochs=40,
#                     batch_size=32,
#                     validation_split=0.1)


# Plot a color image.
# def plot_rgb(rgb):
#     data = [[rgb]]
#     plt.figure(figsize=(2, 2))
#     plt.imshow(data, interpolation='nearest')
#     plt.show()


def scale(n):
    return int(n * 255)


def rgb_predict(name):
    name = name.lower()
    tokenized = t.texts_to_sequences([name])
    padded = preprocessing.sequence.pad_sequences(tokenized, maxlen=maxlen)
    one_hot = np_utils.to_categorical(padded, num_classes=num_classes)
    pred = model.predict(np.array(one_hot))[0]
    r, g, b = scale(pred[0]), scale(pred[1]), scale(pred[2])
    return [r, g, b]
    # plot_rgb(pred)
