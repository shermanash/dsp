import pandas as pd
from pprint import pprint

# read in faculty data from csv
path = '~/ds/metis/prework/dsp/python/faculty.csv'
t = pd.read_csv(path)
# store into a data frame
df = pd.DataFrame(t)

# strip whitespaces or column names and degree column, lowercase column names
df.columns = df.columns.str.strip().str.lower()
#Concatenate two DataFrame columns into a new, single column
df['info'] = df['degree'].map(str) + ',' +  df['title'].map(str)  + ',' + df['email'].map(str)

def remove_lastword(column):
    new = column.replace(regex=True,inplace=False,to_replace=r'([^ ]*$)',value=r'')
    return new


# df['firstname'] = df.name.replace(regex=True,inplace=False,to_replace=r'([^ ]*$)',value=r'')
df['firstname'] = remove_lastword(df.name)
df['lastname'] = df['name'].str.extract('(\w+$)')
df['titleshort'] = remove_lastword(df.title)
df['finaltitle'] = remove_lastword(df.titleshort)
# having trouble removing "of" :/

# df.set_index(df.lastname)
print df.head(5)



# faculty_dict = df.to_dict({ df['lastname']: [\[df['degree'], df['title'], df['email']]]}
mydict = {}
for x in range(len(df)):
    currentid = (df.iloc[x,5], df.iloc[x,6])
    # currentid = df.lastname.iloc[x,0]
    currentvalue = [df.iloc[x,1], df.iloc[x,7], df.iloc[x,3]]
    mydict.setdefault(currentid, [])
    mydict[currentid].append(currentvalue)

pprint(mydict)

# mydict.to_csv('mydict.csv')
import csv
# having trouble copying from tmux here is a csv with the better key design

with open('faculty_2.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, mydict.keys())
    w.writeheader()
    w.writerow(mydict)
