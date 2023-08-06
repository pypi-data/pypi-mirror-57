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

import sys
import typing

from distributionPackage.app.arguments import parseArguments
from distributionPackage.package import Package
from distributionPackage.utility import combineManifests


def main( commandLineArguments: typing.List[ str ] ) :
    userOptions = parseArguments( commandLineArguments )

    thisManifest = combineManifests( userOptions.manifestPaths, userOptions.projectRoot )

    thisPackage = Package( thisManifest, userOptions )
    thisPackage.build()


def entrypoint() :
    main( sys.argv[ 1 : ] )


if __name__ == '__main__' :
    entrypoint()
