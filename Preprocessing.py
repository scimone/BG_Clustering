import numpy as np
import pandas as pd


class Preprocessing():
    def __init__(self, sgv):
        self.sgv = sgv

    def smoothing(self):
        sgv_pd = pd.DataFrame(self.sgv, columns=['sgv'])
        sgv_pd['mov_avg'] = sgv_pd['sgv'].rolling(6).sum()
        return sgv_pd['mov_avg'].dropna().to_numpy()
