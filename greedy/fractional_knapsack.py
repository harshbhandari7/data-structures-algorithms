W = 50
n = 3
Items = [
  { 'weight': 10, 'value': 60 },
  { 'weight': 20, 'value': 100 },
  { 'weight': 30, 'value': 120 }
]

Items.sort(key= lambda x: x['value'] / x['weight'], reverse=True)    
total_value = 0
for i in range(n):
  if Items[i]['weight'] <= W:
    total_value += Items[i]['value']
    W -= Items[i]['weight']
  elif W > 0:
    rem = W / Items[i]['weight']
    total_value = total_value + (Items[i]['value'] * rem)
    W = 0

print(total_value)