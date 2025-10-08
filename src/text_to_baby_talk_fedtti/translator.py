import re
import click
import sys

"""

"""
def replace_letters(word) -> str:
    return word

"""

"""
def replace_words(sentence) -> str:
    translation = []

    common_baby_words = {
        "mother": "mom",
        "father": "dad"
    }

    words = sentence.split()

    for word in words:
        if word in common_baby_words:
            word = common_baby_words[word]
        else:
            if len(word) <= 3:
                if word.isalpha():
                    word = f"{word}-{word}"
            else:
                word = replace_letters(word)
        translation.append(word)

    sentence = " ".join(translation)
    return sentence

"""

"""
def translator(sentence) -> str:
    sentence = sentence.lower()
    sentence = replace_words(sentence)
    text = sentence.capitalize()
    return text

"""

"""
@click.command()
@click.option("--text", prompt = True)
def cli(text):
    baby_talk = translator(text)
    click.echo(f"{baby_talk}\n")

    if click.confirm("Continue?"):
        cli()

    sys.exit(0)
