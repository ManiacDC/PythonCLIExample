import docker
import json


def main():
    client = docker.from_env()
    containers = client.containers.list(all=False)

    extContainers=[]

    for container in containers:
        extContainers.append({
            "id": container.attrs['Id'],
            "image": client.images.get(container.attrs["Image"]).attrs['RepoTags'][0],
            "command": container.attrs["Path"],
            "created": container.attrs["Created"],
            "status": container.attrs["State"]["Status"],
            "ports": container.attrs["NetworkSettings"]["Ports"],
            "names": container.attrs["Name"]
        })
    print(json.dumps(extContainers))

if __name__ == "__main__":
    main()