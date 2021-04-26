import json
import csv

with open("outputs/step2.json") as ip:
    stark= json.load(ip)

def makeHeaders(data):
    fieldnames=[]
    for i in data:
        for header in i:
            fieldnames.append(header) 
        break
    return fieldnames



def writeData(file_name,data,fieldnames):
    with open(file_name, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in data:
            dic={}
            for key in i:
                if key in fieldnames:
                    dic[key]=i[key]
            print(dic)
            writer.writerow(dic)

fieldnames=makeHeaders(stark)
writeData("outputs/data.csv", stark, fieldnames)
print("---DONE---")