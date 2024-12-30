import requests
from bs4 import BeautifulSoup
import pandas as pd

web_url = "https://github.com/topics"

response = requests.get(web_url)

page_contents = response.text
# print(page_contents)
with open('webpage.html', 'w', encoding="utf-8") as f:
    f.write(page_contents)
  
doc = BeautifulSoup(page_contents, 'html.parser')

selection_class = 'f3 lh-condensed mb-0 mt-1 Link--primary'
# topic_title_tags = doc.find_all('p', {'class': selection_class})  ---same as lower---
topic_title_tags = doc.find_all('p', class_ = selection_class)
# print(topic_title_tags)
selection_desc_class = 'f5 color-fg-muted mb-0 mt-1'
topic_desc_tags = doc.find_all('p', class_ = selection_desc_class)
# print(topic_desc_tags[:2])
topic_title_tag0 = topic_title_tags[0]
# print(topic_title_tag0)
div_tag = topic_title_tag0.parent
selection_topic_link_class = 'no-underline flex-1 d-flex flex-column'
topic_link_tags = doc.find_all('a', class_ = selection_topic_link_class)
# print(topic_link_tags[0]['href']) 
topic0_url = "https://github.com" + topic_link_tags[0]['href'] 
# print(topic0_url)
topic_titles = []
for tag in topic_title_tags:
    topic_titles.append(tag.text)

# print(topic_titles)
topic_descs = []
for desc in topic_desc_tags:
    topic_descs.append(desc.text.strip())

# print(topic_descs)
topic_urls = []
base_url = 'https://github.com'
for url in topic_link_tags:
    topic_urls.append(base_url + url['href'])

# print(topic_urls)
topics_dict = {
    'title' : topic_titles,
    'description' : topic_descs,
    'url' : topic_urls
}
topics_df = pd.DataFrame(topics_dict)
# print(topics_df)
topics_df.to_csv('topics.csv', index=None)