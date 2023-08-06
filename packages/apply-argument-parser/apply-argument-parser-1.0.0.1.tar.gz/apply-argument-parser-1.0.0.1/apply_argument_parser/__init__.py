import json
from typing import Any
from argparse import ArgumentParser
from dataclasses import dataclass, Field, MISSING, is_dataclass


def apply_argument_parser(_dataclass: Any):
    if not is_dataclass(_dataclass):
        raise TypeError('apply_argument_parser input must be a dataclass')
    parser = ArgumentParser()
    for key, value in _dataclass.__dataclass_fields__.items():
        f: Field = value

        kwargs = {}
        help_json = {}

        is_optional_type = False

        if hasattr(f.type, '__args__'):
            help_json['type'] = repr(f.type).replace('typing.', '')
            for arg in f.type.__args__:
                if arg == bool:
                    kwargs['action'] = 'store_true'
                    continue
                if hasattr(arg, '__name__'):
                    if arg.__name__ == 'NoneType':
                        is_optional_type = True
                        continue
                kwargs['type'] = f.type
        elif f.type == bool:
            kwargs['action'] = 'store_true'
            help_json['type'] = f.type.__name__
        else:
            kwargs['type'] = f.type
            help_json['type'] = f.type.__name__

        if f.default == MISSING:
            if is_optional_type:
                raise TypeError(
                    f"Invalid Optional type annotation provided with no 'None' default.\n f: {f}")
            kwargs['required'] = True
        elif f.default is not None:
            kwargs['default'] = f.default
            try:
                default_str = repr(f.default)
                help_json['default'] = default_str
            except:
                pass

        if f.metadata:
            help_json.update(f.metadata)

        kwargs['help'] = json.dumps(help_json).replace('"', '').replace('{', '').replace('}', '')

        parser.add_argument(f'--{f.name}', **kwargs)
    return _dataclass(**vars(parser.parse_args()))


@dataclass
class Args:
    test: bool = True


def main(args: Args):
    print(args)


if __name__ == '__main__':
    main(apply_argument_parser(Args))

