import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimetr=",", newline="/n") -> list[dict]:
    list_dict = []
    with open(INPUT_FILE, encoding="utf-8") as in_:
        str_s = in_.readlines()
        str_s = [line.rstrip() for line in str_s]
        headers = str_s[0].split(",")
        str_s.pop(0)

        kolvo_str = len(str_s)
        kolvo_slb = len(headers)
        for i in range(0, kolvo_str):
            list_dict.append({})
            for j in range(0, kolvo_slb):
                str_i = str_s[i].split(",")
                list_dict[i][headers[j]] = str_i[j]
    return list_dict




csv_to_list_dict(INPUT_FILE)

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
