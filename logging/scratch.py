#!/usr/bin/env python

import logging
logger = logging.getLogger()
logging.basicConfig(
        level=logging.DEBUG,
        # filename='foo.log',
        # filemode='w',
        format='%(asctime)s:%(filename)s line %(lineno)s:%(message)s',
        datefmt='%m/%d/%Y'
    )



if __name__ == '__main__':
    try:
        2/0
    except:
        # logger.error('Nope. You can\'t do that.')
        logger.exception('Just some of this.')

    logger.info('Informing you.')
    logger.warning('Warning you.')
    logger.debug('Debugging you.')
