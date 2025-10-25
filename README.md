# Todo App Project

> **Note:** This project uses **Nginx as a reverse proxy / load balancer**.  
> It demonstrates how to use Docker Compose to run multiple services together:  
> a Python application (`web-app`), a PostgreSQL database (`db`), and an Nginx reverse proxy (`nginx`).

This project is designed to give a clear understanding of Docker Compose,  
how to write a Docker Compose file to orchestrate multiple services,  
set environment variables via `.env`, use volumes for persistent data,  
and manage networking between containers.

The project structure:

```
todo_app/
├── app/              # Python application code (database connection and initialization)
│   └── db.py         
├── .env              # Environment variables for the app and database
├── nginx/            # Nginx configuration files
│   └── default.conf  # Reverse proxy / load balancer configuration
├── Dockerfile        # Builds the Docker image for the Python application
├── docker-compose.yml# Orchestrates all services, volumes, and networks
└── README.md         # Project documentation
```

**Details:**

- `app/` contains all Python code for the application, including database connection and table initialization.
- `.env` contains environment variables such as `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `DB_HOST`.
- `nginx/` contains the configuration for Nginx to act as a reverse proxy and load balancer.
- `Dockerfile` builds the Docker image for the Python application.
- `docker-compose.yml` orchestrates all services, defines volumes, networks, and service dependencies.

The application reads environment variables from `.env`,  
and the Nginx container routes traffic to the Python app.  
Docker volumes persist database data across restarts.  
This setup demonstrates proper service communication, environment management,  
and reverse proxy/load balancing with Nginx.

**Running the project:**

```bash
docker compose up --build -d 
```
**Scaling Your App:**

```bash
docker compose up --build -d --scale web-app=3

**Stopping and cleaning up:**

```bash
docker compose down -v
```

Update the `.env` file to modify database credentials or hostnames as needed.

