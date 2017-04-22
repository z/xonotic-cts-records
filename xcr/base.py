import logging

from xcr.config import conf
from xcr.util.logger import ClassPrefixAdapter


class Base(object):

    def __init__(self):
        self.conf = conf
        self.logger = ClassPrefixAdapter(prefix=self.__class__.__name__, logger=logging.getLogger(__name__))
