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

import unittest

from ..options import UserOptions


class TestUserOptions( unittest.TestCase ) :

    def testDefaults( self ) :
        arguments_input = list()

        under_test = UserOptions()
        under_test.parseArguments( arguments_input )

        self.assertEqual( '.', under_test.projectRoot )
        self.assertEqual( [ 'manifest.yml' ], under_test.manifestPath )
        self.assertEqual( 'manifestOutput', under_test.output )


    def testLongOutput( self ) :
        arguments_input = [
            '--output',
            'some/path',
        ]

        under_test = UserOptions()
        under_test.parseArguments( arguments_input )

        self.assertEqual( arguments_input[ 1 ], under_test.output )


    def testShortOutput( self ) :
        arguments_input = [
            '-o',
            'some/path',
        ]

        under_test = UserOptions()
        under_test.parseArguments( arguments_input )

        self.assertEqual( arguments_input[ 1 ], under_test.output )


    def testLongProjectRoot( self ) :
        arguments_input = [
            '--project-root',
            'some/path',
        ]

        under_test = UserOptions()
        under_test.parseArguments( arguments_input )

        self.assertEqual( arguments_input[ 1 ], under_test.projectRoot )


    def testShortProjectRoot( self ) :
        arguments_input = [
            '-r',
            'some/path',
        ]

        under_test = UserOptions()
        under_test.parseArguments( arguments_input )

        self.assertEqual( arguments_input[ 1 ], under_test.projectRoot )


    def testLongManifests( self ) :
        arguments_input = [
            '--manifests',
            'path/file1',
            'path/file2',
        ]

        under_test = UserOptions()
        under_test.parseArguments( arguments_input )

        self.assertEqual( arguments_input[ 1 :3 ], under_test.manifestPath )


    def testShortManifests( self ) :
        arguments_input = [
            '-m',
            'path/file1',
            'path/file2',
        ]

        under_test = UserOptions()
        under_test.parseArguments( arguments_input )

        self.assertEqual( arguments_input[ 1 :3 ], under_test.manifestPath )
