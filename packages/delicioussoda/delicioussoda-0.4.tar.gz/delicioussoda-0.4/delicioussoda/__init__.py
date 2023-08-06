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

__all__ = [
    "DeliciousSoda"
]

# Standard Library Imports
import os
from typing import List, Dict, Union
import urllib.request
from urllib.error import HTTPError

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

    def __str__(self) -> str:
        return f"DeliciousSoda Parsing: {self.__url}"

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
            raise InvalidUrlException("\n\nInvalidUrlException: Invalid Url.\n")

    def __download_robots(self) -> None:
        """
        Downloads robots.txt file from url.
        """
        if self.__url is not None:
            self.__validate_url()
            try:
                self.__robots_file, _ = urllib.request.urlretrieve(self.__url, filename="page.html")
            except HTTPError as error:
                if error.code == 404:
                    raise InvalidUrlException(f"\n\nInvalidUrlException: Site does not have a robots.txt file.\n")
            return
        raise InvalidUrlException("\n\nInvalidUrlException: Invalid Url.\n")

    def get_sitemap(self) -> Union[str, None]:
        """
        Returns the sitemap of the webiste, None if it doesn't exist.
        """
        with open(self.__robots_file, "r") as file:
            for line in file:
                if line.startswith("Sitemap:"):
                    # [9:] removes "Sitemap: " from the string, returning only the url
                    return line[9:].rstrip()
        return None
    
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
                        # [7:] removes "Allow: " from the string, appending only the url #
                        allowed.append(line.rstrip()[7:])
            return allowed
        raise InvalidUrlException("\n\nInvalidUrlException: Invalid Url.\n")

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
                        # [10:] removes "Disallow: " from the string, appending only the url #
                        allowed.append(line.rstrip()[10:])
            return allowed
        raise InvalidUrlException("\n\nInvalidUrlException: Invalid Url.\n")

    def get_all(self) -> Dict[str, List[str]]:
        """
        Returns a dict of both allowed and disallowed directories under User-agent: *.
        """
        if self.__url is not None:
            return {
                "Allow": self.get_allowed(),
                "Disallow": self.get_disallowed()
            }
        raise InvalidUrlException("\n\nInvalidUrlException: Invalid Url.\n")

    def end(self) -> None:
        """
        Deletes "page.html" and performs other clean up tasks.
        """
        os.remove(self.__robots_file)
        if os.path.exists(self.__robots_file):
            raise FileExistsError("\n\nFileExistsError: System failed to delete robot file.\n")


class InvalidUrlException(Exception):
    """ Url passed to DeliciousSoda object is `Invalid`. """
    pass

# Example Usage

if __name__ == "__main__":
    __robot = DeliciousSoda("https://www.google.com")
    __sitemap = __robot.get_sitemap()
    __allowed = __robot.get_allowed()
    __disallowed = __robot.get_disallowed()
    __both = __robot.get_all()
    

    # print(__robot)
    # print(__sitemap)
    # print(__allowed)
    # print(__disallowed)
    # print(__both)

    __robot.end()