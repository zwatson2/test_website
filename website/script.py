import pandas as pd                        
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date

"""

Uses pytrends

TODO
- visualizations for the other queries / data
- refine queries and visualizations
- add by state/city within U.S.
- global vs U.S. query for every visualization

"""

# make the query
pytrends = TrendReq()
pytrends.build_payload(kw_list=['chatGPT'], timeframe='2022-11-01 {}'.format(date.today()))

print()
print()
print("INTEREST OVER TIME:")
print()

# interest over time
df = pytrends.interest_over_time()
df = df.reset_index()
print(df.head(10))
sns.relplot(data=df, x="date", y="chatGPT", kind="line")
plt.show()

print()
print()
print("INTEREST BY REGION:")
print()

# interest by region
df = pytrends.interest_by_region(resolution='COUNTRY')
df = df.reset_index()
df = df.sort_values('chatGPT', ascending=False)
print(df.head(10))
sns.barplot(data=df[:20], x="geoName", y="chatGPT")
plt.show()

print()
print()
print("RELATED QUERIES:")
print()

# Related Queries, returns a dictionary of dataframes
related_queries = pytrends.related_queries()
print("top:")
print(related_queries['chatGPT']['top'][:10])
print("rising:")
print(related_queries['chatGPT']['rising'][:10])

print()
print()
print("RELATED TOPICS:")
print()

# Related Topics, returns a dictionary of dataframes
related_topic = pytrends.related_topics()
print("top:")
print(related_topic['chatGPT']['top'][['value', 'topic_title', 'topic_type']][:10])
print("rising:")
print(related_topic['chatGPT']['rising'][['value', 'topic_title', 'topic_type']][:10])