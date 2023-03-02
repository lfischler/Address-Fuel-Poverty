# Address Fuel Poverty
*An interactive and collaborative data visualisation project for activist and community groups fighting fuel poverty in Scotland*.

Please access the live webapp at [address-fuel-poverty.streamlit.app](https://address-fuel-poverty.streamlit.app/). You can also find a video of the webapp in action [at this link].

---

## Table of Contents

**Academic**
- [Project Motivation](#project-motivation)
- [Project Description](#project-description)
- [Challenges and Suggested Contributions](#challenges-and-suggested-contributions)

**Technical**
- [Installation](#installation)
- [Using the Dashboard](#using-the-dashboard)
- [How to Contribute](#how-to-contribute)
- [Licence](#licence)
- [Credits](#credits)

## Project Motivation
Just under one quarter of all homes in Scotland were estimated to be in fuel poverty in 2019 (Scottish Government, 2019). With the cost of living increasing sharply, many more households are becoming at risk across the country (Brooks, 2022).
The main cause of fuel poverty is poor building condition and inadequate insulation. When this is combined with low household income, a property becomes at risk (Energy Action Scotland, no date). Due to the complexity of these overlapping factors, fuel poverty must be examined as a temporal and spatial issue that exists due to historic lacks of funding (Dowson et al., 2012) and structural inequalities. Activist organisations like Fuel Poverty Action are aware of this and tailor their work accordingly across multiple scales including public demonstrations (Glasgow Times, 2022); campaigning to government ministers and the media (Inform My Opinion, no date)2015) and offering targeted support to individuals and at-risk communities (Fuel Poverty Action, no date). This project makes use of a new medium for such activism: data. 

## Project Description
Data has what Renzi and Langolis describe as "transformative and affective potential". It offers the possibility to shape how we see things and, when used in the hands of activists, can be used to trigger societal change (2020). 
The Address Fuel Poverty webapp builds on Energy Action Scotland’s work creating a National Fuel Poverty Map by additing the additional functionality of  zooming into postcode level to make this work tangible, relatable and specific to local issues and knowledges. This mapping process aims to highlight key spatial inequalities with regards to fuel poverty, such as the unexpected risk to households in the Scottish islands.
Each postcode is assigned a fuel poverty risk score  by combining data from two publicly available datasets: the mean score of all Energy Performance Certificates (Scottish Government, 2022) at that postcode and its Scottish Index of Multiple Deprivation score (Scottish Government, 2020). This data is then made accessible through an interactive postcode lookup page (as inspired by the world of the Central Office of Public Interest’s project *addresspollution.org* (addresspollution.org, 2022)) and an interactive map. This project moves a step beyond the affordances of standard statistical analysis processes and analysis in geo-spatial data software because this platform affords interactivity to users with no data skills whatsoever 
By making the data specific down to postcode level, this project centres the focus on the rural and isolated communities who are most at risk and simultaneously least likely to have capacity and ability to participate  in development conversations (Mansuri, 2013). It aids in avoiding situations where complexity is washed over or hidden
The creation of data activist works of this kind can elevate activist practices in a medium that is “credible and legible" to policymakers (Blacker, 2021) whilst also offering the opportunity to inform grassroots groups in targeting their work in communities to those most at risk.

### Choice of Technologies
Data activism brings the performativity of data, and its agency, out of the hands of the powerful and well-resourced and into the hands of non-powerful (Renzi and Langlois, 2020). This project does that by firstly creating easily accessible map and secondly being implemented within the context of the open source movement with its processes for participation.
We have decided to use the Streamlit platform due to its ease of use and simple integration with the increasingly popular python language. This removes some of the requirement for high levels of data literacy as the Streamlit platform is accessible to those with beginner to intermediate Python skills. The ease-of-use also removes some of the labour associated with activist practices (Kidd, 2019).
The decision to create an interactive map was informed by Rubel et al.’s work teaching spatial justice to children (2016). We embody a "critical spatial perspective" as Rubel et al. describe in their paper "Teaching Mathematics for Spatial Justice" which helps shift analysis of poverty away from just temporal relations between people alone but seeing these within the context of place itself and how this produces and reproduces poverty (2016). In the creation of a choropleth map, a clear overview can be seen when zoomed out to maximum level. Rubel et al. explore the concept of scale in exploring injustices at different levels, and how they interact (2016). In their case they use level from city down to body but this map takes country wide view and allows the zoom to street level. At narrow scale, we can see individual neighbourhoods in a rural town that suffer worse; but at a larger scale we can see that remote, rural and island communities are at the highest risk in Scotland. Understand the varieties of impacts different factors might be having on fuel poverty at different scales to generate specific responses.The decision to make this project open source allows others to see how it’s made and contribute towards it with their own issues and experiences., The decision was informed by Kidd’s work studying an example of data activism and documenting the way it creates connection, a sense of identity and a sense of agency within the communities contributing (2019). Beyond the merits of having analysis reviewed and improved by countless experts, practitioners and people with lived experience; such data activist projects allow for the shaping of a medium that has agency in itself (Blacker, 2021) and can help to not only inform, but build new realities (Renzi and Langlois, 2020).

## Challenges and Suggested Contributions
The creation of the first instantiation of this work is a meditation on the accessibility of data to grassroots, activist groups. It explores the use of a data dashboard technology (Streamlit) that offers quick and easy visualisation of data in an interactive, and shareable format. These suggested features are just a few of the possible directions we imagine that the development of the platform could take.
- We welcome revisions to our use of the calculation we’ve used to create each postcode’s fuel poverty score. In future, we hope to incorporate additional information such as fuel source  (Boardman, 2009) and regional fuel prices.
- We would also like to build the option for users and collaborators to add local accounts of fuel poverty issues as notes embedded within each postcode’s data. Such notes would serve to complement the numeric data by adding additional depth, meaning, and highlight information that may not be observable due to the means of data capture (Blacker, 2021). 


## Installation
To run our Streamlit app on your own device please run the following commands in your terminal
1. Clone the repository
```bash
git clone https://github.com/lfischler/Address-Fuel-Poverty
cd Address-Fuel-Poverty
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
This code has been written and formatted with collaboration in mind. We see the act of collaborating using an open-source and agreed upon framework as fundamental part of data activist practices.
Should you wish to contribute to this work, please keep in mind the key principles with which this code has been written:
1. Comments allow others to quickly understand code and how it is structured; they serve to document not only what's happening in the code but also the reasoning behind it. In our collaborative process, we see the code itself as a form of "lab notebook" with comments serving as the workings and thinking behind it (Lee, 2018). 
2. Use of the Git Version Control System allows for the testing and addition of new features without affecting the functionality of the code itself. We see version control as a key part of the collaborative process to ensure rationale is documented as part of a "transparent" way of working that's reproducible and more accessible to people to collaborate (Blischak, Davenport and Wilson, 2016). We request that all collaborators use branches to merge in their alterations; or forks to develop other directions or applications. The use of GitHub also has the added benefit that activity is associated with profiles that allow us to understand our contributors through their interests, previous work and wider contexts (Peterson, 2014).

**Attribution**
We value the contributions of all our contributors, and we recognize their work through attribution. If you make a significant contribution to our project, we will acknowledge your contribution in the project documentation and release notes.

## Licence
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
You are free to share and adapt this content under the condition that you give appropriate credit; link back to the licence and detail the changes made. If you build upon this material, you must share your contributions under the same lincence. For more details please consult the [Creative Commons website] (https://creativecommons.org/licenses/by-sa/4.0/).

#### Data Licences
Please find datails of the licences of the data used to build this app in the [DATALICENCE.md](licence.md) file.

## Credits
This project would like to acknowledge the contributions of:
- the Streamlit developers for the creation of your platform and the other platforms that made this possible;
- Luke Fraser of North Ronaldsay Community Development Trust and Aquatera for the initial conversations over the last months that gave the idea of mapping fuel poverty and the impacts that it might have; and the benefits for grassroots organisations working on this data;
- [Chris Page](https://github.com/cspagemarine) for your support in getting this work hosted online.