## writing all exception here

import sys
import os
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    """ This function will return the error message with the file and line where exception occured
    """
    _,_,exc_tb = error_detail.exc_info() # the third var will give infor about file and line in which exception occured
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number[{1}] error message[{2}]".format(
        
        file_name, exc_tb.tb_lineno, str(error))
        
    return error_message
    
    
class CustomException(Exception):

    """ This is custom exception function will return error details
    """
    
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message) # as we are inheriting error from above function we have used super here
        self.error_message = error_message_detail(error_message,error_detail=error_detail) #error detail will be tracked by sys
        
    
    def __str__(self):
        return self.error_message
    

# if __name__ == '__main__':
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by Zero Error")
#         raise CustomException(e,sys)
        