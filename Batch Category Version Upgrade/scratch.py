import os
import json
from ConfigLoader.ConfigReader import *


config = load_config_file_value()

print (config["ContentServerHost"])
