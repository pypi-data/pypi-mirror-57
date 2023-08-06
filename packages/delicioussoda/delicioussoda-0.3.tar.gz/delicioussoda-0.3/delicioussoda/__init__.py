"""
DeliciousSoda
~~~~~~~~~~~~~

DeliciousSoda is a webscraper for robots.txt files. Basic usage:

>>> from delicioussoda import DeliciousSoda
>>> s = DeliciousSoda("https://www.google.com")
>>> s.get_allowed()
['Allow: /search/about', 'Allow: /search/static', ...]
>>> robot.end()

:copyright: (c) 2019 by Ben Antonellis.
:license: MIT, see LICENSE for more details. 

"""

# Standard Library Imports
import os
from typing import List, Dict
import urllib.request

# Install Requires
import requests
from requests.exceptions import SSLError

class DeliciousSoda():
    """
    A custom robots.txt parser. Assumes " User-agent: * ".
    """
    
    def __init__(self, url=None):
        self.__url = url
        self.__robots_file = None

        if self.__url is not None:
            self.set_url(url)
            self.__validate_url()
            self.__download_robots()

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
        Checks current url's validity.
        """
        try:
            response = requests.get(self.__url, timeout=5)
        except SSLError:
            raise InvalidUrlException("Invalid Url.")

    def __download_robots(self) -> None:
        """
        Downloads robots.txt file from url.
        """
        if self.__url is not None:
            self.__validate_url()
            self.__robots_file, _ = urllib.request.urlretrieve(self.__url, filename="page.html")
            return
        raise InvalidUrlException("Invalid Url.")
    
    def get_allowed(self) -> List[str]:
        """
        Gets all allowed directories for the url.
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
        Gets all disallowed directories for the url.
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

    def end(self) -> None:
        """
        Deletes "page.html" and performs other clean up tasks.
        """
        os.remove(self.__robots_file)
        if os.path.exists(self.__robots_file):
            raise FileExistsError("System failed to delete robot file.")


class InvalidUrlException(Exception):
    """ Url passed to DeliciousSoda object is `Invalid`. """
    pass

# Example Usage

if __name__ == "__main__":
    robot = DeliciousSoda("https://www.google.com")
    allowed = robot.get_allowed()
    disallowed = robot.get_disallowed()
    both = robot.get_all()
    robot.end()