# Dockerized gRPC-Backed Image Search Engine

This project is a multi-threaded server and client for a simple image search engine built with gRPC and Docker. The server randomly selects and serves images based on user-defined keywords. This README provides an overview of the project, how to run it, and other important details.

## Table of Contents
- [Project Description](#project-description)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Configuration](#configuration)
- [Testing](#testing)
- [License](#license)

## Project Description

The purpose of this project assignment is to become familiar with Docker containers and gRPC, gaining a strong understanding of these essential technologies in modern software development. The project consists of the following components:

- Multi-threaded server for the image search engine.
- gRPC communication between the server and client.
- Containerization using Docker.

## Project Structure

The project has the following directory structure:


- The `client` directory contains the client code, Dockerfile, and requirements.
- The `server` directory contains the server code, Dockerfile, and the image database. The `proto` subdirectory contains the `.proto` file for defining gRPC services.

## Requirements

To run this project, you need:

- Docker
- Python (for running client and server outside of Docker)

## How to Run

1. Clone the project:


2. Build and run the Docker containers for the server and client:


3. To run the client and server outside of Docker, navigate to the respective directories and follow the instructions in the README files within each directory.

## Configuration

You can configure the server and client behavior by adjusting environment variables, server parameters, or modifying the `.proto` file for gRPC service definitions.

## Testing

To test the server and client, follow the testing instructions provided in the project's documentation.

## License

This project is licensed under the XYZ License - see the [LICENSE](LICENSE) file for details.
