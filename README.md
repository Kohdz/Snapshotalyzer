# snapshotalyzer-30000

Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the configuration file created by the AWS cli. e.g.

`aws configure --profile shotty`

## Running

`pipenv run "python shotty/shotty.py <command> <subcommand> <--project=PROJECT>"`

_command_ is instances, volumes, or snapshots
_subcommand_ - depends on command
_project_ is optional

list instances: 'python shotty/shottty.py instanes start'
list volumes: 'python shotty/shotty.py volumes list
create snapshot: 'python shotty/shotty.py instances snapshot --project valkrie'
create snapshot: 'python shotty/shotty.py instances snapshot list
create snapshot: 'python shotty/shotty.py instances snapshot list --all

creating snapshots: - go to instances - select the inntaces - click Actions, choose Instance State and select stop - after a few minuets, reselect the instance - find root device, hover over it and clic EBSID (voluem) - then click action and select "create snapshot"
