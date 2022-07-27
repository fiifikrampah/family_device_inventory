# Family Device Inventory App

[![CircleCI](https://circleci.com/gh/fiifikrampah/family_device_inventory/tree/main.svg?style=svg)](https://circleci.com/gh/fiifikrampah/family_device_inventory/tree/main) [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

<br />
    <a href="https://family-device-inventory.herokuapp.com"><strong>View Demo</strong></a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
- [Family Device Inventory App](#family-device-inventory-app)
  - [About The Project](#about-the-project)
    - [Built With](#built-with)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Deploy as Heroku Container Stack](#deploy-as-heroku-container-stack)
    - [Deploy as Heroku App](#deploy-as-heroku-app)
    - [Deploy to EKS Cluster](#deploy-to-eks-cluster)
      - [Access the Application (Simple Method)](#access-the-application-simple-method)
      - [Access the Application via the K8s dashboard](#access-the-application-via-the-k8s-dashboard)
    - [Enable Cluster and Pod Monitoring (Optional)](#enable-cluster-and-pod-monitoring-optional)
      - [Cluster Monitoring Dashboard](#cluster-monitoring-dashboard)
      - [Pods Monitoring Dashboard](#pods-monitoring-dashboard)
    - [Configure Jenkins CI project (Optional)](#configure-jenkins-ci-project-optional)
    - [Cleanup](#cleanup)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
  - [Acknowledgements](#acknowledgements)
<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple containerized Flask application that allows family members to manage and track the devices they own. Each family member will be able to input information about their own devices as well as quickly retrieve information about other family members' devices. This app is written in Python and uses Postgres for data persistence. The app can be deployed locally as a Docker image, to Heroku as a container/app, or to an EKS cluster that can be easily provisioned using Terraform. Furthermore, the project is easily adaptable to support deployment to other cloud-based services like Azure or Google Cloud.

What motivated me to work on this project?

- I needed a _one-stop-shop_ for tracking all of my family's (many) devices. This way, I'll be able to easily find all of our devices' important information whenever I need it.
- I wanted to put some DevOps concepts like app containerization and TDD into practice:smile:
- While working on personal projects, I hoped to instill good SW development habits.

Of course, this project could be used as a model for creating other bigger and better apps, so any contributions to help improve this template are greatly appreciated. Changes can be suggested by forking this repository and submitting a pull request or opening an issue. Thank you in advance to everyone who will help expand this template!

The acknowledgements section includes a list of resources that I found useful.

### Built With

Here is a list of the major frameworks I used while developing this project:

- [Docker](https://www.docker.com)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Postgresql](https://www.postgresql.org)
- [Heroku](https://www.heroku.com)
- [Terraform](https://www.terraform.io/)
- [Jenkins](https://www.jenkins.io/)
- [Packer](https://www.packer.io/)
- [Ansible](https://www.ansible.com/)
- [Kubernetes](https://kubernetes.io/)
- [Helm](https://helm.sh/)

<!-- GETTING STARTED -->
## Getting Started

Simply follow the steps below to get started on this project. It is assumed that you have access to a shell to run the necessary commands.

### Prerequisites

The following are required to successfully run the project after cloning:

- [Docker](https://docs.docker.com/get-started/)
- [Heroku (Optional)](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
- An AWS account
- [AWS CLI](https://aws.amazon.com/cli/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Terraform](https://www.terraform.io/downloads)
- [Packer](https://www.packer.io/downloads)
- [Helm](https://helm.sh/docs/intro/install/)

### Installation

Here are four easy steps to getting started with a local instance of the app. See the Usage section for Heroku-deployed or EKS-deployed versions.

1. Clone the repo

   ```sh
   git clone https://github.com/fiifikrampah/family_device_inventory
   ```

2. Add required secrets to the.env file and export them to the environment

  ```sh
  set -a && source .env && set +a
  ```

3. Bring up and build the docker-compose instance

   ```sh
   docker-compose up --build -d
   ```

4. Navigate to `localhost:5050` to view the running app locally

<!-- USAGE EXAMPLES -->
## Usage

Locally deploying a Docker container is great, but deploying it on a cloud platform is even better! The Family Database Inventory App can be easily deployed as a Heroku container stack or even deployed to an EKS cluster and monitored using Prometheus.

### Deploy as Heroku Container Stack

To make it easier to deploy the app to Heroku, the following steps have been automated using the Makefile.
To execute the steps from the Makefile, run:
`make heroku`

If you prefer to manually execute or tweak each step of the deployment process, please follow the steps below instead:

1. Log in to heroku using the CLI

   ```sh
    heroku login
   ```

2. Create a heroku app

   ```sh
   heroku create <NAME-OF-APP>
   ```

    You can use the git remote command to confirm that a remote named heroku has been set for the app

    ```sh
    git remote -v
    ```

3. Set the stack of the app to container

   ```sh
   heroku stack:set container
   ```

4. Push the app to heroku

    ```sh
    git push heroku main
    ```

The application will be built, and Heroku will use the run command provided in `heroku.yml` instead of the `Procfile`.

### Deploy as Heroku App

1. Log in to heroku using the CLI

   ```sh
    heroku login
   ```

2. Create a heroku app

   ```sh
   heroku create <NAME-OF-APP>
   ```

    You can use the git remote command to confirm that a remote named heroku has been set for the app:

    ```sh
    git remote -v
    ```

3. Push the app to heroku

    ```sh
    git push heroku main
    ```

The application will be built, and Heroku will use the run command provided in the `Procfile`.

### Deploy to EKS Cluster

1. Add required secrets to the.env file and export them to the environment

  ```sh
  set -a && source .env && set +a
  ```

2. Deploy the project to an EKS cluster that Terraform will automatically create

  ```sh
  make deploy
  ```

#### Access the Application (Simple Method)

1. Run `kubectl get svc`

2. Copy the `External IP` link and change the https to http

#### Access the Application via the K8s dashboard

1. Deploy the k8s dashboard
`kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.6.0/aio/deploy/recommended.yaml`

2. Create the `ClusterRoleBinding` resource
`kubectl apply -f https://raw.githubusercontent.com/hashicorp/learn-terraform-provision-eks-cluster/main/kubernetes-dashboard-admin.rbac.yaml`

3. Generate the authorization token
`kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep service-controller-token | awk '{print $1}')`

4. Copy the token

5. Run `kubectl proxy`

6. Navigate to `http://127.0.0.1:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/`

7. Select token and paste the token there

8. Retrieve the Load balancer endpoint. This can be done by clicking the `services` link in the sidebar

9. Click the link under `External Endpoints`

### Enable Cluster and Pod Monitoring (Optional)

1. Run `make monitoring` to configure Prometheus and Grafana

2. Access Prometheus from `127.0.0.1:8080`

3. Copy the Grafana URL that was printed to the terminal

4. When logging in, enter the username 'admin' and obtain the password hash by running the following commands:
`kubectl get secret --namespace grafana grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo`

#### Cluster Monitoring Dashboard

For creating a dashboard to monitor the cluster:

1. Click '+' button on left panel and select ‘Import’.
2. Enter 3119 dashboard id under Grafana.com Dashboard.
3. Click ‘Load’.
4. Select ‘Prometheus’ as the endpoint under prometheus data sources drop down.
5. Click ‘Import’.

#### Pods Monitoring Dashboard

For creating a dashboard to monitor all the pods:

1. Click '+' button on left panel and select ‘Import’.
2. Enter 6417 dashboard id under grafana.com Dashboard.
3. Click ‘Load’.
4. Enter Kubernetes Pods Monitoring as the Dashboard name.
5. Click change to set the Unique identifier (uid).
6. Select ‘Prometheus’ as the endpoint under prometheus data sources drop down.
7. Click ‘Import’.

### Configure Jenkins CI project (Optional)

1. Install git, docker, and docker pipeline plugins
2. Configure a Pipeline project
3. Add AWS Access Key and Secret

### Cleanup

1. Run `make clean` to tear down all AWS infrastructure and uninstall the helm charts.

<!-- ROADMAP -->
## Roadmap

See the [Github Issues](https://github.com/fiifikrampah/family_device_inventory/issues) for a list of proposed features (and known issues).
Also see the [Changelog](docs/Changelog.md) for a list of current changes.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes [(please write good commit messages)](https://chris.beams.io/posts/git-commit/) (`git commit -m '[Github Issue ID] Add some amazing feature to do...'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Fiifi Krampah - [@JustFiifi](https://twitter.com/JustFiifi) - fiifi.krampah@gmail.com

Project Link: [https://github.com/fiifikrampah/family_device_inventory](https://github.com/fiifikrampah/family_device_inventory)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

- [README Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)
- [TDD with Python, Flask and Docker](https://testdriven.io/courses/tdd-flask/)
- [Flask Boilerplate](https://github.com/hack4impact-uiuc)
- [Heroku Devcenter](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)
- [EKS Workshop](https://www.eksworkshop.com/intermediate/240_monitoring/)
- [Terraform Docs](https://learn.hashicorp.com/collections/terraform/aws-get-started)
