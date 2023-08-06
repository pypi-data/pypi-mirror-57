import pathlib
from dataclasses import dataclass

from .util import execute


@dataclass
class Dependency:
    name: str
    repo: str
    src_dir: pathlib.Path = ''
    version: str = 'master'

    def clone(self, src_dir):
        dest = src_dir / self.name
        if dest.exists():
            execute(f'git checkout master', cwd=dest)
            execute('git pull', cwd=dest)
        else:
            execute(f'git clone {self.repo} {dest}')
        execute(f'git checkout {self.version}', cwd=dest)


def dependencies(version):
    return (
        Dependency(
            'envoy',
            'https://github.com/envoyproxy/envoy.git',
            'api',
            version,
        ),
        Dependency(
            'data-plane-api',
            'https://github.com/envoyproxy/data-plane-api.git',
        ),
        Dependency(
            'googleapis',
            'https://github.com/googleapis/googleapis.git',
        ),
        Dependency(
            'protoc-gen-validate',
            'https://github.com/lyft/protoc-gen-validate.git',
        ),
        Dependency(
            'opencensus-proto',
            'https://github.com/census-instrumentation/opencensus-proto.git',
            'src',
        ),
    )
