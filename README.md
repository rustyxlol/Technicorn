
<p align="center">
  <h3 align="center">Tech Unicorn</h3>

  <p align="center">
    A DevOps assignment
    <br />
  </p>
</p>

# Task

The assignment is divided into five major tasks with each task containing sub-tasks worth bonus points, all tasks are optional.

### Tasks ⭐

1. Create a simple HTTP API
2. Dockerize the application
3. Create a helm chart
4. Deploy to Kubernetes
5. Documentation

## Setup 🛠
1. Clone or download the repository  
```bash
git clone https://github.com/rustyxlol/Technicorn.git
cd Technicorn
```
2. Build using the provided Dockerfile
```bash
docker build --tag technicorn-docked .
```
3. Run the image on port 8000
```bash
docker run -p 8000:8000 technicorn-docked
```
4. Navigate to http://127.0.0.1:8000/ to check if the API works

## Assignments

### Task 1 - Simple RESTful API

A very simple API to demonstrate SQL connections and CRUD operations.

The API provides the following functionalities:

1. Get all users from the database
2. Get user with specific ID from the database
3. Insert user into the database
4. Delete user from the database
5. Update user in the database

### Task 2 - Docker

1. Build the image using `docker build --tag technicorn-docked .`
2. Run the image using `docker run -p 8000:8000 technicorn-docked`

NOTE: For simplicity, the image has been made for **DEVELOPMENT MODE**. If one wants to aim to deploy this into production environment, **GUNICORN** is required.


### Task 3 - Helm Charts

Before Helm, we need to orchestrate.

After task 4

1. Create helm app using `helm create helm-charts`
2. Copy flask template, modify values
3. Run `helm install web helm-charts`
4. Check if it is running using `helm list`

### Task 4 - Kubernetes

Using `minikube`

1. Start minikube using `minikube start`
2. Run `docker-compose build` and `docker-compose up -d`
3. Apply K8s manifests using `kubectl apply -f deployment.yml` and `kubectl apply -f service.yml`
4. Check if it's working by going to the ip provided by `minikube ip` and the port from `kubectl get po,svc`


### Resources

1. [RealPython: REST APIs](https://realpython.com/api-integration-in-python/)
2. [Dockerizing Flask Applications](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/)
3. [Writing Helm charts](https://augustasberneckas.medium.com/write-helm-charts-for-python-flask-app-ee2777fb458c)
