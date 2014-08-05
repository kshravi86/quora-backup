from quora import Quora, Activity
import click
import os
from quorabackup import json_backup, csv_backup

@click.command()
@click.option('--path', '-p', help='Specify a path at which to store the backup files.')
@click.option('--type', '-t', type=click.Choice(['answers', 'questions', 'upvotes', 'question_follows']), help='Specify only one type of activity to be backed up.')
@click.option('--format', '-f', default='json', type=click.Choice(['json', 'csv']), help='Specify a format for the backup. Defaults to JSON.')
@click.argument('user')
def sync(user, path, type, format):
    if path is None:
        path = os.getcwd()
    quora = Quora()
    activity = quora.get_activity(user)
    if format == 'json':
        if type == 'answers':
            json_backup(activity.answers, os.path.join(path, 'answers.json'))
        elif type == 'questions':
            json_backup(activity.questions, os.path.join(path, 'questions.json'))
        elif type == 'upvotes':
            json_backup(activity.upvotes, os.path.join(path, 'upvotes.json'))
        elif type == 'question_follows':
            json_backup(activity.question_follows, os.path.join(path, 'question_follows.json'))
        # elif type == 'user_follows':
        #     json_backup(activity.user_follows, os.path.join(path, 'user_follows.json'))
        else:
            json_backup(activity.answers, os.path.join(path, 'answers.json'))
            json_backup(activity.questions, os.path.join(path, 'questions.json'))
            json_backup(activity.upvotes, os.path.join(path, 'upvotes.json'))
            json_backup(activity.question_follows, os.path.join(path, 'question_follows.json'))
    elif format == 'csv':
        if type == 'answers':
            csv_backup(activity.answers, os.path.join(path, 'answers.csv'))
        elif type == 'questions':
            csv_backup(activity.questions, os.path.join(path, 'questions.csv'))
        elif type == 'upvotes':
            csv_backup(activity.upvotes, os.path.join(path, 'upvotes.csv'))
        elif type == 'question_follows':
            csv_backup(activity.question_follows, os.path.join(path, 'question_follows.csv'))
        # elif type == 'user_follows':
        #     csv_backup(activity.user_follows, os.path.join(path, 'user_follows.csv'))
        else:
            csv_backup(activity.answers, os.path.join(path, 'answers.csv'))
            csv_backup(activity.questions, os.path.join(path, 'questions.csv'))
            csv_backup(activity.upvotes, os.path.join(path, 'upvotes.csv'))
            csv_backup(activity.question_follows, os.path.join(path, 'question_follows.csv'))
            # csv_backup(activity.user_follows, os.path.join(path, 'user_follows.csv'))
    else:
        print 'Backup format has not yet been implemented.'

if __name__ == '__main__':
    sync()