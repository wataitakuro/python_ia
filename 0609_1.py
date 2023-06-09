data_dist = {
    'name':'tarou'
}

key = input('key を入力してください＞')
value = input('valueを入力してください＞')

data_dist[key] = value

print(data_dist)
print(data_dist[key])
print(data_dist.get(key))

