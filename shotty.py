import boto3
import click

session = boto3.session(profile_name='shotty')
ec2 = session.resource('ec2')

# we are using a decorator
# we are handing our function to click
# click gives error if we run our project in and unexpected way
# also, if we use --help, it returns a help option
@click_command()
def list_instances():
    "list EC2 instances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dsn_name)))

    return


if __name__ = '__main__':
    list_instances()
