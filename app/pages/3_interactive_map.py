# %%
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import folium
# from folium.plugins import StripePattern
import os
import branca
# import numpy as np
import json
# import time
import ast

colorscale = branca.colormap.LinearColormap(['#800080',
                                             '#FF0000',
                                             '#FFA500',
                                             '#FFFF00',
                                             '#00FF00']
                                            ).scale(1, 100)
# BASE_DIR = os.path.join(os.path.dirname(__file__), '..', '..')
app_dir = os.path.dirname(os.path.dirname(__file__))


@st.cache_data
def load_data():

    st.spinner(text="Loading Data...")

    fuel_poverty_df_filepath = os.path.join(app_dir,
                                            'data',
                                            'fuel_poverty_data.csv')
    fuel_poverty_df = pd.read_csv(fuel_poverty_df_filepath,
                                  index_col='Postcode')

    simd_series = fuel_poverty_df['simd_percentile']
    simd_series = round(simd_series).fillna(-1).astype(int).replace(-1, None)

    epc_series = fuel_poverty_df['average_energy_efficiency_rating']
    epc_series = round(epc_series).fillna(-1).astype(int).replace(-1, None)

    fpr_series = fuel_poverty_df['fuel_poverty_rating']
    fpr_series = round(fpr_series).fillna(-1).astype(int).replace(-1, None)

    council_areas_df_filepath = os.path.join(app_dir,
                                             'data',
                                             'scottish_areas.csv')
    council_areas_df = pd.read_csv(council_areas_df_filepath,
                                   index_col='District')
    council_areas_df.columns = ['postcodes', 'bounds']

    # simd_full_df = pd.read_csv(os.path.join(
    #     BASE_DIR, 'data', 'postcode_simd.csv'))
    # simd_rank_series = simd_full_df.set_index('Postcode')['SIMD2020v2_Rank']
    # simd_series = (simd_rank_series / simd_rank_series.max())*100
    # simd_series = round(simd_series).astype(int)

    # epc_mean_df = pd.read_csv(os.path.join(BASE_DIR,
    #                                        'data',
    #                                        'epc_grouped_2012-22.csv'))
    # epc_series = epc_mean_df.set_index('Postcode')[
    #     'average_energy_efficiency_rating']
    # epc_series = round(epc_series).astype(int)

    # fpr_series = simd_series.add(epc_series)/2
    # fpr_series = round(fpr_series).fillna(-1).astype(int).replace(-1, None)

    # council_areas = pd.read_csv('https://www.opendata.nhs.scot/dataset/'
    #                             '9f942fdb-e59e-44f5-b534-d6e17229cc7b/'
    #                             'resource/'
    #                             '967937c4-8d67-4f39-974f-fd58c4acfda5/'
    #                             'download/'
    #                             'ca11_ca19.csv')
    # council_area_code_df = council_areas.set_index('CAName')['CA']
    # council_area_code_df = council_area_code_df.drop_duplicates()

    # council_area_names = council_area_code_df.index.unique()
    # council_area_names_list = council_area_names.sort_values().to_list()
    # simd_series = full_df['simd_percentile']
    # epc_series = full_df['average_energy_efficiency_rating']

    # postcode_lookup_df = pd.read_csv(os.path.join(BASE_DIR,
    #                                               'data',
    #                                               'scottish_postcodes_lookup'
    #                                               '.csv'),
    #                                  usecols=['RegistrationDistrict2007Code',
    #                                           'PostcodeDistrict'])
    # council_area_postcodes = postcode_lookup_df \
    #     .groupby('RegistrationDistrict2007Code')['PostcodeDistrict'] \
    #     .apply(lambda x: list(np.unique(x)))

    return simd_series, epc_series, fpr_series, council_areas_df


@st.cache_data
# def import_and_merge_geojson(list_of_postcodes):
def import_geojson(district):

    # for i in range(len(list_of_postcodes)):
    #     filepath = os.path.join(BASE_DIR,
    #                             'data',
    #                             'geo_data',
    #                             f'{list_of_postcodes[i]}.geojson')
    #     if not os.path.exists(filepath):
    #         f = open(os.path.join(BASE_DIR,
    #                               'data',
    #                               'geo_data',
    #                               '01_blank.geojson'))
    #     else:
    #         f = open(filepath)

    #     data = json.load(f)
    #     data_list.append(data)

    # for i in range(len(data_list)):
    #     if i == 0:
    #         bigger_dict = data_list[i]

    #     else:
    #         bigger_dict['features'].extend(data_list[i]['features'])

    filepath = os.path.join(app_dir,
                            'data',
                            'geo_data_by_district',
                            f'{district}.json')
    if not os.path.exists(filepath):
        f = open(os.path.join(app_dir,
                              'data',
                              'geo_data_by_district',
                              '01_blank.geojson'))
    else:
        f = open(filepath)
    data = json.load(f)

    return data


def add_layer(geojson_data_dict, series, show, name):
    # stripe = StripePattern(angle=45,
    #                        color='grey',
    #                        space_color='white')

    def create_style(feature):
        rank = series.get(feature["properties"]["postcodes"], None)
        if rank is None:
            style_dict = {
                "fillOpacity": 0,
                "weight": 0.4,
                # 'fillPattern': sp}
                'fillColor': 'white'}
        else:
            style_dict = {
                "fillOpacity": 0.5,
                "weight": 0,
                "fillColor": colorscale(rank)}
        return style_dict

    def amend_highlight(feature):
        rank = series.get(feature["properties"]["postcodes"], None)
        highlight_dict = {'fillOpacity': 0 if rank is None else 0.7,
                          'weight': 2,
                          'fillColor': "#white" if rank is None
                          else colorscale(rank)}
        return highlight_dict

    # def create_tooltip(feature):
    #     rank = series.get(feature["properties"]["postcodes"])
    #     return folium.features.GeoJsonTooltip(
    #         fields=['postcodes',
    #                 rank],
    #         aliases=["Postcode: ",
    #                  "Score: "])

    # def get_rank(postcode):
    #     return series.get(postcode)

    return folium.GeoJson(geojson_data_dict,
                          style_function=create_style,
                          highlight_function=amend_highlight,
                          show=show,
                          name=name,
                          overlay=False,
                          #   tooltip=create_tooltip(feature))
                          tooltip=folium.features.GeoJsonTooltip(
                            fields=['postcodes'],
                            aliases=["Postcode:  "]))


@st.cache_resource()
def load_map(district, simd_series, epc_series, fpr_series, areas_df):

    geojson_data_dict = import_geojson(district)

    map = folium.Map(tiles=None, prefer_canvas=True)
    folium.TileLayer('cartodbpositron', control=False).add_to(map)

    # sp = StripePattern(angle=45, color='grey', space_color='white')
    # sp.add_to(map)

    add_layer(geojson_data_dict,
              fpr_series,
              True,
              'Fuel Poverty Risk Rating').add_to(map)

    add_layer(geojson_data_dict,
              simd_series,
              False,
              'Index of Multiple Deprivation').add_to(map)

    add_layer(geojson_data_dict,
              epc_series,
              False,
              'EPC Mean for Postcode').add_to(map)

    # map.fit_bounds(map.get_bounds(), padding=(-2, -2))
    bounds = ast.literal_eval(areas_df.loc[district]['bounds'])
    map.fit_bounds(bounds, padding=(-2, -2))
    folium.LayerControl(collapsed=False).add_to(map)

    return map


def main():

    # %%
    simd_series, epc_series, fpr_series, council_areas_df = load_data()

    # st.set_page_config(layout='wide')
    st.title('Interactive Fuel Poverty Map')

    council_area_names_list = council_areas_df.index.to_list()
    council_area_names_list = [' '] + council_area_names_list
    requested_council_area = st.selectbox(
        'Which council area would you like to view?',
        council_area_names_list)

    # %%

    # requested_council_area = 'Aberdeen City'
    if requested_council_area != ' ':
        # progress_text = "Operation in progress. Please wait."
        # my_bar = st.progress(0, text=progress_text)

        # for percent_complete in range(100):
        #     time.sleep(0.05)
        #     my_bar.progress(percent_complete + 1, text=progress_text)

        # selected_council_area_postcodes = get_postcodes(
        #     requested_council_area,
        #     council_area_postcodes,
        #     council_area_code_df)
        selected_council_area_postcodes = council_areas_df.loc[
            requested_council_area]['postcodes']

        map = load_map(requested_council_area,
                       simd_series, epc_series,
                       fpr_series, council_areas_df)
        st.write('Building map...'
                 'There are a lot of polygons to load—so please be patient.')
        st_map = st_folium(map, width=700, height=450)

        st.markdown(f'Showing postcodes {selected_council_area_postcodes} '
                    f'that contain homes in council area'
                    f' {requested_council_area}.'
                    f'\nFor more information on how we calculate our fuel '
                    f'poverty score, please see [the about section]'
                    f'(1_about.py/#our-fuel-poverty-risk-rating).')


if __name__ == "__main__":
    main()
