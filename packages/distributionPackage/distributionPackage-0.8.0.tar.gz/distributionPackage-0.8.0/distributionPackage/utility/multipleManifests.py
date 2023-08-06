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

import typing
import yaml

from packageManifest import Manifest


def combineManifests( manifestPaths: typing.List[ str ], projectRoot: str ) -> Manifest :
    """
    Aggregate separate manifest files into a single entity to create a manifest from.
    """
    yamlData = list()
    for thisFile in manifestPaths :
        with open( thisFile, 'r' ) as yamlFile :
            thisData = yaml.load( yamlFile,
                                  Loader = yaml.SafeLoader )

        assert isinstance( thisData, list )

        yamlData += thisData

    thisManifest = Manifest.from_yamlData( yamlData, projectRoot )

    return thisManifest
