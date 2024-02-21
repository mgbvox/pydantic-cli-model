# Pydantic CLI Models

Pydantic + Click == Perfection (with love to Rust's [clap](https://docs.rs/clap/latest/clap/) library)

[Github](https://github.com/mgbvox/pydantic-cli-model.git)

[Issues](https://github.com/mgbvox/pydantic-cli-model/issues)

Reduce boilerplate by 2x (at least), turning this:

```python
import click
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

@click.command()
@click.option("--name", type=str)
@click.option("--age", type=int)
def main(name, age):
    person = Person(name=name, age=age)
    # ... do something with person ...
```

Into this:

```python
from pydantic_cli_model import CLIModel


class Person(CLIModel):
    name: str
    age: int

@Person.cli
def main(person:Person):
    ...
    # ... do something with person ...
```

And get data validation for free!