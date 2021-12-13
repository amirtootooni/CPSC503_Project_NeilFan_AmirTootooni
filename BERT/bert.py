# import torch
# from transformers import BertForQuestionAnswering
# from transformers import BertTokenizer

from transformers import pipeline
import json



def main(devset, out):
    # bert on squad v1.1
    qa_pipeline = pipeline(
        "question-answering",
        model="csarron/bert-base-uncased-squad-v1",
        tokenizer="csarron/bert-base-uncased-squad-v1"
    )

    # bert on squad v2
    # qa_pipeline = pipeline(
    #     "question-answering",
    #     model="twmkn9/bert-base-uncased-squad2",
    #     tokenizer="twmkn9/bert-base-uncased-squad2"
    # )


    # bert on coqa
    # qa_pipeline = pipeline(
    #     "question-answering",
    #     model="peggyhuang/bert-base-uncased-coqa",
    #     tokenizer="peggyhuang/bert-base-uncased-coqa"
    # )


    print("model set up")

    preds = {}
    dev = json.load(open(devset, encoding='utf-8'))
    total = 0
    for example in dev['data']:
        for p in example['paragraphs']:
            total += len(p['qas'])

    count = 0
    for example in dev['data']:
        for p in example['paragraphs']:
            for q in p['qas']:
                prediction = qa_pipeline({'context': p['context'], 'question': q['question']})
                preds[q['id']] = prediction['answer']
                count += 1
                print('\r' + str(count) + "/" + str(total), end='')

    with open(out, "w", encoding='utf-8') as outfile:
        json.dump(preds, outfile)


main("./coqa_dev.json", "./coqa_dev_preds_cqa.json")

