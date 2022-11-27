import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(file, delimiter = ",") -> list[dict]:

    with open(file) as f:
        dict_ = []
        headers = f.readline().split(delimiter)
        head = [items.rstrip() for items in headers]
        for lines in f:
            lines = lines.split(delimiter)
            lines = [items.rstrip() for items in lines]
            lines = dict(zip(head, lines))
            dict_.append(lines)
        return dict_

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
