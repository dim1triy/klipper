import unittest
from extras.probe import ProbePointsHelper
from test.lib import get_printer_config_mock, load_json


class ProbePointsHelperTest(unittest.TestCase):

    def test_check_position_value(self):

        config = get_printer_config_mock()

        test_cases = load_json('klippy/unit/extras/test_probe_cases.json')

        for case_item in test_cases:
            with self.subTest(case_item=case_item):
                errors = []
                probe = ProbePointsHelper(
                    config, finalize_callback=None, default_points=[]
                    )
                probe.use_xy_offsets(case_item['use_offsets'])

                probe.check_position_value(errors, **case_item['kwargs'])

                self.assertEqual(errors, case_item['result'])
