# wiserly_app

#docker build -t wiserly-inventory-planner:init .

#docker run --rm  --env-file .env --publish 8000:8000 wiserly-inventory-planner:init -e FLASK_APP=prod  --bind 0.0.0.0 manage:app

helm upgrade --install --create-namespace --namespace wiserly-inventory-planner wiserly-inventory-planner helm-charts/
helm list --namespace wiserly-inventory-planner
kubectl get pods,jobs,service -n wiserly-inventory-planner
