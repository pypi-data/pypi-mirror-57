import configparser
import os
import os.path

from shield34_reporter.consts.shield34_properties_constants import Shield34PropertiesConstants
from shield34_reporter.exceptions import Shield34PropertiesFileNotFoundException, Shield34PropertiesSyntaxIncorrect
from shield34_reporter.utils.file_handler import FileHandler


class Shield34Properties:
    DEFAULT_API_BASE_URL = 'https://reports-api.shield34.com'
    isInitialized = False
    configParser = configparser.ConfigParser()
    api_key = None
    api_secret = None
    binding_server_mode = None
    api_base_url = 'https://reports-api.shield34.com'

    @staticmethod
    def get_value(section, key):
        Shield34Properties.initialize()
        if not Shield34Properties.isInitialized:
            raise Shield34PropertiesSyntaxIncorrect
        return Shield34Properties.configParser.get(section, key)

    @staticmethod
    def initialize():
        propertiesFilePath = ""
        if not Shield34Properties.isInitialized:
            path = "."
            while propertiesFilePath == "":
                propertiesFilePath = FileHandler.find_files(path, 'shield34.ini')
                if propertiesFilePath == "":
                    new_path = os.path.abspath(os.path.join(path, os.pardir))
                    if new_path == path:
                        break
                    else:
                        path = new_path

            if propertiesFilePath != "":
                Shield34Properties.configParser.read(propertiesFilePath)
                Shield34Properties.isInitialized = True
                Shield34Properties.api_key = Shield34Properties.get_value(
                    Shield34PropertiesConstants.PROP_REPORTS_SECTION,
                    Shield34PropertiesConstants.PROP_REPORTS_API_KEY)
                Shield34Properties.api_secret = Shield34Properties.get_value(
                    Shield34PropertiesConstants.PROP_REPORTS_SECTION,
                    Shield34PropertiesConstants.PROP_REPORTS_API_SECRET)
                try:
                    Shield34Properties.binding_server_mode = Shield34Properties.get_value(
                        Shield34PropertiesConstants.PROP_PROXY_SECTION,
                        Shield34PropertiesConstants.PROP_PROXY_BINDING_MODE)
                except Exception:
                    Shield34Properties.binding_server_mode = "local"
                try:
                    Shield34Properties.api_base_url = Shield34Properties.get_value(
                        Shield34PropertiesConstants.PROP_REPORTS_SECTION,
                        Shield34PropertiesConstants.PROP_REPORTS_API_BASE_URL)
                except Exception:
                    Shield34Properties.api_base_url = Shield34Properties.DEFAULT_API_BASE_URL
                    pass
            else:
                raise Shield34PropertiesFileNotFoundException
