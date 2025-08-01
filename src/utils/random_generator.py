#%% 
import numpy as np
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

class MonotonicallyIncreasingRNG:
    """Random number generator that produces monotonically increasing integers."""

    def __init__(self, start: int = 0, min_interval: int = 1, max_interval: int = 100, seed: Optional[int] = None):
        """Initialize the generator with a starting point and interval range.
        Args:
            start (int): The starting point for the random number generation.
            min_interval (int): Minimum interval between consecutive random numbers.
            max_interval (int): Maximum interval between consecutive random numbers.
            seed (Optional[int]): Seed for the random number generator for reproducibility.
        """
        self.current = start
        self.min_interval = min_interval
        self.max_interval = max_interval
        self.rng = np.random.default_rng(seed)
    
    def generate(self, size: int = 1) -> np.ndarray:
        """Generate a list of monotonically increasing random integers.
        Args:
            size (int): Number of random integers to generate.
        Returns:
            np.ndarray: An array of monotonically increasing random integers.
        """
        intervals = self.rng.integers(self.min_interval, self.max_interval + 1, size=size)
        random_values = self.current + np.cumsum(intervals)
        self.current = random_values[-1]  # Update current to the last value
        return random_values
    
    def set_current(self, value: int):
        """Set the current value to a specific integer."""
        self.current = value
    
    def set_seed(self, seed: Optional[int]):
        """Set the seed for the random number generator."""
        self.rng = np.random.default_rng(seed)
        
# %%
