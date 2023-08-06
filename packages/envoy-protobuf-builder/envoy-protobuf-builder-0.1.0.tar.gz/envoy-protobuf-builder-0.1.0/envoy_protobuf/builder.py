import os
import pathlib
import shutil
import tempfile
import typing

from protobuf_gen import remap

from .models import dependencies
from .util import (
    execute,
    render,
)

BASE_DIR = pathlib.Path(__file__).parent
PROTO_DIR = 'envoy_proto'


def clone_repos(_deps, src_dir):
    for dep in _deps:
        dep.clone(src_dir)


def skip_it(path) -> bool:
    for skip in ('metrics', 'alpha'):
        if skip in path:
            return True
    return False


def find_protos(path) -> typing.List[str]:
    return [
        str(pathlib.Path(root) / name)
        for root, dirs, files in os.walk(path)
        for name in files
        if name.endswith('.proto') and not skip_it(root)
    ]


def build_protos(_deps, src_dir):
    envoy_protos = find_protos(src_dir / 'envoy/api/envoy')

    remap(
        output_dir_autogen=str(BASE_DIR.parent),
        root_autogen=PROTO_DIR,
        includes=[
            str(src_dir / dep.name / dep.src_dir)
            for dep in _deps
        ],
        input_proto=envoy_protos + [
            # 3rd party
            'google/api/annotations.proto',
            'google/api/http.proto',
            'google/rpc/status.proto',
            'gogoproto/gogo.proto',
            'validate/validate.proto',
            'opencensus/proto/trace/v1/trace_config.proto',
        ],
    )

    return BASE_DIR.parent / PROTO_DIR


def package(src_dir, proto_dir, version):

    pkg_dir = pathlib.Path(tempfile.mkdtemp(prefix='proto-'))

    templates = (BASE_DIR / 'templates').iterdir()
    for template in templates:
        dest = pkg_dir / template.name
        render(template, dest, version=version)
        print(f'{template} -> {dest}')
    shutil.copytree(proto_dir, pkg_dir / PROTO_DIR)
    return pkg_dir


def run(src_dir_path, version, clone=True):
    if src_dir_path:
        src_dir = pathlib.Path(src_dir_path)
        src_dir.mkdir(exist_ok=True)
    else:
        src_dir = pathlib.Path(
            tempfile.mkdtemp(prefix='proto-src-')
        )

    _deps = dependencies(version)
    if clone:
        clone_repos(_deps, src_dir)
    proto_dir = build_protos(_deps, src_dir)
    pkg_dir = package(src_dir, proto_dir, version)
    execute('pip install -e .', cwd=str(pkg_dir))
    shutil.rmtree(pkg_dir)
