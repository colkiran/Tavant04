
import logging

logging.basicConfig(level=logging.DEBUG, filename="mylog1.log", filemode="a",
                format = "Time :%(asctime)s, \n"
                         "LevelName :%(levelname)s, \n"
                         "Message   :%(message)s, \n"
                         "Filename  :%(filename)s, \n"
                         "Lineno    :%(lineno)s, \n"
                         "Name      :%(name)s, \n"
                         "ProcessID :%(process)d, \n"
                         "ProcessName :%(processName)s, \n"
                         "Thread    :%(thread)d, \n"
                         "ThreadName :%(threadName)s, \n")

inv = 1
num = 0
st = "======================================================================\n"
try:
    inv = 1 / num

except ZeroDivisionError as z:
    logging.debug(z)
except TypeError as t:
    logging.warning(t)
except ValueError as v:
    logging.error(v)
except Exception as e:
    logging.critical(e)
else:
    logging.info(f"Inverse of {num} is {inv}")
finally:
    logging.info(f"{str}")

