<!--

EC2 instance is a virtual server in AWS cloud
EC2's have hardrives attached to them, which Amazon calls Volumes
Volumes have data on them;
ofcourse you would like to back that date on the volumes up

AWS allows you to backup that data using snapshots
A snapshot is just an entire copy of the data at one point in time
you can use snapshots to restore server in case it gets deleted
or you can use it to make exact duplicates of that server
this allows you to scale up your application

aws allows you to manage snapshots with a control pannel
but that is a cursome process espically if you have alot of servets

thus we can add automation using pyhton

A command line took to manage snapshots


shotty instances --help
shotty instances list
shotty snapshot list
shotty instances snapshot --project=Valkyrie


First, install pipenv: then

```
    pipenv install
    pipenv run 'python _find_meteors.py'


 ````


click makes building command lineinterfaces in python easy

 -->

<!--



snapshotalyzer-30000
Demo project to manage AWS EC2 instance snapshots
#
About
This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

Configuring
shotty uses the configuration file created by the AWS cli. e.g.

`aws configure --profile shotty`

Running
pipenv run "python shotty/shotty.py

<command> <subcommand> <--project=PROJECT>"

command is instances, volumes, or snapshots subcommand - depends on command project is optional -->
