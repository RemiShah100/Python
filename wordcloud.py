import nltk
nltk.download()
from nltk.corpus import stopwords
from os import path
import numpy as np
from PIL import Image
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

stop = stopwords.words('english')

path = r'C:\UBER Project\harry potter 5 text.txt'

stop.append('-')
stop.append('said')

wc = {}

with open(path, 'r') as f:
    for line in f:
        for word in line.split():
            word = word.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(':', '').\n
            replace(';', '').replace('"', '')
            if word not in stop:
                wc[word] = wc.get(word, 0) + 1

x = Counter(wc)

ordered = x.most_common()

d = path.dirname(r'C:\Users\Student\Uber Project\car.jpg')

carimg = np.array(Image.open(path.join(d, "car.jpg")))

def grey_color_func(word, font_size, position, orientation, random_state=None,**kwargs):
    return "hsl(0, 100%, 100%)"
wordcloud = WordCloud(background_color='black', color_func=grey_color_func, width=1000, height=1000, mask=carimg).generate_from_frequencies(wc)

plt.figure(figsize=(10,10))
plt.axis('off')
plt.imshow(wordcloud)
plt.show()