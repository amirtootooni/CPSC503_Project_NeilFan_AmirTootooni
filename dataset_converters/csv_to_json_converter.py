import json
import csv
import re



def csv_to_json(dev, pred, out):
    dev_json = json.load(open(dev, encoding='utf-8'))
    predictions = []
    outputdic = {}
    with open(pred, mode='r', encoding='utf-8') as predcvs:
        reader = csv.reader(predcvs, delimiter=',')
        for index, row in enumerate(reader):
            if index > 0:
                predictions.append(row[1])

        count = 0
        for example in dev_json['data']:
            for p in example['paragraphs']:
                for q in p['qas']:
                    outputdic[q['id']] = predictions[count]
                    count += 1


    with open(out, "w") as outfile:
        json.dump(outputdic, outfile)

csv_to_json(r"C:\Users\Amirhossein\Desktop\CPSC 503 Repo\Datasets_in_squad2_format\squad2_dev.json", r"C:\Users\Amirhossein\Desktop\CPSC 503 Repo\results\t5_out_domain\squad2.csv", r"C:\Users\Amirhossein\Desktop\CPSC 503 Repo\squad_t5_pred.json")