import unittest
import reactor
from configfile import PrinterConfig
from extras.probe import ProbePointsHelper
from klippy import Printer
from test.lib import load_json


class ProbePointsHelperTest(unittest.TestCase):

    def test_check_position_value(self):
        main_reactor = reactor.SelectReactor(gc_checking=False)
        printer = Printer(main_reactor, None, {
            'config_file': 'test/klippy/screws_tilt_adjust.cfg',
        })
        printer_config = PrinterConfig(printer)
        config = printer_config.read_main_config()

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
