# import libraries
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import folium
import os
import branca
import json
import ast
from urllib.request import urlopen

# set global variables
app_dir = os.path.dirname(os.path.dirname(__file__))
# this variable points to the main folder of the app

file_locations = pd.read_csv(os.path.join(app_dir,
                                          'file_locations.csv'),
                             index_col='filename')


@st.cache_data  # cache the data that was loaded for quicker loadtimes
def load_postcode_data():
    '''
    Loads the data required for running the interactive fuel poverty map.
    This data was created in the correct format using the data-restructuring.py
    file.

    Outputs: List of series objects containing:
        Scottish Index of Multiple Deprivation Score per postcode,
        Mean EPC score per postcode,
        Generated fuel poverty risk rating per postcode.
    '''

    st.spinner(text="Loading Data...")
    # show data is loading

    # load data in format created using data-restructuring.py
    # fuel_poverty_df_filepath = os.path.join(app_dir,
    #                                         'data',
    #                                         'fuel_poverty_data.csv')
    fuel_poverty_df_filepath = file_locations.loc['fuel_poverty_data.csv']['location']
    fuel_poverty_df = pd.read_csv(fuel_poverty_df_filepath,
                                  index_col='Postcode')

    # create series' from main dataframe for building map layers and store in a
    # list for iterating through. Rounds values and saves in correct format for
    # reading by folium map (using 'None' values)
    simd_series = fuel_poverty_df['simd_percentile']
    simd_series = round(simd_series).fillna(-1).astype(int).replace(-1, None)
    epc_series = fuel_poverty_df['average_energy_efficiency_rating']
    epc_series = round(epc_series).fillna(-1).astype(int).replace(-1, None)
    fpr_series = fuel_poverty_df['fuel_poverty_rating']
    fpr_series = round(fpr_series).fillna(-1).astype(int).replace(-1, None)
    series_list = [simd_series, epc_series, fpr_series]

    return series_list


@st.cache_data
def load_council_area_df():
    '''
    import the council area dataframe with summary data for each area
    including bounds data.

    Output: area summary dataframe including area boundary details.
    '''

    # council_areas_df_filepath = os.path.join(app_dir,
    #                                          'data',
    #                                          'scottish_areas.csv')
    council_areas_df_filepath = file_locations.loc['scottish_areas.csv']['location']
    council_areas_df = pd.read_csv(council_areas_df_filepath,
                                   index_col='District')
    council_areas_df.columns = ['postcodes', 'bounds']
    # load and import council areas dataframe created in data-restructuring.py

    return council_areas_df


def import_geojson(district):
    '''
    Import shape files for each local area.

    Output: dictionary containing featurecollection.
    '''

    url = file_locations.loc[f'{district}.json']['location']
    f = urlopen(url)
    data = json.loads(f.read())
    # import data and load using json format to python dictionary

    return data


def add_layer(geojson_data_dict, series, show, name):
    '''Add a layer of polygon data to the map.'''

    colorscale = branca.colormap.LinearColormap(['#800080',
                                                 '#FF0000',
                                                 '#FFA500',
                                                 '#FFFF00',
                                                 '#00FF00']
                                                ).scale(1, 100)
    # this colourscale is used to colour the scores on each polygon

    def create_style(feature):
        '''creates a style dictionary for the polygons'''

        rank = series.get(feature["properties"]["postcodes"], None)
        # get a rank value for that polygon's data

        # set rank to colour unless the value is empty
        # also set border style
        if rank is None:
            style_dict = {
                "fillOpacity": 0,
                "weight": 0.4,
                'fillColor': 'white'}
        else:
            style_dict = {
                "fillOpacity": 0.5,
                "weight": 0,
                "fillColor": colorscale(rank)}
        return style_dict

    def amend_highlight(feature):
        '''creates style dictionary for highlighted polygon'''

        rank = series.get(feature["properties"]["postcodes"], None)
        # get a rank value for that polygon's data

        highlight_dict = {'fillOpacity': 0 if rank is None else 0.7,
                          'weight': 2,
                          'fillColor': "#white" if rank is None
                          else colorscale(rank)}
        # sets style for highlights including lineweight, colour, opacity

        return highlight_dict

    # build geojson map with tooltip, name and styles
    return folium.GeoJson(geojson_data_dict,
                          style_function=create_style,
                          highlight_function=amend_highlight,
                          show=show,
                          name=name,
                          overlay=False,
                          tooltip=folium.features.GeoJsonTooltip(
                            fields=['postcodes'],  # show postcode when
                                                   # highlighted
                            aliases=["Postcode:  "]))


def load_map(geojson_data_dict, district, series_list, areas_df):

    # creates a new map item with cartodbpositron layer
    map = folium.Map(tiles=None, prefer_canvas=True)
    folium.TileLayer('cartodbpositron', control=False).add_to(map)

    # import bounds of local council area (convert from list first)
    bounds = ast.literal_eval(areas_df.loc[district]['bounds'])
    map.fit_bounds(bounds, padding=(-2, -2))

    # assigns layer name and display status
    layer_display_status = [False, False, True]
    layer_names = ['Index of Multiple Deprivation',
                   'Energy Preformance Mean for Postcode',
                   'Fuel Poverty Risk Rating']

    # for each layer in the list, add it to the map
    for i in range(len(series_list)):
        add_layer(geojson_data_dict,
                  series_list[i],
                  layer_display_status[i],
                  layer_names[i]).add_to(map)

    # add key with layer control
    folium.LayerControl(collapsed=False).add_to(map)

    # print map
    st_map = st_folium(map, width=700, height=450)


def main():

    # run functions to load the data required
    series_list = load_postcode_data()
    council_areas_df = load_council_area_df()

    # formattin the page
    st.title('Interactive Fuel Poverty Map')

    # display dropdown menu of different council aresa
    council_area_names_list = council_areas_df.index.to_list()
    council_area_names_list = [' '] + council_area_names_list
    requested_council_area = st.selectbox(
        'Which council area would you like to view?',
        council_area_names_list)

    if requested_council_area != ' ':
        # set council area requested
        selected_council_area_postcodes = council_areas_df.loc[
            requested_council_area]['postcodes']

        st.write('Building map. '
                 'There are a lot of polygons to load???so please be patient...')

        # import spatial polygon data and load map
        geojson_data_dict = import_geojson(requested_council_area)
        load_map(geojson_data_dict,
                 requested_council_area,
                 series_list,
                 council_areas_df)

        # give details on which postcodes we're seeing
        st.markdown(f'Showing postcodes {selected_council_area_postcodes} '
                    f'that contain homes in council area'
                    f' {requested_council_area}.'
                    f'\nFor more information on how we calculate our fuel '
                    f'poverty score, please see [the about section]'
                    f'(1_about.py).')


if __name__ == "__main__":
    main()
