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

import os


class ChangeDirectory :
    def __init__( self, directory ) :
        self.newDirectory = directory
        self.previousDirectory = None


    def __enter__( self ) :
        self.previousDirectory = os.path.realpath( os.path.abspath( os.path.curdir ) )

        # Change to the new directory\
        os.chdir( self.newDirectory )


    def __exit__( self, exc_type, exc_val, exc_tb ) :
        # Restore the original directory
        os.chdir( self.previousDirectory )
