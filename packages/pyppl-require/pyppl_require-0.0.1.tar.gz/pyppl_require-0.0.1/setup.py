# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['pyppl_require']
install_requires = \
['cmdy', 'pyppl']

entry_points = \
{'console_scripts': ['pyppl-require = pyppl_require:console',
                     'pyppl_require = pyppl_require:console']}

setup_kwargs = {
    'name': 'pyppl-require',
    'version': '0.0.1',
    'description': 'Requirement manager for processes of PyPPL',
    'long_description': '# pyppl_require\n\nRequirement manager for processes of [PyPPL](https://github.com/pwwang/PyPPL).\n\n## Installation\n```shell\npip install pyppl_require\n```\n\n## Using API\n```python\nfrom pyppl import registerPlugins, Proc\n# have to register before process definition\nregisterPlugins(\'pyppl_require\')\n\nproc = Proc(desc = \'A short description\', long = \'\'\'\n@requires:\n  q:\n    desc: A command line tool that allows direct execution of SQL-like queries on CSVs/TSVs\n    url: http://harelba.github.io/q/index.html\n    version: 1.7.1\n    validate: "{{args.harelba_q}} -v"\n    install: |\n      wget https://cdn.rawgit.com/harelba/q/1.7.1/bin/q -O /tmp/q;\n      chmod +x /tmp/q;\n      sed -i \'s@#!/usr/bin/env python@#!/usr/bin/env python2@\' /tmp/q;\n      install /tmp/q "{{args.harelba_q | ?.__contains__: \'/\' | =:_ | !:\'$bindir$/\'}}"\n\'\'\')\nproc.args.hrelba_q = \'/bin/q\'\n\nproc.require_validate()\n```\n\n```shell\n[proc] Validating q ... Failed.\n[proc] Validation command: bash -c \'q -v\'\n[proc]   bash: q: command not found\n```\n\n```python\n# ...\nproc.require_install(bindir = \'/home/usr/bin/\')\n```\n\n```shell\n[proc] Validating q ... Failed.\n[proc] Validation command: bash -c \'q -v\'\n[proc]   bash: q: command not found\n[proc] Installing q ...\n[proc]   --2019-12-11 18:11:20--  https://cdn.rawgit.com/harelba/q/1.7.1/bin/q\n[proc]   Resolving cdn.rawgit.com... 151.139.237.11\n[proc]   Connecting to cdn.rawgit.com|151.139.237.11|:443... connected.\n[proc]   HTTP request sent, awaiting response... 301 Moved Permanently\n[proc]   Location: https://raw.githubusercontent.com/harelba/q/1.7.1/bin/q [following]\n[proc]   --2019-12-11 18:11:20--  https://raw.githubusercontent.com/harelba/q/1.7.1/bin/q\n[proc]   Resolving raw.githubusercontent.com... 199.232.28.133\n[proc]   Connecting to raw.githubusercontent.com|199.232.28.133|:443... connected.\n[proc]   HTTP request sent, awaiting response... 200 OK\n[proc]   Length: 80435 (79K) [text/plain]\n[proc]   Saving to: `/tmp/q\'\n[proc]\n[proc]        0K .......... .......... .......... .......... .......... 63%  565K 0s\n[proc]       50K .......... .......... ........                        100%  642K=0.1s\n[proc]\n[proc]   2019-12-11 18:11:20 (591 KB/s) - `/tmp/q\' saved [80435/80435]\n[proc]\n[proc] Succeeded!\n[proc] Validating q ... Installed.\n```\n\n## Using command-line tool\n\n`my-pipeline.py`\n\n```python\nfrom pyppl import Proc, PyPPL\n# no need to register before process definition\n\nproc = Proc(desc = \'A short description\', long = \'\'\'\n@requires:\n  q:\n    desc: A command line tool that allows direct execution of SQL-like queries on CSVs/TSVs\n    url: http://harelba.github.io/q/index.html\n    version: 1.7.1\n    validate: "{{args.harelba_q}} -v"\n    install: |\n      wget https://cdn.rawgit.com/harelba/q/1.7.1/bin/q -O /tmp/q;\n      chmod +x /tmp/q;\n      sed -i \'s@#!/usr/bin/env python@#!/usr/bin/env python2@\' /tmp/q;\n      install /tmp/q "{{args.harelba_q | ?.__contains__: \'/\' | =:_ | !:\'$bindir$/\'}}"\n\'\'\')\nproc.args.hrelba_q = \'/bin/q\'\n\n# but have to specify in PyPPL\nPyPPL({\n    \'default\': {\'_plugins\': [\'pyppl_require\']}\n}).start(proc).require().run()\n```\n\n```shell\n> pyppl-require --help\nDescription:\n  Requirement manager for processes of PyPPL\n\nUsage:\n  pyppl-require <command> [OPTIONS]\n\nAvailable commands:\n  validate            - Validate if the requirements have been installed.\n  install             - Install the requirements.\n  help [COMMAND]      - Print help message for the command and exit.\n\n> pyppl-require my-pipeline.py validate\n[tsv.pTsvSql] Validating q ... Failed.\n[tsv.pTsvSql] Validation command: bash -c \'q -v\'\n[tsv.pTsvSql]   bash: q: command not found\n\n```\n\n',
    'author': 'pwwang',
    'author_email': 'pwwang@pwwang.com',
    'url': 'https://github.com/pwwang/pyppl_require',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
