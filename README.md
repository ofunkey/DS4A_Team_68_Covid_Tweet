# DS4A_Team_68_Covid_Tweet


[Web Application on Heroku](https://covid-tweets-exploration.herokuapp.com/)


## An Analysis of Twitter Comments During Covid-19

![covid](https://github.com/ofunkey/DS4A_Team_68_Covid_Tweet/blob/main/images/covid19-image.png)

### Can we predict public sentiment as new Covid-19 variants emerge?

Two years after the first recorded outbreak of Covid-19, the world continues to deal with constant changes and uncertainties within their everyday lives as variants take hold of public health and policy. The pandemic has placed a significant amount of stress on individuals, from job security and economic stability to overall health. Popularity of social media sites has increased in the last 15-years, and as it serves many purposes, one of which is to be used as a large platform for people to be heard and seen.

By analyzing user posts across Twitter, we hope to uncover a trend within individual sentiments regarding their outlook on the world and their own lives. Has there been a significant shift in perspectives from when the first outbreak began, to the Delta variant, and now Omicron? Can we predict where public sentiment will shift, as new variants continue to surface? Can an increase of awareness for resources be timed in such a way that provides more help during the hardest hit periods?


### Background
In this project, we explored and analysed Covid-19 posts within the first 10-day window of each variant to find interesting discoveries in the tweets during the pandemic.
Data analysis was performed on the numerical features related to Twitter account users' and their posts. The module VaderSentiment, was utilized in performing Natural Language Processing (NLP) Sentiment analysis. Once patterns and trends were uncovered, a web application was created highlighting the findings  through the following:

- The Dataframe
- Sentiment
- Heat Map
- Word Cloud
- Prediction

A user-friendly application was created by using an open source package called Streamlit.

### Data Collection and Pre-Processing
Source - Covid-19 Twitter Chatter dataset from [Zenodo](https://zenodo.org/record/5775023#.YcJfP2jMIrB) and Tweeter API 
Collection -Utilized Twarc2 package to transform list of tweet_ids to full tweets by hydration and selected posts within a 10-day window of each variant (Beta, Delta, & Omicron) 

Tabular Pre-processing : Extracted each hour, renamed columns, created variant name by date, & parse data types
NLP Text Pre-processing : Applied lowercase, removed punctuations, URLs, & stop words, tokenized and lemmatized tweet text

### [Web Application on Heroku](https://covid-tweets-exploration.herokuapp.com/)

#### Data Frame
The entire data frame is displayed by default
* User can adjust how many rows to show 
* Filter options: Variant (Beta, Delta, & Omicron) user-selected columns, specific date range, 
* Posts can be filted by user-input keyword search
* Correlation map between numerical columns
* Scatterplots based on user-selected columns 

##### Correlation map of numerical columns
Observed positive correlation between like_count and reply_count, like_count and retweet_count 
![correlation_map](https://github.com/ofunkey/DS4A_Team_68_Covid_Tweet/blob/main/images/correlation_heatmap.PNG)

##### Scatterplot of like_counts vs re_tweets_counts
![scatterplot](https://github.com/ofunkey/DS4A_Team_68_Covid_Tweet/blob/main/images/scatterplot.PNG)

#### Heat Map
* Sentiment scores of all text, aggregated into one value (mean), across hour (x-axis) & variant (y-axis)
* Radio button 'no' allows the user to input a text for filtering and display the heat map on the subset of sentiment scores 

![heatmap1](https://github.com/ofunkey/DS4A_Team_68_Covid_Tweet/blob/main/images/heatmap1.PNG)

* Radio button 'no' allows the user to input a text for filtering and display the heat map on the subset of sentiment scores 
![heatmap2](https://github.com/ofunkey/DS4A_Team_68_Covid_Tweet/blob/main/images/heatmap2.PNG)

#### Sentiment
* A bar-plot highlighting sentiment across each variant (Beta, Delta, & Omicron
* Trend - More shares of positive sentiment for the Beta & Delta variants
* Time series aggregated by selected time intervals & selection of variant 

![sentiment1](https://github.com/ofunkey/DS4A_Team_68_Covid_Tweet/blob/main/images/sentiment1.PNG)
![sentiment2](https://github.com/ofunkey/DS4A_Team_68_Covid_Tweet/blob/main/images/sentiment2.PNG)
![sentiment3](https://github.com/ofunkey/DS4A_Team_68_Covid_Tweet/blob/main/images/sentiment3.PNG)

#### Prediction
* Used VaderSentiment module to extract sentiment scores
* Classify scores into 3 categories: Positive (green), Negative (red), and Neutral (gray)
* Sentiment analysis based on user-input text, where score & classification are returned 
* Score ranges from -1 to 1 with the following ranges:

       - Neutral (-0.5, 0.5), Positive (0.5, 1), & Negative (-1, -0.5)
     
 ![prediction](https://github.com/ofunkey/DS4A_Team_68_Covid_Tweet/blob/main/images/prediction.PNG)

#### Word Cloud
* The more frequent the word was used, the larger the size of the word display
* Each text has a sentiment score highlighted by color:

  - Red for negative
  - Green for positive
  - Gray for neutral
* Slider allows user to define the number of words to display

##### Word Cloud with 75 top words
Words like vaccine, health, life are averagely positive sentiments, whereas words like death, risk, lockdown words are averagely negative sentiments and covid case, new covid, pandemic, covid are averagely neutral sentiments.

![wordcloud1](https://github.com/ofunkey/DS4A_Team_68_Covid_Tweet/blob/main/images/wordcloud1.PNG)

##### Word Cloud with 30 top words
![wordcloud2](https://github.com/ofunkey/DS4A_Team_68_Covid_Tweet/blob/main/images/wordcloud2.PNG)
