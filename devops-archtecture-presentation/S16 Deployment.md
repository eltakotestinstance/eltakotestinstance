---
marp: true
color: 'white'
paginate: true
backgroundImage: url('auticon.png')
---

# S16 DevOps and architecture

Modes of deployment for the Raspberry Pi 4b.

---

# Test deployment platform

- Raspberry 4b with 4gb Ram 32gb micro-sd card.
- Yocto Linux with poky distribution Nanbield branch.
- With several necessary development tools like a ssh server, editor, systat e.g.
- Every deployment method has their own image with the services needed installed


---

# Test deployment

1. EltatoSoftwareDelpoymentMonitor(esdm)
   - Small rest api written in C# using dotnet 8.0
   - Uses Serilog and Opentelemetry
   - Uses Metalama for aspect-oriented programming
   - Build in Kestrel http server
   - Uses https with self-generated certificate
   - Swagger for api testing

2. PostgreSQL relational database



---

# Tested Deployment methods

- Everything natively deployed.
- Main application natively deployed, database and otel-collector containerized.
- Everything deployed wia docker using docker compose or docker stack.
- Using Suses Kubernetes implementation K3S.
- Aspire Orchestration with docker compose deployment

---

# Pro/cons of native deployment

## **Pros**

- Resources consumption is minimal.
- Can be updated with Nuget/Linux packages.

## **Cons**

- Has no defined state.
- Updates can break/fail.
- Updating the database could be prone to errors.
- Can only be tested on the deployment platform.

---

# Native deployment CPU usage

![image](native-cpu.png)

---

# Docker compared to other virtualization methods

![image](docker-architecture.png)

---

# Sample Dockerfile

![image](sample-dockerfile.png)

---

# Sample docker compose file

![image](sample-dockercomposefile.png)

---

# Details of hybrid deployment

- Dotnet 8.0.1 package form a third-party Layer.
- Docker from the official Yocto meta-virtualization  layer.
- Docker compose file with postgres and otel-collector container
- Systemd needed for docker.



---

# Pro/cons of hybrid deployment

## **Pros**

- Software stack can be updated with Nuget/Linux packages.
- Setup of postgres database is much easier than in native

## **Cons**

- Has no defined state.
- Updates can break/fail.
- Can only be tested on the deployment platform.

---
# Hybrid deployment CPU usage

![image](hybrid-cpu.png)

---

# Details of docker deployment

- Docker from the official Yocto meta-virtualization  layer.
- Systemd for dependent docker services.
- One Deployment with docker Stack.
- One Deployment with docker compose.
- Both variants have the same resource profile.

---

# Pro/cons of docker deployment

## **Pros**

- Has a defined state.
- Full testing is relatively easy(can be done on Development Computers).
- Deployment Process is easily be automated.

## **Cons**

- Memory consumption, on 1 GB ram is already at limit capacity.
- The process of storing secrets is not very though out.
- Not as many fail saves as Kubernetes

---

# Docker deployment CPU usage

![image](native-cpu.png)

---

## Docker with/without empty container memory comparision

![image](docker-empty-container.png)

---

# Excursion Yocto package


Yocto package               | Systemd startupfile
:--------------------------:|:-------------------------:
![image](yocto-package.png) | ![image](systemd-startup.png)

---

# How kubernetes works

![image](k8-architecture.png)

---

# How k3s works

![image](k3s-architecture.jpg)

---
# Sample k8s config files

Sample pod config | Sample secret config | Sample service config
:----------------:|:-------------------:|:-------------------------:
![image](k8s-pod-config.png) | ![image](k8s-secret-config.png)  | ![image](k8s-service-config.png) 



---

# Details of the Kubernetes deployment

- K3s from the official meta-virtualization layer.
- Docker from the official meta-virtualization layer.
- Systemd needed for k3s.
- Some SE-Linux components needed from the official meta-security layer.
- Special startup parameters for Raspberry Pi 4b.

---

# Pro/cons of kubernetes deployment

## **Pros**

- Has a defined state.
- Deployment Process can easily be automated.
- The whole deployment process is very well-thought-out.
- Has many fail-safe mechanisms.
- You could duplicate your application during an update.

## **Cons**

- Committed memory is already over limit capacity on 4gb Ram.
- Many functions of the software is not needed.
- Additional dependency on k3s developer (Suse Inc).

---

# Kubernetes deployment CPU usage

![image](k3s-cpu.png)

---

## K3s with/without empty container Memory comparision

![image](k3s-empty-memory.png)

---

#  What is .net aspire

- “.NET aspire is an opinionated, cloud ready stack for building observable, production ready, distributed applications”
- It helps you with the start of development, because its very easy to develop a working prototype without much effort.
- It comes with a aspire dashboard which is a very easy and good way to visualize logs, traces and metrics.
- If you use azure cloud services, the deployment form your aspire app is streamlined.

---

# Sample orchestration file

![image](aspire-orchestration.png)

---

# .net aspire pitfalls

![image](aspire-pitfalls-database1.png)

![image](aspire-pitfalls-database2.png)

![image](aspire-pitfalls-httpclient.png)

---

# aspire CPU usage usr/sys

![image](apire-cpu.png)

---

# Comparison of CPU usage for user

![image](all-cpu-usr.png)

---

# Comparison of CPU usage for system

![image](all-cpu-sys.png)

---

# Comparison of memory used

![image](all-memory-used.png)

---

# Comparison of memory committed

![image](all-memory-committed.png)

---

# My recommendations

- Depends on the device's resources.
- Best developer experience is in my opinion k3s.
- If only 1 GB of ram is available native deployment would be my choice.
- If 2-4 GB of ram is available docker deployment would be my choice.
- If 8 GB of ram is available k3s would be my choice.
