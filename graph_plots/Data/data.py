'''

@author: dan
'''
from __future__ import division

import numpy as np

from random import randint

from copy import deepcopy
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.preprocessing import MinMaxScaler


class Adata(object):

    def make2DDatas(self):

        datasets = [make_moons(n_samples=100, noise=0.1, random_state=13),
                    make_circles(n_samples=100, noise=0.1,
                                 factor=0.5, random_state=123),
                    make_classification(n_features=3, n_redundant=0, n_informative=2, random_state=1, n_clusters_per_class=1)]

        X, Y = datasets[0]  # moons or discs
        scaler = MinMaxScaler(feature_range=(0, 1))
        X = scaler.fit_transform(X)
        return {"X": X, "Y": Y}

    def make3DDatas(self):

        # rng = np.random.RandomState(2)
        # xx += 2 * rng.uniform(size=xx.shape)
        # ln = (xx,yy)
        # datasets = [make_moons(n_samples=300, noise=0.3, random_state=0),
        #             make_circles(n_samples=300,noise=0.2, factor=0.5, random_state=1),
        #             ln]

        datasets = [make_moons(n_samples=100, noise=0.1, random_state=123),
                    make_circles(n_samples=100, noise=0.1,
                                 factor=0.5, random_state=123),
                    make_classification(n_features=3, n_redundant=0, n_informative=2, random_state=1, n_clusters_per_class=1)]

        X, Y = datasets[2]  # moons or discs
        scaler = MinMaxScaler(feature_range=(0, 1))
        X = scaler.fit_transform(X)
        return {"X": X, "Y": Y}

    def make1DDatas(self):
        #X = np.random.normal(size=100)
        #XX=np.arange(0, 105, 1)
        #XX = np.random.randint(low=-50, high=50, size=1000)
        X = np.linspace(-10., 11., num=100)
        Y = (X - 2) * np.cos(2 * X)
        #YY = XX**2 + XX - 1
        # Make sure that it X is 2D
        #N = 1000
        #s = 10
        #XX = s*np.random.rand(N)
        #XX = np.sort(XX)
        #YY = np.sin(XX) + 0.1*np.random.randn(N)
        X = X[:, np.newaxis]
        return {"X": X, "Y": Y}

    def makeHistData(self):
        a = np.random.randint(0, size=20, high=10)
        Y, X = self.np_frequecy(a)
        ldatas = zip(X, Y)
        return ldatas

    def np_frequecy(self, dras):
        al = np.array(dras)
        al = al.ravel()
        al = np.sort(al, axis=None)
        mx = max(al)
        hist_bins = np.histogram(al, bins=np.linspace(
            0, mx+1, num=(mx+2), dtype=np.int))
        return hist_bins
