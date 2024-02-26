from xml.dom.minidom import parseString
import requests
import csv

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)

with open('week02_train_latitudes.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        latNodes = objTrainPositionsNode.getElementsByTagName("TrainLatitude")
        if latNodes:
            latNode = latNodes.item(0)
            if latNode and latNode.firstChild:
                TrainLatitude = latNode.firstChild.nodeValue.strip()
                train_writer.writerow([TrainLatitude])
            else:
                print("Latitude value is missing for a node.")
        else:
            print("No TrainLatitude nodes found.")
