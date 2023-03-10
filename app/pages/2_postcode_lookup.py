import streamlit as st
import pandas as pd
import os
import numpy as np

# Links for use in body text
more_simd = ('https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/')
more_epc = ('https://www.mygov.scot/energy-performance-certificates')

# Title and intro
st.markdown('# Postcode Lookup Tool')
st.markdown('This tool allows practitioners and community members to quickly '
            'look up a fuel poverty risk for a specific postcode.')

# Global variables
app_dir = os.path.dirname(os.path.dirname(__file__))
# root directory for app

file_locations = pd.read_csv(os.path.join(app_dir,
                                          'file_locations.csv'),
                             index_col='filename')

# load data in format created using data-restructuring.py
fuel_poverty_df_filepath = file_locations.loc['fuel_poverty_data.csv']['location']
fuel_poverty_df = pd.read_csv(fuel_poverty_df_filepath,
                              index_col='Postcode')

# create series' from main dataframe for building map layers and store in a
# list for iterating through
simd_series = fuel_poverty_df['simd_percentile']
epc_series = fuel_poverty_df['average_energy_efficiency_rating']
fpr_series = fuel_poverty_df['fuel_poverty_rating']
series_list = [simd_series, epc_series, fpr_series]

# user inputs postcode
postcode = st.text_input('Postcode', '')
postcode = postcode.strip().upper()  # clean user input

# extract scores for that particular postcode from series items and saves to
# a dictionary
score_dict = {'simd percentile score': 'n/a',
              'epc score': 'n/a',
              'fpr score': 'n/a'}
score_dict_keys_list = list(score_dict)
for i in range(len(series_list)):
    if postcode in series_list[i] and not np.isnan(series_list[i][postcode]):
        score_dict[score_dict_keys_list[i]] = round(series_list[i][postcode])
    else:
        score_dict[score_dict_keys_list[i]] = 'n/a'

# if 'submit' button is pressed...
if st.button('Submit'):
    if postcode == '' or postcode == ' ':
        st.markdown('Please enter a postcode.')
        # if no postcode has been entered, alert the user

    if score_dict['simd percentile score'] != 'n/a':
        # if there is a value saved under simd score:

        # display overview table with three columns containing score for that
        # value and further information. Scores are shown using the inbuilt
        # Streamlit metric format
        st.markdown('## Postcode Overview'
                    '\nLower numbers mean a worse score.')
        col1, col2, col3 = st.columns(3)
        with col1:
            score = score_dict['simd percentile score']
            value = str(score) + '/100'
            st.markdown('**Index of Multiple Deprivation score**')
            st.metric(label="Percentile",
                      value=value)
            st.markdown(f'[About the SIMD.]({more_simd})')

        with col2:
            score = score_dict['epc score']
            value = str(score) + '/100'
            st.markdown('**Mean EPC rating for this postcode**')
            st.metric(label="Mean Score",
                      value=value)
            st.markdown(f'[About EPC ratings.]({more_epc})')

        with col3:
            score = score_dict['fpr score']
            value = str(score) + '/100'
            st.markdown('**Estimated fuel poverty risk rating**')
            st.metric(label="Score",
                      value=value)
            st.markdown('[How we calculate this.](1_about.py#our-fuel-poverty-risk-rating)')

    else:
        st.write('Sorry. This postcode has not been recognised.')
        # else, inform the user that postcode isn't in our database
