import sys
from Networksecurity.logging import logger
    
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail:sys):
        self.error_message = error_message
        _, _, exec_tb=error_detail.exc_info()

        self.lineno=exec_tb.tb_lineno
        self.file_name=exec_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in the python script name [{0}] line number [{1}] error message [{1}]".format(
        self.file_name, self.lineno, str(self.error_message))
