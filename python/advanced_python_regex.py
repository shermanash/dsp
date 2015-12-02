
import pandas as pd

####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
# read in faculty data from csv
t = pd.read_csv('faculty.csv')
# store into a data frame
df = pd.DataFrame(t)
# strip whitespaces or column names and degree column, lowercase column names
df.columns = df.columns.str.strip().str.lower()
df.degree = df.degree.str.strip()
df.title = df.title.str.strip()
# remove periods from the degree column
df.degree.replace(regex=True,inplace=True,to_replace=r'\.',value=r'')
# create series from the degre column
degree_series = pd.Series(df.degree)
# split the degree series by whitespace
split_series = degree_series.str.split(' ')
# make new DF of all degrees
degree_frame = split_series.apply(lambda x: pd.Series(list(x)))
# stack and count values of all degrees
print degree_frame.stack().value_counts()


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

# count how many in title column contain 'Ass' and how many don't
df.assistants = df.title.str.contains(r'Ass')
print df.assistants.value_counts()
# there are 24 assistants and 13 professors


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.
print df.email


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

# create new column "email_domains"
df.email_domains = df.email.replace(regex=True,inplace=False,to_replace=r'.*@',value=r'')
print df.email_domains.value_counts()

