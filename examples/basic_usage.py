from pydantic import Field

from pydantic_cli_model import CLIModel


class Foo(CLIModel):
    """Define your cli arguments as model fields.

    Field descriptions will populate the cli --help documentation for that argument.
    """
    a: str = Field(description="A is for apple!")
    b: float = Field(description="bzzzzz, I'm a B.")


@Foo.cli
def main(model: Foo):
    """Your main entrypoint is fed a validated Foo model, which you can treat like any other pydantic model."""
    print(model)


if __name__ == "__main__":
    main()
