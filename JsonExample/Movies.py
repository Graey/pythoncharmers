# This code takes a movie title, searches for it in the json file and returns the year if it is present
import json


# Defining the search method
def search(search):
    with open("Movies.json") as file:
        data = json.loads(file.read())

    # Iterating through the json array
    for movie in data:
        # Finding the movie
        if movie["title"] == search:
            return movie["year"]

# Test
print(search("Knives Out"))
