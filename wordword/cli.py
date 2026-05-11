import click
from inspector import inspect
from corpus import Corpus
from personality import score_personality


@click.group()
def cli():
    """wordworld — A word intelligence toolkit."""
    pass

@cli.command()
@click.argument('word')
def info(word):
    """Inspect a single word."""
    result = inspect(word)
    click.echo(f"Word: {result['word']}")
    click.echo(f"Length: {result['length']}")
    click.echo(f"Syllables: {result['syllable_count']}") 
    click.echo(f"Palindrome: {result['is_palindrome']}")
    click.echo(f"Unique chars: {result['unique_letters']}")
    click.echo(f"Starts vowel: {result['start_with_vowel']}")

@cli.command()
@click.argument('filepath', type=click.Path(exists=True))
def analyze(filepath):
    """Analyze a text file."""
    corpus = Corpus(filepath)
    fp = corpus.fingerprint()
    for key, value in fp.items():
        click.echo(f' {key:25} {value}')

@cli.command()
@click.argument('filepath', type=click.Path(exists=True))
def personality(filepath):
    """Personality report of a text file."""
    result = score_personality(filepath)
    click.echo(f"Formality: {result.formality}")
    click.echo(f"Complexity: {result.complexity}")
    click.echo(f"Emotionality: {result.emotionality}") 
    click.echo(f"Rhythm: {result.rhythm}")
    click.echo(f"Richness: {result.richness}")

@cli.command()
@click.argument('filepath1', type=click.Path(exists=True))
@click.argument('filepath2', type=click.Path(exists=True))
def compare_personality(filepath1, filepath2):
    """Compare personality report of two text files."""
    result1 = score_personality(filepath1)
    result2 = score_personality(filepath2)
    click.echo(f"Formality:\n file 1: {result1.formality} , file 2: {result2.formality}")
    click.echo(f"Complexity:\n file 1: {result1.complexity} , file 2: {result2.complexity}")
    click.echo(f"Emotionality:\n file 1: {result1.emotionality} , file 2: {result2.emotionality}") 
    click.echo(f"Rhythm:\n file 1: {result1.rhythm} , file 2: {result2.rhythm}")
    click.echo(f"Richness:\n file 1: {result1.richness} , file 2: {result2.richness}")


if __name__ == '__main__': 
    cli()
