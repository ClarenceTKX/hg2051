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
from nltk.corpus import words