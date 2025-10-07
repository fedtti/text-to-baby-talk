import click
from .translator import TextToBabyTalk

@click.command()
def main():
    """"""
    translator = TextToBabyTalk.translator()
    click.echo(translator)

if __name__ == "__main__":
    main()
