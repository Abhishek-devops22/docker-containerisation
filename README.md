# Sample FastAPI app in Docker

## Project layout

```
.
├── app/
│   ├── __init__.py
│   └── main.py          # FastAPI app (/ and /health)
├── requirements.txt
├── Dockerfile           # multi-stage build, non-root user, healthcheck
├── .dockerignore
└── docker-compose.yml
```

## Option 1: plain Docker

```bash
# Build the image
docker build -t sample-api:latest .

# Run the container (detached, port 8000 on host -> 8000 in container)
docker run -d --name sample-api -p 8000:8000 -e APP_ENV=production sample-api:latest

# Check it
curl http://localhost:8000/
curl http://localhost:8000/health
docker ps                    # STATUS shows (healthy) once the healthcheck passes
docker logs -f sample-api

# Stop and remove
docker stop sample-api && docker rm sample-api
```

## Option 2: Docker Compose

```bash
docker compose up -d --build   # build and start
docker compose logs -f         # follow logs
docker compose down            # stop and remove
```

Interactive API docs are at http://localhost:8000/docs.

## Notes

- **Multi-stage build**: dependencies are installed in a `builder` stage, and only the virtualenv is copied into the final image, keeping it small.
- **Non-root**: the container runs as the `app` user.
- **Layer caching**: `requirements.txt` is copied before the source code, so code changes don't reinstall dependencies.
- **Port**: change the internal port with `-e PORT=9000 -p 9000:9000`.
- **Adapting to your app**: replace `app/` and `requirements.txt`, then update the `CMD` in the Dockerfile if your entrypoint differs (e.g. `gunicorn` for Flask).
