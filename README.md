# wiserly_app

#docker build -t wiserly-inventory-planner:init .

#docker run --rm  --env-file .env --publish 8000:8000 wiserly-inventory-planner:init -e FLASK_APP=prod  --bind 0.0.0.0 manage:app

helm upgrade --install --create-namespace --namespace wiserly-inventory-planner wiserly-inventory-planner helm-charts/
helm list --namespace wiserly-inventory-planner
kubectl get pods,jobs,service -n wiserly-inventory-planner
kubectl get secret $(kubectl get sa jenkins-admin -n wiserly-inventory-planner -o jsonpath={.secrets[0].name}) -n wiserly-inventory-planner -o jsonpath={.data.token} | base64 --decode
kubectl config set-context --current --namespace=K21
ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print $2}'