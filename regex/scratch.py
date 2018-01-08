#!/usr/bin/env python

import re

import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


msg = ['qa011_duplicate_individuals.sql',
    'QA010_middle_initial_in_first_name.sql',
    'qa910_something_utterly_useless.sql',
    'qa9876_malformed.sql',
    'QA472_probably_not_needed.sql']


if __name__ == '__main__':

    p = re.compile(r'(qa[0-9]{3}(?=\D))(\w*).sql', re.I)
    print('p')
    for i in msg:
        s = p.sub(r'\1_DISCONTINUED\2.sql', i)
        print(s)

    # p = re.compile(r'(qa[0-9]{3})(?=\D)', re.I)
    # print('p')
    # for i in msg:
    #     s = p.sub('QA000', i)
    #     print(s)
