import numpy as np

class NoiseFilter:
    def __init__(self, window_size = 10):
        """
        A simple "Moving Average" model to smooth out sensor noise
        """
        self.window_size = window_size
    
    def clean(self, noise_data):
        """
        Applies the filter to the data using convolution
        """
        
        # Create a list of weights
        kernel = np.ones(self.window_size) / self.window_size
        
        # Apply the sliding window math
        smoothed_signal = np.convolve(noise_data, kernel, mode='same')
        
        return smoothed_signal
    
