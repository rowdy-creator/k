from collections import Counter

with open("sample.txt", "r")as file: 
    text=file.read().lower()

words=text.split()

freq=Counter(words)

top10=freq.most_common(10)

print("top 10 frequent word:")

for word, count in top10:


    print(word, ":", count)