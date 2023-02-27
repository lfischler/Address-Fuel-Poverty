# %%
# Import Libraries
import pandas as pd
import os
import numpy as np
import json
import geopandas
# from shapely.geometry import Point, LineString
# import matplotlib
# import topojson as tp


# %%
# Load the epc data and generate mean values

epc_data_filepath = os.path.join('source_data', 'D_EPC_data_2012-2022Q3')
# location of the epc data
epc_data_filepath_list = list(os.walk(epc_data_filepath))[0][2]
# get the name of every file in this folder and add to list

epc_data_csv_filelist = []
# create a list of filepaths for every file
for filename in epc_data_filepath_list:
    if filename.endswith(".csv"):
        epc_data_csv_filelist.append(os.path.join(epc_data_filepath, filename))

cols = ["Postcode", "Current energy efficiency rating"]
epc_data_df_full = pd.concat(map(pd.read_csv, epc_data_csv_filelist))
epc_data_df_subset = epc_data_df_full[cols]
epc_data_df_postcode_mean_df = epc_data_df_subset.groupby("Postcode").mean()
epc_data_df_postcode_mean_df.columns = ["average_energy_efficiency_rating"]
epc_data_df_postcode_mean_df['average_energy_efficiency_rating'] = round(
    epc_data_df_postcode_mean_df['average_energy_efficiency_rating']
    ).astype(int)


# %%
# Load the simd data
simd_data_filepath = os.path.join('source_data', 'postcode_simd.csv')
simd_full_df = pd.read_csv(simd_data_filepath)
simd_df_subset = simd_full_df[['Postcode', 'SIMD2020v2_Rank']]
simd_df_subset = simd_df_subset.set_index('Postcode')
simd_df_subset['simd_percentile'] = (simd_df_subset['SIMD2020v2_Rank']
                                     / simd_df_subset['SIMD2020v2_Rank']
                                     .max())*100
simd_df_subset['simd_percentile'] = round(
    simd_df_subset['simd_percentile']).astype(int)
simd_df = simd_df_subset[['simd_percentile']]

# %%
filepath = os.path.join('source_data', 'scotland_postcodes.csv')
postcodes_lookup_df = pd.read_csv(filepath)
postcodes_in_use = postcodes_lookup_df[postcodes_lookup_df['In Use?'] == 'Yes']
postcodes_df = postcodes_in_use[['Postcode', 'District', 'Postcode district']]
postcodes_df = postcodes_df.set_index('Postcode')

# %%
# Create full dataframe
full_df = postcodes_df
full_df = full_df.join(simd_df)
full_df = full_df.join(epc_data_df_postcode_mean_df)
full_df['fuel_poverty_rating'] = full_df['simd_percentile'] \
    .add(full_df['average_energy_efficiency_rating'])/2

areas_df = pd.DataFrame(full_df
                        .groupby('District')['Postcode district']
                        .apply(lambda x: list(np.unique(x))))

# %%
# import all postcode shape files and join
bigger_dict_dict = {}
bounds_dict = {}
gdf_dict = {}
for i in range(len(areas_df)):
    list_of_postcodes = areas_df.iloc[i]['Postcode district']

    data_list = []
    for j in range(len(list_of_postcodes)):
        filepath = os.path.join('source_data',
                                'geo_data',
                                f'{list_of_postcodes[j]}.geojson')
        if not os.path.exists(filepath):
            f = open(os.path.join('source_data',
                                  'geo_data',
                                  '01_blank.geojson'))
        else:
            f = open(filepath)

        data = json.load(f)
        data_list.append(data)

    for j in range(len(data_list)):
        if j == 0:
            bigger_dict = data_list[j]

        else:
            bigger_dict['features'].extend(data_list[j]['features'])

    bigger_dict_dict[areas_df.index[i]] = bigger_dict

    gdf = geopandas.GeoDataFrame.from_features(bigger_dict, crs="EPSG:4326")
    gdf_dict[areas_df.index[i]] = gdf

    list_bounds = gdf.total_bounds.tolist()
    bounds = [[list_bounds[1], list_bounds[0]],
              [list_bounds[3], list_bounds[2]]]
    bounds_dict[areas_df.index[i]] = bounds

areas_df['bounds'] = bounds_dict
# save the bounds to the areas_df dataframe to be exported later


# %%
# simplify geojson (test - not working)

# gdf = gdf_dict[areas_df.index[0]]

# topo = tp.Topology(gdf.to_crs({'init':'epsg:3857'}), prequantize=False)
# simple = topo.toposimplify(1).to_gdf()

# simple.plot()


# %%
# export geodata
for i in range(len(areas_df)):
    filename = f'{areas_df.index[i]}.json'
    filepath = os.path.join('app', 'data', 'geo_data_by_district', filename)

    with open(filepath, 'w') as f:
        json.dump(bigger_dict_dict[areas_df.index[i]], f)


# %%
# create list of postcodes in each local area
areas_df.to_csv(os.path.join('app', 'data', 'scottish_areas.csv'))
full_df.to_csv(os.path.join('app', 'data', 'fuel_poverty_data.csv'))
