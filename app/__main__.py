from argparse import ArgumentParser, Namespace

from app.utils.greet import greet


class Args(Namespace):
    name: str


def parse_args() -> Args:
    parser = ArgumentParser()
    parser.add_argument("--name", type=str, required=True)
    return parser.parse_args(namespace=Args())


def main(args: Args):
    greetings = greet(args.name)
    print(greetings)


if __name__ == "__main__":
    args = parse_args()
    main(args)
