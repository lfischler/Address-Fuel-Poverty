# Address Fuel Poverty
*An interactive and collaborative data visualisation project for activist and community groups fighting fuel poverty in Scotland*.

Please access the live webapp at [address-fuel-poverty.streamlit.app](https://address-fuel-poverty.streamlit.app/).

---

## Table of Contents

**Academic**
- [Project Motivation](#project-motivation)
- [Project Description](#project-description)
- [Choice of Technologies](#choice-of-technologies)
- [Challenges and Suggested Contributions](#challenges-and-suggested-contributions)

**Technical**
- [Installation](#installation)
- [Using the Dashboard](#using-the-dashboard)
- [How to Contribute](#how-to-contribute)
- [Licence](#licence)
- [Credits](#credits)

## Project Motivation
Just under one quarter of all homes in Scotland were estimated to be in fuel poverty in 2019 (Scottish Government, 2019). With the cost of living increasing rapidly, many more households will be at risk across Scotland (Brooks, 2022) if action isn’t taken now.

The main cause of fuel poverty is poor building condition and inadequate insulation. When this is combined with low household income, a property becomes at risk (Energy Action Scotland, no date). Due to the complexity of these overlapping factors, fuel poverty must be examined as a temporal and spatial issue that exists due to historic lack of funding (Dowson _et al._, 2012) and structural inequalities. Activist organisations, such as Fuel Poverty Action, tailor their work accordingly. They campaign across multiple scales including public demonstrations (Glasgow Times, 2022); campaigning to government ministers and the media (Inform My Opinion, no date)2015) and offering targeted support to individuals and at-risk communities (Fuel Poverty Action, no date).

This project makes use of a new medium for such activism: data.

## Project Description

Data has what Renzi and Langolis describe as "transformative and affective potential". It offers the possibility to shape how we see things and, when in the hands of activists, can be used to trigger societal change (2020).

The Address Fuel Poverty webapp builds on Energy Action Scotland’s work creating a National Fuel Poverty Map (2021) by adding the ability to zoom beyond just regional level down to individual postcode level making the data tangible, relatable, and specific. This mapping process aims to highlight key spatial inequalities with regards to fuel poverty such as a risk to households in rural and exposed areas (who often have less capacity and ability to participate in development conversations (Mansuri, 2013)) and the impact of local issues and contexts.

Each postcode has been assigned a fuel poverty risk score by combining data from two publicly available datasets: the mean score of all Energy Performance Certificates (Scottish Government, 2022) since 2012 at that postcode; and its Scottish Index of Multiple Deprivation score (Scottish Government, 2020). This data is accessed through an interactive postcode lookup page (as inspired by the Central Office of Public Interest’s project *_addresspollution.org*_ (2022)_)_ and an interactive map.

The creation of data activist work of this kind can elevate activist practices in a medium that is “credible and legible" to policymakers (Blacker, 2021) whilst also offering the opportunity to inform grassroots groups in targeting their work in communities to those most at risk.

### Choice of Technologies
Address Fuel Poverty depends on a series of open-source technologies:

- [The Python programming language]([https://www.python.org/about/](https://www.python.org/about/)) an packages numpy and pandas;  
- [The Streamlit platform](https://streamlit.io/);  
- [The Folium geospatial maps based on leaflet.js](https://python-visualization.github.io/folium/).

We have decided to use the Streamlit platform due to its ease of use and simple integration with the popular python language, removing the requirement for high levels of data literacy. This, in turn, removes some of the labour associated with activist practices (Kidd, 2019) that can exclude individuals suffering from existing injustices from taking part (Mansuri, 2013).

The decision to create an interactive map was informed by Rubel et al.’s work teaching spatial justice to children. Their project aims to shift analysis of poverty to be understood within the context of place itself and how spatial relations produce and reproduce poverty. Rubel et al. explore injustices at different scales, and how they interact. In their work they begin at city level and end at the level of the individual (2016); we have instead created a Folium choropleth map which gives a birds-eye-view over a whole region; yet can be zoomed down to postcode level detail where individual neighbourhoods can be examined. This level of detail allows activists to understand the impacts different factors might be having on fuel poverty at different scales to generate specific responses. It also addresses the challenges of getting data about specific locations, in particular rural and isolated locations, to inform decisions about development projects (Gunderson, 2023).

Data activism brings the performativity of data out of the hands of the powerful and well-resourced and into the hands of non-powerful (Renzi and Langlois, 2020). The decision to make this project open source, with the code freely available on GitHub, allows anyone to see and assess how the results are calculated and visualised. It gives the option for experts, practitioners, and people with lived experience to contribute towards it or remix it into new work. We hope that, by bringing open source practices to fuel poverty work, we can engage and re-engage communities in a space for participation that is novel and comprised of “unlikely networks” (Erasmus, 2023).

This decision was informed by Kidd’s work studying data activism and documenting the way it creates connection, identity and a sense of possibility to enact change on their situation (2019). Such data activist projects allow for the shaping of data as a medium that has agency in itself (Blacker, 2021) and can help to not only inform, but build new realities (Renzi and Langlois, 2020).

## Challenges and Suggested Contributions
The first instantiation of this work is an exploration in the accessibility of data to grassroots activist groups. It explores the use of a data dashboard technology that offers quick and easy visualisation of data in an interactive and shareable format. These suggested features are just a few of the possible directions we imagine that the development of the platform could take:

- Loading postcode level geospatial data is very resource intensive and slow within the Streamlit platform. Any input on optimisation is appreciated.
- Revisions to the calculation we’ve used for each postcode’s fuel poverty score such as incorporating fuel source (Boardman, 2009) and regional fuel prices.
- Option for users and collaborators to add local accounts of fuel poverty issues as notes embedded within each postcode’s data. Such notes would serve to complement the numeric data by adding additional depth and highlighting information that may not be observable due to the means of data capture (Blacker, 2021).

## How to Contribute
This code has been written and formatted with collaboration in mind. We see the act of collaborating in an open-source format as political; a fundamental part of data activist practices.

Should you wish to contribute to this work, please keep in mind the key principles with which this code has been written:

1. Comments allow others to quickly understand code. In our collaborative process, we see the code itself as a form of "lab notebook" with comments documenting not only what's happening in the code but also the reasoning behind that (Lee, 2018).

2. Use of the Git Version Control System allows for the testing and addition of new features without affecting the functionality of the code itself. We see version control as a key part of the collaborative process to ensure a transparent way of working that's reproducible and accessible (Blischak, Davenport and Wilson, 2016). We request that all collaborators use branches to merge in their alterations; or forks to develop other directions or applications.

## Bibliography
- _addresspollution.org_ (2022) _addresspollution.org_. Available at: https://addresspollution.org/ (Accessed: 1 March 2023).
- Blacker, S. (2021) ‘Strategic translation: pollution, data, and Indigenous Traditional Knowledge’, _Journal of the Royal Anthropological Institute_, 27(S1), pp. 142–158. Available at: https://doi.org/10.1111/1467-9655.13485.
- Blischak, J.D., Davenport, E.R. and Wilson, G. (2016) ‘A Quick Introduction to Version Control with Git and GitHub’, _PLOS Computational Biology_, 12(1), p. e1004668. Available at: https://doi.org/10.1371/journal.pcbi.1004668.
- Boardman, B. (2009) _Fixing Fuel Poverty: Challenges and Solutions_. London: Routledge, pp. xxiii–xxiii. Available at: https://doi.org/10.4324/9781849774482.
- Brooks, L. (2022) ‘Don’t let “warm banks” become as vital as food banks, Scottish charities urge’, _The Guardian_, 12 October. Available at: https://www.theguardian.com/uk-news/2022/oct/12/warm-banks-fuel-poverty-crisis-scotland (Accessed: 1 March 2023).
- Dowson, M. _et al._ (2012) ‘Domestic UK retrofit challenge: Barriers, incentives and current performance leading into the green deal’. Available at: https://doi.org/10.1016/j.enpol.2012.07.019.
- Energy Action Scotland (2021) _Press Release: Scottish Fuel Poverty Map_. Available at: https://www.eas.org.uk/scottish-fuel-poverty-map (Accessed: 28 February 2023).
- Energy Action Scotland (no date) _Fuel Poverty Overview_. Available at: https://www.eas.org.uk/fuel-poverty-overview (Accessed: 28 February 2023).
- Erasmus, C.-L. (2023) ‘Case Study: Accountability Lab’. _Inclusive Society_, University of Edinburgh, 23 January.
- Fuel Poverty Action (no date) _About Fuel Poverty Action_, _Fuel Poverty Action_. Available at: https://www.fuelpovertyaction.org.uk/about-us/ (Accessed: 28 February 2023).
- Glasgow Times (2022) ‘Activists protest in Scottish Power over rising energy bills’, _Glasgow Times_, 3 December. Available at: https://www.glasgowtimes.co.uk/news/scottish-news/23168097.activists-protest-scottish-power-glasgow-rising-bills/ (Accessed: 28 February 2023).
- Gunderson, K. (2023) ‘Case Study: Grand Bequest’. _Inclusive Society_, University of Edinburgh, 24 January.
- Inform My Opinion (no date) ‘Inform My Opinion - IMO/REAL MEDIA: Grassroots campaigns - Fuel Poverty Action’. Available at: https://podcasts.google.com/feed/aHR0cHM6Ly9hdWRpb2Jvb20uY29tL2NoYW5uZWxzLzQwNDk2NDMucnNz/episode/dGFnOmF1ZGlvYm9vLmZtLDIwMTUtMTItMzA6L2Jvb3MvNDAwNTExNQ (Accessed: 1 March 2023).
- Kidd, D. (2019) ‘Extra-activism: counter-mapping and data justice’, _Information, communication & society_, (7), pp. 954–970. Available at: https://doi.org/10.1080/1369118X.2019.1581243.
- Lee, B.D. (2018) ‘Ten simple rules for documenting scientific software’, _PLOS Computational Biology_, 14(12), p. e1006561. Available at: https://doi.org/10.1371/journal.pcbi.1006561.
- Mansuri, G., and Vijayendra Rao (2013) _Localizing Development : Does Participation Work?. Policy Research Report_. International Bank for Reconstruction and Development / The World Bank. Available at: https://openknowledge.worldbank.org/bitstream/handle/10986/11859/9780821382561.pdf?sequence=1&isAllowed=y.
- Peterson, K. (2014) ‘The GitHub Open Source Development Process’.
- Renzi, A. and Langlois, G. (2020) ‘Renzi, A. and Langlois, G. (2015) “Data / Activism” Elmer, G. et al. (eds.)Compromised Data: From social media to Big Data, , London: Bloomsbury, pp. 202–225.’, in, pp. 202–225.
- Rubel, L.H. _et al._ (2016) ‘Teaching Mathematics for Spatial Justice: An Investigation of the Lottery’, _Cognition and instruction_, (1), pp. 1–26. Available at: https://doi.org/10.1080/07370008.2015.1118691.
- Scottish Government (2019) _Scottish House Condition Survey: 2019 Key Findings_.
- Scottish Government (2020) _Scottish Index of Multiple Deprivation 2020 [Dataset]_. Available at: https://statistics.gov.scot/data/scottish-index-of-multiple-deprivation (Accessed: 1 March 2023).
- Scottish Government (2022) _Domestic Energy Performance Certificates - Q3 2022 [Dataset_. Available at: https://statistics.gov.scot/data/domestic-energy-performance-certificates (Accessed: 1 March 2023).

## Installation
To run our Streamlit app on your own device please run the following commands in your terminal
1. Clone the repository
```bash
git clone https://github.com/lfischler/Address-Fuel-Poverty
```
2. Install the required dependencies 
```bash
pip install -r requirements.txt
```
3. Launch the app
```bash
streamlit run app/home.py
```
4. Once the app is running, you can view it in your web browser at `http://localhost:8501`.
Note: If you encounter any errors during installation or setup, please consult the [Streamlit documentation](https://docs.streamlit.io/) for troubleshooting tips and support.


## Using The Dashboard
1. To use the *Postcode Lookup* feature, please enter the required postcode in the box for summary metrics giving an indication of fuel poverty risk.
2. To use the *Interactive Map* feature, a local council area must be selected from the list (please note that this page can be very slow to load due to the complexity of data being displayed). The map can be zoomed and layers can be added or removed depicting the data available for each postcode.
3. The webapp also contains further reading and key definitions on how data has been sourced and calculated on its *About* page.  

## How to Contribute
If you'd like to modify the app to suit your specific needs, you can do so by editing the `home.py` file and the files within the `pages` folder. Should you wish to download the original data from which the app was built, please use the `data-restructuring.py` file for reference on how the app's data files were built.

This code has been written and formatted with collaboration in mind. We see the act of collaborating using an open-source and agreed upon framework as fundamental part of data activist practices

Should you wish to contribute to this work, please keep in mind the key principles with which this code has been written:
1. Comments allow others to quickly understand code and how it is structured; they serve to document not only what's happening in the code but also the reasoning behind it. In our collaborative process, we see the code itself as a form of "lab notebook" with comments serving as the notes and workings (Lee, 2018). 
2. Use of the Git Version Control System allows for the testing and addition of new features without affecting the functionality of the code itself. We see version control as a key part of the collaborative process to ensure rationale is documented as part of a "transparent" way of working that's reproducible and more accessible to people to collaborate (Blischak, Davenport and Wilson, 2016). We request that all collaborators use branches to merge in their alterations; or forks to develop other directions or applications. The use of detailed commit messages is encouraged in collaborating and editing this code (Blischak, Davenport and Wilson, 2016).

### Attribution
We value the contributions of all our contributors, and we recognize their work through attribution. If you make a significant contribution to our project, we will acknowledge your contribution in the project documentation and release notes.

## Licence
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
You are free to share and adapt this content under the condition that you give appropriate credit; link back to the licence and detail the changes made. If you build upon this material, you must share your contributions under the same lincence. For more details please consult the [Creative Commons website](https://creativecommons.org/licenses/by-sa/4.0/).

## Credits
This project would like to acknowledge the contributions of:
- the Streamlit developers for the creation of your platform and the other platforms that made this possible;
- Luke Fraser of North Ronaldsay Community Development Trust and Aquatera for the conversations that led to mapping fuel poverty; and the benefits for grassroots organisations;
- [Chris Page](https://github.com/cspagemarine) for your support in getting this work hosted online.