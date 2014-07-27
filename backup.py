from quora import Quora, Activity
import click
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

def csv_backup(new, filepath):
    import csv
    if os.path.isfile(filepath):
        csv_data = csv.reader(open(filepath))
        old_ids = []
        for row in csv_data:
            old_ids.append[0]
    else:
        print 'bye'


@click.command()
@click.option('--path', '-p', help='Specify a path at which to store the backup files.')
@click.option('--format', '-f', default='json', type=click.Choice(['json', 'csv']))
@click.argument('user')
def sync(user, path, format):
    if path is None:
        path = os.getcwd()
    quora = Quora()
    activity = quora.get_activity(user)
    if format == 'json':
        json_backup(activity.answers, os.path.join(path, 'answers.json'))
        json_backup(activity.questions, os.path.join(path, 'questions.json'))
        json_backup(activity.upvotes, os.path.join(path, 'upvotes.json'))
        json_backup(activity.question_follows, os.path.join(path, 'question_follows.json'))
        # json_backup(activity.user_follows, os.path.join(path, 'user_follows.json'))
    elif format == 'csv':
        csv_backup(activity.answers, os.path.join(path, 'answers.csv'))
        csv_backup(activity.questions, os.path.join(path, 'questions.csv'))
        csv_backup(activity.upvotes, os.path.join(path, 'upvotes.csv'))
        csv_backup(activity.question_follows, os.path.join(path, 'question_follows.csv'))
        # csv_backup(activity.user_follows, os.path.join(path, 'user_follows.csv'))
    else:
        print 'Backup format has not yet been implemented.'

if __name__ == '__main__':
    sync()