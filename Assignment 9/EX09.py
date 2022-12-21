
#Author: Pankhuri
#Description:Read a pre-processed set of news and extract information about their content

#importing the libraries

import pandas as pd
import numpy as np
import transformers
from transformers import pipeline
import nltk
import matplotlib.pyplot as plt
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

from wordcloud import WordCloud

df = pd.read_csv('News_2021.csv')

merged = []     #merging content and description to one list
for i in range(769):
    if (pd.isna(df.loc[i,"content"])):
        merged.append(df["description"][i].lower())
    else:
        merged.append(df["description"][i].lower()+df["content"][i].lower())

df["merged"] = merged

#applying stopword to the list
with open("stopwords_en.txt", "r") as f:
    stopwords = f.read().splitlines()

df["merged"] = df["merged"].apply(lambda x: " ".join([word for word in x.split() if word not in stopwords]))

words_dict = dict()

all_words=[]
for i in df["merged"]:
    temp_arr=i.split(' ')
    for j in temp_arr:
        all_words.append(j.lower())
len(all_words)

for i in all_words:
    if i in words_dict:
        words_dict[i]=words_dict[i]+1
    else:
        words_dict[i] = 1

w_count = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)

w_count = w_count[:20]

#counting 20 common words
print('\nThe 20 most common words are:\n', w_count)

#finding articles related to covid-19
co_19=list()
co_words=['covid-19','covid', 'coronavirus', 'vaccine', 'vaccination', 'antibody', 'moderna', 'pfizer', 'johnson']
for i in df['merged']:
    temp_arr=i.split(' ')
    if("covid-19" in temp_arr or "covid" in temp_arr or "coronavirus" in temp_arr or 'vaccination' in temp_arr or 'antibody' in temp_arr or 'moderna' in temp_arr or 'pfizer' in temp_arr or 'johnson' in temp_arr):
        co_19.append("Related")
    else:
        co_19.append("Not Related")

df['Covid-19'] = co_19
values = df['Covid-19'].value_counts()
percentage = (values["Related"]*100)/df.shape[0]
print('The % of the total articles related to Covid-19 is:', percentage)


clean_text_str = ' '.join(all_words)                       # vader needs strings as input. Transforming the list into string

vad_sentiment = analyzer.polarity_scores(clean_text_str)

pos = vad_sentiment['pos']
neg = vad_sentiment['neg']
neu = vad_sentiment['neu']

print('\nThe following is the distribution of the sentiment for all the articles')
print('\nIt is positive for', '{:.1%}'.format(pos))
print('\nIt is negative for', '{:.1%}'.format(neg))
print('\nIt is neutral for', '{:.1%}'.format(neu))

result=[]

for i in range(769):
    if(df['Covid-19'][i]=='Not Related'):
        result.append(df['title'])

clean_text_str1 = ' '.join(result)                       # vader needs strings as input. Transforming the list into string

vad_sentiment = analyzer.polarity_scores(clean_text_str1)

pos = vad_sentiment['pos']
neg = vad_sentiment['neg']
neu = vad_sentiment['neu']

print('\nThe following is the distribution of the sentiment for all the articles which is not related to Covid-19')
print('\nIt is positive for', '{:.1%}'.format(pos))
print('\nIt is negative for', '{:.1%}'.format(neg))
print('\nIt is neutral for', '{:.1%}'.format(neu))

#Finding words in article which is not-related to covid

w_count_notrelated=dict()

not_related_words=list()
for i in range(769):
    if(df["Covid-19"][i]=='Not Related'):
        temp_arr=df["merged"][i].split(' ')
        for j in temp_arr:
            not_related_words.append(j.lower())


#Generating wordclouds
unique_string = (" ").join(not_related_words)        #converting list to string
wordcloud = WordCloud(background_color ='white',max_words = 2000).generate(unique_string)
plt.subplot(211)
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Wordcloud for articles not related to COVID-19')
plt.show()

unique_string = (" ").join(all_words)   #converting list to string
wordcloud = WordCloud(background_color ='white',max_words = 2000).generate(unique_string)
plt.subplot(211)
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Wordcloud for all articles')
plt.show()

print('\nEnd of the processing\n')


