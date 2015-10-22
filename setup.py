from setuptools import setup, find_packages

setup(
    name="parchment",
    version="0.1.0",
    packages=find_packages(),
    description="a simple static site generator",
    include_package_data=True,
    author="Taff Gao",
    author_email="gaotongfei1995@gmail.com",
    url="https://github.com/gaotongfei/parchment",
    install_requires=[
        "click==5.1",
        "Jinja2==2.8",
        "MarkupSafe==0.23",
        "mistune==0.7.1",
        "PyYAML==3.11",
        "wheel==0.24.0"
    ],
    entry_points='''
        [console_scripts]
        parchment_init = src.commands.init_command:init
        parchment_g = src.commands.generate_command:generate
        parchment_generate = src.commands.generate_command:generate
    ''',
)
