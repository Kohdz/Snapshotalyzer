# snapshotalyzer

A python-based command line utility to manage AWS EC2 instances using boto3. This includes lifecycle management, listing instances and volumes, and managing snapshots.

Table Of Contents:

1. [Setup](#setup)
   - [Installation](#installation)
   - [Configuring](#configuring)
   - [Running](#running)
2. [Background Information](#background-information)
3. [Sample Commands](#sample-commands)
4. [TODO](#todo)

## Setup

### Installation:

snapshotalyzer can be installed using a distrubution wheel hosted in AWS S3 bucket

`pip install https://snapshotalyzer-dist-demo.s3.amazonaws.com/snapshotalyzer-0.1-py3-none-any.whl`

## Configuring

shotty uses the configuration file created by the AWS cli. e.g.

`aws configure --profile shotty`

## Running

`pipenv run "python shotty/shotty.py <command> <subcommand> <--project=PROJECT>"`

_command_ is instances, volumes, or snapshots
_subcommand_ - depends on command
_project_ is optional

## Background Information

An `EC2` instance is a virtual server in AWS cloud. `EC2's` have hardrives attached to them, which Amazon calls `volumes`. Volumes have data on them. AWS allows you to backup the volumes/data using `snapshots`. A `snapshot` just an entire copy of the data at one point in time. You can use `snapshots`to restore server in case it gets deleted
or you can use it to make exact duplicates of that server in case you need to scale up your application. AWS allows you to manage snapshots with a control pannel, howerver, depending on how many instances you have this can be quite a cumbersome process.

Here is the process one has to go through to make a `snapshot`:

    1. go to your instances
    2. select the instances you would like to create a snapshot of
    3. click the acction button, hover over `Instance State` and select stop.
    4. Wait for the instances to stop; depending on how large the instance is, it may take considerable time
    5. reselect the instanc
    6. find the `root device`, click it and on the popup select `EBSID`, which is the volume
    7. Click the action button again and select "create snapshot"
    8. Once complete, restart the instances

## Sample Commands:

list instances: `python shotty/shottty.py instanes start`
list volumes: 'python shotty/shotty.py volumes list
create snapshot: 'python shotty/shotty.py instances snapshot --project valkrie'
create recent snapshot: 'python shotty/shotty.py instances snapshot list
create all snapshot: 'python shotty/shotty.py instances snapshot list --all

## TODO:

1. Add the ability to "reboot" instaces
2. Add a "-force" flag to the "instances stop", "start", "snapshot", and "reboot" commands
   - if "-project" isn't set, exit the command immediately with an error message, unless "-force" is set
3. Add a "-profile" option oto the "ci" group, which let's you specifiy a different profile
   - e.g "shotty -profile Kyle instances stop -force"
