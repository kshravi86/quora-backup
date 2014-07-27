from quora import Quora, Activity
import click

quora = Quora()

@click.command()
@click.argument('user')
def sync(user):
    print quora.get_activity(user)