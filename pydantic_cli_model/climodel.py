from typing import Callable

import click
from pydantic import BaseModel, Field, ValidationError


class CLIModel(BaseModel):

    @classmethod
    def cli(cls, fn: Callable):
        def wrapper(**kwargs):
            try:
                validated_data = cls.model_validate(kwargs)
            except ValidationError as e:
                raise click.UsageError(e)

            return fn(validated_data)

        for field, value in cls.model_fields.items():
            wrapper = click.option(
                f"--{field.lower()}", f"-{field.lower()[0]}", type=value.annotation,
                help=value.description)(wrapper)

        return click.command(name=cls.__name__.lower())(wrapper)
