# Vars for build
USERNAME ?= fiifikrampah
PROJECT_NAME ?= fdi
DOCKER_IMAGE ?= $(USERNAME)/$(PROJECT_NAME)
ENVIRONMENT ?= prod
GIT_TAG ?= $(strip $(shell git rev-parse --abbrev-ref HEAD | sed -e "s/\//_/g"))
GIT_COMMIT = $(strip $(shell git rev-parse --short HEAD))
DOCKER_TAG ?= $(GIT_TAG)-$(GIT_COMMIT)

# Supported Macros
default: deploy
build: terraform_init terraform_plan
docker: docker_build docker_push
deploy: build terraform_apply kube_deploy
monitoring: metrics
heroku: heroku_build
jenkins: jenkins_build

# Optional Heroku container stack deployment
heroku_build:
	heroku login
	heroku create $(PROJECT_NAME)_$(DOCKER_TAG)
	heroku stack:set container
	git push heroku main

image:
	@echo Docker Image: $(DOCKER_IMAGE):$(DOCKER_TAG)

docker_build:
	# Build Docker image
	docker build  -f Dockerfile -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

docker_push:
	# Push to DockerHub
	docker push $(DOCKER_IMAGE):$(DOCKER_TAG)

jenkins_build:
	# Initialize packer for building AMI
	packer init jenkins/packer

	# Build the AMI
	packer build jenkins/packer

	# Initialize terraform providers
	terraform -chdir=jenkins/terraform init

	# Run Terraform plan for Jenkins build
	terraform -chdir=jenkins/terraform plan

	# Build the Jenkins infrastructure
	terraform -chdir=jenkins/terraform apply -auto-approve

terraform_init:
	# Initialize terraform providers
	terraform -chdir=terraform init

terraform_plan:
	# Run Terraform plan for FDI build
	terraform -chdir=terraform plan -var aws_access_key=$(AWS_ACCESS_KEY_ID) -var aws_secret_key=$(AWS_SECRET_ACCESS_KEY)

terraform_apply:
	# Build the FDI infrastructure
	terraform -chdir=terraform apply -var aws_access_key=$(AWS_ACCESS_KEY_ID) -var aws_secret_key=$(AWS_SECRET_ACCESS_KEY) -auto-approve

kube_deploy:
	# Configure kubectl
	aws eks --region $(shell terraform -chdir=terraform output -raw region) update-kubeconfig --name $(shell terraform  -chdir=terraform output -raw cluster_name)

	# Install the application
	helm install fdi kubernetes

metrics:
	# Create a k8s namespace for prometheus
	kubectl create namespace prometheus

	# Add k8s stable repo for prometheus
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

	# Install prometheus and override some default settings
	helm install prometheus prometheus-community/prometheus \
	--namespace prometheus \
	--set alertmanager.persistentVolume.storageClass="gp2" \
	--set server.persistentVolume.storageClass="gp2"

	# Forward ports to access prometheus
	kubectl port-forward -n prometheus deploy/prometheus-server 8080:9090

	# Echo prometheus url
	@echo 127.0.0.1:8080

	# Add the Grafana helm repo
	helm repo add grafana https://grafana.github.io/helm-charts

	# Install Grafana
	kubectl create namespace grafana

	helm install grafana grafana/grafana \
	--namespace grafana \
	--set persistence.storageClassName="gp2" \
	--set persistence.enabled=true \
	--set adminPassword='VerySecurePass' \
	--values monitoring/grafana/grafana.yaml \
	--set service.type=LoadBalancer

	export ELB=$(kubectl get svc -n grafana grafana -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
	@echo "http://$(ELB)"

	# Display Grafana password hash
	kubectl get secret --namespace grafana grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

clean:
	# Destroy infrastructure
	terraform -chdir=terraform destroy -var aws_access_key=${AWS_ACCESS_KEY_ID} -var aws_secret_key=${AWS_SECRET_ACCESS_KEY} -auto-approve
	terraform -chdir=jenkins/terraform destroy -auto-approve

	# Uncomment to optionally remove Terraform state files as part of clean up process
	# rm -f terraform/terraform.tfstate*
	# rm -f jenkins/terraform/terraform.tfstate*

	# Uninstall the helm charts:
	- helm uninstall fdi
	- helm uninstall prometheus --namespace prometheus
	- kubectl delete ns prometheus
	- helm uninstall grafana --namespace grafana
	- kubectl delete ns grafana
