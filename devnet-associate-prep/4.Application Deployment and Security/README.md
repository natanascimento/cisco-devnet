# Application Deployment and Security

# Edge computing

Edge computing is computing that takes place at or near the physical location of either the user or the source of the data. By placing computing services closer to these locations, users benefit from faster, more reliable services while companies benefit from the flexibility of hybrid cloud computing. Edge computing is one way that a company can use and distribute a common pool of resources across a large number of locations.

- Moving the data processing and storage closer to the user
- CDN : Content Delivery Network

- Pros:
    - Speed/Latency
    - Privacy
    - Resiliency
    - Scalability

- Cons
    - Resource Requirements
    - Infrastructure Complexity
    - Distribution of Security, Knowledge, etc

# Cloud Computing Types

## Private Cloud 

- Built on the organization's own infrastructure

## Public Cloud

- Publicly available cloud infrastructure over internet like Azure, Google Cloud Plataform, Amazon Web Services and any more.

## Hybrid Cloud

- Mix of clouds, using public and private cloud for provide a better experience

# Deployment Types 

## Virtual Machines

- Software defined machine

## Bare Metal 

- Refers to the physical computer components
- VMs live inside it

Hypervisor

- Software that manages the virtual environments on the Bare Metal
- Ex: VMWare, VirtualBox, HiperV
- Types:
    - Type 1
        - Directly on the Machine
        - Enterprise grade
        - No underlying os
    - Type 2
        - Runs inside a os
        - Ex: VMWare, VirtualBox

## Containers 

- Another layer of abstraction above VMs
- Isolated execution environments

<div class='img-docker' align="center">
    <img src="https://www.docker.com/sites/default/files/d8/2018-11/docker-containerized-appliction-blue-border_2.png" alt="Docker" width="500">
</div>

# CI/CD Pipeline

## Continuous Integration (CI)

- Provide automation for application deployment, using combination of code changes from multiples contributers based a single code

- Components:
    - Source Code Control:
        - Version Control Management System like a Git; 
    - Automated Build:
        - Automatic Compilation;
    - Unit Testing:
        - Automating the testing of individual components of software;
        - Test Driven Development;
    - Branch Merging:
        - Merging Branches;
    - Integration Testing:
        - How the individual components come together;

## Continuous Delivery (CD)

- Automating the delivery of IT services to the users

- Components:
    - Central Repository
        - Pushing the code into the centralized Repository
    - System Testing
        - How entire system is tested
        - Code has access to all system resources it needs
    - Deployment
        - Environment cloning
        - Infrastructure as code
    - User-Acceptance Testing

# Docker 

Deploying Docker image in local developer environment

```sh
docker build -t dockerfile:version  => #building a container from Dockerfile

docker images  => #show all docker images

docker run -d -p 8501:8501 dockerfile  => #running container with params -d (detached) and -p (port forwarding (HOST_PORT:CONTAINER_PORT))

docker ps -a  => #show informations about all containers

docker stop <CONTAINER_ID>  => #stop container

docker start <CONTAINER_ID>  => #start container

docker pull <DOCKER_ID>  => #getting the image using Docker ID
```

For deploy example in ***"Interpret contents of a Dockerfile/"*** we can use:
```sh
docker build -t dockerfile:version
docker run -d -p 8501:8501 dockerfile
```

# Application Security

## Application security issues related to secret protection, encryption (storage and transport), and data handling

### Data in transit:
    - Use HTTPS, SFTP, SSH in place of HTTP, FTP, telnet;
    - Securing data in transportation from source to destination;
    - No clear text transmission;


### Data in Rest:
    - Files are encrypted;
    - Database is encrypted;
    - RAM purge correctly;
    - Apps are auth correctly;
    - using environment variables or .env Files;
    - Disk encryption:
        - Windows - bitlocker;
        - MacOS - File Vault;
        - Linux - Tomb;
        - SQL server:
            - Master Key;
            - Slave Key;

## Firewall, DNS, Load Balancers and Reverse Proxy importance

### Firewall

- Enforce a set of rules about which data packets are allowed to enter or leave a network 

### DNS

- Contains a database of public IP addresses and their associated hostnames and often resolves or translates those names to IP addresses, as requested

### Load Balancers

- Distributes network and application traffic across different servers

### Reverse Proxy

- Retrieves resources on behalf of a client from one or more servers, then returns resources to the client, this appearing as if originated from the service itself 

## Top OSWAP Threats 

- XSS (Cross Site Scripiting):
    - Browser side script;
    - Script can acess cookies, session tokens;

- SQL Injections:
    - Manipulation of SQL Commands; 

- CSRF (Cross Site Request Forgery):
    - Request from remote user;

