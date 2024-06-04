## FastAPI CRUD for Products

This is a basic CRUD (Create, Read, Update, Delete) application for managing products using FastAPI. The project is Dockerized for easy deployment.

### Prerequisites

* Python 3.10 or later

### Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/vineetpatel725/fastapi-crud-app.git
```

2. **Install dependencies:**

```bash
pip install requirements.txt
```

3. **Update database configuration in config(.ini)**

```bash
[database]
host = Host
port = Port
name = Database
username = Username
password = Password
```
4. **Run Application without docker:**

```bash
start.sh
```
### Running the application(Using Docker)

This approach is recommended for a production-like environment.

* Build the Docker image:

```bash
docker compose build
```

* Start the application and database:

```bash
docker compose up -d
```

The API will be accessible on port `8000` by default (http://localhost:8000/). It is configurable.

### Code Structure

The core functionalities reside in these files:

* `main.py`: Entry point for the FastAPI application.
* `db.py`: Handles database connectivity.
* `models/`: Defines the models.
* `schemas/`: Defines data schemas for request and response data.
* `routes/`: Defines the routes.
* `config/`: Handles required configurations for application 
