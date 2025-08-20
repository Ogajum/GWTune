#%% 
import numpy as np
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

class MonotonicallyIncreasingRNG:
    """Random number generator that produces monotonically increasing integers.
        The i-th integer = start + i * part_range + random_offset
        Random offsets are drawn from a uniform distribution [0, part_range).
    """

    def __init__(self, start: int = 0, part_range : int = 100, seed: Optional[int] = None):
        """Initialize the generator with a starting point and a range of uniform distribution.
        Args:
            start (int): The starting point for the random number generation.
            part_range (int): uniform distribution range for the random numbers.
            seed (Optional[int]): Seed for the random number generator for reproducibility.
        """
        self.current_part = start # the start number of current part
        self.part_range = part_range
        self.rng = np.random.default_rng(seed)
    
    def generate(self, size: int = 1) -> np.ndarray:
        """Generate a list of monotonically increasing random integers.
        Args:
            size (int): Number of random integers to generate.
        Returns:
            np.ndarray: An array of monotonically increasing random integers.
        """
        diffs = self.rng.integers(0, self.part_range, size=size)
        random_values = self.current_part + np.arange(0, size*self.part_range, self.part_range) + diffs
        self.current_part = self.current_part + size * self.part_range
        return random_values
    
    def set_current(self, value: int):
        """Set the current value to a specific integer."""
        self.current_part = value
    
    def set_seed(self, seed: Optional[int]):
        """Set the seed for the random number generator."""
        self.rng = np.random.default_rng(seed)
        
# %%
