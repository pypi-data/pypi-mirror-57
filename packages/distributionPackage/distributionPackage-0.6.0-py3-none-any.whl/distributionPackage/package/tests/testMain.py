#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 Integrated Device Technology, Inc.
# All Rights Reserved
#
# See LICENSE file in this project
#

import unittest.mock

from ...main import entrypoint

# !! DO NOT DELETE. Used by unittest.mock below
import distributionPackage.main


class TestMain( unittest.TestCase ) :

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

        mock_options = unittest.mock.MagicMock()
        mock_options.manifestPaths = ['file1', 'file2']

        with unittest.mock.patch( 'distributionPackage.main.Package' ), \
             unittest.mock.patch( 'distributionPackage.main.open' ), \
             unittest.mock.patch( 'distributionPackage.main.parseArguments',
                                  return_value = mock_options ), \
             unittest.mock.patch( 'distributionPackage.main.yaml.load',
                                  side_effect = [ [ expectedYamlData[ 0 ] ],
                                                  [ expectedYamlData[ 1 ] ] ] ), \
             unittest.mock.patch.object( distributionPackage.main.Manifest, 'from_yamlData' ) as mock_yamlData :
            entrypoint()

            mock_yamlData.assert_called_once_with( expectedYamlData, mock_options.projectRoot )


if __name__ == '__main__' :
    unittest.main()
