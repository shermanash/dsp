# -*- coding: utf-8 -*-
#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.



import csv
import pandas as pd
import numpy as np


csvpath = '~/ds/metis/prework/dsp/python/football.csv'

def worst_goaldiff(csvpath):
    # read csv to pandas dataframe
    df = pd.read_csv(csvpath)
    # add column to frame "goal differential"
    df['goal_diff'] = df['Goals'] - df['Goals Allowed']
    # sort by goal diff (doesnt return both teams in event of tie yet**)
    df.sort_values(by = ['goal_diff'], ascending=True)
    # get last row in the sorted frame (maybe not the best way)
    worst_team_differential = df.tail(1)
    return(worst_team_differential['Team'])


print worst_goaldiff(csvpath)





