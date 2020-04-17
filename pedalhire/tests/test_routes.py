from .test_basic import BasicTest
from pedalhire import app
from pedalhire.constants.global_constants import COMMON_PREFIX
import os
import unittest

class RoutesTests(BasicTest):
    def test_main_page(self):
        response = self.app.get(COMMON_PREFIX, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
