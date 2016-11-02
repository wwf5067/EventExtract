import json
import collections

sum_dict = {}
with open('counter',encoding='utf-8') as f:
    for line in f.readlines()[:4]:
        counter = json.loads(line[8:-2])
        for i in counter:
            if i not in sum_dict:
                sum_dict[i] = counter[i]
            else:
                sum_dict[i] += counter[i]
    sum_dict = sorted(sum_dict.items(), key=lambda d: d[1], reverse=True)
    print(sum_dict)
    #json_dict = json.dumps(sum_dict)
