__author__ = 'zxy'

import time
import threading
from pocket.retrieve import Retrieve


class PeriodRetrieveTask(threading.Thread):
    all_items = None

    __last_update_time = 0
    __interval_sec = 3600*24
    __thread_stop = False

    def __init__(self, interval_secs=3600*24):
        super(PeriodRetrieveTask, self).__init__()
        self.__interval_sec = interval_secs

    # @staticmethod
    # def all_items():
    #     return PeriodRetrieveTask.all_items

    def __retrieve_task(self):
        now = time.time()
        if now - self.__last_update_time < self.__interval_sec:
            return

        # print 'start retrieve task'
        r = Retrieve()
        items = r.get_all_items()
        if items is None:
            return

        PeriodRetrieveTask.all_items = items
        self.__last_update_time = now

    def run(self):
        while not self.__thread_stop:
            print 'Thread Object, Time:%s\n' %(time.ctime())
            self.__retrieve_task()
            time.sleep(5)

    def stop(self):
        self.__thread_stop = True
