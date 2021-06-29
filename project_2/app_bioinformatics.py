######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
######################
# Page Title
######################

image = Image.open('project_2/dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]  # Skips the sequence name (first line)
sequence = ''.join(sequence)  # Concatenates list to string

st.write("""
***
""")

# Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# 1. Print dictionary
st.subheader('1. Print dictionary')


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d


X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X

# 2. Print text
st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

# 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

# 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart - Using Altair')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)

# Display Bar Chart using Plotly
st.subheader('4. Display Bar chart - Using Plotly')
plotly_template = "plotly_dark"
title_text, x_axis_text, y_axis_text = "Nucleotide Count", "Nucleotide", "Count"
width_text, height_text = 400, 400
font_text, font_size_text, font_color_text = "Times New Roman", 14, "silver"

fig = px.bar(df.sort_values(by="count", ascending=False), x="nucleotide",
             y="count", color_discrete_sequence=["royalblue"])
fig.update_layout(title=title_text, width=width_text, height=height_text,
                  template=plotly_template, xaxis_title=x_axis_text, yaxis_title=y_axis_text, font=dict(family=font_text, size=font_size_text, color=font_color_text), showlegend=False)
fig.update_traces(marker_line_color='black', marker_line_width=1, opacity=1)
st.write(fig)
