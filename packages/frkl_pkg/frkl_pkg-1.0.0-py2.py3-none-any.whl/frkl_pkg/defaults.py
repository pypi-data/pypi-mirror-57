# -*- coding: utf-8 -*-
import os

DEFAULT_CONDA_INSTALL_PATH = os.path.expanduser("~/miniconda3")
NON_VENV_PYTHON_VERSIONS = ["1", "2", "3.0", "3.1", "3.2"]

LOOKUP_PATHS = [
    os.path.expanduser("~/.local/bin"),
    os.path.join(DEFAULT_CONDA_INSTALL_PATH, "bin"),
    os.path.expanduser("~/Library/Python/2.7/bin"),
]


LOOKUP_PATHS_STRING = ":".join(LOOKUP_PATHS)


PIP_WHEEL_DOWNLOAD_URL = "https://files.pythonhosted.org/packages/00/b6/9cfa56b4081ad13874b0c6f96af8ce16cfbc1cb06bedf8e9164ce5551ec1/pip-19.3.1-py2.py3-none-any.whl"
VIRTUALENV_WHEEL_DOWNLOAD_URL = "https://files.pythonhosted.org/packages/c5/97/00dd42a0fc41e9016b23f07ec7f657f636cb672fad9cf72b80f8f65c6a46/virtualenv-16.7.7-py2.py3-none-any.whl"
