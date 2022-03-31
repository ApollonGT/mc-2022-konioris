#Firstly, we run the necessary code from previous file

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Google-Playstore.csv')
df['Category'] = df['Category'].str.replace('Music & Audio', 'Music')
df['Category'] = df['Category'].str.replace('Educational', 'Education')

# Creating a table with the top 10 categories based on the number of apps

df.insert(24, 'Number of Apps', 1)
group = df.groupby('Category').sum()[['Number of Apps']].reset_index()
group1 = group.sort_values(by = 'Number of Apps', ascending = False)
top10 = group1.head(10)
print(top10)

# We can also see this table, graphically!

plt.figure(figsize = (18, 9))
sns.barplot(x = 'Category', y = 'Number of Apps', data = top10)
plt.title('Top 10 Categories based on the Number of Apps', fontsize = 15)
plt.xlabel('Category', fontsize = 13)
plt.ylabel('Number of Apps', fontsize = 13);

