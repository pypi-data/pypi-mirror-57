import argparse
import typing


class UserOptions :

    DEFAULT_MANIFEST_FILE: str
    DEFAULT_OUTPUT_DIR: str

    __parsedArguments: list
    __parser: argparse.ArgumentParser


    def __init__( self ) : ...


    def __getattr__( self, item: str ) -> typing.Any : ...


    def parseArguments( self, commandLineArguments: typing.List[ str ] ) : ...


    #
    # These properties are fulfilled using the ``__getattr__`` method. They are described here as properties to
    # assist with PyCharm type hinting.
    #
    @property
    def manifestPath( self ) -> typing.List[ str ] : ...


    @property
    def output( self ) -> str : ...


    @property
    def projectRoot( self ) -> typing.str : ...
