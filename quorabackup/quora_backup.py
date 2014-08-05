import os

def json_sync_items(old, new):
    # need to come up with a faster way to do this
    # db implementations will be much faster
    ids = []
    for item in old:
        ids.append(item['id'])
    for item in new:
        if item['id'] not in ids:
            old.append(item)
    return old

def json_backup(new, filepath):
    import json
    if os.path.isfile(filepath):
        with open(filepath) as outfile:
            old = json.load(outfile)
        old = json_sync_items(old, new)
        with open(filepath, 'w') as outfile:
            json.dump(old, outfile)
    else:
        with open(filepath, 'w') as outfile:
          json.dump(new, outfile)

def csv_sync_items(writer, old_ids, new, fieldnames):
    # need to come up with a faster way to do this
    # db implementations will be much faster
    for item in new:
        if item['id'] not in old_ids:
            row = []
            for field in fieldnames:
                if field in item.keys():
                    row.append(item[field].encode('utf8'))
                else:
                    row.append(None)
            writer.writerow(row)

def csv_backup(new, filepath):
    import csv
    fieldnames = ['id', 'published', 'link', 'title', 'summary']
    if os.path.isfile(filepath):
        old_ids = []
        with open(filepath, 'r') as file:
            csv_data = csv.reader(file)
            for row in csv_data:
                old_ids.append(row[0])
        with open(filepath, 'a') as fp:
            writer = csv.writer(fp, delimiter=',')
            csv_sync_items(writer, old_ids, new, fieldnames)
    else:
        with open(filepath, 'wb') as fp:
            writer = csv.writer(fp, delimiter=',')
            writer.writerow(fieldnames)
            for item in new:
                row = []
                for field in fieldnames:
                    if field in item.keys():
                        row.append(item[field].encode('utf8'))
                    else:
                        row.append(None)
                writer.writerow(row)