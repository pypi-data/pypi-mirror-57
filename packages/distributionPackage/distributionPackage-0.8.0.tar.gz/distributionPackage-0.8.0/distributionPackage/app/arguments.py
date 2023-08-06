#
# Copyright 2018 Russell Smiley
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
Parse command line arguments.
"""

import argparse

from .options import PackageOptions


def parseArguments( arguments ) :
    """
    Parse ``sys.argv[1:]`` style command line arguments.

    :param arguments: Command line arguments.

    :return: ``PackageOptions`` object.
    """
    parser = argparse.ArgumentParser( description = 'Build a distribution package from a manifest' )
    parser.add_argument( '-a', '--append',
                         action = 'store_true',
                         default = False,
                         dest = 'append',
                         help = 'Append to an existing distribution package, if it exists. Created otherwise. ('
                                'default disabled)' )
    parser.add_argument( '-m', '--manifests',
                         default = ['manifest.yml'],
                         dest = 'manifest_path',
                         help = 'Manifest file(s) to use to build the package. (default manifest.yml)',
                         nargs = '*' )
    parser.add_argument( '-o', '--output',
                         default = '.',
                         help = 'Directory to place the generated distribution files. Created if not present. ('
                                'default ./)' )
    parser.add_argument( '-p', '--package',
                         default = 'distribution-out',
                         help = 'Filename stub of output package, not including suffix or version info. (default '
                                'distribution-out)' )
    parser.add_argument( '-r', '--project-root',
                         default = '.',
                         dest = 'projectRoot',
                         help = 'Project root to package files from. (default ./)' )
    parser.add_argument( '-n', '--no-tar',
                         action = 'store_false',
                         default = True,
                         dest = 'buildTar',
                         help = 'Disable tar, gzip output distribution. (default enabled)' )
    parser.add_argument( '-z', '--zip',
                         action = 'store_true',
                         default = False,
                         dest = 'buildZip',
                         help = 'Enable zip output distribution. (default disabled)' )

    args = parser.parse_args( arguments )

    packageOptions = PackageOptions( args )

    return packageOptions
