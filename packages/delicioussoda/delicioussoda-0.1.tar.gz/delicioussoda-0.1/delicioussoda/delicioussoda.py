"""
DeliciousSoda
~~~~~~~~~~~~~

DeliciousSoda is a webscraper for robot.txt files. Basic usage:

>>> from delicioussoda import DeliciousSoda
>>> s = DeliciousSoda("https://www.google.com")
>>> s.get_allowed()
['Allow: /search/about', 'Allow: /search/static', ...]

:copyright: (c) 2019 by Ben Antonellis.
:license: MIT, see LICENSE for more details. 

"""

from typing import List, Dict

import urllib.request
import requests
from requests.exceptions import SSLError

class DeliciousSoda():
    """
    A custom robots.txt parser. Assumes " User-agent: * "
    """
    
    def __init__(self, url=None):
        self.__url = url
        self.__robots_file = None

    def set_url(self, url: str) -> None:
        """
        Sets DeliciousSoda to retrieve robots.txt from this url.
        """
        if not url.endswith("robots.txt"):
            if url.endswith("/"):
                self.__url = f"{url}robots.txt"
            else:
                self.__url = f"{url}/robots.txt"
        else:
            self.__url = url
        self.__download_robots()

    def __validate_url(self) -> None:
        """
        Checks current url's validity
        """
        try:
            response = requests.get(self.__url, timeout=5)
        except SSLError:
            raise InvalidUrlException("Invalid Url.")

    def __download_robots(self) -> None:
        """
        Downloads robots.txt file from url
        """
        if self.__url is not None:
            self.__validate_url()
            self.__robots_file, _ = urllib.request.urlretrieve(self.__url, filename="page.html")
            return
        raise InvalidUrlException("Invalid Url.")
    
    def get_allowed(self) -> List[str]:
        """
        Gets all allowed directories for the url
        """
        if self.__url is not None:
            with open(self.__robots_file, "r") as file:
                allowed = []
                for line in file:
                    if line == "\n":
                        break
                    if line.startswith("Allow:"):
                        allowed.append(line.rstrip())
            return allowed
        raise InvalidUrlException("Invalid Url.")

    def get_disallowed(self) -> List[str]:
        """
        Gets all disallowed directories for the url
        """
        if self.__url is not None:
            with open(self.__robots_file, "r") as file:
                allowed = []
                for line in file:
                    if line == "\n":
                        break
                    if line.startswith("Disallow:"):
                        allowed.append(line.rstrip())
            return allowed
        raise InvalidUrlException("Invalid Url.")

    def get_all(self) -> Dict[str, List[str]]:
        """
        Returns a dict of both allowed and disallowed directories under User-agent: *.
        """
        if self.__url is not None:
            return {
                "Allow": self.get_allowed(),
                "Disallow": self.get_disallowed()
            }
        raise InvalidUrlException("Invalid Url.")

class InvalidUrlException(Exception):
    """ Url passed to DeliciousSoda object is `Invalid`. """
    pass