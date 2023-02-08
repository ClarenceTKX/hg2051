import nltk
# groceries = list()
# groceries.append("bread")
# groceries.append("cheese")
# groceries.insert(0, "oil")
# print(groceries)
# groceries.remove('bread')
# print(groceries)
#
# print(groceries.count("cheese"))
# print('one one one'.count('o'))
# favourites = list(groceries)

# i = range(0, 1, 10)
# print(i)

# other string functions: .pop(), .pop(i), .reverse(), .sort(), .index('cereal')

s = ('There are seven days, there are seven days,',
     'there are seven days in a week.',
     'Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday')

#seminar 2 qns
# How many times does the word “day” occur in the string?
day_c = 0;
for i in s:
    day_c += i.count('day')
print("The word day appears ", day_c, " times.")

#How many times do the tokens “day”, “days”, and “days,” (note the comma) occur in the list of tokens (use split())?
t_day = 0
t_days = 0
t_days2 = 0
for i in s:
    t_day += i.count('day')
    t_days += i.count('days')
    t_days2 += i.count('days,')
print("token day appears ", t_day, " times, token days appears ", t_days, " times, and token days, appears ", t_days2, " times.")

# How many tokens are there in total?
tokens = 0
for i in s:
    temp = i.split()
    tokens += len(temp)
print("There are ", tokens, " tokens.")

# Find the relative frequency of the token “are” (number of times it occurs over the count of all tokens)
t_are = 0
for i in s:
    t_are += i.count('are')

relfreq = float((t_are / tokens) * 100)
relfreq = round(relfreq, 2)
print("The relative frequency of are is: ", relfreq, "%.")

# What is the set of unique words?
unique_words = []
for i in s:
    word = i.split()
    for j in word:
        if unique_words.count(j) > 0:
            continue
        else:
            unique_words.append(j)
print(unique_words)

# What is the set of unique letters?
unique_letters = []
for i in s:
    for j in i:
        if j.isalnum() == True:
            if unique_letters.count(j) > 0:
                continue
            else:
                unique_letters.append(j)
print(unique_letters)