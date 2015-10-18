from setuptools import setup, find_packages
import src

setup(
    name='Taff Gao',
    version='v0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'Cython',
        'Jinja2',
        'MarkupSafe',
        'mistune',
        'PyYAML',
        'wheel'
    ],
    entry_points='''
        [console_scripts]
		parchment_init = src.commands.init_command:init
        parchment_g = src.commands.generate_command:generate
        parchment_generate = src.commands.generate_command:generate
    ''',
)
