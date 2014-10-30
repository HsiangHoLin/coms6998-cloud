import boto.ec2
import boto.beanstock


def connect_ec2(access, secret_key):
    return boto.ec2.connect_to_region("us-east-1",
        saws_access_key_id=access,
        aws_secret_access_key=secret_key)


def get_running_instances(conn):
    reservations = conn.get_all_reservations()
    running = []
    for res in reservations:
        for ins in res.instances:
            running.append(ins.id)
    return reservations


def get_security_groups(conn):
    return conn.get_all_security_groups()


def create_security_group(conn, name):
    if name not in get_security_groups(conn):
        web = conn.create_security_group('apache', 'Our Apache Group')
        web.authorize('tcp', 80, 80, '0.0.0.0/0')
        web.authorize('tcp', 22, 22, '0.0.0.0/0')


def get_key_pairs(conn):
    return conn.get_all_key_pairs()


def launch_instance(conn):
    conn.run_instances(
        'ami-76817c1e',
        key_name='CCBDKey',
        instance_type='t2.micro',
        security_groups=['CCBDSecGrp'])


def stop_instance(conn, id):
    conn.stop_instances(instance_ids=id)


def stop_all(conn, instances):
    conn.stop_instances(instance_ids=instances)


def terminate_instance(conn, id):
    conn.terminate_instances(instance_ids=id)


def terminate_all(conn, instances):
    conn.terminate_instances(instance_ids=instances)


def create_ebs(conn):
    conn.create_volume(30, "us-east-1")


def get_all_ebs(conn):
    return conn.get_all_volumes()


def attach_volume(conn, ins_id, vol_id):
    conn.attach_volume(vol_id, ins_id, "/dev/sdx")
