# Hello World — FastMCP example

A minimal example showing a FastMCP server and a small async Python client.
This repository contains a tiny server that exposes a `say_hello` tool and a client
that calls it. The project is designed to be run with Docker Compose.

## What’s included

- `server/` — server code and server `Dockerfile`.
- `client/` — client code and client `Dockerfile`.
- `requirements.txt` — Python dependencies used by both images.
- `docker-compose.yml` — Compose file that builds and runs both services.

## Prerequisites

- Docker
- Docker Compose (v2+ recommended)

## Quick start

From the project root (`mcp/01-hello-world`) run:

```bash
# validate compose file
docker compose config

# build and run (server + client)
docker compose up --build

# or run a quick one-shot run that exits when the client finishes:
docker compose up --build --abort-on-container-exit
```

The server listens on port 8000 and exposes the MCP endpoint at `/mcp`.
The client calls the `say_hello` tool once and prints the result.

## Sample response

When the client calls the `say_hello` tool, the server returns a JSON-like
response. For this example the client will receive something like:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Hello, Jhon Doe !"
    }
  ],
  "structuredContent": {
    "result": "Hello, Jhon Doe !"
  },
  "isError": false
}
```


## Running pieces individually

- Start only the server:

```bash
docker compose up --build hello-mcp-server
```

- Run client once (container will run the client script and exit):

```bash
docker compose run --rm hello-mcp-client
```

## Notes & design choices

- The Compose file builds two small images. Both Dockerfiles install the
  dependencies from the project `requirements.txt` to take advantage of layer
  caching.

- A simple TCP-based healthcheck is included for the server. The client uses
  `depends_on` so it starts after the server container is started.

## Troubleshooting

- If the client fails to connect, check that the server container is running and
  listening on port 8000. Inspect logs with:

```bash
docker compose logs hello-mcp-server
```

- If you change dependencies, rebuild images with:

```bash
docker compose build --no-cache
```

