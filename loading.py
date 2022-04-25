# Importing the libraries that are utilised in this python file

import pandas as pd
import missingno as msno 
from log import logger

# Importing the dataset 

df = pd.read_csv('Google-Playstore.csv')
logger.error(df.head())

# Getting information about the columns and the shape of our data

logger.info(df.info())
logger.info(df.shape)

# As we can see, there are columns with upper letters and spaces, so we use the lambda function to convert all columns to snake case!

df.rename(lambda x: x.lower().strip().replace(' ', '_'), axis = 1, inplace = True)
logger.info(df.columns) 

# We can also observe that some variables have wrong type, so we convert them into the right one

# Firstly, we convert the the column of size from categorical to numerical data

df['size'] = pd.to_numeric(df['size'].str.replace(r'[k, M]', ''), errors = 'coerce', downcast = 'float')

# Then, we split the scraped_time feature into date and time because the information of time is unnecessay and it will be dropped

df['scraped_date'] = pd.to_datetime(df['scraped_time']).dt.date
df['scraped_time'] = pd.to_datetime(df['scraped_time']).dt.time

# Additionally, we convert the columns of released, last updated and scraped date from categorical to date data

df['released'] = pd.to_datetime(df['released'], format ='%b %d, %Y', infer_datetime_format = True, errors = 'coerce')
df['last_updated'] = pd.to_datetime(df['last_updated'], format ='%b %d, %Y', infer_datetime_format = True, errors = 'coerce')
df['scraped_date'] = pd.to_datetime(df['scraped_date'])

# Now we drop the unnecessary featutes

df.drop(['app_id', 'installs', 'developer_id', 'developer_website', 'developer_email',
         'privacy_policy', 'editors_choice', 'scraped_time'], axis = 1, inplace = True)

# Check the results 

logger.info(df.info())

# Getting information about the app categories

logger.info(df['category'].value_counts())

# As We can see that there are some columns that are identical, such as education and educational, 
# music and music & audio. So, we need to merge these columns.

df['category'] = df['category'].str.replace('Music & Audio', 'Music')
df['category'] = df['category'].str.replace('Educational', 'Education')

# Dealing with missing values

logger.info(df.isnull().sum())
msno.matrix(df);

# We apply the pad method of the interpolate function which utilises the existing values for the data imputation

df.interpolate(method = 'pad', limit_direction = 'forward', inplace = True)
logger.info(df.isnull().sum())

# Finally, checking for duplicated rows

dp = df[df.duplicated()]
logger.info(dp.shape[0])

# There are no duplicated rows in our data!

