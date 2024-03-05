#follow logger for python documentation
'''

In Python, a logger is a component of the logging 
module which allows developers to create, configure, 
and manage logging within their applications.
 It provides a way to track and record events that occur during the execution of a program, 
 such as informational messages, warnings,
 errors, and debugging information. Loggers help in debugging, troubleshooting, and monitoring applications.


'''



import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)



#to check whether the logger file work properly or not


# if __name__=="__main__":
#     logging.info("Logging has started")