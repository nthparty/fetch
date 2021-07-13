import unittest
import os
import warnings
from fetch import Fetch


class TestFetch(unittest.TestCase):
    f = Fetch()
    fixtures_dir = f"{os.path.dirname(os.path.realpath(__file__))}/fixtures/"

    def test_workflow_single_repo(self):

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        targets = [
            {
                "name": "nthparty/fetch",
                "files": ["fetch/fetch.py"],
                "ref": "85d549faeabe134fa312ad304f8504f212c40bad"
            }
        ]

        dependencies = self.f.fetch(targets)
        content = self.f.build(dependencies)
        self.assertTrue(content == open(f"{self.fixtures_dir}/fetch_single_repo.txt").read())

    def test_workflow_multiple_repo(self):

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        targets = [
            {
                "name": "nthparty/fetch",
                "files": ["fetch/fetch.py"],
                "ref": "85d549faeabe134fa312ad304f8504f212c40bad"
            },
            {
                "name": "nthparty/oblivious",
                "files": ["oblivious/oblivious.py", "test/test_oblivious.py"],
                "ref": "daa92da7197cdcd5dfc89854fa1b672f37096e74"
            }
        ]

        dependencies = self.f.fetch(targets)
        content = self.f.build(dependencies)
        self.assertTrue(content == open(f"{self.fixtures_dir}/fetch_multiple_repo.txt").read())
