def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
# parrot(1)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

# NLTK readings
import nltk
from nltk.corpus import gutenberg
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
# print(emma.concordance("surprize"))

# program to display info about each text by: loop of fileid values and computing stats for each
# print("Avg. Word Length | Avg. Sentence Length | No. of times (per vocab)")
# for fileid in gutenberg.fileids():
#     num_chars = len(gutenberg.raw(fileid))
#     num_words = len(gutenberg.words(fileid))
#     num_sts = len(gutenberg.sents(fileid))
#     num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
#     print(round(num_chars/num_words), round(num_words/num_sts), round(num_words/num_vocab), fileid)

#raw() gives content of files without ling.processing; sents() divides text into sentences with a list of words each
macbeth_sts = gutenberg.sents('shakespeare-macbeth.txt')
# print(macbeth_sts[116])
longest_len = max(len(s) for s in macbeth_sts)
# print([s for s in macbeth_sts if len(s) == longest_len])

# 1.2 web and chat text
from nltk.corpus import webtext
# for fileid in webtext.fileids():
    # print(fileid, webtext.raw(fileid)[:65])

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
# print(chatroom[123])

#1.3 brown corpus
from nltk.corpus import brown
# print(brown.categories())
# news_text = brown.words(categories='news')
# fdist = nltk.FreqDist(w.lower() for w in news_text)
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# for m in modals:
#     print(m + ':', fdist[m], end=' ')

# cfd = nltk.ConditionalFreqDist(
#     (genre, word)
#     for genre in brown.categories()
#     for word in brown.words(categories=genre))
# genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# print(cfd.tabulate(conditions=genres, samples=modals))

# 1.6 annotated text corpora
# use nltk.org/data to check download instructions

# 1.7 corpora in other langs
# print(nltk.corpus.cess_esp.words())
# from nltk.corpus import udhr
# languages = ['Chickasaw', 'English', 'German_Deutsch',
# 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
# cfd = nltk.ConditionalFreqDist(
#     (lang, len(word))
#     for lang in languages
#     for word in udhr.words(lang + '-Latin1'))
# cfd.plot(cumulative=True)

#1.8 text corpus structure
# fileids()	the files of the corpus
# fileids([categories])	the files of the corpus corresponding to these categories
# categories()	the categories of the corpus
# categories([fileids])	the categories of the corpus corresponding to these files
# raw()	the raw content of the corpus
# raw(fileids=[f1,f2,f3])	the raw content of the specified files
# raw(categories=[c1,c2])	the raw content of the specified categories
# words()	the words of the whole corpus
# words(fileids=[f1,f2,f3])	the words of the specified fileids
# words(categories=[c1,c2])	the words of the specified categories
# sents()	the sentences of the whole corpus
# sents(fileids=[f1,f2,f3])	the sentences of the specified fileids
# sents(categories=[c1,c2])	the sentences of the specified categories
# abspath(fileid)	the location of the given file on disk
# encoding(fileid)	the encoding of the file (if known)
# open(fileid)	open a stream for reading the given corpus file
# root	if the path to the root of locally installed corpus
# readme()	the contents of the README file of the corpus

# 2.2 Counts
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))

genre_word = [(genre, word)
    for genre in ['news', 'romance']
    for word in brown.words(categories=genre)]
# print(len(genre_word), genre_word[:4], "\n", genre_word[-4:])

cfd = nltk.ConditionalFreqDist(genre_word)
# print(cfd.conditions())

from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))

# print(cfd.tabulate(conditions=['English', 'German_Deutsch'], samples=range(10), cumulative=True))

#testing knowledge
# def letter_lookup(words):
#     d = {}
#     for word in words:
#         for letter in word:
#                 d[letter] = d.get(letter, set())
#                 d[letter].add(word)
#
#     return d
#
# d = letter_lookup('python programming provides endless possibilities'.split())
# print(d['p'])
# print(d['e'])

#testing knowledge 2: most frequent words for each genre of the brown corpus
# cfd = nltk.ConditionalFreqDist(
#     (genre, word)
#     for genre in brown.categories()
#     for word in brown.words(categories=genre))
# categories = brown.categories()
# for cat in categories:
#     print(cfd[cat].most_common(5))

# accounting for stopwords
# stopwords = nltk.corpus.stopwords.words('english')
# cfd = nltk.ConditionalFreqDist(
#     (genre, w)
#     for genre in brown.categories()
#     for w in brown.words(categories=genre) if w.lower() not in stopwords if w.isalpha())
# categories = brown.categories()
# for cat in categories:
#     print(cfd[cat].most_common(5))



# genre_word = [(genre, word)
#     for genre in ['news', 'romance']
#     for word in brown.words(categories=genre)]
# print(len(genre_word), genre_word[:4], "\n", genre_word[-4:])
#
# cfd = nltk.ConditionalFreqDist(genre_word)
# print(cfd.conditions())
# from nltk.corpus import brown
# # print(brown.categories())
# news_text = brown.words(categories='news')
# fdist = nltk.FreqDist(w.lower() for w in news_text)
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# for m in modals:
#     print(m + ':', fdist[m], end=' ')
#
# cfd = nltk.ConditionalFreqDist(
#     (genre, word)
#     for genre in brown.categories()
#     for word in brown.words(categories=genre))
# genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# print(cfd.tabulate(conditions=genres, samples=modals))

#clean text function
from nltk.tokenize import sent_tokenize, word_tokenize
import string
emmaS = sent_tokenize(gutenberg.raw('austen-emma.txt'))

#adjusted function for punctuation and 's intact for semantic sense
def clean_text(sentences):
    cleaned_sentences = []
    for sentence in sentences:
        # Remove new lines
        sentence = sentence.replace('\n', ' ')
        # Remove punctuation marks, except for the apostrophe
        sentence = sentence.translate(str.maketrans("", "", string.punctuation.replace("'", "")))
        cleaned_sentences.append(sentence)

    cleaned_sentences_final = []
    for sentence in cleaned_sentences:
        if sentence.startswith("'"):
            sentence = sentence[1:]
        if sentence.endswith("'"):
            sentence = sentence[:-1]
        cleaned_sentences_final.append(sentence)
    return cleaned_sentences_final

cleanedS = clean_text(emmaS[1:100])
tokens = []
for s in cleanedS:
    i = nltk.word_tokenize(s)
    tokens.append(i)
jtokens = []
[jtokens.extend(token) for token in tokens]
pos = nltk.pos_tag(jtokens)
print(pos)

# trying out TF-IDF for feature extraction and SVM model training
# from sklearn.feature_extraction.text import TfidfVectorizer
# vectorizer = TfidfVectorizer()
# tfidf_vectors = vectorizer.fit_transform(macbeth_sts)
# corpus = [emma_cleaned[1:3]]
# print(corpus)
# vectorizer = TfidfVectorizer()
# tfidf_vectors = vectorizer.fit_transform(corpus)
# print(tfidf_vectors)
#
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
#
# labels = [0, 1] # 0 for 'adventure', 1 for 'fantasy'
# # split data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(tfidf_vectors, labels, test_size=0.25)
# # create an SVM model with a linear kernel
# model = SVC(kernel='linear')
# # train the model
# model.fit(X_train, y_train)
# # make predictions on the test data
# y_pred = model.predict(X_test)
# # evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# precision = precision_score(y_test, y_pred, average='weighted')
# recall = recall_score(y_test, y_pred, average='weighted')
# f1 = f1_score(y_test, y_pred, average='weighted')
# print("Accuracy:", accuracy)
# print("Precision:", precision)
# print("Recall:", recall)
# print("F1-score:", f1)
