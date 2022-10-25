# Marvel Characters Deep Dive

## Objective
The main goal of this project is to put together everything I learned so far as part of the Data Analytics bootcamp I'm currently taking. 

The structure of this project is:

1) Finding a public database of a specific topic I'm interested in OR that I want to further analyse.

2) Use either APIs or Web Scrapping (or both techniques) in order to extend the data available in the main dataframe so the analysis can be richer or more extensive.

3) Once the information has been condensed altogether and some hypotheses or objectives have been defined, there is some analysis that has been done in order to confirm or reject these hypotheses.

The topic chosen for this project is Marvel Characters.

## Project hypotheses

The hypotheses I defined for this project are the following:
1) Comics and series have roughly the same amount of projects within each of them.
2) Superhuman powers represent the 70% of all the different superpowers.
3) The top 5 superheroes by number of comics are all men.
4) The proportion of comics, series, stories and events is proportionate by gender.

## Finding the main database


I found the main database for my analysis in Kaggle: https://www.kaggle.com/datasets/amirdhavarshinis/marvel-characters?resource=download

The initial view of this database was something like the following: 

![](images/Screenshots%20for%20README/Screenshot%201.PNG)

After cleaning a little bit this database (mainly formatting the name of the characters, but more cleaning was done when merging with the API info), the output of the main database was the following:

![](images/Screenshots%20for%20README/Screenshot%202.PNG)


## Finding a suitable API

The information included in the main database was pretty categorical, so I wanted to include more numerical data. In order to do that, I used the official API provided by Marvel, which is including some data such as comics and series released,  as well as smaller stories, by each Marvel character.

In order for me to download the information from this API, I had to request the information a lot of times given the daily limit in the number of requests you can do as well as in the actual number of variables that can be requested by specific request (100 per request). On top of that, there was some manual work that had to be done in order to execute the request in Python - i.e. adding a timestap variable as well as a hash (previously converted from the key provided by Marvel).

The output you get after one request looks like the below:

![](images/Screenshots%20for%20README/Screenshot%203.PNG)

After getting all the requests done, I created some comprehension lists so I could get all of them together and split them by variable: comics, series, stories and events. Once this has done, I defined a new dictionary: key(name of the column, e.g. comics) and value(name of the comprehension list, e.g. comic_list) which I then converted into a DataFrame using Pandas:

![](images/Screenshots%20for%20README/Screenshot%204.PNG)

I was now able to merge it with the main database from Kaggle that I cleaned, so it looked like the below:

![](images/Screenshots%20for%20README/Screenshot%205.PNG)

I did more cleaning now I had both databases together so I could get rid of those columns with NaN values as well as everything that wasn't relevant for the study:

![](images/Screenshots%20for%20README/Screenshot%206.PNG)

Then, I realised the column "superpowers" is not very efficient as it stands given it's a huge string containing different descriptions, so I did categorise it into different "superpowers" via using a conditional function, so the final dataframe after incorporating the API data is the following:

![](images/Screenshots%20for%20README/Screenshot%207.PNG)
## Doing some Web Scrapping
Last but not least, did some web scrapping in order to add gender information to the data set - i.e. if a Marvel character is female or male, so that could help me with the analysis afterwards.

To do that, I did use the Marvel Wiki website as it does include a link for each Marvel character and the HTML structure is fairly similar.

First of all, I created a comprehension list including all the links in the first row of the main dataframe, so I could get all of them together in one place. I then realised each link had to be modified so when applying the BeautifulSoup library it could read them as an HTML object, so I did run some replacement functions in order to have readable links.

Once this was done, I did run a nested loop using web scrapping so I could get the gender information across the entire list of links I previously got (a link by Marvel character).The output of this after converting it into a DataFrame object was the following:

![](images/Screenshots%20for%20README/Screenshot%208.PNG)

And the final dataframe used for analysis after web scrapping was the following:

![](images/Screenshots%20for%20README/Screenshot%209.PNG)

## Hypotheses & statistics analysis
First of all, I ran some general statistics to get more familiarised with the dataset and the information I could access:



 ![](images/figure_2.jpg)

And looking at the same data by super power instead:

![](images/figure_3.jpg)

As well as the number of superheroes by super power and by gender:

![](images/figure_17.jpg) ![](images/figure_18.jpg)![](images/figure_19.jpg)

Looking at the number of superheroes by gender or by main super power declared depending on the number of comic collections released:

![](images/figure_35.jpg) ![](images/figure_36.jpg)

With regards to the hypotheses defined for this project:
#####1) Comics and series have roughly the same amount of projects within each of them.

If we look at the total number of comics & series, we can see that there is a way larger number of comics collections released than actual series made:

![](images/figure_24.jpg)
#####2) Superhuman powers represent the 70% of all the different superpowers.

After looking into what each super power represent vs. the total, we can see that Superhuman powers actually represent 56.3%:

![](images/figure_26.jpg)

 

#####3) The top 5 superheroes by number of comics are all men.

If we look at the top 5:
![](images/figure_29.jpg)

We can see that all of them are men, but let's see what happens if we look at the top 15 instead:

![](images/figure_30.jpg)

In this case, the top superhero woman is Storm in position #7!

#####4) The proportion of comics, series, stories and events is proportionate by gender.

If we look at the total by project type and by gender, we can see that there is a similar pattern for both genders when it comes to different projects released, with Comics and small Stories being the key ones, however the number is way bigger for superhero men rather than for women:

![](images/figure_31.jpg)

## Summary

Let's see if the hypotheses are True or False:


1) Comics and series have roughly the same amount of projects within each of them - <font color='red'>FALSE</font> (Comics have way more!)

2) Superhuman powers represent the 70% of all the different superpowers - <font color='red'>FALSE</font> (It is the one representing the biggest chunk, but it's 56.3%)

3) The top 5 superheroes by number of comics are all men - <font color='green'>TRUE</font>

4) The proportion of comics, series, stories and events is similar regardless of gender - <font color='green'>TRUE</font>. However, the number of projects done for superhero men is way larger than for superhero women.

![](images/Screenshots%20for%20README/Ironman.webp)

## Repository content

1) Jupyter notebooks:
    a) Dataframe for project 2 Ironhack
    b) API and Merging - Project 2
    c) Web Scraping - Marvel Project 2
    d) Charts and analysis - Project 2
2) main.py, alongside the following for reference:
    a) cleaning.py
    b) visualization.py
    c) APIWeb.py
3) images folder - key charts and screenshots used for this report
4) Datasource - folder that includes the main Marvel_Characters.csv from Kaggle
