#Author: Pankhuri

import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def txt_clean(word_list, stopwords, min_len):
    clean_words = []
    for line in word_list:
        parts = line.strip().split()
        for word in parts:
            word_l = word.lower()
            if word_l not in stopwords:
                if word_l.isalpha():
                    if len(word_l) > min_len:
                        clean_words.append(word_l)
    return clean_words

pro_txt_file = open('pro_space.txt', 'r',encoding='utf8')          #read all files
con_txt_file = open('cons_space.txt', 'r',encoding='utf8')
stopwords_file = open('stopwords_en.txt', 'r',encoding='utf8')

stopwords_list = []                                # initializing lists
pro_txt_words = []
con_txt_words = []
punctuation_list = [".", ",", ":", ";", "?", "(", ")", "[", "]", "'", "!", "-", "/", "$"]

for word in stopwords_file:                        # populating the list of stopwords
    stopwords_list.append(word.strip())

for word in pro_txt_file:
   pro_txt_words.append(word.strip())

for word in con_txt_file:
   con_txt_words.append(word.strip())


stopwords_list.extend(['space', 'colonization', 'Mars', 'year',
                  'earth', 'spaceX', 'billion','humans', 'living', 'professor','the', 'and'])

min_len = 3

pro_clean_words = txt_clean(pro_txt_words,stopwords_list,min_len)       # cleaning the words and getting the list of unique words
con_clean_words = txt_clean(con_txt_words,stopwords_list,min_len)


analyzer = SentimentIntensityAnalyzer()                                 # calculating the sentiment using vader library

pro_clean_text_str = ' '.join(pro_clean_words)                         # vader needs strings as input
pro_vad_sentiment = analyzer.polarity_scores(pro_clean_text_str)        #Transforming the list into string

pro_pos = pro_vad_sentiment ['pos']
pro_neg = pro_vad_sentiment ['neg']
pro_neu = pro_vad_sentiment ['neu']

print ('\nThe following is the distribution of the sentiment for pro Space Colonization')
print ('\nIt is positive for', '{:.1%}'.format(pro_pos))
print ('\nIt is negative for', '{:.1%}'.format(pro_neg))
print ('\nIt is neutral for', '{:.1%}'.format(pro_neu))

con_clean_text_str = ' '.join(con_clean_words)
con_vad_sentiment = analyzer.polarity_scores(con_clean_text_str)

con_pos = con_vad_sentiment ['pos']
con_neg = con_vad_sentiment ['neg']
con_neu = con_vad_sentiment ['neu']

print ('\n The following is the distribution of the sentiment for con Space Colonization')
print ('\n It is positive for', '{:.1%}'.format(con_pos))
print ('\n It is negative for', '{:.1%}'.format(con_neg))
print ('\n It is neutral for', '{:.1%}'.format(con_neu))


#calculate pro and con bigrams
pro_bigrammed = list(nltk.bigrams(pro_clean_words))
print('\nThe following are the bigrams extracted from the pro text')
print(pro_bigrammed)
con_bigrammed = list(nltk.bigrams(con_clean_words))
print('\nThe following are the bigrams extracted from the con text')
print(con_bigrammed)

#print 5 most common bigrams and their frequencies for pros and cons
freqdist_pro = nltk.FreqDist(pro_bigrammed).most_common(10)
freqdist_con = nltk.FreqDist(con_bigrammed).most_common(10)
print('\nThe most frequent bigrams and their frequencies from the pro file are as follows: \n', freqdist_pro)
print('\nThe most frequent bigrams and their frequencies from the con file are as follows: \n', freqdist_con)

"""for i in pro_txt_words:
    if i in punctuation_list:
        i.remove()"""

# defining the wordcloud parameters
wc_pro = WordCloud(background_color = 'white', max_words=2000)
wc_con = WordCloud(background_color = 'white', max_words=2000)

# generating word cloud
wc_pro.generate(pro_clean_text_str)
wc_con.generate(con_clean_text_str)

# show the clouds
plt.figure(figsize=(30,15))
plt.subplot(211)
plt.imshow(wc_pro)
plt.axis('off')
plt.title('Pro word Cloud')
plt.subplot(212)
plt.imshow(wc_con)
plt.axis('off')
plt.title('Con word Cloud')
plt.show()

print("This is end of processing")

