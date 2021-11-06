from kubernetes import client, config
import json



def main():
    config.load_kube_config()

    v1 = client.CoreV1Api()

    pods = v1.list_namespaced_pod("default")

    extPods=[]

    for pod in pods.items:
        readyCount = 0
        restartCount = 0
        for status in pod.status.container_statuses:
            if status.ready:
                readyCount +=1
            restartCount += status.restart_count

            
        extPods.append({
            "namespace": pod.metadata.namespace,
            "name": pod.metadata.name,
            "ready": '{0}/{1}'.format(readyCount, len(pod.status.container_statuses)),
            "status": pod.status.phase,
            "restarts": restartCount,
            "created": pod.status.start_time.strftime("%c")
        })
    print(json.dumps(extPods))

if __name__ == "__main__":
    main()