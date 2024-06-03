import numpy as np
import pandas as pd
import os
from pathlib import Path


class FileProcessor:
    def __init__(self, file_location):
        self.file_location = file_location

    def read_file(self):
        if not os.path.isfile(self.file_location):
            raise FileNotFoundError(f"No file found at {self.file_location}")
        
        with open(self.file_location, 'r') as file:
            content = file.read()
        
        # Create a DataFrame with a single column 'Content' containing the entire text
        df = pd.DataFrame([content], columns=['Content'])
        df['FileName'] = os.path.basename(self.file_location)
        return df

    def process_file(self):
        data = self.read_file()
        # Add your processing logic here
        return data
