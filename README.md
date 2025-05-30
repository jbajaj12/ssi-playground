# APM Test App – Datadog Workshop Companion

This is a simple Next.js application that simulates basic API behavior to help you understand how application traces are generated and captured by the Datadog agent and tracer.

---

## 🛠️ Getting Started

### ✅ Prerequisites

Before installing and running the app, make sure you have the following installed on your machine:

- **Homebrew**: [https://brew.sh/](https://brew.sh/)
- **NPM**, installed via Homebrew:
  ```bash
  brew install npm
    ```
- **Visual Studio Code (recommended)**: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)

## 🚀 Installation
Open your terminal and follow the steps below to clone the repo and start the application:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ccdaniele/se-ssi-playground
   cd apm-test/
   ```
2. **Install dependencies**:
   ```bash
   npm install
   ```
3. **Start the application**:
   ```bash
   npm run dev
   ```
4. **Open your browser**: Navigate to [http://localhost:3000](http://localhost:3000) to view the application.


## Deploying app in Kubernetes

1. **Ensure you have a Kubernetes cluster running**: You can use Minikube, Kind, or any other Kubernetes service.
2. Apply the application manifest to deploy the app in your Kubernetes cluster:

```
kubectl apply -f kubernetes/apm-app/app_manifest.yaml
```
3. Let’s wait a couple of minutes and confirm that the application has been successfully deployed by running: 

```
kubectl get pods 
```
​
   The output should be similar to this: 
```
NAME                       READY   STATUS    RESTARTS   AGE
apm-app-xxxxxxxxx   1/1     Running   0          106s
```
​
4. Copy the name of the pod and let’s access to the application by creating a tunnel between kubernetes and our mac: 

```
kubectl port-forward apm-app-xxxxxxxxx 3000:3000
```
​
5. Now open localhost:3000 in your browser and you should see the app. 
