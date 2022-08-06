import os
# os.chdir('/home/project/workspace-cli/wrcli/workspace_ui')
# conf_file = "/home/project/workspace-cli/tests/conf_parse/workspace-opt-field-miss-val.yaml"
from gvars import *
from init_ui import init_ui

import logging
logging.basicConfig(level=logging.DEBUG)


def build_ui(configs_dir):
    """ Build UI based o the cofigs folder. 
    Config folder must have file ui_config.yaml, and all images that are used to the UI.
    """
    logging.info(f'building UI from configs folder {configs_dir}')
    # Make sure UI is initiated
    init_ui()
    # Read configs
    







