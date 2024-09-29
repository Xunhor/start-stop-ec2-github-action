import boto3
import os
import sys

def control_ec2(action, instance_id):
    ec2 = boto3.client('ec2', region_name=os.environ['AWS_REGION'])

    try:
        instance_info = ec2.describe_instances(InstanceIds=[instance_id])
        state = instance_info['Reservations'][0]['Instances'][0]['State']['Name']

        if action == "start":
            if state == "running":
                print(f'A instância {instance_id} já está em execução.')
            else:
                response = ec2.start_instances(InstanceIds=[instance_id])
                print(f'Iniciando a instância: {instance_id}')
                print(response)

        elif action == "stop":
            if state == "stopped":
                print(f'A instância {instance_id} já está parada.')
            else:
                response = ec2.stop_instances(InstanceIds=[instance_id])
                print(f'Parando a instância: {instance_id}')
                print(response)

        else:
            print('Ação inválida. Use "start" ou "stop".')
            sys.exit(1)

    except Exception as e:
        print(f'Erro ao controlar a instância: {e}')
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python ec2_control.py <start|stop> <instance_id>")
        sys.exit(1)

    action = sys.argv[1].lower()
    instance_id = sys.argv[2]
    control_ec2(action, instance_id)
