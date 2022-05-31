import csv


episode_given_title = {}

with open('Book2.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)
        #print(row[0], row[3].split("Transcription")[0][1:-1].replace("\"", " ").replace("  "," "))
        title = row[3].split("Transcription")[0][1:-1].replace("\"", " ").replace("  "," ")
        episode = row[0]
        episode_given_title[title] = episode
    
    search_string = input("What do you want to see in One Piece?")
    
    for k,v in episode_given_title.items():
        if search_string.lower() in k.lower():
            print(v, k)