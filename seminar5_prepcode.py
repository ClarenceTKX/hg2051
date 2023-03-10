import nltk
sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
print(list(nltk.bigrams(sent)))
#each word as condition, frequency dist. generated over each word

#generate_model() generates text in a loop
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

# cfd() to generate the dist
cfd['living']
# generate_model() generates text from given distribution
print(generate_model(cfd, 'living'))
# most likely word order: living > creature > substances > : > ... > soul
# cfdist = ConditionalFreqDist(pairs)	create a conditional frequency distribution from a list of pairs
# cfdist.conditions()	the conditions
# cfdist[condition]	the frequency distribution for this condition
# cfdist[condition][sample]	frequency for the given sample for this condition
# cfdist.tabulate()	tabulate the conditional frequency distribution
# cfdist.tabulate(samples, conditions)	tabulation limited to the specified samples and conditions
# cfdist.plot()	graphical plot of the conditional frequency distribution
# cfdist.plot(samples, conditions)	graphical plot limited to the specified samples and conditions
# cfdist1 < cfdist2	test if samples in cfdist1 occur less frequently than in cfdist2

#wordnet
from nltk.corpus import wordnet as wn
print(wn.synsets('motorcar'))
#synset == synonym set (collection of synonymous words/lemmas)
print(wn.synset('car.n.01').lemma_names())

#provides definition for synset; example in the example() function
print(wn.synset('car.n.01').definition())
print(wn.synset('car.n.01').examples())
#words of synset are more useful than the examples/defn for programs

print(wn.synset('car.n.01').lemmas())
print(wn.lemma('car.n.01.automobile'))
print(wn.lemma('car.n.01.automobile').synset())
print(wn.lemma('car.n.01.automobile').name())
for s in wn.synsets('car'):
    print(s.lemma_names())

for s in wn.synsets('dish'):
    print(s.lemma_names())

motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
print(sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()))

motorcar.hypernyms()
paths = motorcar.hypernym_paths()
print([synset.name() for synset in paths[0]])
print([synset.name() for synset in paths[1]])

wn.synset('tree.n.01').part_meronyms()
wn.synset('tree.n.01').substance_meronyms()
wn.synset('tree.n.01').member_holonyms()

for synset in wn.synsets('mint', wn.NOUN):
    print(synset.name() + ':', synset.definition())

wn.synset('walk.v.01').entailments()
wn.synset('eat.v.01').entailments()
wn.synset('tease.v.03').entailments()

wn.lemma('supply.n.02.supply').antonyms()
wn.lemma('rush.v.01.rush').antonyms()
wn.lemma('horizontal.a.01.horizontal').antonyms()
wn.lemma('staccato.r.01.staccato').antonyms()

right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')
right.lowest_common_hypernyms(minke)
right.lowest_common_hypernyms(orca)
right.lowest_common_hypernyms(tortoise)
right.lowest_common_hypernyms(novel)

# knowledge check
# what percentage of the text???s vocabulary are not in the wordlist?
from nltk.corpus import words
def pctNP_vocab(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    corpus_vocab = set(w.lower() for w in nltk.corpus.words.words())
    pct = float(-(len(text_vocab) - len(corpus_vocab))/len(corpus_vocab))
    return pct
print(pctNP_vocab(nltk.corpus.gutenberg.words('austen-sense.txt')))
# what percentage of the wordlist are present in the text?
def pct_vocab(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    corpus_vocab = set(w.lower() for w in nltk.corpus.words.words())
    pct = (float(len(text_vocab)/len(corpus_vocab)))
    return pct
print(pct_vocab(nltk.corpus.gutenberg.words('austen-sense.txt')))

# Use the ARPABET transcriptions in the nltk.corpus.cmudict corpus to devise a function for
# identifying rhyming words (how they are identified is up to you).
# What are the largest clusters of rhyming words?
def rhyme(syllable):
    entries = nltk.corpus.cmudict.entries()
    return [word for word, pron in entries if pron[-(len(syllable)):] == syllable]

syl1 = ["N", "IH0", "K", "S"]
print(rhyme(syl1))
syl2 = ["F", "AY1", "ER0"]
print(rhyme(syl2))

# What are the hyponyms of student?
for synset in wn.synsets('student', wn.NOUN):
    print(synset.name() + ':', synset.definition())
student = wn.synset('student.n.01')
student_types = student.hyponyms()
print(sorted(lemma.name() for synset in student_types for lemma in synset.lemmas()))

# Use the lowest_common_hypernyms() method on synsets to find what is the shared hypernym of student and professor.
prof = wn.synset('professor.n.01')
lecturer = wn.synset('lecturer.n.01')
print(prof.lowest_common_hypernyms(student))
# [Synset('person.n.01')]

# How about professor and lecturer?
print(prof.lowest_common_hypernyms(lecturer))
# [Synset('educator.n.01')]