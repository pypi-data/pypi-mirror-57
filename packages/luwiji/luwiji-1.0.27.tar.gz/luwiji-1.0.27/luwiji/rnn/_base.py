import os
import pandas as pd
from IPython.display import Image


class BaseDemoRNN:
    def __init__(self):
        self.data = pd.DataFrame([[i, i+0.5] for i in range(1, 27)], columns=["feature1", "feature2"])


class BaseIllustrationRNN:
    def __init__(self):
        here = os.path.dirname(__file__)
        self.i_have_a_pen = Image(f"{here}/assets/i_have_a_pen.png", width=800)
        self.rnn_representation = Image(f"{here}/assets/rnn_representation.png", width=800)
        self.multilayer = Image(f"{here}/assets/multilayer.png", width=800)
        self.blstm = Image(f"{here}/assets/blstm.png", width=600)
        self.bptt = Image(f"{here}/assets/bptt.png", width=800)
        self.wolf_husky = Image(f"{here}/assets/wolf_husky.png", width=800)
        self.i_have_an_apple = Image(f"{here}/assets/i_have_an_apple.png", width=800)
        self.context = Image(f"{here}/assets/context.png", width=800)
        self.rnn_math = Image(f"{here}/assets/rnn_math.png", width=800)
        self.lstm = Image(f"{here}/assets/lstm.png", width=800)
        self.memory = Image(f"{here}/assets/memory.png", width=800)
        self.pyramid_blstm = Image(f"{here}/assets/pyramid_blstm.png")
        self.sequence_model = Image(f"{here}/assets/sequence_model.jpeg")
        self.gru = Image(f"{here}/assets/gru.png", width=400)
        self.lstm_math = Image(f"{here}/assets/lstm_math.png", width=400)
        self.forecast = Image(f"{here}/assets/forecast.png", width=850)
        self.batching = Image(f"{here}/assets/batching.png", width=850)
