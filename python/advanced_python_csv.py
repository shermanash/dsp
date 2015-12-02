
import pandas as pd

# read in faculty data from csv
t = pd.read_csv('faculty.csv')
# store into a data frame
df = pd.DataFrame(t)

# strip whitespaces or column names and degree column, lowercase column names
df.columns = df.columns.str.strip().str.lower()
# write file to csv
df.email.to_csv('emails.csv', index=False)


