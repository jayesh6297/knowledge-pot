# Getting Started

For learning purpose we are using minikube to mimic single cluster on our local system. feel free to use kind or k3s
For development purpose. and testing things out on local system

## installation of minikube
if you're on arch linux you can directly fire command `sudo pacman -S minikube` if not you do following. 

```sh
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```

**Setting Up &rarr;**

We will need docker or podman with minkube in order to run it. Although podman is supported it has experimental driver so i suggest we use docker for smoother transition and some less errors. When using docker there is not need to use hypervisor. lets start with configuration

=== "start cluster with docker driver"

    ```sh
    minikube start --driver=docker
    ```
=== "set docker driver as default"

    ```sh
    minikube config set driver docker
    minikube start
    ```
either of command will be fine. if you use docker only then i suggest you use minikube config to set docker driver as always.

- Check the minikube node ip using `minikube IP`. Or you can ssh into it using `minikube ssh` &larr; this will take you into minikube node
- Fire `minikube status` to check running status
- Hit `docker ps` after `minikube ssh` to check running containers and all services running in control plane

!!! note
    minikube only create one node and it behaves as master and worker node

!!! note
    For our convinience we will set shortcut to `minikube` as `mk` 
    1. open `.zshrc` or `.bashrc` in your favourite editor
    2. type alias mk="minikube"
