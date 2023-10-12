<h1 align="center" id="heading"> <span style="color:red"> <em> Impact of Recreational Activities on Public Health: </em> <br> Heart Disease and Public Facilities </span> </h1>
<h3 align="center" id="heading"> 12 October 2023 <br> 
<em> Python, Big Data, and Databases (ECO395m)  </em> <br> <h3>
<h3 align="center" id="heading"> Bevo’s Group: Xiangmeng Qin, Tianyu Wang, Meilin Li, Yueting Zhang, & Machete Baker
 </h3>
  

## Introduction & Background

### Introduction:
In recent years, health and wellness have become focal points for many communities, with heart disease mortality rates often used as a benchmark for overall community health. Parallelly, the presence and popularity of outdoor recreational facilities, which are known to contribute to healthier lifestyles, have seen significant attention from policymakers and health advocates alike. Our project seeks to explore a potentially overlooked connection: "Is there any relationship between the heart disease mortality rates and the popularity of outdoor activity facilities within a state?"

### Background:
Heart disease remains a paramount health concern in the United States and worldwide. Its onset can be influenced by a myriad of factors, including diet, genetics, and notably, physical activity. Outdoor recreational facilities, such as parks, trails, and sports complexes, play a crucial role in promoting physical activity among residents of an area. The accessibility, quality, and popularity of these facilities can potentially impact the overall health outcomes of a community.
However, the direct relationship between heart disease mortality and the prevalence and popularity of such facilities has not been extensively studied. Do states with more popular outdoor facilities exhibit lower heart disease mortality rates due to increased physical activity among their residents? Or do other factors overshadow this potential correlation?
By exploring this relationship, we aim to provide valuable insights that could influence future urban planning, healthcare policies, and community wellness programs.

## Source of data
Our sources of data firstly include outdoor activity facilities across the United States, as taken from the Recreational.Gov site (https://www.recreation.gov/). The Recreation Information Database (RIDB) serves as a valuable resource for the public, offering a central hub for accessing information on recreational activities and destinations across the United States. It stands as an official and comprehensive platform catering to the needs of countless visitors to federal lands, historical sites, museums, and various other points of interest. It is a public API scraping site. However, we limit our analysis to states that are basically in the same climate and region. We argue that it contains similar types of outdoor activities, and thus can be comparable.

The list of states we have selected are that among the Pacific Northwest (PNW):
  1. Washington
  2. Oregon
  3. Idaho
  4. Montana
  5. Wyoming 

The details of facilities are captured from the recreation.gov, we scraped through API and selected aforementioned 5 states at first using longitude and latitude by Geopy package. For example, (50, -96) would be Texas, but then we were able to match on state level. (The region of the Pacific Northwest being the exact same climate may not  be 100% correct, but that’s the result of narrow selections.)

Secondly, the CDC website is designed to provide users with quick and easy access to the wide range of medical information and data available. The site is home to the latest news, information, and publications from the Center, as well as an extensive data archive accessible to the public. Heart disease mortality data among US adults by states are taken from the CDC website—Centers for Disease Control and Prevention, and then focused/divided by states (by use of CSV directly).


## Running the code

In order to examine the impact of recreational activities on public health, we are looking to pull data from the recreational.gov website in the form of API Scraping, and information from the CSV on Heart Disease Mortality rates. Our code is written to run in Python 3.11. Installation pip is required to run the code effectively. The code is kept inside “main.py” under folder “Code”, and should be run from that file. The data set on Heart Disease Mortality can be pulled from the file called “Data”, which is specified in the code folder. Both “Data” and “Code” are under the main folder in git called “eco395m-MidtermProject”. If you would like to run on your local IDE you can: Clone the project repository to your local machine by running the following command in your terminal, navigate to the project directory using the cd command, Install the required Python packages listed in the requirements.txt file. With the environment set up and dependencies installed, you can now execute the main script, main.py. The script will retrieve data related to heart disease mortality among U.S. adults and recreational facilities in specific states (WA, OR, ID, MT, WY) using API calls. Upon successful execution, you will find the results and any output data in the project directory or specified locations within the code. Please note that this code is designed to retrieve and process data based on specific states and API endpoints. Please ensure you have the necessary API key (in this case, the 'api_key' variable in the code) as it's required for accessing the data sources from the recreational government site (https://ridb.recreation.gov/docs#/Facilities) and the code will not run without the unique key. In order to run this code, you will need to replace the API Key variable with your very own. This can be done by visiting the link above, making an account, and confirming your account via email, (no payment required.) You are also able to edit the amount of facilities passed through the code. The “Limit” refers to this, and can enter anywhere from 1 to 1000. The API scraping is then edited to retrieve only the data of relevance mentioned, and then is merged with the Heart disease data on location before getting various lines of analysis and graph plotting performed. Pandas and Matplotlib are the most commonly used data collection methods and can be imported to run the code.





## Methodology

In this section, we will outline the methodology used to investigate the relationship between heart disease mortality and the popularity of outdoor activity facilities by state. The study is divided into some key steps. Firstly, for Heart Disease Mortality Data– the dataset is already relatively structured. However, we perform necessary data validation to ensure its accuracy. We filter the dataset to focus on relevant variables, such as mortality rates, and geographical coordinates. Additionally, for our second dataset, outdoor activity facilities data, we API scrape by retrieving the number of outdoor activity facilities by its count and location (counties, state, and long./latitude were available). The API site provides numerous data, and thus we are only interested in the facility count, the type of activity, and the location. The script proceeds to make API requests to the Recreation Information Database (RIDB) using the requests library. It sends requests to the RIDB API to fetch information about outdoor activity facilities in the same selected states. For each state in the Pacific Northwest (PNW), that we define as Washington (WA), Oregon (OR), Wyoming (WY), Idaho (ID), and Montana (MT),  the script retrieves facility data, including information about outdoor activities. This data is converted to JSON format, and the JSON responses are collected and stored in the api_data list. The location was given in terms of latitude and longitude/counties/zips/states across the sets. We also are given a range of states across the United States, but are only investigating that of the Pacific NorthWest. We argue that activity popularity is similar among states of regional similarity. We then categorize these facilities (their IDs) and activities (types placed in a dictionary). The limit has to be between 1 and 1000. Note that if the limit is entered above 50, it will take longer to API Scrape as the data influx is increasing exponentially. We recommend setting between 5-10. We merge the cleaned heart disease mortality dataset with the scraped outdoor activity facilities dataset based on geographical location. This integration enables us to analyze the relationship between heart disease mortality rates and the popularity of outdoor activities by state. After the data gets integrated, normalizing for population, we conduct statistical analyses to explore potential relationships, specifically correlation analysis.




## Limitations of the data

This analysis could be improved in several ways:

The precise selection of domains. We simply choose The Pacific Northwest by longitude and latitude, but in the real world the circumstances could be more complicated. Reasonable and more precise method to decide the region would be helpful to improve the quality of this analysis.

More states contained. We selected only 5 states to display if there are any relationships between the two items, but it would be more clear and conclusive for this analysis to contain more states, 10 states, 20 states, etc.

More factors about outdoor activities. We choose the facilities of outdoor activities as one item to measure the outdoor activity, but there are huge factors out of our consideration like outdoor sports without facilities, and so on. Adding more outdoor factors could raise the robust of this analysis.

Another limitation is that California’s (CA) data made the code super slow to run effectively, (because its associated data is incredibly large,) so we changed CA to Wyoming (WY). We thus had to redefine the region, as the PNW is now defined as WA, OR, ID, MO, and WY (instead of CA). However, part of the write is up to us to define what the PNW is, as some people define it including canada, northern california, with wyoming, or just WA / OR/ ID.

The other limitation is the speed in which the code can run - the API scraping takes awhile from the public, open domain, free government site, and retrieving hundreds of thousands of data points can take a long time. Thus, we have to limit the amount of facilities we pass through the code per state. If we had more time, better processors, and better more exclusive access, we could pass through more data and get na even more complete picture/analysis of our research question.

## Analysis & Results

### <scatter_plot.png>

By examining the scatter, we can discern the relationship between participation rates in outdoor activities and the mortality rate due to heart attacks. In this analysis, we've focused on three specific activities – camping, fishing, and hiking – within the same state, using consistent colors to enhance the visual clarity of this relationship.

Our observations reveal a somewhat unexpected trend: higher participation rates in these outdoor activities appear to weakly coincide with elevated heart attack mortality rates. This finding seems to challenge the conventional notion that engagement in outdoor activities generally promotes better health.

Several factors may underlie this counterintuitive result. One plausible explanation is that outdoor activities inherently entail a higher degree of risk, which could contribute to the elevated mortality rates.

Consequently, it is advisable to exercise caution when recommending outdoor activities to individuals who may have underlying heart conditions. While these activities can offer numerous health benefits, it's crucial to consider an individual's health status and potential risks before encouraging excessive participation.


### <histogram_pretty.png>

To study the effect by different activities, the histogram is faceted according to two key rates: heart disease mortality rate and activity participation rate. For the participation rate part, each activity is categorized by a unique color, while in the mortality rate part the columns are in another distinctively different color. First, the result of histogram echoes with the result of scatter plot, which indicates some weakly positive relationship between the outdoor activity participation rate and heart disease mortality rate. As for different activities, we can discover that fishing seems to have the weakest relationship with heart disease mortality since for the columns of WY, fishing reaches a distinctively high rate, but WY doesn’t have the highest mortality rate, given the rate of other two activities are also relatively high. Generally speaking, among the three activities, camping and hiking are more obviously to have a positive relationship with the mortality rate than fishing. This also matches our common sense that among outdoor activities, fishing is quieter and doesn’t require as strong cardio-pulmonary function as camping and hiking. 

 

## Analysis Extension

Activity Specific Analysis: Breakdown by type of outdoor facility. Do certain facilities like swimming pools or hiking trails have a more pronounced correlation with heart disease rates compared to others?

Time-Series Analysis: Track changes over time. If more outdoor facilities are introduced in a certain area, does heart disease mortality decrease over the subsequent years?

Quantifying Popularity: Rather than just looking at the number of facilities, leverage data on actual usage rates. A state may have numerous facilities, but if they're underutilized, the potential health benefits may not be realized.



## Conclusion

In conclusion, our investigation into the relationship between heart disease mortality rates and the popularity of outdoor activity facilities within specific states has yielded valuable insights and raised thought-provoking questions.

Our findings, as depicted in the scatter plot and histograms, present a somewhat unexpected trend. We observed that higher participation rates in outdoor activities, specifically camping, fishing, and hiking, were weakly associated with elevated heart attack mortality rates. This result challenges the conventional belief that outdoor activities inherently promote better health. We hypothesize that the increased risk associated with certain outdoor activities might contribute to the higher mortality rates observed.

This research sheds light on the complexity of factors influencing public health and underscores the need for a nuanced approach when promoting outdoor activities. It's crucial to consider individual health conditions and risk factors, especially in those with underlying heart conditions. Our study suggests that a one-size-fits-all recommendation for outdoor activities may not be appropriate.

As we move forward, potential avenues for further investigation include a more detailed analysis of specific types of outdoor facilities and their impact, as well as a time-series analysis to track changes in health outcomes over time. Additionally, quantifying the actual usage rates of these facilities could provide a more comprehensive understanding of their influence on public health.

In conclusion, while outdoor activities offer numerous benefits, a cautious and individualized approach is essential to ensure they contribute positively to community well-being and public health.


## References & Acknowledgements


Data retrieved from the following sites:

https://ridb.recreation.gov/docs

https://data.cdc.gov/Heart-Disease-Stroke-Prevention/Heart-Disease-Mortality-Data-Among-US-Adults-35-by/i2vk-mgdh/explore/query/SELECT%0A%20%20%60year%60%2C%0A%20%20%60locationabbr%60%2C%0A%20%20%60locationdesc%60%2C%0A%20%20%60geographiclevel%60%2C%0A%20%20%60datasource%60%2C%0A%20%20%60class%60%2C%0A%20%20%60topic%60%2C%0A%20%20%60data_value%60%2C%0A%20%20%60data_value_unit%60%2C%0A%20%20%60data_value_type%60%2C%0A%20%20%60data_value_footnote_symbol%60%2C%0A%20%20%60data_value_footnote%60%2C%0A%20%20%60stratificationcategory1%60%2C%0A%20%20%60stratification1%60%2C%0A%20%20%60stratificationcategory2%60%2C%0A%20%20%60stratification2%60%2C%0A%20%20%60topicid%60%2C%0A%20%20%60locationid%60%2C%0A%20%20%60location_1%60/page/filter

Reference Material:

https://www.dataquest.io/blog/python-api-tutorial/

Krueger, Edward. Shree Menon. “API Calls & Data Scraping.”, “Pandas.”, ECO395, University of Texas, Austin, Austin, October, 2023.

https://pandas.pydata.org/docs/user_guide/10min.html
