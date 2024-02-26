
from xml.dom.minidom import parseString
import requests
import csv

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)
# check it works
# newl='' gets rid of the new lines when printing
#print (doc.toprettyxml(newl='')) #output to console

# if I want to store the xml in a file
#with open("trainxml.xml","w") as xmlfp:
    #doc.writexml(xmlfp)

with  open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        if traincode.startswith('D'):
            #print (traincode)
        
        
            dataList = []
            for retrieveTag in retrieveTags:
                datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
                dataList.append(datanode.firstChild.nodeValue.strip())
        
                print (dataList)
                train_writer.writerow([dataList])