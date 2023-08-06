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
Test package options relating to manifest specification.
"""

import os
import unittest

from ..arguments import parseArguments


class TestManifestArgument( unittest.TestCase ) :

    def testDefaultManifest( self ) :
        """
        Manifest defaults
        """
        expectedDefaultManifests = ['manifest.yml']

        packageOptions = parseArguments( list() )

        actualManifests = packageOptions.manifestPaths

        self.assertEqual( expectedDefaultManifests, actualManifests )


    def testShortFormManifest( self ) :
        """
        Short form manifest option.
        """
        manifestFile = 'some-manifest.yml'
        expectedManifests = [manifestFile]

        packageOptions = parseArguments( [ '-m', manifestFile ] )

        actualManifests = packageOptions.manifestPaths

        self.assertEqual( expectedManifests, actualManifests )


    def testLongFormManifest( self ) :
        """
        Long form manifest option.
        """
        manifestFile = 'some-manifest.yml'
        expectedManifests = [manifestFile]

        packageOptions = parseArguments( [ '--manifests', manifestFile ] )

        actualManifests = packageOptions.manifestPaths

        self.assertEqual( expectedManifests, actualManifests )


    def testMultiplemManifests( self ) :
        """
        Long form manifest option.
        """
        expectedManifests = ['file1.yml', 'file2.yml']

        inputArguments = [ '--manifests' ] + expectedManifests
        packageOptions = parseArguments( inputArguments )

        actualManifests = packageOptions.manifestPaths

        self.assertEqual( expectedManifests, actualManifests )


    def testManifestWithOutput( self ) :
        """
        The user specified manifest must be used independently of other arguments.
        """
        expectedManifestArgument = ['some/manifest.yml']
        outputArgument = 'another/path'

        inputArguments = [
            '-m',
            expectedManifestArgument[0],
            '-o',
            outputArgument,
        ]

        packageOptions = parseArguments( inputArguments )

        actualManifests = packageOptions.manifestPaths

        self.assertEqual( expectedManifestArgument, actualManifests )


if __name__ == '__main__' :
    unittest.main()
