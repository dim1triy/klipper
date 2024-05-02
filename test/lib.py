import json
import os
import reactor
from configfile import PrinterConfig
from klippy import Printer


def load_json(file_path):
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_path)
    with open(file, mode='r') as fp:
        return json.load(fp)


def get_printer_config_mock(config_file=None):
    if not config_file:
        config_file = 'test/klippy/screws_tilt_adjust.cfg'

    main_reactor = reactor.SelectReactor(gc_checking=False)
    printer = Printer(main_reactor, None, {
        'config_file': config_file,
    })
    printer_config = PrinterConfig(printer)

    return printer_config.read_main_config()
