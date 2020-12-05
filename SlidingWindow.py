import numpy as np


class SlidingWindow():

    def __init__(self, time_data, window_size=24, start_time=0, stride=1):
        """
        Sliding window approach: Multiple vectors of length "window_size" are created from "time_data" vector, each shifted by "stride" time steps
        :param time_data: list of time data
        :param window_size: width of sliding window
        :param start_time: index at which the sliding window should start
        :param stride: time steps over which the window should slide
        """
        self.time_data = np.array(time_data)
        self.window_size = window_size
        self.start_time = start_time
        self.stride = stride

    def normalize(self):
        self.time_data = (self.time_data - np.min(self.time_data)) / (np.max(self.time_data) - np.min(self.time_data))

    def get_window_matrix(self):
        sub_windows = self.start_time + np.expand_dims(np.arange(self.window_size), 0) + np.expand_dims(
            np.arange(len(self.time_data) - self.window_size + 1 - self.start_time), 0).T
        window_matrix = self.time_data[sub_windows[::self.stride]]
        return window_matrix
