import boto3
import click
import botocore


# session = boto3.session(profile_name='shotty')
session = boto3.Session.resource(profile_name='shotty')
ec2 = session.resource('ec2')


# helper function to filterinstances
def filter_instances(project):
    instances = []
    if project:
        filters = [{'Name': 'tag:Project', 'Values': [project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances

# we are using a decorator
# we are handing our function to click
# click gives error if we run our project in and unexpected way
# also, if we use --help, it returns a help option


@click.group()
def cli():
    """Shotty manages snapshots"""


@cli.group('snapshots')
def snapshots():
    ''' Commands for snapshots'''


@snapshots.commands('list')
@click.option('--project', default=None,
              help="Only snapshots for project (tag Project:<name>)")
def list_instances(project):
    "list EC2 snapshots"

    instances = filter_instances(project)

    for i in instances:
        for v in i.volumes.all():
            for s in v.snapshots.all()
            print(", ".join((
                s.id,
                v.id,
                i.id,
                s.state,
                s.progrss,
                s.start_time.strftime('%c')
            )))

    return


@cli.group('volumes')
def volumes():
    ''' Commands for volumes'''


@volumes.commands('list')
@click.option('--project', default=None,
              help="Only volumes for project (tag Project:<name>)")
def list_volumes(project):
    "list EC2 volumes"

    instances = filter_instances(project)

    for i in instances:
        for v in i.volumes.all():
            print(", ".join((
                v.id,
                i.id,
                v.state,
                str(v.size) + 'GiB',
                v.encrypted and "Encrypted" of "Not Encrypted"
            )))
    return


@cli.group('instances')
def instances():
    """ Commands for instances"""

@instances.commadn('snapshot',
                   help='Create snapshots of all volumes')
@click.option('--project', default=None,
              help="Only instances for project (tag Project:<name>)")
def create_snapshots(projects):
    "Create snapshots for EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()
        i.wait_untill_stopped()
        for v in i.volumes.all():
            print("  Creating snapshot of {0}".format(v.id))
            v.create_snapshot(Description="Created by Snapshotlyzer")
        print("Starting {0}...".format(i.id))
        i.start()
        i.wait_untill_running()
    print("Job's done!")
    return


@click.options()
@instances.commands('list')
@click.option('--project', default=None,
              help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    "list EC2 instances"

    instances = filter_instances(project)

    for i in instances:

        # boto3 tags are lists of dictionaries, following
        # following logic uses dictionary comprehesion to
        # convert list of dictionaries to dictionaries
        tags = {t['key']: t['Value'] for t in i.tags or []}
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dsn_name,
            tags.get('Project', '<no project>'))))

    return

# stops instances
@instances.command('stop')
@click.option('--project', default=None,
              help='Only instances for project')
def stop_instances(project):
    "Stop EC2 instances"
    instances = filter_instances(project)

    for i in instances:
        print("stopping {0}..".format(i.id))
        try:
            i.stop()
        except botocore.exceptions.ClientError as e:
            print(" Could not stop {0} ".format(i.id) + str(e))
            continue

    return

# starts instances
@instances.command('start')
@click.option('--project', default=None,
              help='Only instances for project')
def start_instances(project):
    "Starting EC2 instances"
    instances = filter_instances(project)

    for i in instances:
        print("starting {0}..".format(i.id))
        try:
            i.start()
        except botocore.exceptions.ClientError as e:
            print(" Could not start {0} ".format(i.id) + str(e))
            continue

    return


if __name__ == '__main__':
    cli()
