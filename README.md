
<h1 align="center" id="heading"> <span style="color:red"> <em> Impact of Recreational Activities on Public Health: </em> <br> Heart Disease and Public Facilities </span> </h1>
<h3 align="center" id="heading"> 12 October 2023 <br> 
<em> Python, Big Data, and Databases (ECO395m)  </em> <br> <h3>
<h3 align="center" id="heading"> Bevo’s Group: Xiangmeng Qin, Tianyu Wang, Meilin Li, Yueting Zhang, & Machete Baker
 </h3>
  

## Introduction & Background

In recent years, health and wellness have become focal points for many communities, with heart disease mortality rates often used as a benchmark for overall community health.  Its onset can be influenced by a myriad of factors, including diet, genetics, and notably, physical activity.  Outdoor recreational facilities, such as parks, trails, and sports complexes, play a crucial role in promoting physical activity among residents of an area.  The accessibility, quality, and popularity of these facilities can potentially impact the overall health outcomes of a community.


However, the direct relationship between heart disease mortality and the prevalence and popularity of such facilities has not been extensively studied.     Our project seeks to explore a potentially overlooked connection: "Is there any relationship between the heart disease mortality rates and the participation of outdoor activity facilities within a state?”   Do states with more popular outdoor facilities exhibit lower heart disease mortality rates due to increased physical activity among their residents?  Or do other factors overshadow this potential correlation?  By exploring this relationship, we aim to provide valuable insights that could influence future urban planning, healthcare policies, and community wellness programs.


## Source of data
Our sources of data consist of 2 sets. Firstly, we include outdoor activity facilities across the United States, as taken from the Recreational.Gov site. (Please see references for the link to the 2 data sets via URL / Web.) The Recreation Information Database (RIDB) serves as a valuable resource for the public, offering a central hub for accessing information on recreational activities and destinations across the United States. It stands as an official and comprehensive platform catering to the needs of countless visitors to federal lands, historical sites, museums, and various other points of interest. It is a public API scraping site. However, we limit our analysis to states that are basically in the same climate and region. We argue that it contains similar types of outdoor activities, and thus can be comparable. (Please see methodology for how to retrieve the data from this site for reproducibility.)

The list of states we have selected are that among the Pacific Northwest (PNW):
Washington,
Oregon,
Idaho,
Montana,
and Wyoming.
The details of facilities are captured from the recreation.gov, we scraped through API and selected aforementioned 5 states, at first using longitude and latitude by Geopy package, but then we were able to match on state level.

Secondly, the CDC website is designed to provide users with quick and easy access to the wide range of medical information and data available. The site is home to the latest news, information, and publications from the Center, as well as an extensive data archive accessible to the public. Heart disease mortality data among US adults by states are taken from the CDC website—Centers for Disease Control and Prevention, and then focused/divided by states (by use of CSV directly).

We focus on Heart mortality, number of facilities, facility ID, state, and the number of entries in terms of columns of data.

We retrieved this data in the month of October of the year 2023. The information on the CDC and Recreational site is not subject to copyright, and is in the public domain.



## Running the code
In order to examine the impact of recreational activities on public health, we are looking to pull data from the recreational.gov website in the form of API Scraping, and information from the CSV on Heart Disease Mortality rates by National Health Statistics Reports. Our code is written to run in Python 3.11. The required Python packages are listed in the requiredments.txt file. The code is kept inside “main.py” under folder “code”, and should be run from that file. The data set on Heart Disease Mortality can be pulled from the folder called “data”. Thus, the command for running the main.py would be: python code/main.py. This command will call three files, main.py, sort_test.py and data_reform_test.py. The script will retrieve data related to heart disease mortality among U.S. adults and recreational facilities in specific states (WA, OR, ID, MT, WY) using API calls. The sort_test.py and data_reform_test.py files will scrape the data from api, clean and write it into a csv file which contains the number of activities normalized by population and the heart disease mortality rate. Upon successful execution, you will find the sample_result.csv in the “data” directory. Please note that this code is designed to retrieve and process data based on specific states and API endpoints. Before running the code, please replace the api key config.json with the authorized api key. Our api key was requested from the recreational government site (https://ridb.recreation.gov/docs#/Facilities). In order to run this code, you will need to replace the API Key variable with your very own. For the usage of recreation data api, you are also able to edit the amount of facilities passed through the code. The “limit” refers to this, and can enter anywhere from 1 to 1000. Considering computer capability and execution time, we set the limit to 100 after careful assessment. For a limit of 100, the possible execution time is 2-3 minutes, varies depend on different equipment capability. After getting the csv output from running code/main.py, you may then process to generate beautiful histogram and scatter plot by running python code/scatter_plot.py and python code/histogram_pretty.py. Again, the result .png files will be saved in data folder. 





## Methodology

In this section, we will outline the methodology used to investigate the relationship between heart disease mortality and the popularity of outdoor activity facilities by state. The study is divided into some key steps. Firstly, for Heart Disease Mortality Data– the dataset is already relatively structured. However, we perform necessary data validation to ensure its accuracy. We filter the dataset to focus on relevant variables, such as mortality rates, and geographical coordinates. Additionally, for our second dataset, outdoor activity facilities data, we API scrape by retrieving the number of outdoor activity facilities by its count and location (counties, state, and long./latitude were available). The API site provides numerous data, and thus we are only interested in the facility count, the type of activity, and the location. The script proceeds to make API requests to the Recreation Information Database (RIDB) using the requests library. It sends requests to the RIDB API to fetch information about outdoor activity facilities in the same selected states. For each state in the Pacific Northwest (PNW), that we define as Washington (WA), Oregon (OR), Wyoming (WY), Idaho (ID), and Montana (MT),  the script retrieves facility data, including information about outdoor activities. This data is converted to JSON format, and the JSON responses are collected and stored in the api_data list. The location was given in terms of latitude and longitude/counties/zips/states across the sets. We also are given a range of states across the United States, but are only investigating that of the Pacific NorthWest. We argue that activity popularity is similar among states of regional similarity. We then categorize these facilities (their IDs) and activities (types placed in a dictionary). We merge the cleaned heart disease mortality dataset with the scraped outdoor activity facilities dataset based on geographical location. This integration enables us to analyze the relationship between heart disease mortality rates and the popularity of outdoor activities by state. After the data gets integrated, normalizing for population, we conduct statistical analyses to explore potential relationships, specifically correlation analysis.




## Limitations of the data

This analysis could be improved in several ways:

The precise selection of domains. We simply choose The Pacific Northwest by longitude and latitude, but in the real world the circumstances could be more complicated. Reasonable and more precise method to decide the region would be helpful to improve the quality of this analysis.

More states contained. We selected only 5 states to display if there are any relationships between the two items, but it would be more clear and conclusive for this analysis to contain more states, 10 states, 20 states, etc.

More factors about outdoor activities. We choose the facilities of outdoor activities as one item to measure the outdoor activity, but there are huge factors out of our consideration like outdoor sports without facilities, and so on. Adding more outdoor factors could raise the robustness of this analysis.

Another limitation is that California’s (CA) data made the code super slow to run effectively, (because its associated data is incredibly large,) so we changed CA to Wyoming (WY). We thus had to redefine the region, as the PNW is now defined as WA, OR, ID, MO, and WY (instead of CA). However, part of the write is up to us to define what the PNW is, as some people define it including canada, northern california, with wyoming, or just WA / OR/ ID.

The other limitation is the speed in which the code can run - the API scraping takes awhile from the public, open domain, free government site, and retrieving hundreds of thousands of data points can take a long time. Thus, we have to limit the amount of facilities we pass through the code per state. If we had more time, better processors, and better more exclusive access, we could pass through more data and get na even more complete picture/analysis of our research question.

## Analysis & Results



![scatter plot](data/scatter_plot.png)

By examining the scatter, we can discern the relationship between participation rates in outdoor activities and the mortality rate due to heart attacks. In this analysis, we've focused on three specific activities – camping, fishing, and hiking – within the same state, using consistent colors to enhance the visual clarity of this relationship.

Our observations reveal a somewhat unexpected trend: higher participation rates in these outdoor activities appear to weakly coincide with elevated heart attack mortality rates. This finding seems to challenge the conventional notion that engagement in outdoor activities generally promotes better health.

Several factors may underlie this counterintuitive result. One plausible explanation is that outdoor activities inherently entail a higher degree of risk, which could contribute to the elevated mortality rates. Consequently, it is advisable to exercise caution when recommending outdoor activities to individuals who may have underlying heart conditions. While these activities can offer numerous health benefits, it's crucial to consider an individual's health status and potential risks before encouraging excessive participation.



![scatter plot](data/histogram2.png)

To study the effect by different activities, the histogram is faceted according to two key rates: heart disease mortality rate and activity participation rate. For the participation rate part, each activity is categorized by a unique color, while in the mortality rate part the columns are in another distinctively different color. First, the result of histogram echoes with the result of scatter plot, which indicates some weakly positive relationship between the outdoor activity participation rate and heart disease mortality rate. As for different activities, we can discover that fishing seems to have the weakest relationship with heart disease mortality since for the columns of WY, fishing reaches a distinctively high rate, but WY doesn’t have the highest mortality rate, given the rate of other two activities are also relatively high. 

Generally speaking, among the three activities, camping and hiking are more obviously to have a positive relationship with the mortality rate than fishing. This also matches our common sense that among outdoor activities, fishing is quieter and doesn’t require as strong cardio-pulmonary function as camping and hiking. 


## Analysis Extension

### Activity specific analysis: 

To gain a deeper understanding of the relationship between outdoor activity and mortality from heart disease, a more detailed approach could be employed. It would be insightful to break down the data by specific types of outdoor facilities, such as swimming pools, hiking trails, stadiums, or recreation centers. This could reveal whether certain facilities have a more pronounced correlation with heart disease rates, compared to others. For example, if swimming pools are significantly associated with lower death rates from heart disease, compared to hiking trails, this information could guide the development of specific types of outdoor facilities in areas with high rates of heart disease.

### Time series analysis: 

In order to assess the long-term effects of outdoor activities on heart disease rates, a time series analysis should be performed. The analysis will track changes over time, looking at whether introducing more outdoor facilities in a given area leads to a decline in heart disease deaths in subsequent years. The benefits of increased outdoor activity participation can take time to become apparent, and understanding time-based trends can provide valuable insights for policy makers and urban planners.

### Quantify popularity and utilization: 

In addition to considering the number of outdoor facilities, it is important to know the actual utilization data. A state may have numerous facilities, but if they are underutilized, the potential health benefits may not be fully realized. Surveying the utilization of these facilities can help determine whether encouraging greater participation is effective. In addition, this analysis can help identify patterns of underutilization and develop strategies to maximize the health impact of existing facilities.

These extensions can deepen our understanding of the relationship between outdoor activity and heart disease mortality, providing more refined insights that can guide targeted interventions to improve the health and well-being of communities.



## Conclusion

In conclusion, our investigation into the relationship between heart disease mortality rates and the popularity of outdoor activity facilities within specific states has yielded valuable insights and raised thought-provoking questions.   Our findings, as depicted in the scatter plot and histograms, higher participation rates in these outdoor activities appear to weakly coincide with elevated heart attack mortality rates.     We observed that higher participation rates in outdoor activities, specifically camping, fishing, and hiking, were weakly associated with elevated heart attack mortality rates. This result challenges the conventional belief that outdoor activities inherently promote better health. We hypothesize that the increased risk associated with certain outdoor activities might contribute to the higher mortality rates observed.

This research sheds light on the complexity of factors influencing public health and underscores the need for a nuanced approach when promoting outdoor activities.   It's crucial to consider individual health conditions and risk factors, especially in those with underlying heart conditions.   Our study suggests that  while outdoor activities offer numerous benefits, a cautious and individualized approach is essential to ensure they contribute positively to community well-being and public health.

## References & Acknowledgements


Data retrieved from the following sites:

https://ridb.recreation.gov/docs

https://data.cdc.gov/Heart-Disease-Stroke-Prevention/Heart-Disease-Mortality-Data-Among-US-Adults-35-by/i2vk-mgdh/explore/query/SELECT%0A%20%20%60year%60%2C%0A%20%20%60locationabbr%60%2C%0A%20%20%60locationdesc%60%2C%0A%20%20%60geographiclevel%60%2C%0A%20%20%60datasource%60%2C%0A%20%20%60class%60%2C%0A%20%20%60topic%60%2C%0A%20%20%60data_value%60%2C%0A%20%20%60data_value_unit%60%2C%0A%20%20%60data_value_type%60%2C%0A%20%20%60data_value_footnote_symbol%60%2C%0A%20%20%60data_value_footnote%60%2C%0A%20%20%60stratificationcategory1%60%2C%0A%20%20%60stratification1%60%2C%0A%20%20%60stratificationcategory2%60%2C%0A%20%20%60stratification2%60%2C%0A%20%20%60topicid%60%2C%0A%20%20%60locationid%60%2C%0A%20%20%60location_1%60/page/filter

Reference Material:

https://www.dataquest.io/blog/python-api-tutorial/

Krueger, Edward. Menon, Shree. “API Calls & Data Scraping.”, “Pandas.”, ECO395, University of Texas, Austin, Austin, October, 2023.

https://pandas.pydata.org/docs/user_guide/10min.html
