from setuptools import find_packages,setup
setup(
    name = 'xes-lib',
    version = '0.1.6',
    author = 'xes',
    description = '学而思库',
    packages = find_packages(),
    install_requires = ["requests", "pypinyin"]
    #注意!有__init__.py的文件夹才会被打包
)