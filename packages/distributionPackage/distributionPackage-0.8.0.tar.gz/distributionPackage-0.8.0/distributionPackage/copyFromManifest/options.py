#
# Copyright 2019 Russell Smiley
#
# This file is part of distributionPackage.
#
# distributionPackage is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# distributionPackage is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with distributionPackage.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Implement user command line options for ``copyFromManifest`` command.
"""

import argparse
import typing


class UserOptions :
    """
    Command line options encapsulation and parsing.
    """

    DEFAULT_MANIFEST_FILE = 'manifest.yml'
    DEFAULT_OUTPUT_DIR = 'manifestOutput'


    def __init__( self ) :
        self.__parsedArguments = None
        self.__parser = argparse.ArgumentParser(
            description = 'Copy files specified in one or more manifests into a directory, preserving directory '
                          'hierarchy of the source files. Creates the output directory if necessary.'
        )

        self.__parser.add_argument( '-m', '--manifests',
                                    default = [ '{0}'.format( self.DEFAULT_MANIFEST_FILE ) ],
                                    dest = 'manifestPath',
                                    help = 'Manifest file(s) to use to build the package. (default {0})'.format(
                                        self.DEFAULT_MANIFEST_FILE ),
                                    nargs = '*' )
        self.__parser.add_argument( '-o', '--output',
                                    default = '{0}'.format( self.DEFAULT_OUTPUT_DIR ),
                                    help = 'Directory to place the generated distribution files. Created if not '
                                           'present. (default {0}'.format( self.DEFAULT_OUTPUT_DIR ) )
        self.__parser.add_argument( '-r', '--project-root',
                                    default = '.',
                                    dest = 'projectRoot',
                                    help = 'Project root to package files from. (default ./)' )


    def __getattr__( self, item: str ) -> typing.Any :
        value = getattr( self.__parsedArguments, item )

        return value


    def parseArguments( self, commandLineArguments: typing.List[ str ] ) :
        self.__parsedArguments = self.__parser.parse_args( commandLineArguments )
