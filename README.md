# Running the Project with Docker

This project utilizes Docker for containerized execution of its components. Follow the instructions below to build and run the project using Docker Compose.

## Requirements

- Docker version 20.10 or higher
- Docker Compose version 1.29 or higher

## Setup Instructions

1. **Build the Docker Images**

   Run the following command to build the Docker images for the services:

   ```bash
   docker-compose build
   ```

2. **Run the Services**

   Start the services using Docker Compose:

   ```bash
   docker-compose up
   ```

   This will start the following services:

   - `cli`: Executes the CLI application located in the `./cli` directory.
   - `pair_programing_demo`: Runs the pair programming demo application from the `./pair programing demo` directory.

## Configuration

- The `cli` service uses the entrypoint `python cli/main.py`.
- The `pair_programing_demo` service executes `python source.py`.
- Uncomment the `env_file` lines in the `docker-compose.yml` file if environment variables are required.

## Notes

- No ports are exposed by default in the provided configuration.
- Ensure all dependencies are defined in the `pyproject.toml` file for proper installation during the build process.

For further details, refer to the respective `Dockerfile` and `docker-compose.yml` files.