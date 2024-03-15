#Author Emma Dunleavy
#Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, 
#and stores it into a file called "cso.json". 

#use 'shift', 'alt' & 'F' to format the text in json file

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"


def get_all():   
    response = requests.get(url) 
    return response.json()

if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(get_all()), file=fp)