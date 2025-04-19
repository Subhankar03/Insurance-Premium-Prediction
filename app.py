import pandas as pd, streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
from nbconvert import HTMLExporter


# Use README.md to generate the content
with open('README.md', encoding='utf-8') as f:
	md = f.read()
with open('Insurance Premium Prediction.ipynb', encoding='utf-8') as f:
	nb_html, _ = HTMLExporter().from_file(f)
	nb = f.read()

st.set_page_config(page_title='Insurance Premium Prediction',
                   page_icon='Health Insurance.png',
                   layout='wide')
col1, col2 = st.columns((.06, .94), vertical_alignment='center')
col1.image('Health Insurance.png', width=64)
col2.title('Insurance Premium Prediction')
st.write('')

# Show user selected table
@st.fragment
def show_dataset():
	st.dataframe(pd.read_csv('Insurance.csv'), hide_index=True)
	
# Button to download the notebook
@st.fragment
def download_notebook():
	st.download_button(
		'Download notebook', nb,
		file_name='Insurance Premium Prediction.ipynb',
		icon=':material/download:')


# Add 2 tabs: Overview, Notebook
overview, notebook = st.tabs([':material/description: Overview', ':material/code: Notebook'])
with notebook:
	components.html(nb_html, height=6700, scrolling=True)

with overview:
	col1, col2 = st.columns((.7, .3))
	with col2:  # Add a lottie animation
		st_lottie('https://lottie.host/ab92068e-5f7b-43bd-b7ef-09ce1b65b7fd/W0b897hMO7.json')
	# Project overview, Objective
	col1.markdown(md[md.find('## Project') : md.find('## Methodology')])
	
	# Expander to show the dataset
	with st.expander('See the dataset', icon=':material/table:'):
		st.caption('''
		The dataset contains demographic and health-related information for individuals,
		along with their corresponding medical insurance charges
		''')
		show_dataset()
	
	# Methodology, Key Takeaways, Conclusion
	st.markdown(md[md.find('## Methodology'):])
	st.divider()
	download_notebook()