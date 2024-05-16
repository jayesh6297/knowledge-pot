# Using Kubectl command

!!! tip 
    for simplicity add alias `kc`=`kubectl`

## Simple commands
- `kc cluster-info` checks the cluster information by showing coredns, control planes information and ip address.
- `kc get nodes` or `kc get no` displays the nodes.
- `kc get namespaces` displays all namespaces in node.
-  No pods have yet been generated in the default namespace. However, you can attempt `kc get po -n kubesystem`, which retrieves all pods in the kubsystem namespace.
- `kc get po -n kubesystem -o wide` gives you more information such as ip address of each pod and nodes it associated with.

## Creating pods
- `kc run pod_name --image image_name` this command creates and runs pod and it will also automatically pulls image form dockerhub for us. ex `kc run nginx --image nginx` will create pod named nginx with image nginx. You can view using `kc get po -o wide nginx` command to check if pod is running or not.
- Describe the same pod using `kc describe po nginx`, It will show you details such as name, container, ip, namespace, label, node starttime, etc.
- Even though we deployed nginx pod but we can not access the port. Because we haven't created services necessary to access to exposed address.
- Now lets get some extra information about the pod
    - Fire `mk ssh`
    - Fire `docker ps --filter name=nginx`
    - You can see 2 pods &rarr
        - 1st is normal pod which is what we created
        - 2nd with `pause` keyword created by k8s to keep container namespace
        - we shoudn't not touch the second pod type
    - Now go to container using `docker exec -it container_id sh`
        - hit `cat /etc/hostname` which will show you hostname of pod
        - hit `hostname -i` which will show you ip of pod and should be same as we saw in when we ran `describe` command
    - Finally fire `curl localhost` abd you should see welcome page of nginx
- You can delete pod using `kc delete po nginx`

## Managin deployments
- Create deployment using `kc deploy deployment-name --image deployment-image` which will also create neccessary pods in our case it's just one. ex `kc deply nginx-deployment --image nginx`
- Describe same deployment using `kc describe deploy nginx-deployment`, you will get deployment details
- Use `kc scale deploy ngnix-deployment --replicas 5` to scale up the replicaset to 5, which essentially means it will include 5 pods. 
- Scale deployment using provided quantities of replicas. Likewise, you can use the same command to scale down; but, this time, specify the number of less desired replicas, and it will scale down to that amount.
 
!!! warning
    pod and deployment are different entities in k8s

## Managing services
- Even after we created the deployment, one of the client's pod connections will still fail. However, if you ssh into the node and attempt to connect to the pod's IP, you will succeed since pods' IPs are dynamic; hence, it isn't recommended to connect to them using an IP address to mitigate such a scenario. We will now create service to facilitate communication between pods and also client.
- Creating cluster ip
    - cluster ip are accessible in any cluster within the node.
    - generally they are excellent choice for internal communication withini cluster as once ip is assigned is never chnages.
    - use `kc expose deploy nginx-deployment --port 8080 --traget 80` to create cluster ip.
    - it will also take care of load balancing for us.
    - you can view clusterIP info using `kc get svc -o wide`. so you can fiddle with ip to communicate internally.
- Creating node port
    - use command `kc expose deploy nginx-deployment --type NodePort --port 80` 
    - node port are accessible outside of cluster such our client
    - port assigned to service url is of random
    - to get the service url hit the command `mk service nginx-deployment --url`
- Creating load balancer using command `kc expose deploy nginx-deployment --type LoadBalancer --port 80`. there will be external IP which is pending in ase of minkube and & will be assigned automatically in cloud. It is also accessible outside of cluster and can be accessed using localhost in our case.
