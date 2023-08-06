===================
envoy-proto-builder
===================

.. image:: https://img.shields.io/pypi/v/envoy_protobuf.svg
        :target: https://pypi.python.org/pypi/envoy-protobuf-builder

.. image:: https://img.shields.io/travis/dpetzold/envoy_protobuf.svg
        :target: https://travis-ci.org/dpetzold/envoy-protobuf-builder


Builds and installs Envoy protocol buffers and the following
dependencies:

* data-plane-api
* googleapis
* protoc-gen-validate
* opencensus-proto


How it works
------------

Clones the Envoy repository and associated dependencies to a temporary
location. Builds the proto files into virtual Python module and installs
the module with pip. The protobuf files are available in ``envoy_proto``.


Installation
------------

.. code::

    pip installl envoy-proto-builder

Usage
-----

Running with no arguments will install the Envoy files from the master branch.

.. code::

    usage: envoy-protobuf-builder [-h] [--version VERSION] [--src-dir SRC_DIR] [--no-clone]

    optional arguments:
      -h, --help         show this help message and exit
      --version VERSION  The Envoy version to build. Defaults to master.
      --src-dir SRC_DIR  The directory to clone the repositories to. If not specified a temporary
                         location is used.
      --no-clone         Build the files with cloning the repositories.


Code Sample
-----------

.. code:: python

    from .common import make_any
    from envoy_proto.envoy.config.filter.accesslog.v2.accesslog_pb2 import AccessLog
    from envoy_proto.envoy.config.accesslog.v2.file_pb2 import FileAccessLog
    from envoy_proto.envoy.api.v2.core.config_source_pb2 import ConfigSource
    from envoy_proto.envoy.api.v2.listener.listener_pb2 import (
      Filter,
      FilterChain,
    )
    from envoy_proto.envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2 import (
      HttpConnectionManager,
      HttpFilter,
      Rds,
    )


    FilterChain(
        filters=[
            Filter(
                name='envoy.http_connection_manager',
                typed_config=make_any(
                    HttpConnectionManager(
                        stat_prefix='ingress_http',
                        rds=Rds(
                            route_config_name='local_route',
                            config_source=ConfigSource(
                                path='/etc/envoy/routes.yaml',
                            )
                        ),
                        http_filters=[
                            HttpFilter(name='envoy.router')
                        ],
                        access_log=[
                            AccessLog(
                                name='envoy.file_access_log',
                                typed_config=make_any(
                                    FileAccessLog(
                                        format='''\
    %REQ(:METHOD)% %REQ(:AUTHORITY)%%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% -> %UPSTREAM_CLUSTER% %REQ(:PATH)% %RESPONSE_CODE% %RESPONSE_FLAGS%\n''',
                                        path='/dev/stdout',
                                    )
                                )
                            )
                        ]
                    )
                )
            )
        ]
    )
