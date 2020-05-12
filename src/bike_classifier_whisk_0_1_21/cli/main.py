import click
import json
from bike_classifier_whisk_0_1_21.models.model import Model

@click.group()
def cli():
    pass

@cli.command()
@click.argument('x')
def predict(x):
    """
    Generate a model prediction.
    Example usage: bike_classifier_whisk_0_1_21 predict [[1,2],[3,4]]
    """
    model = Model()
    x_parsed = str(x)
    res = model.predict(x_parsed)
    click.echo(res)

if __name__ == "__main__":
    cli()
