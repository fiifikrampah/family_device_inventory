# Family Device Inventory App [![CircleCI](https://circleci.com/gh/fiifikrampah/family_device_inventory/tree/main.svg?style=svg)](https://circleci.com/gh/fiifikrampah/family_device_inventory/tree/main)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

<br />
    <a href="https://family-device-inventory.herokuapp.com"><strong>View Demo</strong></a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
        <ul>
            <li><a href="#deploy-as-heroku-container-stack">Deploy as Heroku Container Stack</a></li>
            <li><a href="#deploy-as-heroku-app">Deploy as Heroku App</a></li>
        </ul>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple containerized Flask application that allows members of a family to easily manage and keep track of devices they own. Each family member will be able to input information about devices they own, as well as quickly retrieve information about devices owned by other family members. This app is written in Python with Postgres as the chosen data persistence. The app can be deployed locally as a Docker image or deployed to Heroku as a container/app. Moreover, the project can be easily tweaked to support deployment to other cloud-based services such as AWS, Azure or Google Cloud.

Why did I decide to build this?

* Needed a _one-stop-shop_ for keeping track of all the (many) devices my family owns. This way, I'll be able to easily find all important information about our devices whenever I need to.
* Wanted to practice some DevOps concepts such as app containerization, TDD etc. :smile:
* Desired to enforce good SW development habits while working on personal projects.

Of course, this project may be utilized as an example for building other greater and better apps, so any contributions to help improve this template are more than welcome. One may suggest changes by forking this repo and creating a pull request or opening an issue. Thanks in advance to all the people who will contribute to expanding this template!

A list of resources I found helpful are listed in the acknowledgements.

### Built With

Here is a list of major frameworks I employed while building this project:

* [Docker](https://www.docker.com)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Postgresql](https://www.postgresql.org)
* [Heroku](https://www.heroku.com)

<!-- GETTING STARTED -->
## Getting Started

To get started with this project, simply follow the steps below. It is assumed one has access to a shell to execute the necessary commands.

### Prerequisites

Below are the software needed to successfully run the project after cloning:

* [Docker](https://docs.docker.com/get-started/)
* [Heroku (Optional)](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

### Installation

Here are 4 simple steps to get started with running a local instance of the app. For the Heroku-deployed version, see the Usage section.

1. Clone the repo

   ```sh
   git clone https://github.com/fiifikrampah/family_device_inventory
   ```

2. Export the environmental variables from the .env file

   ```sh
    source .env
   ```

3. Bring up and build the docker-compose instance

   ```sh
   docker-compose up --build -d
   ```

4. Navigate to `localhost:5050` to view the running app locally

<!-- USAGE EXAMPLES -->
## Usage

Deploying a Docker container locally is very good, but deploying it on a cloud platform is even better! One can easily deploy the Family Database Inventory App as either a Heroku container stack or as a regular Heroku app.
> **_Note:_**  The Heroku CLI must be installed before executing the steps below.

### Deploy as Heroku Container Stack

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

* [README Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)
* [TDD with Python, Flask and Docker](https://testdriven.io/courses/tdd-flask/)
* [Flask Boilerplate](https://github.com/hack4impact-uiuc)
* [Heroku Devcenter](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)
