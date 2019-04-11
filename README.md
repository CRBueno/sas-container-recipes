<div align="center">  
<h1>SAS<sup>®</sup> Viya<sup>®</sup> Container Recipes</h1>
<img src="docs/sas-container-icon.jpg" alt="SAS Containers Icon" height="200">
<p>Framework to build SAS Viya Docker images and create deployments using Kubernetes.</p>

<a href="https://www.sas.com/en_us/software/viya.html">
    <img src="https://img.shields.io/badge/SAS%20Viya-3.4-blue.svg?&colorA=0b5788&style=for-the-badge&logoWidth=30&logo=data:image/png;base64,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"
        alt="SAS Viya Version"/></a>
<a href="https://www.docker.com/">
    <img src="https://img.shields.io/badge/Docker--ce-18+-blue.svg?&style=for-the-badge&colorA=066da5"
        alt="Docker Version"></a>
<a href="https://kubernetes.io/">
    <img src="https://img.shields.io/badge/Kubernetes-1.0+-blue.svg?&style=for-the-badge&colorA=0b5788"
        alt="Kubernetes Version"></a>
</div>

<br>
Container deployments are more lightweight and don't have as much
overhead as traditional virtual machines. By running a SAS engine inside a 
container, you can provision resources more efficiently to address a wide variety
of SAS workloads. Select a base SAS recipe and create custom containers 
with specific products or configurations – e.g, access to data sources, in-database
code and scoring accelerators, or specific analytic capabilities.
For more information see [SAS for Containers](http://support.sas.com/rnd/containers/).

<br>

## Quick Start
Use the instructions on this page to quickly build and launch SAS Viya containers. 
For more extensive infomation about building and launching SAS Viya containers, 
see the [GitHub Project Wiki Page](https://github.com/sassoftware/sas-container-recipes/wiki)
For either single or multiple containers, addons found in 
[the addons directory](https://github.com/sassoftware/sas-container-recipes/tree/master/addons) 
can enhance the base SAS Viya images with SAS/ACCESS, LDAP configuration, and more. 
For each addon, review the [Appendix](https://github.com/sassoftware/sas-container-recipes/wiki/Appendix:-Under-the-Hood#addons)
for important information and any possible prerequisite requirements.

1. Locate your SAS Viya for Linux Software Order Email (SOE) and retrieve the 
`SAS_Viya_deployment_data.zip` file from it. Not sure if your organization 
purchased SAS Software? [Contact Us](https://www.sas.com/en_us/software/how-to-buy.html) 
or get [SAS License Assistance](https://support.sas.com/en/technical-support/license-assistance.html). 
If you have not purchased SAS Software but would like to give it a try, 
please check out our [Free Software Trials](https://www.sas.com/en_us/trials.html).
    
2. Download the latest <a href="https://github.com/sassoftware/sas-container-recipes/releases" alt="SAS Container Recipes Releases">
        <img src="https://img.shields.io/github/release/sassoftware/sas-container-recipes.svg?&colorA=0b5788&colorB=0b5788&style=for-the-badge&" alt="Latest Release"/></a> 
or `git clone git@github.com:sassoftware/sas-container-recipes.git`

3. Choose your flavor and follow the recipe to build, test, and deploy your container(s).

    a. If you are looking for an environment tailored towards individual data scientists and developers, you will be interested in a [SAS programming-only deployment running on a single container](https://github.com/sassoftware/sas-container-recipes#for-a-single-user---sas-viya-programming-only-deployment-running-on-a-single-container).

    b. If you would like an environment suitable for collaborative data science work, then you may be interested in a SAS programming-only deployment or a SAS Viya full [deployment on multiple containers](https://github.com/sassoftware/sas-container-recipes#for-one-or-more-users---sas-viya-programming-only-or-sas-viya-full-deployment-running-on-multiple-containers).


<br>

---

<br>

## For a Single User - SAS Viya Programming-Only Deployment Running on a Single Container

Use these instructions to create a SAS Viya programming-only deployment in a single container for
an independent data scientist or developer to execute SAS code. All code and
data should be stored in a persistent location outside the container.
This deployment includes SAS Studio, SAS Workspace Server, and a CAS server,
which provides in-memory analytics for symmetric multi-processing (SMP).

**A [supported version](https://success.docker.com/article/maintenance-lifecycle) of [Docker-ce (community edition)](https://docs.docker.com/install/linux/docker-ce/centos/) is required.**

### Build the Image

Run the following to create a user 'sasdemo' with the password 'sasdemo' for product evaluation.
A [non-root user](https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user) 
is recommended for all build commands.
```
 ./build.sh --type single --zip ~/my/path/to/SAS_Viya_deployment_data.zip --addons "auth-demo"
```                         

### Run the Container

After the container is built then instructions for how to run the image will be printed out.
```
 docker run --detach --rm --hostname sas-viya-programming \
 --env CASENV_CAS_VIRTUAL_HOST=<my_host_address> \
 --env CASENV_CAS_VIRTUAL_PORT=8081 \
 --publish-all \
 --publish 8081:80 \
 --name sas-viya-programming \
 sas-viya-programming:<VERSION-TAG>  
```
Use the `docker images` command to see what images were built and what the most recent tag is (example: tag `19.0.1-20190109112555-48f98d8`).
Once the docker run command is completed, use `docker ps` to list the running container. 

### Log on to SAS Studio
Go to the address `http://<myhostname>:8081` and start using SAS Studio! 
The `--addons "auth-demo"` build argument created a default user with the username 'sasdemo' and the password 'sasdemo' for product evaluation.

<img src="docs/sas-logon-screen-sasdemo.png" alt="SAS Logon Screen" style="width: 80%; height: 80%; object-fit: contain;">

For more info see the [GitHub Project Wiki Page](https://github.com/sassoftware/sas-container-recipes/wiki).

<br>

---

<br>

## For One or More Users - SAS Viya Programming-Only or SAS Viya Full Deployment Running on Multiple Containers

Use these instructions to build multiple Docker images and then use the images 
to create a SAS Viya programming-only or a SAS Viya full deployment in Kubernetes. 
These deployments can have SMP or massively parallel processing (MPP) CAS servers,
which provide in-memory analytics, and can be used by one or more users. 

A programming-only deployment supports data scientists and programmers who use 
SAS Studio or direct programming interfaces such as Python or REST APIs. 
Understand that this type of deployment does not include SAS Drive, 
SAS Environment Manager, and the complete suite of services that are 
included with a full deployment. Therefore, make sure that you are providing 
your users with the features that they require.

### Prerequisites

- A [supported version](https://success.docker.com/article/maintenance-lifecycle) of [Docker-ce](https://docs.docker.com/install/linux/docker-ce/centos/) (community edition) on Linux or Mac must be installed on the build machine
- Access to a Docker registry: The build process will push built Docker images automatically to the Docker registry. Before running `build.sh` do a `docker login docker.registry.company.com` and make sure that the `$HOME/.docker/config.json` is filled in correctly.
- Access to a Kubernetes environment and [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) installed (required for the deployment step but not required for the build step)
- **Strongly recommended:** A local mirror of the SAS software. [Here's why](https://github.com/sassoftware/sas-container-recipes/wiki/The-Basics#why-do-i-need-a-local-mirror-repository). 

### How to Build
Examples of running `build.sh` to build multiple containers are provided below. A non-root user is recommended for all build commands.

**See the `docs/usage.txt` file or run `./build.sh --help` for the list of all required and optional arguments.**


#### Example One: Programming-Only Deployment, Mulitple Containers

```    
  ./build.sh \
  --type multiple \
  --zip /path/to/SAS_Viya_deployment_data.zip \
  --docker-registry-namespace myuniquename \
  --docker-registry-url myregistry.myhost.com \
  --addons "auth-demo"
```

Here's a summary of what this command does:
- Multiple Docker images for a programming-only deployment are created (`--type multiple`). The software that is deployed is determined by the software entitlement that is provided in the ZIP file from the Software Order Email (`--zip /path/to/SAS_Viya_deployment_data.zip`).
- The images are pushed to the namespace in the Docker Registry (`--docker-registry-namespace myuniquename`), which is located at the Docker registry URL (`--docker-registry-url myregistry.myhost.com`).
- The ingress path (`--virtual-host user-myproject.mylocal.com`) provides the HTTP and HTTPS routes from outside the Kubernetes cluster to services within the cluster.
- A default user is added (`--addons "auth-demo"`), which can be used to log on to SAS Studio. A list of all addons is available in the [project GitHub Wiki](https://github.com/sassoftware/sas-container-recipes/wiki/Appendix:-Under-the-Hood).


#### Example Two: Full Deployment, Multiple Containers

```
  ./build.sh \
  --type full \
  --zip /path/to/SAS_Viya_deployment_data.zip \
  --docker-registry-namespace myuniquename \
  --docker-registry-url myregistry.myhost.com \
  --addons "auth-sssd"
```

Here's a summary of what this command does:
- Multiple Docker images for a full deployment are created (`--type full`). The software that is deployed is determined by the software entitlement that is provided in the ZIP file from the Software Order Email (`--zip /path/to/SAS_Viya_deployment_data.zip`).
- The images are pushed to the namespace in the Docker Registry (`--docker-registry-namespace myuniquename`), which is located at the Docker registry URL (`--docker-registry-url myregistry.myhost.com`).
- The ingress path (`--virtual-host user-myproject.mylocal.com`) provides the HTTP and HTTPS routes from outside the Kubernetes cluster to services within the cluster.
- SSSD is configured inside the container (`--addons "auth-sssd"`) to allow the container authentication to connect to LDAP or Active Directory. A list of all addons is available in the [project GitHub Wiki](https://github.com/sassoftware/sas-container-recipes/wiki/Appendix:-Under-the-Hood).

### Running Multiple Containers

The build process creates Kubernetes manifests that you use to run multiple containers. 

   * For a SAS Viya programming-only deployment, the Kubernetes manifests are located at `builds/multiple/manifests/`
   * For a SAS Viya full deployment, the Kubernetes manifests are located at `builds/full/manifests/`

For information about using the manifests, see [Build and Run SAS Viya Multiple Containers](https://github.com/sassoftware/sas-container-recipes/wiki/Build-and-Run-SAS-Viya-Multiple-Containers).

### Log on to SAS Studio

After the containers are running, users can sign on to SAS Studio.

- If you deployed a programming-only environment, then your environment contains SAS Studio 4.4.
- If you deployed a full environment, then your environment contains both SAS Studio 4.4 and SAS Studio 5.1. By default, you will log on to SAS Studio 5.1.

Here are some examples of how to log on:

- For SAS Studio 4.4 via Docker run without TLS:

  `https://docker-host:8081/SASStudio`

- For SAS Studio 4.4 via Kubernetes:

  `https://ingress-path/SASStudio`

- For SAS Studio 5.1:

  `https://ingress-path/SASStudioV`

<img src="docs/sas-logon-screen.png" alt="SAS Logon Screen" style="width: 80%; height: 80%; object-fit: contain;">

<br>

---

<br>

## Additional Resources

- [Wiki: Documentation](https://github.com/sassoftware/sas-container-recipes/wiki)
- [Issues: Questions and Project Improvements](https://github.com/sassoftware/sas-container-recipes/issues)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [Docker Documentation](https://docs.docker.com/)
- [SAS License Assistance](https://support.sas.com/en/technical-support/license-assistance.html)
- [SAS Software Purchase](https://www.sas.com/en_us/software/how-to-buy.html)
- [SAS Software Trial](https://www.sas.com/en_us/trials.html)

<br>

---

<br>

## Copyright

Copyright 2018 SAS Institute Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

&nbsp;&nbsp;&nbsp;&nbsp;https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
