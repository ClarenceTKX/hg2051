import nltk
import random2
from nltk.corpus import stopwords
moby = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
moby_lower = moby.lower()
sentences = moby_lower.split('\r\n')
print('There are ', len(sentences), ' lines in Moby Dick.')
words = moby_lower.split()
print('There are ', len(words), ' words in Moby Dick.')

average = float(len(words)/len(sentences))
print(average)
# task 2: NLTK sampling
# i = 0
# temp = []
# while i < 40:
#     temp.append(random2.randrange(0, 7558))
#     i += 1
# print(temp)

# tempsentences = []
# for i in temp:
#     tempsentences.append(sentences[i])
# print(tempsentences)

# unique_tokens = []
# for i in sentences:
#     temp = i.split()
#     for j in temp:
#         if unique_tokens.count(j) > 0:
#             continue
#         else:
#             unique_tokens.append(j)

# convert to list comprehension
unique_tokens = list(set([j for i in sentences for j in i.split()]))
# map version of code:
# unique_tokens = list(set(map(lambda i:i.split(), sentences)))

print(len(unique_tokens))

# stopwords = stopwords.words('english')
# sansSW = []
# for any(word in unique_tokens for word in stopwords):
#     sansSW.append(word)

# fdist = nltk.FreqDist(moby.split())
# print(fdist)
# print(fdist.most_common(50))