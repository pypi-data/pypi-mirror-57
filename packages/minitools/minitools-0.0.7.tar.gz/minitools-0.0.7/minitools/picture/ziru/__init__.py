import numpy as np

from io import BytesIO
from PIL import Image

from minitools.ml.knn import KNearestNeighbor

__all__ = 'Ziru',


class Ziru(KNearestNeighbor):
    threshold = 140
    shape = (1, 10)

    @classmethod
    def createTrainingSet(cls, png):
        with open(png, 'rb') as f:
            res = cls().process(f.read())
            np.savetxt(png.replace(".png", ".txt"), res)

    def __init__(self, trainSetPaht=None):
        self.loadTrainingSet(trainSetPaht)

    def loadTrainingSet(self, trainPath):
        if trainPath:
            self.labels = list(trainPath[:trainPath.find('.')])
            self.trainSet = np.loadtxt(trainPath)

    def process(self, body: bytes):
        image = Image.open(BytesIO(body))
        image = image.resize((300, 30), Image.ANTIALIAS).convert('L')
        self.img2gsi(image)
        return self.cutting(image)

    def img2gsi(self, image):
        col, row = image.size
        box = image.load()
        for x in range(col):
            for y in range(row):
                box[x, y] = 1 if box[x, y] > self.threshold else 0

    def cutting(self, image):
        row, col = self.shape
        image_col, image_row = image.size
        height = image_row // row
        weight = image_col // col
        res = []
        for r in range(row):
            for c in range(col):
                box = (c * weight, r * height, (c + 1) * weight, (r + 1) * height)
                res.append(self.box2vector(np.array(image.crop(box), 'f')))
        return np.array(res)

    def classify0(self, vector: np.ndarray):
        return self.classify(vector, self.trainSet, self.labels)

    def get_price(self, body: bytes):
        return [self.classify0(r) for r in self.process(body)]


"""
Ziru.createTrainingSet("4983571602.png")

zr = Ziru("4983571602.txt")

with open("4978123605.png", 'rb') as f:
    print(zr.get_price(f.read()))
"""
