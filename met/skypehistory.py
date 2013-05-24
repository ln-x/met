# -*- coding: utf-8 -*-
import Skype4Py

skype = Skype4Py.Skype()
skype.FriendlyName = 'Extract_chat_history'
skype.Attach()

if not skype.Client.IsRunning:
        print 'Starting Skype..'
        skype.Client.Start()

chats = skype.Chats

for f in friends:
	print f.Handle, ' ', f.FullName, ' ', f.MoodText

for c in chats:
    # c.Messages is a tuple, to be able to sort it,
    # convert it into a list
    msg_list = list(c.Messages)
    # Sorting based on timestamps, with custom compare fct
    def message_timestamp_cmp(x, y):
        return int(x.Timestamp - y.Timestamp)
        # why are timestamps float and not int in Skype4Py?
    msg_list.sort(message_timestamp_cmp)
    for m in msg_list:
        #print type(m.Body)
        print m.Sender.FullName, ' : ', m.Body.encode('utf-8')
        
        