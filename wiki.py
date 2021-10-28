import wikipedia

search =input("Search : ")
result = wikipedia.summary(search,sentences = 2)
print(result)
