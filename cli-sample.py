import argparse

import kubernetes_cli
import docker_cli
parser = argparse.ArgumentParser(description='execute a command')
parser.add_argument('action', default="",
                    help="kubernetes or docker")
args = parser.parse_args()
if args.action == "kubernetes":
    kubernetes_cli.main()
elif args.action == "docker":
    docker_cli.main()
else:
    print('unknown argument')