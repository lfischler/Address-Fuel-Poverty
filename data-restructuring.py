# %%
# Import Libraries

import pandas as pd
import os
import numpy as np
import json
import geopandas


# %%
# Load the epc data and generate mean values

epc_data_filepath = os.path.join('source_data', 'D_EPC_data_2012-2022Q3')
# location of the epc data
epc_data_filepath_list = list(os.walk(epc_data_filepath))[0][2]
# get the name of every file in this folder and add to list

epc_data_csv_filelist = []
# create a list of filepaths for every file identified
for filename in epc_data_filepath_list:
    if filename.endswith(".csv"):
        epc_data_csv_filelist.append(os.path.join(epc_data_filepath, filename))

cols = ["Postcode", "Current energy efficiency rating"]
epc_data_df_full = pd.concat(map(pd.read_csv, epc_data_csv_filelist))
# create master dataframe with postcode epc data

epc_data_df_subset = epc_data_df_full[cols]
epc_data_df_postcode_mean_df = epc_data_df_subset.groupby("Postcode").mean()
epc_data_df_postcode_mean_df.columns = ["average_energy_efficiency_rating"]
epc_data_df_postcode_mean_df['average_energy_efficiency_rating'] = round(
    epc_data_df_postcode_mean_df['average_energy_efficiency_rating']
    ).astype(int)
# create mean value for all properties in each postcode


# %%
# Load the simd data

simd_data_filepath = os.path.join('source_data', 'postcode_simd.csv')
simd_full_df = pd.read_csv(simd_data_filepath)
# load the scottish index of multiple deprivation data

simd_df_subset = simd_full_df[['Postcode', 'SIMD2020v2_Rank']]
simd_df_subset = simd_df_subset.set_index('Postcode')
simd_df_subset['simd_percentile'] = (simd_df_subset['SIMD2020v2_Rank']
                                     / simd_df_subset['SIMD2020v2_Rank']
                                     .max())*100
# reformat dataframe and turn into percentile

simd_df_subset['simd_percentile'] = round(
    simd_df_subset['simd_percentile']).astype(int)
simd_df = simd_df_subset[['simd_percentile']]
# round to nearest integer and save

# %%
# process scottish postcode data

filepath = os.path.join('source_data', 'scotland_postcodes.csv')
postcodes_lookup_df = pd.read_csv(filepath)
# import data that links scottish postcodes with local authority

postcodes_in_use = postcodes_lookup_df[postcodes_lookup_df['In Use?'] == 'Yes']
postcodes_df = postcodes_in_use[['Postcode', 'District', 'Postcode district']]
postcodes_df = postcodes_df.set_index('Postcode')
# create dataframe of postcodes including their local authority

# %%
# Create full dataframe of all data per postcode

full_df = postcodes_df
full_df = full_df.join(simd_df)
full_df = full_df.join(epc_data_df_postcode_mean_df)
# join all dataframes so there's one line per postcode

full_df['fuel_poverty_rating'] = full_df['simd_percentile'] \
    .add(full_df['average_energy_efficiency_rating'])/2
# create fuel poverty rating by combining epc and simd values
# this will be exported

areas_df = pd.DataFrame(full_df
                        .groupby('District')['Postcode district']
                        .apply(lambda x: list(np.unique(x))))
# create overview dataframe wiht list of all postcodes in one area
# this will be exported, too

# %%
# import all postcode shape files and join

bigger_dict_dict = {}  # will store featurecollection data per authority
bounds_dict = {}  # will store the max and min co-ords for each district
gdf_dict = {}  # will store geodataframe for each district

for i in range(len(areas_df)):
    # for every district:

    list_of_postcodes = areas_df.iloc[i]['Postcode district']
    # get list of area postcodes in that district

    data_list = []
    for j in range(len(list_of_postcodes)):
        # iterate through the list of area postcodes

        filepath = os.path.join('source_data',
                                'geo_data',
                                f'{list_of_postcodes[j]}.geojson')
        # generate filepath for each area postcode to import geojson

        if not os.path.exists(filepath):
            # if this file doesn't exist, import blank
            f = open(os.path.join('source_data',
                                  'geo_data',
                                  '01_blank.geojson'))
        else:
            f = open(filepath)
            # import area postcode file

        data = json.load(f)
        data_list.append(data)
        # save geodata to list

    for j in range(len(data_list)):
        # for the length of all area postcodes imported:
        if j == 0:
            bigger_dict = data_list[j]
            # for the first one, use the first dictionary

        else:
            bigger_dict['features'].extend(data_list[j]['features'])
            # else add the features of each area postcode to the
            # featurecollection

    bigger_dict_dict[areas_df.index[i]] = bigger_dict
    # save that dictionary to a bigger dictionary of dictionaries

    gdf = geopandas.GeoDataFrame.from_features(bigger_dict, crs="EPSG:4326")
    # create geopandas dataframe
    gdf_dict[areas_df.index[i]] = gdf
    # save that to dictionary of geopandas dataframes

    list_bounds = gdf.total_bounds.tolist()
    # get the bounds of each area postcode
    bounds = [[list_bounds[1], list_bounds[0]],
              [list_bounds[3], list_bounds[2]]]
    # restructure the bounds to co-ordinate format
    bounds_dict[areas_df.index[i]] = bounds
    # save to dictionary of bounds lists

areas_df['bounds'] = bounds_dict
# save the bounds to the areas_df dataframe to be exported later


# %%
# simplify geojson (test - not working)

# from shapely.geometry import Point, LineString
# import matplotlib
# import topojson as tp


# # gdf = gdf_dict[areas_df.index[0]]

# topo = tp.Topology(gdf.to_crs({'init':'epsg:3857'}), prequantize=False)
# simple = topo.toposimplify(1).to_gdf()

# simple.plot()


# %%
# export geodata

for i in range(len(areas_df)):
    # for each district
    filename = f'{areas_df.index[i]}.json'  # create filename
    filepath = os.path.join('app', 'data', 'geo_data_by_district', filename)
    # set location for filepath

    with open(filepath, 'w') as f:
        json.dump(bigger_dict_dict[areas_df.index[i]], f)
        # export that local area geodata


# %%
# create list of postcodes in each local area

areas_df.to_csv(os.path.join('app', 'data', 'scottish_areas.csv'))
# export area summary data
full_df.to_csv(os.path.join('app', 'data', 'fuel_poverty_data.csv'))
# export main data to map
