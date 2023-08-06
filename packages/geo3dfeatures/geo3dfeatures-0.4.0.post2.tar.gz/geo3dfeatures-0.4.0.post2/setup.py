# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['geo3dfeatures', 'geo3dfeatures.tools']

package_data = \
{'': ['*']}

install_requires = \
['daiquiri>=1.5.0,<2.0.0',
 'dask>=0.20.2,<0.21.0',
 'laspy>=1.5.1,<2.0.0',
 'numpy>=1.15,<2.0',
 'pandas>=0.23.4,<0.24.0',
 'plotly>=4.1,<5.0',
 'plyfile>=0.7.0,<0.8.0',
 'scikit-learn>=0.21,<0.22',
 'scipy>=1.2,<2.0',
 'seaborn>=0.9.0,<0.10.0',
 'tables>=3.5,<4.0',
 'tqdm>=4.31.1,<5.0.0']

entry_points = \
{'console_scripts': ['geo3d = geo3dfeatures.tools.__main__:main']}

setup_kwargs = {
    'name': 'geo3dfeatures',
    'version': '0.4.0.post2',
    'description': 'Extract geometry features from 3D point clouds',
    'long_description': 'Extract geometry features from 3D point clouds\n\n# Content\n\nThe project contains the following folders:\n\n+ [geo3dfeatures](./geo3dfeatures) contains source code\n+ [docs](./docs) contains some mardown files for documentation purpose and\n  images\n+ [examples](./examples) contains some Jupyter notebooks for describing data\n+ [tests](./tests); `pytest` is used to launch several tests from this folder\n\nAdditionally, running the code may generate extra subdirectories in a chosen\ndata repository (`./data`, by default).\n\n# How to install\n\nThis projects runs with Python3, every dependencies are managed\nthrough [poetry](https://poetry.eustace.io/).\n\n## Installation from source\n\n```\n$ git clone ssh://git@git.oslandia.net:10022/Oslandia-data/geo3dfeatures.git\n$ cd geo3dfeatures\n$ virtualenv -p /usr/bin/python3 venv\n$ source venv/bin/activate\n(venv)$ poetry install\n```\n\n# Contribution\n\nSee [CONTRIBUTING.md](./CONTRIBUTING.md).\n\n# Run commands\n\nIn order to get the available program commands, consider the program help (`geo3d -h`):\n\n```\nusage: geo3d [-h] {info,sample,index,featurize,cluster,train,predict} ...\n\nGeo3dfeatures framework for 3D semantic analysis\n\npositional arguments:\n  {info,sample,index,featurize,cluster,train,predict}\n    info                Describe an input .las file\n    sample              Extract a sample of a .las file\n    index               Index a point cloud file and serialize it\n    featurize           Extract the geometric feature associated to 3D points\n    cluster             Cluster a set of 3D points with a k-means algorithm\n    train               Train a semantic segmentation model\n    predict             Predict 3D point semantic class starting from a\n                        trained model\n\noptional arguments:\n  -h, --help            show this help message and exit\n```\n\nAny further CLI documentation may be printed with `geo3d <command> -h`.\n\n# Documentation\n\nSome documentation is available, that describes the set of considered geometric\nfeatures, the fixtures (*i.e.* dummy datasets) used for test purpose and a\npractical pipeline use case:\n\n- [Feature set](./docs/features.md)\n- [Test fixtures](./docs/test_fixtures.md)\n- [Command pipeline](./docs/pipeline.md)\n\n# Examples\n\nThe following example has been generated starting from\na [CANUPO](http://nicolas.brodu.net/en/recherche/canupo/) dataset (file `scene.xyz`, with 500k points, 50 neighbors and all the features):\n\n![scene](./docs/images/scene_kmean.png)\n\n___\n\nOslandia – 2019-2020\n',
    'author': 'Damien Garaud',
    'author_email': 'damien.garaud@oslandia.com',
    'url': 'https://github.com/oslandia/geo3dfeatures',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
