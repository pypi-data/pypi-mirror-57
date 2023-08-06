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

from ..app import main

# !! DO NOT DELETE. Used by unittest.mock below
import distributionPackage.copyFromManifest


class TestCopyFromManifest( unittest.TestCase ) :

    def testExecution( self ) :
        """
        Test that data from multiple manifests is aggregated correctly.
        """

        mock_manifestPaths = [ 'file1', 'file2' ]
        mock_projectRoot = 'some/path'

        mock_arguments = [
            '-m',
            *mock_manifestPaths,
            '-r',
            mock_projectRoot,
        ]

        with unittest.mock.patch( 'distributionPackage.copyFromManifest.app.combineManifests' ) as mock_combine :
            main( mock_arguments )

            mock_combine.assert_called_once_with( mock_manifestPaths, mock_projectRoot )


if __name__ == '__main__' :
    unittest.main()
