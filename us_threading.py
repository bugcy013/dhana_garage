__author__ = 'dhana013'

import threading

def do_this():

    x = 0
    print "this is our do_this thread!..........  "
    while (x < 300):
        # print 'while loopp............'
        x += 1
        pass

    print x


def do_after_this():

    x = 0
    print "this is our after_do_this thread!..........  "
    while (x < 600):
        # print 'while loopp............'
        x += 1
        pass

    print x

def main():

    # global dead
    # dead = False

    our_thread = threading.Thread( target=do_this, name = 'OurThread')
    our_thread.start()

    # print threading.active_count()
    # print threading.enumerate()
    # print our_thread.is_alive()

    our_thread.join()

    our_thread = threading.Thread( target=do_after_this, name = 'OurThread-2')
    our_thread.start()


if  __name__ == '__main__' :
    main()