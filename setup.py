from setuptools import setup

setup(
    name='snapshotalyzer',
    version='0.1',
    author="Umair Shabbir",
    author_email="",
    description="SnapshotAlyzer is a tool to manage AWS EC2 snapshots",
    license="GLPv3+",
    packages=['shotty'],
    url="https://github.com/Kohdz/Snapshotalyzer",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
