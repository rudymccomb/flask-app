# Build from current directory
$ docker build -t bnet/rudymccomb/helloworld:1.0.0 .

# Run  Container in the background (as a daemon)
docker run -p 5000:5000 -d bnet/rudymccomb/helloworld:1.0.0

In order for Kubernetes to schedule this app properly it needs to know the shape of the piece, this is where resource limits and requests for cpu and memory come in to play.

# See whats currently running in K8's
$ kubectl get pods

# Deploy to K8 from file
$ kubectl create -f deployments/helloworld.yaml

What machine did this land on? 
The K8 scheduler figures this out at runtime

# Check status of app in K8
$ kubectl get pods
NAME                            READY   STATUS   RESTARTS   AGE
helloworld-314234566-sw9fg      1/1     Running  0          19s

# Check the entire K8's Infrastructure
$ kubectl get pods -o wide
NAME                            READY   STATUS   RESTARTS   AGE     IP             NODE
helloworld-314234566-sw9fg      1/1     Running  0          19s     10.185.0.91    gke-pyth-default-pool-sdfaj4jhjf-nf6p

# Delete app workload from K8
$ kubectl delete pods helloworld-314234566-sw9fg 
pod "helloworld-314234566-sw9fg" deleted

# Check the entire K8's Infra
# Notice the workload has been terminated and replaced quickly
$ kubectl get pods -o wide
NAME                            READY   STATUS       RESTARTS   AGE     IP             NODE
helloworld-314234566-68rj0      1/1     Running      0          2s      10.185.4.71    gke-pyth-default-pool-sdfaj4jhjf-lgxc
helloworld-314234566-sw9fg      1/1     Terminating  0          56s     10.185.0.90    gke-pyth-default-pool-sdfaj4jhjf-nf6p

# Lets look further into K8
# Notice the load balancer at 35.188.11.252
$ kubectl get svc
NAME                            CLUSTER-IP      EXTERNAL-IP      PORT(S)         AGE
helloworld                      10.187.240.15   35.188.11.252    80:30708/TCP    8h
helhelloworld                   10.187.249.131  104.154.110.184  80:30081/TCP    8h
kubernetes                      10.187.240.1    <none>           443/TCP         8h

# We cant run production python with flask...one request at a time
# the container way of handling this would be to write an even bigger Dockerfile with uwsgi and nginx but that we dont want to put # all that and pack it in the apps container and launch it all with a script. thus creating an init system
# Lets see how we can better solve this with K8's
# Lets put it in a seperate deployment object
$ deployments/helloworld-uwsgi.yaml

The above deployment has a sep conainer for nginx and our python app

#Lets deploy the app
$ kubectl create -f deployments/helloworld-uwsgi.yaml

# now lets delete the deployment
$ kubectl delete deployment helloworld helloworld-uwsgi