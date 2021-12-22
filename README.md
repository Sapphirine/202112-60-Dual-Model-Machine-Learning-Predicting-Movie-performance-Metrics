# Movie_Predictions_wjl2128
Project for Columbia University Topics in Information Processing. Movie Prediction Dual linear Regression models

## Required Python Packages
* Bullet list
* Pandas
* bs4
* urllib
* requests
* googleapiclient.discovery
* ast
* time
* selenium  NOTE: GOOGLE CHROME MUST BE INSTALLED ON DEVICE IN ORDER TO WORK AS EXPECTED. CHROME DRIVER IS ALSO LOCATED IN SOURCE FILES.
* re
* Pyspark
* operator
* numpy
* matplotlib

## Source Data files
* movies2020.csv - contains Data of 154 movies released in 2020 (title, domestic box office sales)
* key_words.csv - contains a list of 2000+ words with associated ranking (-5 to 5)
* Chromedriver - needed to use the Selenium python chrome libraries
* Good_movies_2022.csv - Contains 'Expected Good' movie title dataset
* Bad_movies_2022.csv - Contains 'Expected Bad' movie title dataset

## Runtime process
1. CSV_IMBD.py - Takes in movies2020.csv and outputs the Rotten Tomato ranks (movies2020_ratings.csv)
2. CSV_key_words.py - takes list of titles and produces a csv with codes attached as column with Youtube API. 
* NOTE: THIS IS RUN FOR THE FOLLOWING DATA SETS movies2020.csv, Good_movies_2022.csv, Bad_movies_2022.csv
* NOTE: LINE 18 AND LINE 50 NEEDS TO BE CHANGED TO AVOID OVERWRITING OF DATA. 
* NOTE: file outputs for movies2020.csv, Good_movies_2022.csv, Bad_movies_2022.csv should be named movies2020_codes.csv, good_movies2022_codes.csv, Bad_movies2022_codes.csv respectfuly
3. word_ranker.py  - Takes list of YouTube API codes and pulls comments for each video 
* NOTE: THIS IIS RUN PROGRAMATICALLY FOR movies2020_codes.csv, good_movies2022_codes.csv, Bad_movies2022_codes.csv 
* NOTE: file outputs named programatically output files are as followed bad_word_rating.csv,good_word_rating.csv,word_rating.csv
4. Regression_Calc.ipynb - first trains the models and then runs the analysis on the model performance. After the 2022 movies are formatted and run through both models to produce data analytics visuals. 
NOTE: All steps are clearly outlined and results are shown in the notebook on open if more detail is needed look at the source file and results contained :)

## Figure Outputs
All figure outputs are contained within the python notebook source file Regression_Calc.ipynb
