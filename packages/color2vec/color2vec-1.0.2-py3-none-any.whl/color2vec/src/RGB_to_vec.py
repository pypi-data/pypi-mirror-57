from __future__ import absolute_import
from __future__ import print_function
import numpy as np
# # import comet_ml in the top of your file
# from comet_ml import Experiment

# # Add the following code anywhere in your machine learning file
# experiment = Experiment(api_key="iEJDqOgS8QPlGv7hK3MYESLE2",
#                         project_name="text-similarity", workspace="iiitian-chandan")

import random
from keras.datasets import mnist
from keras.models import Model
from keras.layers import Input, Flatten, Dense, Dropout, Lambda
from keras.optimizers import RMSprop
import tensorflow as tf
from keras import backend as K
import keras

num_classes = 2
epochs = 20


def euclidean_distance(vects):
    x, y = vects
    sum_square = K.sum(K.square(x - y), axis=1, keepdims=True)
    return K.sqrt(K.maximum(sum_square, K.epsilon()))


def eucl_dist_output_shape(shapes):
    shape1, shape2 = shapes
    return (shape1[0], 1)


# def contrastive_loss(y_true, y_pred):
#     '''Contrastive loss from Hadsell-et-al.'06
#     http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf
#     '''
#     margin = 1
#     square_pred = K.square(y_pred)
#     margin_square = K.square(K.maximum(margin - y_pred, 0))
#     return K.mean(y_true * square_pred + (1 - y_true) * margin_square)


# def create_pairs(x, digit_indices):
#     '''Positive and negative pair creation.
#     Alternates between positive and negative pairs.
#     '''
#     pairs = []
#     labels = []
#     n = min([len(digit_indices[d]) for d in range(num_classes)]) - 1
#     for d in range(num_classes):
#         for i in range(n):
#             z1, z2 = digit_indices[d][i], digit_indices[d][i + 1]
#             pairs += [[x[z1], x[z2]]]
#             inc = random.randrange(1, num_classes)
#             dn = (d + inc) % num_classes
#             z1, z2 = digit_indices[d][i], digit_indices[dn][i]
#             pairs += [[x[z1], x[z2]]]
#             labels += [1, 0]
#     return np.array(pairs), np.array(labels)


def siameseModel(input_shape=(3,)):
    '''Base network to be shared (eq. to feature extraction).
    '''
    input = Input(shape=input_shape)
    #     x = Flatten()(input)
    dense1 = Dense(8)(input)
    #     dense1 = keras.activations.elu(dense1,alpha=1.0)
    dense2 = Dense(32, activation="relu")(dense1)
    #     dense2 = keras.activations.elu(dense2, alpha=1.0)
    dense3 = Dense(64, activation="relu")(dense2)
    #     dense3 = keras.activations.elu(dense3, alpha=1.0)
    dense4 = Dense(128, activation="relu")(dense3)
    #     dense4 = keras.activations.elu(dense4, alpha=1.0)
    dense5 = Dense(128, activation="relu")(dense4)
    #     dense5 = keras.activations.elu(dense5, alpha=1.0)
    dense5 = Dense(64, activation="relu")(dense5)
    dense5 = Dense(32, activation="relu")(dense5)
    dense5 = Dense(8)(dense5)
    dense6 = Dense(3)(dense5)
    #     dense6 = keras.activations.elu(dense6, alpha=1.0)
    model = Model(input, dense6)
    return model


def compute_accuracy(y_true, y_pred):
    '''Compute classification accuracy with a fixed threshold on distances.
    '''
    pred = y_pred.ravel() < 0.5
    return np.mean(pred == y_true)


def accuracy(y_true, y_pred):
    '''Compute classification accuracy with a fixed threshold on distances.
    '''
    return K.mean(K.equal(y_true, K.cast(y_pred < 0.5, y_true.dtype)))


from keras import backend as K
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
import cv2  # Not actually necessary if you just want to create an image.
import numpy as np
import matplotlib.pyplot as plt


def plot_space_image(image):
    plt.figure(figsize=(2, 2))
    plt.imshow(image)
    return plt.show()


_EPSILON = K.epsilon()


def contrastive_loss_fn(batch_size):
    def contrastive_loss(y_true, y_pred):
        def _contrastive_loss(y1, D):
            g = tf.constant(1.0, shape=[1], dtype=tf.float32)
            return K.mean(y1 * K.square(D) +
                          (g - y1) * K.square(K.maximum(g - D, 0)))

        y_pred = K.clip(y_pred, _EPSILON, 1.0 - _EPSILON)
        loss = tf.convert_to_tensor(0, dtype=tf.float32)
        g = tf.constant(1.0, shape=[1], dtype=tf.float32)
        h = tf.constant(0.0, shape=[1], dtype=tf.float32)
        for i in range(0, batch_size, 3):
            try:
                q_embedding = y_pred[i + 0]
                p_embedding = y_pred[i + 1]
                n_embedding = y_pred[i + 2]
                D_q_p = K.sqrt(K.sum((q_embedding - p_embedding) ** 2))
                D_q_n = K.sqrt(K.sum((q_embedding - n_embedding) ** 2))
                L_q_p = _contrastive_loss(g, D_q_p)
                L_q_n = _contrastive_loss(h, D_q_n)
                loss = (loss + L_q_p + L_q_n)
            except:
                continue
        loss = loss / (batch_size * 2 / 3)
        zero = tf.constant(0.0, shape=[1], dtype=tf.float32)
        return tf.maximum(loss, zero)

    return contrastive_loss


# from tensorflow.keras import backend as K
import tensorflow as tf

_EPSILON = K.epsilon()


def accuracy_fn(batch_size):
    def accuracy(y_true, y_pred):
        y_pred = K.clip(y_pred, _EPSILON, 1.0 - _EPSILON)
        accuracy = 0
        for i in range(0, batch_size, 3):
            try:
                q_embedding = y_pred[i + 0]
                p_embedding = y_pred[i + 1]
                n_embedding = y_pred[i + 2]
                D_q_p = K.sqrt(K.sum((q_embedding - p_embedding) ** 2))
                D_q_n = K.sqrt(K.sum((q_embedding - n_embedding) ** 2))
                accuracy += tf.cond(D_q_n > D_q_p, lambda: 1, lambda: 0)
            except:
                continue
        accuracy = tf.cast(accuracy, tf.float32)
        return accuracy * 100 / (batch_size / 3)

    return accuracy


# the data, split between train and test sets
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train = x_train.astype('float32')
# x_test = x_test.astype('float32')
# x_train /= 255
# x_test /= 255
# input_shape = x_train.shape[1:]

# create training+test positive and negative pairs
# digit_indices = [np.where(y_train == i)[0] for i in range(num_classes)]
# tr_pairs, tr_y = data["x"], data["y"]

# # digit_indices = [np.where(y_test == i)[0] for i in range(num_classes)]
# te_pairs, te_y = data["x"], data["y"]
# input_shape =(3,)
# # network definition
# base_network = create_base_network(input_shape)

# input_a = Input(shape=input_shape)
# # input_b = Input(shape=input_shape)

# # because we re-use the same instance `base_network`,
# # the weights of the network
# # will be shared across the two branches
# processed_a = base_network(input_a)
# # processed_b = base_network(input_b)

# # distance = Lambda(euclidean_distance,
# #                   output_shape=eucl_dist_output_shape)([processed_a, processed_b])

model = siameseModel()

# train_X = np.array(list(train_data["x1"])).reshape(len(train_data), 3)
# # train_X2 = np.array(list(train_data["x2"])).reshape(len(train_data),3)
# train_Y = np.array(train_data["y"])
#
# test_X = np.array(list(test_data["x1"])).reshape(len(test_data), 3)
# # test_X2 = np.array(list(test_data["x2"])).reshape(len(test_data),3)
# test_Y = np.array(test_data["y"])

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def print_color3d_space(vectors, colors, epoch="1"):
    x = []
    y = []
    z = []
    color = np.array(colors)
    for i in range(len(vectors)):
        x.append(vectors[i][0])
        y.append(vectors[i][1])
        z.append(vectors[i][2])
    #         color.append(colors[i])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=color / 255.0, marker='o')
    plt.show()
    plt.savefig(str(epoch) + "result.jpg")
    try:
        plot_space_image(str(epoch) + "result.jpg")
    except:
        pass


#     experiment.log_asset_data(self, str(epoch)+"result.jpg", file_name=None, overwrite=False, step=None)


class Metrics(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.return_corr_dict = {}
        self.return_text_dict = {}
        self.return_image_dict = {}

    def on_epoch_end(self, epoch, epoch_logs):
        sim_list_image = []
        sim_list_text = []
        sim_list = []
        sim_list = []
        new_model = Model(self.model.input, self.model.layers[-1].output)
        predicted_value = new_model.predict(test_X)
        print_color3d_space(predicted_value, test_data["x1"], epoch)


# train
rms = RMSprop()
# _loss_tensor = globals()["contrastive_loss_fn"](24)
model.compile(loss=contrastive_loss_fn(24),
              optimizer=tf.train.MomentumOptimizer(learning_rate=0.01, momentum=0.9, use_nesterov=True),
              metrics=[accuracy_fn(24)])

model.load_weights("color2vec/src/model/color_siames_model.h5")


def vector_prediction(RGB):
    RGB =np.array(RGB).reshape(3,)
    print(RGB.shape)
    predicted_value = model.predict(np.array([RGB]))
    return list(predicted_value[0])
