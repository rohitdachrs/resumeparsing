"""
The main objective of this code is to 
scrape all the universities in india statewise.
"""
## Importing Libraries
import os
import pandas as pd
import numpy as np
from autoscraper import AutoScraper

## Creating an object of autoscraper
scraper = AutoScraper()
## Specifying the URL from which the data has to be scrapped
for index in range(2,28):
    if index == 2:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["A.T. Still University"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 3:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["B.S. Abdur Rahman Crescent Institute of Science and Technology"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 4:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["C.D.A. College"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 5:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["D.A. Tsenov Academy of Economics"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 6:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["E.A. Buketov University of Karaganda"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 7:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["Fachhochschule Aachen"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 8:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["G.H. Raisoni University"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 9:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["HAAGA-HELIA ammattikorkeakoulu"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 10:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["I.M. Seçenov adina Birinci Moskva Dövlet Tibb Universitetinin Baki"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 11:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["J.C. Bose University of Science and Technology"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 12:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["K L University"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 13:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["L.B. Goncharov Kazakh Road Academy"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 14:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["M. Akmullah Bashkir State Pedagogical University"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 15:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["N.P.I. University of Bangladesh"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 16:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["O.M. Beketov National University of Urban Economy in Kharkiv"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 17:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["P P Savani University"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 18:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["Qalam Institute of Higher Education"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 19:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["Rabia Balkhi University"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 20:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["S. Toraighyrov Pavlodar State University"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 21:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["Ta Hwa University of Science and Technology"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 22:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["U.P. Pt. Deen Dayal Upadhyaya Veterinary Science University and Cattle Research Institute"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 23:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["V. N. Karazin Kharkiv National University"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 24:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["Wa Polytechnic"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 25:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["Xavier University"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 26:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["Yadanabon University"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
    if index == 27:
        url = "https://www.4icu.org/reviews/index{}.htm".format(index)
        ## Creating a wanted list in which I am specifying the type of info I want
        wanted_list = ["Z.H. Sikder University of Science and Technology"]
        universities = scraper.build(url,wanted_list)
        ## Printing a list of all the central universities.
        #print(universities)
        print(len(universities))
    
     