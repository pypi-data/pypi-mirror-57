import base64
import signal
import subprocess
import sys

import click
import zstd


@click.group()
def cli():
    pass


@cli.command(
    help="Compress each line of process' stdout with zstandard.",
    context_settings={'ignore_unknown_options': True},
)
@click.option('--level', default=3, type=int, help='Compression level')
@click.argument('command', nargs=-1, type=click.UNPROCESSED)
def run(level, command):
    def terminate_child(*args, **kwargs):
        # will break readline loop and letov will exit
        proc.terminate()
        proc.wait()

    compressor = zstd.ZstdCompressor(level=level)
    proc = subprocess.Popen(
        command,
        universal_newlines=True,
        stdout=subprocess.PIPE,
    )
    signal.signal(signal.SIGINT, terminate_child)
    signal.signal(signal.SIGQUIT, terminate_child)
    signal.signal(signal.SIGTERM, terminate_child)

    try:
        for data in iter(proc.stdout.readline, ''):
            if data:
                compressed = compressor.compress(data.encode())
                encoded = base64.b64encode(compressed).decode()
                sys.stdout.write(encoded + '\n')
    finally:
        terminate_child()
