import argparse

from .builder import run


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        default='master',
        help='The Envoy version to build. Defaults to master.'
    )
    parser.add_argument(
        '--src-dir',
        help=(
            'The directory to clone the repositories to. If not specified '
            'a temporary location is used.'
        )
    )
    parser.add_argument(
        '--no-clone',
        default=False,
        action='store_true',
        help='Build the files with cloning the repositories.'
    )

    args = parser.parse_args()

    run(args.src_dir, args.version, not args.no_clone)
