#Author: Joe Timmerman (https://github.com/joetimmerman)

import logging
import os
import time
import sys

sys.path.append('python-slackclient')

from slackclient import SlackClient

log = logging.getLogger('type')
logging.basicConfig()
log.setLevel(logging.DEBUG)

TOKEN = os.environ["SLACK_API_TOKEN"]
log.debug(TOKEN)
sc = SlackClient(TOKEN)

if sc.rtm_connect():
    while sc.server.connected is True:
        event = sc.rtm_read()
        log.debug(event)
        try:
            if event:
                if event[0]['type'] == 'user_typing':
                    currChannel = event[0]['channel']
                    # The rtm_set_typing method requires my fork of the Slack dev kit for Python
                    sc.rtm_set_typing(currChannel)
        except Exception as e:
            log.debug(e)
        time.sleep(1)
else:
    print('Connection failed')
