import wikipedia

def search(query):
    result = wikipedia.summary(query, sentences=5)
    print(result)


def yes(opinion):
    if opinion == "y":
        query = input("Search: ")
        search(query)
    else:
        pass


query = input("Search: ")
search(query)
while True:
    reply = input("\n Would you like to search another query ? [y] or [n]: ")
    yes(reply)
    if reply == "n":
        print("\n Thank You for using")
        break
    else:
        print("Say yes or no.")
