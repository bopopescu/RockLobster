import requests
import os
import time
import uuid
import logging
import subprocess
from distutils.spawn import find_executable

logger = logging.getLogger(__name__)


class NgrokTunnel:

    def __init__(self, port, auth_token, subdomain_base="zoq-fot-pik"):
        """Initalize Ngrok tunnel.

        :param auth_token: Your auth token string you get after logging into ngrok.com
        :param port: int, localhost port forwarded through tunnel
        :parma subdomain_base: Each new tunnel gets a generated subdomain. This is the prefix used for a random string.
        """
        assert find_executable("ngrgit ok"), "ngrok command must be installed, see https://ngrok.com/"
        self.port = "8000"
        self.auth_token = "7q6seEUoqjcQQ2GzfQFtg_3GqGnsvWCDoZUoUVv6QHo"
        self.subdomain = "{}-{}".format(subdomain_base, str(uuid.uuid4()))

    def start(self, ngrok_die_check_delay=0.5):
        """Starts the thread on the background and blocks until we get a tunnel URL.
        :return: the tunnel URL which is now publicly open for your localhost port
        """

        logger.debug("Starting ngrok tunnel %s for port %d", self.subdomain, self.port)

        self.ngrok = subprocess.Popen(["ngrok", "-authtoken={}".format(self.auth_token), "-log=stdout", "-subdomain={}".format(self.subdomain), str(self.port)], stdout=subprocess.DEVNULL)

        # See that we don't instantly die
        time.sleep(ngrok_die_check_delay)
        assert self.ngrok.poll() is None, "ngrok terminated abrutly"
        url = "https://{}.ngrok.io".format(self.subdomain)
        return url

    def stop(self):
        """Tell ngrok to tear down the tunnel.

        Stop the background tunneling process.
        """
        self.ngrok.terminate()

tunnel = NgrokTunnel(8000, "7q6seEUoqjcQQ2GzfQFtg_3GqGnsvWCDoZUoUVv6QHo")
tunnel.start()

swiftype_engine_search_query = "checkout"

swiftype_engine_urls = {
    "faq": "https://search-api.swiftype.com/api/v1/engines/paddle-faq/search.json",
    # "documentation": "https://search-api.swiftype.com/api/v1/engines/paddle-documentation/search.json",
    # "blog": "https://search-api.swiftype.com/api/v1/engines/paddle-blog/search.json",
    # "developer": "https://search-api.swiftype.com/api/v1/engines/paddle-developer/search.json",

}

swiftype_call_params = {
    "auth_token": "6oMTu5o6HVtFMPjbHTDJ",
    "q": swiftype_engine_search_query
}

def call_swiftype_search(url):
    response = requests.get(url, swiftype_call_params)
    return response

