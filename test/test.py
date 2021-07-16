import unittest
import os
import warnings
from fetching import Fetching


class TestFetch(unittest.TestCase):
    f = Fetching()
    fixtures_dir = f"{os.path.dirname(os.path.realpath(__file__))}/fixtures/"

    def fetch_build_compare(self, targets: list, compare_file: str):

        dependencies = self.f.fetch(targets)
        content = self.f.build(dependencies)

        return content == open(f"{self.fixtures_dir}/{compare_file}").read()

    def test_single_by_ref(self):

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        targets = [
            {
                "name": "nthparty/fetching",
                "files": ["fetching/fetching.py"],
                "ref": "055ad6af491f5cd7d308f4fbc5c32852d8748f59"
            }
        ]

        self.assertTrue(self.fetch_build_compare(targets, "fetch_single_by_ref.txt"))

    def test_multiple_by_ref(self):

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        targets = [
            {
                "name": "nthparty/fetching",
                "files": ["fetching/fetching.py"],
                "ref": "055ad6af491f5cd7d308f4fbc5c32852d8748f59"
            },
            {
                "name": "nthparty/oblivious",
                "files": ["oblivious/oblivious.py", "test/test_oblivious.py"],
                "ref": "daa92da7197cdcd5dfc89854fa1b672f37096e74"
            }
        ]

        self.assertTrue(self.fetch_build_compare(targets, "fetch_multiple_by_ref.txt"))

    def test_single_by_tag(self):

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        targets = [
            {
                "name": "pypa/pip",
                "files": ["NEWS.rst"],
                "tag": "21.0"
            }
        ]

        self.assertTrue(self.fetch_build_compare(targets, "fetch_single_by_tag.txt"))

    def test_multiple_by_tag(self):

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        targets = [
            {
                "name": "pypa/twine",
                "files": ["twine/wheel.py", "twine/__main__.py"],
                "tag": "3.2.0"
            },
            {
                "name": "pypa/pip",
                "files": ["setup.py"],
                "tag": "21.1"
            }
        ]

        self.assertTrue(self.fetch_build_compare(targets, "fetch_multiple_by_tag.txt"))

    def test_mixed(self):

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        targets = [
            {
                "name": "nthparty/fetching",
                "files": ["fetching/fetching.py"],
                "ref": "055ad6af491f5cd7d308f4fbc5c32852d8748f59"
            },
            {
                "name": "pypa/twine",
                "files": ["twine/wheel.py", "twine/__main__.py"],
                "tag": "3.2.0"
            },
            {
                "name": "pypa/pip",
                "files": ["setup.py"],
                "tag": "21.1"
            },
            {
                "name": "nthparty/oblivious",
                "files": ["oblivious/oblivious.py", "test/test_oblivious.py"],
                "ref": "daa92da7197cdcd5dfc89854fa1b672f37096e74"
            }
        ]

        self.assertTrue(self.fetch_build_compare(targets, "fetch_mixed.txt"))
