# Project ideas — FastMCP examples

A collection of small ideas and prototypes demonstrating usage patterns for FastMCP.
Each example contains a minimal server and a demo client (typically under `server/` and
`client/`) and is intended to be run with Docker Compose.

## What’s included

- `server/` — example server and `Dockerfile` (when applicable).
- `client/` — example client and `Dockerfile` (when applicable).
- `docker-compose.yml` — orchestration file to run server + client together.
- `README.md` — example-specific instructions.

## Prerequisites

- Docker
- Docker Compose (v2+ recommended)

## Quick start

1. Change to the example folder you want to try:

```bash
cd mcp/03-project-ideas/<example-name>
```

2. Build and start the services:

```bash
docker compose config         # validate the compose file
docker compose up --build     # build and start server + client

# for a one-shot run that exits when the client finishes:
docker compose up --build --abort-on-container-exit
```

3. Check logs if something fails:

```bash
docker compose logs <service-name>
```

Most examples expose the MCP endpoint at `/mcp` and listen on port 8000.

## How to contribute

To add a new idea, create a folder with this minimal layout:

- `<idea>/server/` — server code and `Dockerfile`.
- `<idea>/client/` — client script and `Dockerfile`.
- `<idea>/docker-compose.yml` — to run both services.
- `<idea>/README.md` — short description and usage instructions.

Keep examples small and self-contained so they can be run easily with `docker compose`.

---

Short and direct; see each example's README for details and example-specific notes.
