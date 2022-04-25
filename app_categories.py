#Firstly, we import necessary libraries along with the df from a previous module

import matplotlib.pyplot as plt
import seaborn as sns
from loading import df
from log import logger

# Creating a table with the top 10 categories based on the number of apps

df.insert(17, 'Number of Apps', 1)
group = df.groupby('category').sum()[['Number of Apps']].reset_index()
group1 = group.sort_values(by = 'Number of Apps', ascending = False)
top10 = group1.head(10)
logger.info(top10)

# We can also see this table, graphically!

plt.figure(figsize = (18, 9))
sns.barplot(x = 'category', y = 'Number of Apps', data = top10)
plt.title('Top 10 Categories based on the Number of Apps', fontsize = 15)
plt.xlabel('Category', fontsize = 13)
plt.ylabel('Number of Apps', fontsize = 13);

