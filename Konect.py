import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv


url = "http://konect.cc/networks/"

# Get request to fetch html content
reqs = requests.get(url).text
# tables = reqs.find("table")

# Parse the html content
soup = BeautifulSoup(reqs, 'lxml')

# Title of page
# print(soup.title.text)

#   Creating a Dict.
dataset_repo = []
# Find all hrefs and its attributes

#To test just for 20 rows
# line = 20
# count = 0

#find all hrefs in the table
for link in soup.find("table").find_all("a"):

    #Only find hrefs that have a category
    if "categories" in link.get('href'):
        continue


    # Concatenate beginning of the url with what is available
    h_link = link.get('href')
    whole_str = "http://konect.cc/networks/" + h_link
    links = []

    #The dataset name of each link
    name = link.text

    #append every link concatenated to list called "link"
    for i in range(1, 2):
        links.append(whole_str)

        urls_2 = []
        for href in links:
            source = requests.get(href).text

            #Slow down the pace of scraping
            #sleep(randint(5, 15))
            soup2 = BeautifulSoup(source, 'lxml')

            #find all dataset description
            description = soup2.find("p").text


            for link in soup2.find("table").find_all("a", href=True):
                if "categories" in link.get('href'):
                    continue

                #get all download link and concatenate konect url to the beginning of each
                h_link2 = link.get('href')
                download = "http://konect.cc/networks/" + h_link2


    dataset_repo.append([name, description, links[-1], [download][-1]])

    #print([name, description, links[-1], [download][-1]])

    #To limit the row to 20
    # if line == count:
    #     break
    # count += 1

#Write file to path and also include header
with open('/Users/lade/Downloads/Konect.csv', 'w') as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerow(['Name', 'Description', 'Link', 'Download'])
    writer.writerows(dataset_repo)

selection = input("Search dataset: ")

#search the dataset_repo list for the input in the name or description
#dataset  = [name for name in dataset_repo or description for description in dataset_repo]
dataset  = [x[0] for x in dataset_repo]# or x[1] for x in dataset_repo]


if selection in dataset:
    for x in range(0, len(dataset_repo)):
        if selection == dataset_repo[x][0]: #or dataset_repo[x][1]:
            print(dataset_repo[x])

        else:
            print("Not found")

#if selection.lower() in name.lower() or selection.lower() in description.lower():


