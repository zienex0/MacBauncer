import logging

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='mac_app_bouncer.log', 
                    filemode='a')

def log_info_message(message: str):
    logging.info(message)

def log_warning_message(message: str):
    logging.warning(message)

def log_error_message(message:str):
    logging.error(message)