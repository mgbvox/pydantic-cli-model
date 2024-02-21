from pydantic import Field, field_validator

from pydantic_cli_model import CLIModel

"""
Define your cli arguments as model fields.

Field descriptions will populate the cli --help documentation for that argument.
"""


class Person(CLIModel):
    """Models a person. Comprehensive, obviously."""

    name: str = Field(description="A name, like Aislin, Balthazar, Joe, or suchlike.")
    age: int = Field(description="Ain't nothing but a number (ewww, gross!)")
    height: float = Field(description="Inches, meters, you name it.")

    @field_validator("height")
    @classmethod
    def validate_height(cls, value: float):
        if value < 0:
            raise ValueError("You must obey the laws of physics, alas.")
        return value


database: dict[str, Person] = {}


# Your main entrypoint is fed a validated Person model, which you can treat like any other pydantic model!
@Person.cli
def main(model: Person):
    """Adds a person to our super-secure high-tech database."""
    database[model.name] = model
    print(f"Person {model.name} has been added to the database.")


if __name__ == "__main__":
    main()
