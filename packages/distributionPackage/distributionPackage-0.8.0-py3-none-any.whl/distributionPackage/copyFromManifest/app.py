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

import logging
import os
import shutil
import sys
import typing

from packageManifest import Manifest

from distributionPackage.utility import combineManifests

from .options import UserOptions


log = logging.getLogger( 'copyFromManifest' )


def copyFiles( thisManifest: Manifest, projectRoot: str, destinationDir: str ) :
    log.debug( 'Destination directory for copy files, {0}'.format( destinationDir ) )
    os.makedirs( destinationDir,
                 exist_ok = True )

    filesToPackage = thisManifest.apply()
    for thisFile in filesToPackage :
        sourcePath = os.path.join( projectRoot, thisFile )
        destinationPath = os.path.join( destinationDir, thisFile )

        log.info( 'src, {0}, dst, {1}'.format( sourcePath, destinationPath ) )

        os.makedirs( os.path.dirname( destinationPath ),
                     exist_ok = True )

        shutil.copyfile( sourcePath, destinationPath )


def main( commandLineArgument: typing.List[ str ] ) :
    log.setLevel( logging.DEBUG )

    userOptions = UserOptions()
    userOptions.parseArguments( commandLineArgument )

    thisManifest = combineManifests( userOptions.manifestPath, userOptions.projectRoot )

    log.debug( 'Source file root, {0}'.format( userOptions.projectRoot ) )

    copyFiles( thisManifest, userOptions.projectRoot, userOptions.output )


def entrypoint() :
    main( sys.argv[ 1 : ] )


if __name__ == '__main__' :
    entrypoint()
