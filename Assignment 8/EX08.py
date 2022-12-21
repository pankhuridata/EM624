import bs4 as bs                                            #importing libraries
import nltk
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



clean_words = []                                              # cleaning the text input file
def txt_clean(word_list, stopwords, min_len):

    for line in word_list:
        parts = line.strip().split()
        for word in parts:
            word_l = word.lower()
            if word_l not in stopwords:
                if word_l.isalpha():
                    if len(word_l) > min_len:
                        clean_words.append(word_l)
    return clean_words


url = "https://www.nytimes.com/"                                        # first importing the url
body = requests.get(url)                                                # to open the url
soup = bs.BeautifulSoup(body.content, "html.parser")                    #print(soup)
# to identify the number if pages


soup1 = bs.BeautifulSoup(body.content, 'html.parser').find_all("span", {"class", "pageInfo"})

cnt=0                                                 #print(soup1)
heading = []
for i in (soup.find_all('h3')):
    heading.append(i.get_text())
print(i)

cl_list=[]
for sentence in heading:
    sentence.replace("'","").replace('[',"").replace(']',"").replace("’t","t").replace("’s","s")
    cl_list.append(sentence)
    print(sentence)
    print('List:', cl_list)


S_word = open('stopwords_en.txt', 'r',encoding='utf8')           # reading input stopwords files
stpword_file = S_word.read()
Stopwords = []
min_len = 3
Stopwords.extend(['World', 'Cup', 'Trump', 'Thanksgiving','Russia', 'War','Advertisement', 'Covid'])   #updating the stopworlds list

for word in stpword_file.strip().split():
    Stopwords.append(word.lower())

clean_word = txt_clean(heading,Stopwords, min_len)         # cleaning the words and getting the list of unique words

analyzer = SentimentIntensityAnalyzer()                       # calculating the sentiment using vader library

clean_text_str = ' '.join(clean_word)                       # vader needs strings as input. Transforming the list into string

vad_sentiment = analyzer.polarity_scores(clean_text_str)

pos = vad_sentiment['pos']
neg = vad_sentiment['neg']
neu = vad_sentiment['neu']

print('\nThe following is the distribution of the sentiment for The New York Times')
print('\nIt is positive for', '{:.1%}'.format(pos))
print('\nIt is negative for', '{:.1%}'.format(neg))
print('\nIt is neutral for', '{:.1%}'.format(neu))

bigram = list(nltk.bigrams(clean_word))                        # calculate bigrams
print('\nThe following are the bigrams extracted from The New York Times:')
print(bigram)

freq = nltk.FreqDist(bigram).most_common(5)      # print most common bigrams and their frequencies for pros and cons
print('\nThe most frequent bigrams and their frequencies from The New York Times are as follows:',freq)

str_words = ' '.join(heading)                                 # WordCloud generation
wc = WordCloud(background_color ='white',max_words = 2000)
wc.generate(str_words)
plt.imshow(wc)
plt.axis('off')
plt.show()

print("\n This is end of processing")