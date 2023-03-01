import re
from datetime import datetime
from tabulate import tabulate

cursor = input("")

cursor = re.sub('[^A-Za-z0-9|\\{,":_]+', '', cursor)  # Remove all special characters that would mess up regex filtering
post_ar = []
post_ids = re.findall(pattern='"code":"[a-zA-Z0-9_.-]*"', string=cursor)  # Regex get video codes from json
post_timestamps = re.findall(pattern='"timestamp":[0-9]*', string=cursor)  # Regex get timestamps from json

del post_ids[-1:]  # Delete last post because it's repeated in the response
del post_timestamps[-5:]  # Delete last 5 timestamps because they are not related with posts

for i in range(len(post_ids)):
    # From JSON to string value
    post_timestamps[i] = post_timestamps[i].replace("\"", "").split(":")[1]
    # Add "." on the right place of instagram timestamp format, so I can convert it to python timestamp format
    post_timestamps[i] = post_timestamps[i][:10] + "." + post_timestamps[i][10:]
    # convert changed timestamp to datetime strftime with specific format
    post_timestamps[i] = datetime.fromtimestamp(float(post_timestamps[i])).strftime('%m/%d/%y %H:%M')

    # From JSON to String value
    post_ids[i] = post_ids[i].replace("\"", "").split(":")[1]

    # Append to post ar in dict format, so I can order urls by datetime at the same time later with sorted lambda
    post_ar.append({'id': post_ids[i], 'date': post_timestamps[i]})

# Order dict array by datetime from the most recent sent to latest
post_ar = sorted(post_ar, key=lambda x: datetime.strptime(x['date'], '%m/%d/%y %H:%M'), reverse=False)

# using tabulate lib to list posts and did some nice logic to display array of dictionaries with it
print(tabulate([(f"https://www.instagram.com/p/{x['id']}", x['date']) for x in [i for i in post_ar]],
               headers=["Code", "Date"]))
