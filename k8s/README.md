Kubernetes Multi-Tier Deployment Guide
1. Local Deployment Instructions (minikube/kind)
To deploy this infrastructure to a local environment, follow these steps:

a. Start the Cluster: Ensure you have a local cluster running.

minikube start OR kind create cluster.

b. Apply Manifests: Use the following command to deploy the frontend, backend, and cache tiers :

kubectl apply -f ./deployment.yaml

kubectl apply -f ./hpa.yaml

c. Verify Status: Check that all pods are running and services are active:

kubectl get pods

kubectl get svc

d. Access the App: If using Minikube, open the frontend service in your browser:

minikube service frontend-service

2. Explanation of Scaling and Self-Healing 

Scaling Capabilities

The infrastructure utilizes Horizontal Pod Autoscaling (HPA) to handle traffic fluctuations:
Automatic Scaling: The backend-hpa monitors CPU and Memory utilization.
Thresholds: If average CPU utilization exceeds 70%, the HPA triggers the deployment of additional replicas (up to 10) to maintain performance.
Elasticity: Once traffic subsides, the HPA will scale down to the minimum requirement (2 replicas) to optimize resource usage.

Self-Healing Capabilities
The deployment is designed to be resilient and self-correcting through the following mechanisms:
Liveness Probes: Kubernetes continuously checks the /health endpoint. If the Backend API becomes unresponsive, the container is automatically restarted.
Readiness Probes: The /ready endpoint ensures that a Pod does not receive traffic until it has successfully completed initialization or cache connections.
Replication Controller: By setting replicas: 2, Kubernetes ensures that if a Node fails, the Pods are rescheduled on healthy nodes to maintain the desired state at all times.