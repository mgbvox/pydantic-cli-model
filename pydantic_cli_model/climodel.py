from typing import Callable

import click
from pydantic import BaseModel, ValidationError


def indent(s: str, n: int, sep: str = "\t") -> str:
    return sep * n + s


def nl_join(*lines) -> str:
    return "\n\n".join(lines)


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
                f"--{field.lower()}",
                f"-{field.lower()[0]}",
                type=value.annotation,
                help=value.description,
            )(wrapper)

        clsname = f"<{cls.__name__}>"

        wrapper.__doc__ = nl_join(
            fn.__doc__,
            f"Inputs are validated as a {clsname} pydantic model.",
            f"Model {clsname}:",
            indent(cls.__doc__, 1),
        )

        cmd = click.command(name=cls.__name__.lower())(wrapper)

        return cmd
