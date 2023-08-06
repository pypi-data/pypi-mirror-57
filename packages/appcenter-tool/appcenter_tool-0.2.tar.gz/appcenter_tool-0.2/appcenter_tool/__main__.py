import argparse

from .utils import trigger_build


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('api_key', help='API key for app center')
    parser.add_argument('branch', help='Target branch to build')
    parser.add_argument('projects', nargs='+', help='List of project names')
    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    api_key = args.api_key
    projects = args.projects
    branch = args.branch

    for project in projects:
        trigger_build(project, api_key, branch)


if __name__ == '__main__':
    main()
