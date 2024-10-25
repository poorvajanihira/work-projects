import json
import os.path

import pandas as pd


def parse_json(json_file):
    f = open(json_file, 'r+')
    csv_data = {}
    response = json.load(f)
    emotion_graph_child = response['emotion_graph']['child']
    for i, emotion_graph_key in enumerate(emotion_graph_child):
        if emotion_graph_key['key'] == 'emotion_graph':
            data = emotion_graph_child[i]['data']
            for emotion in data.keys():
                csv_data[emotion] = data[emotion]
        elif emotion_graph_key['key'] == 'attention_engagemnet_graph':
            data = emotion_graph_child[i]['data']
            for emotion in data.keys():
                csv_data[emotion] = data[emotion]
    return csv_data


def write_to_csv(csv_data, target_csv_path):
    df = pd.DataFrame.from_dict(csv_data)
    df.to_csv(target_csv_path, index=False)


if __name__ == '__main__':
    json_files = ["Sample_data.json"]
    target_folder = "emotion_response"
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)
    for json_file_path in json_files:
        target_csv_path = os.path.join(target_folder, json_file_path.rsplit('.', 1)[0]+'.csv')
        csv_data = parse_json(json_file_path)
        write_to_csv(csv_data, target_csv_path)