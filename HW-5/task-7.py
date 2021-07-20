import json

result = []
dict = {}
total_profit = 0
counter = 0
with open('text_7.txt', 'r', encoding='utf-8') as f:
    list = f.readlines()
    for firm in list:
        info = firm.split()
        profit = int(info[2]) - int(info[3])
        if profit > 0:
            counter += 1
            total_profit += profit
        dict[info[0]] = profit

average_profit = {
    "average_profit": total_profit/counter}

result.append(dict)
result.append(average_profit)

with open("task_7.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(result)
