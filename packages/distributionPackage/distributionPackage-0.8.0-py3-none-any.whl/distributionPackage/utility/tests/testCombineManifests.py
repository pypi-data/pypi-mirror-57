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

import unittest.mock

from ..multipleManifests import combineManifests

import distributionPackage.utility.multipleManifests

class TestCombineManifests( unittest.TestCase ) :

    def testMultipleYamlUnion( self ) :
        """
        Test that data from multiple manifests is aggregated correctly.
        """
        expectedYamlData = [
            {
                'include' : {
                    'files' : [ 'LICENSE', 'README.md' ],
                },
            },
            {
                'exclude' : {
                    'files' : [ 'README.md' ],
                },
            },
        ]

        mock_manifestPaths = ['file1', 'file2']
        mock_projectRoot = 'some/path'
        with unittest.mock.patch( 'distributionPackage.utility.multipleManifests.open' ), \
             unittest.mock.patch( 'distributionPackage.utility.multipleManifests.yaml.load',
                                  side_effect = [ [ expectedYamlData[ 0 ] ],
                                                  [ expectedYamlData[ 1 ] ] ] ), \
             unittest.mock.patch.object( distributionPackage.utility.multipleManifests.Manifest, 'from_yamlData' ) as \
                mock_yamlData :
            combineManifests(mock_manifestPaths, mock_projectRoot)

            mock_yamlData.assert_called_once_with( expectedYamlData, mock_projectRoot )
