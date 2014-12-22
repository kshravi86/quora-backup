import click
from quorabackup import QuoraBackup

@click.command()
@click.option('--path', '-p', help='Specify a path at which to store the backup files.')
@click.option('--type', '-t', type=click.Choice(['answers', 'questions', 'upvotes', 'user_follows']), help='Specify only one type of activity to be backed up.')
@click.option('--format', '-f', default='json', type=click.Choice(['json', 'csv', 'mongodb']), help='Specify a format for the backup. Defaults to JSON.')
@click.option('--mongodburi', '-m', help='Specify a MongoDB URI. If not specified, tries localhost.')
@click.argument('user')
def sync(user, path, type, format, mongodburi):
    q = QuoraBackup(user)
    q.backup(format, mongodb_uri=mongodburi, path=path, type=type)

if __name__ == '__main__':
    sync()