# Dynamic versioning plugin for Poetry
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This package is a plugin for [Poetry](https://github.com/sdispater/poetry)
to enable dynamic versioning based on tags in your version control system,
powered by [Scmver](https://pypi.com/scmver).

Since Poetry does not yet officially support plugins
(refer to [this issue](https://github.com/sdispater/poetry/issues/693))
as of the time of writing on 2019-12-10, this package takes some novel
liberties to make the functionality possible. As soon as official support
lands, this plugin will be updated to do things the official way.


## Installation
Python 3.5 (or newer) and Poetry 0.12.1 (or newer) are required.

* Run `pip install poetry-scmver`
* Add this to your pyproject.toml:
  ```toml
  [tool.scmver]
  enable = true
  ```

Note that you must install the plugin in your global Python installation,
**not** as a dependency in pyroject.toml, because the virtual environment
that Poetry creates cannot see Poetry itself and therefore cannot patch it.

## Configuration
In your pyproject.toml file, you may configure the following options:

`[tool.scmver]`: General options.

  * `enable`: Boolean. Default: false. Since the plugin has to be installed globally, this setting is an opt-in per project. This setting will likely be removed once plugins are officially supported.
  * `root`: A path of the working directory. Default: ``'.'``
  * `spec`: A version specifier to construct the public version indentifiers. It will be incremented by the number of commits from the latest tag.
    
    * ``major``: It will increment the major version.
    * ``minor``: It will increment the minor version.
    * ``micro`` or ``patch``: It will increment the micro (patch) version.
    * ``post``: It will increment the post-release segment.
    * ``major.dev``: It will increment the development release segment after incrementing the major version by 1.
    * ``minor.dev``: It will increment the development release segment after incrementing the minor version by 1.
    * ``micro.dev`` or ``patch.dev``: It will increment the development release segment after incrementing the micro (patch) version by 1.
    
    Default: ``'post'``
  
  * `local`: A ``string`` to construct the local version identifiers.

    Available keywords:

    * ``{distance}``
    * ``{reivison}``
    * ``{branch}``
    * ``{utc}``      - Return value of ``datetime.datetime.utcnow()``
    * ``{local}``    - Return value of ``datetime.datetime.now()``

    Default: ``'{local:%Y-%m-%d}'``

  * `version`: A regular expression object to extract the version from SCM tags. It should contain the version group.
  * `write_to`: A path to a file which will be generated using ``template``.
  * `template`: A format string which is used by ``write_to``.
    Available keywords:

    * ``{version}``
    * ``{revision}``
    * ``{branch}``

  * `bazaar.tag`: A regular expression pattern to filter tags.
  * `fossil.tag`: A regular expression pattern to filter tags.
  * `git.tag`: It will be passed to ``git describe`` as ``--match``.
  * `mercurial.tag`: A regular expression pattern to filter tags.
  * `subversion.tag`: A regular expression pattern to filter tags.
  * `subversion.trunk`: A relative repository path of the trunk directory. Default: ``'trunk'``
  * `subversion.branches: A relative repository path of the directory where branches are located. Default: ``'branches'``
  * `subversion.tags`: A relative repository path of the directory where tags are located. Default: ``'tags'``

Simple example:

```toml
[tool.semver]
enable = true
write_to = "version.py"
```

## Implementation
In order to side-load plugin functionality into Poetry, this package
does the following:

* Upon installation, it delivers a `zzz_poetry_semver.pth`
  file to your Python site-packages directory. This forces Python to
  automatically load the plugin after all other modules have been loaded
  (or at least those alphabetically prior to `zzz`).
* It patches `builtins.__import__` so that, whenever the first import from
  Poetry finishes, `poetry.console.main` will be patched. The reason we have
  to wait for a Poetry import is in case you've used the get-poetry.py script,
  in which case there is a gap between when Python is fully loaded and when
  `~/.poetry/bin/poetry` adds the Poetry lib folder to the PYTHONPATH.
* The patched version of `poetry.console.main` will then, when called,
  additionally patch either `poetry.poetry.Poetry.create()` or
  `poetry.factory.Factory.create_poetry()` (depending on your Poetry version)
  to replace the version from your pyproject.toml file with the dynamically
  generated version.

## Changelog

See [Changelog](CHANGELOG.md)

## License

See [License](LICENSE.txt)