import json
import csv
import re


def coqa_to_squad(coqa_file, output_file):
    coqa_json = json.load(open(coqa_file))
    count = 0
    with open(output_file, mode='w', encoding='utf-8', newline="") as outcvs:
        writer = csv.writer(outcvs, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        for coqa_example in coqa_json['data']:
            context = "||context|| : " + coqa_example['story']
            for index, q in enumerate(coqa_example['questions']):
                question = " ||question|| : " + q['input_text']
                #answer = " ||answers|| : " + coqa_example['answers'][index]['span_text']
                context = context + question
                num_tokens = len(re.findall(r'\w+', context))
                writer.writerow([context, coqa_example['answers'][index]['span_text'], num_tokens])
                #if num_tokens > 512:
                #    count +=1
                #context = context + answer

    print(count)


def quac_to_squad(quac_file, output_file):
    quac_json = json.load(open(quac_file))
    with open(output_file, mode='w', encoding='utf-8', newline="") as outcvs:
        writer = csv.writer(outcvs, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)

        for quac_example in quac_json['data']:
            for p in quac_example['paragraphs']:
                context = "||context|| : " + p['context']
                for q in p['qas']:
                    # if q['orig_answer']['text'] != 'CANNOTANSWER':
                        question = " ||question|| : " + q['question']
                        # answer = " ||answers|| : " + q['orig_answer']['text']
                        context = context + question
                        writer.writerow([context, q['orig_answer']['text']])
                        # context = context + answer


def squad_to_csv(input_file, output_file):
    data_json = json.load(open(input_file, encoding='utf-8'))
    with open(output_file, mode='w', encoding='utf-8', newline="") as outcvs:
        writer = csv.writer(outcvs, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        count = 0
        for example in data_json['data']:
            for p in example['paragraphs']:
                context = "||context|| : " + p['context']
                for q in p['qas']:
                    count += 1
                    question = " ||question|| : " + q['question']
                    answer_text = 'CANNOTANSWER' if q['is_impossible'] else q['answers'][0]['text']
                    answer = " ||answers|| : " + answer_text
                    context = context + question
                    writer.writerow([context, answer_text])
                    context = context + answer


        print(count)

#coqa_to_squad("C:/Users/Amirhossein/Desktop/CPSC 503 Repo/Datasets_in_squad2_format/coqa-dev.json", "C:/Users/Amirhossein/Desktop/CPSC 503 Repo/Datasets_in_squad2_format/coqa_short_context.csv")
#quac_to_squad("C:/Users/Amirhossein/Desktop/CPSC 503 Repo/Datasets_in_squad2_format/val_v0.2.json", "C:/Users/Amirhossein/Desktop/CPSC 503 Repo/Datasets_in_squad2_format/quac_short_context.csv")
squad_to_csv("C:/Users/Amirhossein/Desktop/CPSC 503 Repo/Datasets_in_squad2_format/nq_dev_lite.json", "C:/Users/Amirhossein/Desktop/CPSC 503 Repo/Datasets_in_squad2_format/nq.csv")