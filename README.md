# fetching

Python tool for automatically wrapping multiple (possibly private) Python libraries \
into a single portable module file.

## purpose

This tool can be used to automatically extract files from multiple repositories and \
package them into a single portable module file.

## installation and usage

The package is available on PyPi:

```shell
python -m pip install fetching
```

The library can be imported as follows:

```python
from fetching import Fetching

targets = {"name": "pypa/pip", "files": ["src/pip.py"], "tag": "2.1.1"}
dependencies, requirements = Fetching().fetch_and_build(targets)
```

And can also be run as a standalone module:

```bash
python -m fetching --targets "<DEPENDENCIES>" --token <GH_TOKEN> --dest <output_file_path>
```

The `targets` argument in both of the above examples is a list of dictionaries with the following \
structure:

```json
{
  "name": <REPOSITORY_NAME>,
  "files": [<FILE_PATHS>],
  "tag": <RELEASE_TAG>
}
```

If you need to pull from a specific commit hash rather than a release tag, you can omit the `tag` \
parameter and instead include a `ref` parameter with the target commit hash. If both `tag` and `ref` \
are omitted, target dependencies will be pulled from the most recent commit on `main`.

Fetching relies on the GitHub API, and as such won't work unless you either pass a valid \
token to the `fetch_and_build()` method, or store one in either the `GH_TOKEN` or `GITHUB_TOKEN` \
environment variables.

## testing

Running `test.py` relies on either the `GH_TOKEN` or `GITHUB_TOKEN` environment variables \
being set.