# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['et_micc']

package_data = \
{'': ['*'],
 'et_micc': ['templates/app-simple/{{cookiecutter.project_name}}/tests/test_{{cookiecutter.cli_app_name}}.{{cookiecutter.py}}',
             'templates/app-simple/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/*',
             'templates/app-sub-commands/{{cookiecutter.project_name}}/tests/test_{{cookiecutter.cli_app_name}}.{{cookiecutter.py}}',
             'templates/app-sub-commands/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/*',
             'templates/module-cpp/{{cookiecutter.project_name}}/tests/test_cpp_{{cookiecutter.module_name}}.{{cookiecutter.py}}',
             'templates/module-cpp/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/cpp_{{cookiecutter.module_name}}/CMakeLists.txt',
             'templates/module-cpp/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/cpp_{{cookiecutter.module_name}}/CMakeLists.txt',
             'templates/module-cpp/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/cpp_{{cookiecutter.module_name}}/CMakeLists.txt',
             'templates/module-cpp/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/cpp_{{cookiecutter.module_name}}/{{cookiecutter.module_name}}.cpp',
             'templates/module-cpp/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/cpp_{{cookiecutter.module_name}}/{{cookiecutter.module_name}}.cpp',
             'templates/module-cpp/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/cpp_{{cookiecutter.module_name}}/{{cookiecutter.module_name}}.cpp',
             'templates/module-cpp/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/cpp_{{cookiecutter.module_name}}/{{cookiecutter.module_name}}.rst',
             'templates/module-cpp/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/cpp_{{cookiecutter.module_name}}/{{cookiecutter.module_name}}.rst',
             'templates/module-cpp/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/cpp_{{cookiecutter.module_name}}/{{cookiecutter.module_name}}.rst',
             'templates/module-f2py/{{cookiecutter.project_name}}/tests/test_f2py_{{cookiecutter.module_name}}.{{cookiecutter.py}}',
             'templates/module-f2py/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/f2py_{{cookiecutter.module_name}}/{{cookiecutter.module_name}}.f90',
             'templates/module-f2py/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/f2py_{{cookiecutter.module_name}}/{{cookiecutter.module_name}}.f90',
             'templates/module-f2py/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/f2py_{{cookiecutter.module_name}}/{{cookiecutter.module_name}}.rst',
             'templates/module-f2py/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/f2py_{{cookiecutter.module_name}}/{{cookiecutter.module_name}}.rst',
             'templates/module-py/{{cookiecutter.project_name}}/tests/test_{{cookiecutter.module_name}}.{{cookiecutter.py}}',
             'templates/module-py/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/{{cookiecutter.module_name}}.{{cookiecutter.py}}',
             'templates/package-base/hooks/*',
             'templates/package-base/{{cookiecutter.project_name}}/.gitignore',
             'templates/package-base/{{cookiecutter.project_name}}/.gitignore',
             'templates/package-base/{{cookiecutter.project_name}}/.gitignore',
             'templates/package-base/{{cookiecutter.project_name}}/LICENSE',
             'templates/package-base/{{cookiecutter.project_name}}/LICENSE',
             'templates/package-base/{{cookiecutter.project_name}}/LICENSE',
             'templates/package-base/{{cookiecutter.project_name}}/pyproject.toml',
             'templates/package-base/{{cookiecutter.project_name}}/pyproject.toml',
             'templates/package-base/{{cookiecutter.project_name}}/pyproject.toml',
             'templates/package-base/{{cookiecutter.project_name}}/tests/__init__.{{cookiecutter.py}}',
             'templates/package-base/{{cookiecutter.project_name}}/tests/__init__.{{cookiecutter.py}}',
             'templates/package-base/{{cookiecutter.project_name}}/tests/test_{{cookiecutter.package_name}}.{{cookiecutter.py}}',
             'templates/package-base/{{cookiecutter.project_name}}/tests/test_{{cookiecutter.package_name}}.{{cookiecutter.py}}',
             'templates/package-general-docs/hooks/*',
             'templates/package-general-docs/{{cookiecutter.project_name}}/APPS.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/APPS.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/APPS.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/AUTHORS.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/AUTHORS.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/AUTHORS.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/HISTORY.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/HISTORY.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/HISTORY.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/apps.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/apps.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/apps.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/apps.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/apps.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/authors.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/authors.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/authors.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/authors.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/authors.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/history.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/history.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/history.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/history.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/history.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/index.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/index.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/index.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/index.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/index.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/installation.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/installation.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/installation.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/installation.rst',
             'templates/package-general-docs/{{cookiecutter.project_name}}/docs/installation.rst',
             'templates/package-general/hooks/*',
             'templates/package-general/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}/*',
             'templates/package-simple-docs/hooks/*',
             'templates/package-simple-docs/{{cookiecutter.project_name}}/API.rst',
             'templates/package-simple-docs/{{cookiecutter.project_name}}/API.rst',
             'templates/package-simple-docs/{{cookiecutter.project_name}}/README.rst',
             'templates/package-simple-docs/{{cookiecutter.project_name}}/README.rst',
             'templates/package-simple-docs/{{cookiecutter.project_name}}/docs/*',
             'templates/package-simple/hooks/*',
             'templates/package-simple/{{cookiecutter.project_name}}/{{cookiecutter.package_name}}.{{cookiecutter.py}}']}

install_requires = \
['click>=7.0,<8.0',
 'cookiecutter>=1.6.0,<2.0.0',
 'semantic_version>=2.8.3,<3.0.0',
 'sphinx-click>=2.3.0,<3.0.0',
 'sphinx-rtd-theme>=0.4.3,<0.5.0',
 'tomlkit>=0.5.8,<0.6.0',
 'walkdir>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['micc = et_micc:cli_micc.main']}

setup_kwargs = {
    'name': 'et-micc',
    'version': '0.10.0',
    'description': 'A practical Python project skeleton generator.',
    'long_description': '****\nMicc\n****\n\n.. image:: https://img.shields.io/pypi/v/micc.svg\n        :target: https://pypi.python.org/pypi/micc\n\n.. image:: https://img.shields.io/travis/etijskens/micc.svg\n        :target: https://travis-ci.org/etijskens/micc\n\n.. image:: https://readthedocs.org/projects/micc/badge/?version=latest\n        :target: https://micc.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n\n`Micc <https://github.com/etijskens/et-micc>`_ is a Python project manager: it helps \nyou organize your Python project from simple single file modules to fully fledged \nPython packages containing modules, sub-modules, apps and binary extension modules \nwritten in Fortran or C++. Micc_ organizes your project in a way that is considered good\npractice by a large part of the Python community. \n\n* Micc_ helps you create new projects. You can start small with a simple one-file \n  package and add material as you go, such as:\n  \n  * Python **sub-modules** and **sub-packages**,\n  * **applications**, also known as command line interfaces (CLIs). \n  * **binary extension modules** written in C++ and Fortran. Boiler plate code is \n    automatically added as to build these binary extension with having to go through\n    al the details. This is, in fact, the foremost reason that got me started on this\n    project: For *High Performance Python* it is essential to rewrite slow and \n    time consuming parts of a Python script or module in a language that is made \n    for High Performance Computing. As figuring out how that can be done, requires \n    quite some effort, Micc_ was made to automate this part while maintaining the \n    flexibility. \n  * Micc_ adds typically files containing example code to show you how to add your\n    own functionality.\n    \n* Micc_ can automatically **extract documentation** from the doc-strings of your files, \n  and build html documentation that you can consult in your browser, or a .pdf \n  documentation file.\n* With a little extra effort the generated html **documentation is automatically published** \n  to `readthedocs <https://readthedocs.org>`_.\n* Micc_ helps you with **version management and control**.\n* Micc_ helps you with **testing** your code.\n* Micc_ helps you with **publishing** your code to e.g. `PyPI <https://pypi.org>`_, so\n  that you colleagues can use your code by simply running `pip install your_nifty_package`.\n  \nFor details see the `Micc documentation <https://et-micc.readthedocs.io/en/latest/>`_.\n\nMicc_ does not do all of this by itself. For many things it relies on other strong \nopen source tools and it is therefor open source as well (MIT Licence). Here is a list \nof tools micc_ is using or cooperating with happily:\n\n* `poetry <https://github.com/sdispater/poetry>`_: dependency management, virtual \n  environments.\n* `pyenv <https://github.com/pyenv/pyenv>`_: management of different Python versions\n* `pipx <https://github.com/pipxproject/pipx/>`_: installation of CLIs in a system-wide  \n  way.\n* `cookiecutter <https://github.com/audreyr/cookiecutter>`_ for creating templates for \n  all the things that can be added to your project.\n* `sphinx <http://www.sphinx-doc.org/>`_: building of documentation.\n* `git <https://www.git-scm.com/>`_: version control.\n* `python-semanticversion <https://github.com/rbarrois/python-semanticversion/blob/master/docs/index.rst>`_:\n  management of version string according to version specification `Semver 2.0 <http://semver.org/>`_.\n* `pytest <https://www.git-scm.com/>`_: testing your code.\n* `click <https://click.palletsprojects.com/en/7.x/>`_: a pythonic and intuitive \n  way of developing CLIs. \n* `F2py <https://docs.scipy.org/doc/numpy/f2py/>`_, which is part of `Numpy <https://numpy.org/>`_, \n  the standard for numerical computing in Python. F2py_ easily transforms modern Fortran\n  code into performant binary extension modules.\n* `CMake <https://cmake.org>`_ and `pybind11 <https://pybind11.readthedocs.io/en/stable/>`_ as the \n  glue between C++ code and performant binary extension modules.\n\nRoadmap\n=======\nThese features are still on our wishlist:\n\n* Contininous integtration (CI)\n\n',
    'author': 'Engelbert Tijskens',
    'author_email': 'engelbert.tijskens@uantwerpen.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/etijskens/et-micc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
