import streamlit as st
import pandas as pd
import numpy as np
import datetime
from pathlib import Path
from data import FileProcessor

st.title('Data Visualizer')



start_date = st.date_input("Start date", value=None)
st.write("Start date is:", start_date)

end_date = st.date_input("End date", value=None)
st.write("End date is:", end_date)

root_folder = Path(r'./test.txt')

processor = FileProcessor(root_folder)
files_output = processor.process_file()

st.write(files_output)

