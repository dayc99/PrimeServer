__author__ = 'joseph'

#Built in python 3.4

import rpyc
from rpyc.utils.server import ThreadedServer # or ForkingServer

from PrimeNumbers import *


class MyService(rpyc.Service):

    def on_connect(self):
        # code that runs when a connection is created
        # (to init the service, if needed)
        pass
        #prime_numbers = PrimeNumbers()

    def on_disconnect(self):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        pass

    def exposed_get_primes(self, number): # this is an exposed method
        """Return all primes numbers less than or equal to the parameter"""
        return Prime_Number.primes(Prime_Number,number)




#Start Server
if __name__ == "__main__":
    server = ThreadedServer(MyService, port = 12345)
    server.start()