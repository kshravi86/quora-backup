from quora import Quora, Activity
import click
import os

def sync_items(old, new):
    for item in new:
        if item.id 

@click.command()
@click.option('--path', '-p', help='specify a path to store the JSON files at')
@click.argument('user')
def sync(user, path):
    if path is None:
        path = os.getcwd()
    quora = Quora()
    activity = quora.get_activity(user)
    

if __name__ == '__main__':
    sync()