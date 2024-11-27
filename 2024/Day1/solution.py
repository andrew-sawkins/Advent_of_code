import sys
import os

# Add the parent directory of the current folder (2024) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import read_input

input_data = read_input(2024, 1)
print(input_data)