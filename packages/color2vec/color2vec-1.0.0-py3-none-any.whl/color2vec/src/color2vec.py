import os

from color2vec.src.string_to_RGB import *
from color2vec.src.RGB_to_vec import *
from color2vec.src.lab import *
from color2vec.src.annoy_similarity import *
import numpy as np

# import color2vec.src.annoy_similarity

class Color2Vec:
    def __init__(self):
        """

        """
        self.pool = []
        print("Color2Vec initialized.")

    def string2vec(self, color_string="greendeck"):
        print("Input Color string: ", color_string)
        rgb = rgb_predict(color_string)
        return vector_prediction(rgb)

    def string2RGB(self, color_string="greendeck"):
        print("Input Color string: ", color_string)
        return rgb_predict(color_string)

    def string2LAB(self, color_string="greendeck"):
        print("Input Color string: ", color_string)
        rgb = rgb_predict(color_string)
        return rgb2lab(rgb)

    def RGB2LAB(self, rgb):
        print("Input RGB color: ", rgb)
        return rgb2lab(rgb)

    def RGB2vec(self, rgb):
        print("Input RGB color: ", rgb)
        return vector_prediction(rgb)

    def distance(self, items, type="string"):

        if type == "string":
            rgbs = [rgb_predict(color_string) for color_string in items]
            vecs = [vector_prediction(rgb) for rgb in rgbs]

        elif type == "RGB":
            vecs = [vector_prediction(rgb) for rgb in items]

        else:
            pass

        return np.linalg.norm(items[0] - items[1])

    def buildAnnoy(self, items, type="string"):

        if type == "string":
            rgbs = [rgb_predict(color_string) for color_string in items]
            vecs = [vector_prediction(rgb) for rgb in rgbs]

        elif type == "RGB":
            vecs = [vector_prediction(rgb) for rgb in items]
        elif type == "vec":
            vecs = items

        else:
            raise
        self.pool = vecs
        return index(vecs)

    def similar(self, target, build_annoy, k=5, include_distance=True):
        print("pool: ")
        print(self.pool)

        if type(target) == type("x"):
            target = vector_prediction(rgb_predict(target))
        elif type(target) == type([]):
            target = vector_prediction(target)

        if target in self.pool:
            pass
        else:
            self.pool.append(target)
            self.buildAnnoy(self.pool, type="vec")

        return similar_index(target, self.pool, build_annoy, k, include_distance)
