# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import argparse


def coqa_to_squad(coqa_file, output_file):
    coqa_json = json.load(open(coqa_file))
    data = []

    for coqa_example in coqa_json['data']:
        context = coqa_example['story']
        for index, q in enumerate(coqa_example['questions']):
            question_text = q['input_text']
            para = {'context': context, 'qas': [{'question': question_text, 'answers': []}]}
            data.append({'paragraphs': [para]})
            qa = para['qas'][0]
            qa['id'] = coqa_example['id'] + str(index)
            ans_string = coqa_example['answers'][index]['span_text']
            start = coqa_example['answers'][index]['span_start']
            qa['answers'].append({'text': ans_string, 'answer_start': start})
            qa['is_impossible'] = False

    coqa_as_squad = {'data': data, 'version': '2.0'}

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(coqa_as_squad, outfile, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    params = argparse.ArgumentParser()
    params.add_argument('--coqa_file', help='coqa file')
    params.add_argument('--output_file', help='Output file in SQuAD format')

    args = params.parse_args()

    coqa_to_squad(args.coqa_file, args.output_file)
