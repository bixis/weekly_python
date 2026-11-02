#!/usr/bin/env python3
import ezgmail

# This script will reply automaticallqy to any email received in the inbox.
# I'm doing it the "Automate the Boring Stuff with Python" way.

MY_EMAIL = 'myemail@gmail.com'
AUTOMATIC_REPLY_MESSAGE = 'Thank you for your email. I will get back to you as soon as possible. \n Julian Linares'

def notification_system(threads):
    ''' Notify the user if there are more than 20 unread emails '''
    if len(threads) > 20:
        ezgmail.send(MY_EMAIL, 'You have more than 20 unread emails. Please check your inbox and reply to them as soon as possible.')

def automatic_reply(threads):
    ''' Automatically reply to any unread email '''
    for thread in threads:
        thread.reply(AUTOMATIC_REPLY_MESSAGE)
        
if __name__ == '__main__':
    unread_threads = ezgmail.unread()
    notification_system(unread_threads)
    automatic_reply(unread_threads)