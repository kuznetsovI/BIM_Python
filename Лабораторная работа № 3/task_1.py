import json
def task():
    with open('input.json') as f:
        data= json.load(f)
    summa=sum([item["score"]*item["weight"] for item in data])
    return round(summa, 3)
print(task())
