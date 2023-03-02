import streamlit as st

st.markdown('''# About
Thank you for visiting the fuel poverty community data hub webapp. This webapp provides a free service allowing users to explore the possible risk of fuel poverty at different postcodes in Scotland.

A household is in fuel poverty when over 10% of its adjusted income is spent on heating their home (Scottish Government, 2019). For the purposes of calculating a fuel poverty risk score, we use a predicted risk derived from the combination of the average energy performance certificate rating for that postcode and its rank on the Scottish Index of Multiple Deprivation.

This project is open source and is licenced under [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). We encourage conversation around, and collaboration on future iterations of this work. Please check out the [Address Fuel Poverty GitHub](https://github.com/lfischler/Address-Fuel-Poverty) repository for more information on how you can take part.

#### Energy Performance Certificate Dataset (EPC)
The webapp uses the Scottish Government's publicly available Energy Performance Certificate dataset. This dataset contains the data from all energy performance certificates that have been carried out since 2012. An EPC must be completed when a building is bought, sold, or rented to tenant.

We've mapped out the mean EPC score for each postcode using only the overall scores. For more details on EPC scores please see the [Scottish Government Website](https://www.mygov.scot/energy-performance-certificates).

#### Scottish Index of Multiple Deprivation Dataset (SIMD)
The Scottish Index of Multiple Deprivation dataset is used as a measure of deprivation to compile the fuel poverty risk score. It is a score assigned by the Scottish Government to analyse deprivation and its effects on households.

For more information about the Scottish Index of Multiple Deprivation Score and how it is calculated, please see the [Scottish Government Website](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/).

#### Our Fuel Poverty Risk Ratings
We use the two data sources above to give postcodes a unique fuel poverty risk rating. This risk rating is calculated by generating the mean of the percentile EPC rating and the percentile SIMD rating to directly compare the two biggest factors in fuel poverty.

## Fuel Poverty Action
For more details on fuel poverty and what you can do to fight it, please check out the following activist resources:

- [Fuel Poverty Action](https://www.fuelpovertyaction.org.uk/) - UK Wide
- [End Fuel Poverty Coalition](https://www.endfuelpoverty.org.uk/) - UK Wide
- [Energy Action Scotland](https://www.eas.org.uk/) - Scotland
- [The Scottish Government's Page on Fuel Poverty](https://www.gov.scot/policies/home-energy-and-fuel-poverty/fuel-poverty/)

**References**
- Scottish Government (2019) _Scottish House Condition Survey: 2019 Key Findings_.
- Scottish Government (2020) _Scottish Index of Multiple Deprivation 2020 [Dataset]_. Available at: [https://statistics.gov.scot/data/scottish-index-of-multiple-deprivation](https://statistics.gov.scot/data/scottish-index-of-multiple-deprivation) (Accessed: 1 March 2023).
- Scottish Government (2022) _Domestic Energy Performance Certificates - Q3 2022 [Dataset_. Available at: [https://statistics.gov.scot/data/domestic-energy-performance-certificates](https://statistics.gov.scot/data/domestic-energy-performance-certificates) (Accessed: 1 March 2023).''')
