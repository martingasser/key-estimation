import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

from partitura import load_musicxml
from partitura.musicanalysis import estimate_key
from partitura.utils import key_name_to_fifths_mode, fifths_mode_to_key_name


st.title('Key estimator')

uploaded_file = st.file_uploader("Choose a musicxml file", type='musicxml')
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    score = load_musicxml(uploaded_file)
    key = estimate_key(score)
    st.title(f'Estimated key: {key}')
