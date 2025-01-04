# Benchmark Apps 部署至 Minikube

## 專案結構

benchmark-app/ ├── Dockerfile 
               ├── app.py 
               ├── benchmark-apps.yaml 
               ├── service-monitor.yaml 
               └── README.md

## 步驟 1: 準備 Benchmark 測試程式

### 1.1 編寫測試程式
`app.py` 已包含在專案中。

### 1.2 編寫 Dockerfile
`Dockerfile` 已包含在專案中。

### 1.3 構建並推送 Docker 映像
如果您使用 Docker Hub：

```bash
# 構建 Docker 映像
docker build -t <your-dockerhub-username>/benchmark-app:latest .

# 推送到 Docker Hub
docker push <your-dockerhub-username>/benchmark-app:latest
```

如果您使用 Minikube 的內部 Docker daemon：

```bash
eval $(minikube docker-env)
docker build -t benchmark-app:latest .
```
