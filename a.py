import os
import json

app_folder = '/home/jon/agh2'


l = list(os.walk(app_folder))
l = list(filter(lambda x: '.git' not in x[0], l))
l = list(filter(lambda x: '/app' not in x[0], l))
l = list(filter(lambda x: '__pycache__' not in x[0], l))
l = list(filter(lambda x: 'metadata' not in x[0], l))
l = list(filter(lambda x: 'temp' not in x[0], l))
l = list(filter(lambda x: x[0] != app_folder, l))
lol = list(map(lambda x: list(map(lambda y: x[0] + '/' + y, x[2])), l))
flat = [item for sublist in lol for item in sublist]
flat_t = list(map(lambda x: (x, x.replace(app_folder, '')), flat))
print(json.dumps(flat_t, indent=4))