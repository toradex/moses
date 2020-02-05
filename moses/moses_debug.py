import logging
import config
import targetdevice
import platformconfig
import applicationconfig
import remotedocker

logging.basicConfig(level=logging.DEBUG)

config.init_config()
