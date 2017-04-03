# -*- coding: utf-8 -*-

import logging

class ForensicLog:

    def __init__(self, logName):
        try:
            # 로깅을 설정
            logging.basicConfig(filename = logName, level = logging.DEBUG, format = '%(asctime)s %(message)s')
        except:
            print "Forensic Log Initialization Failure ... Aborting"
            exit(0)
    
    def writeLog(self, logType, logMessage):
        if logType == "INFO":            # 유용한 정보 메시지
            logging.info(logMessage)
        elif logType == "WARNING":       # 비정상적인 상황 발생, 정상 진행 가능
            logging.warning(logMessage)
        elif logType == "ERROR":         # 비정상적인 상황 발생, 오작동 가능성
            logging.error(logMessage)
        else:
            logging.error(logMessage)
    
    def __del__(self):
        logging.info("Logging Shutdown")
        logging.shutdown()