# Prodigy Docker Templates

Docker templates for running Prodigy locally. This repo can be extended to run Prodigy on a cloud. For more details, read [Prodigy's deployment docs](https://prodi.gy/docs/deployment).

We recommend installing [Docker Desktop](https://www.docker.com/products/docker-desktop/), which can help managing images/containers, viewing logs, and easier start/run/close of containers.

# Local setup

1. Clone this repo:

```
git clone https://github.com/wesslen/prodigy-docker-templates
```

2. Create a `.env` file with your `PRODIGY_KEY`. You will need a Prodigy license key, see [docs](https://prodi.gy/docs/install) for details.

3. Modify `requirements.txt`, `run.sh`, `prodigy.json`, and `Dockerfile`:

- Add in new packages to `requirements.txt`
- Modify `run.sh` for import data, script (e.g., Prodigy command to run), etc.
- Modify `prodigy.json` for configuration settings
- Modify `Dockerfile` for other environmental variables (user names for session, etc.) 

4. Build:

Depending on your OS, run:

**Windows**

```
docker build --platform=windows/amd64 -t prodigy-docker . 
```

**M1 Mac**

```
docker build --platform=linux/arm64 -t prodigy-docker . 
```

**Intel Mac**

```
docker build --platform=darwin/amd64 -t prodigy-docker . 
```

**Linux**

```
docker build --platform=linux/amd64 -t prodigy-docker . 
```

5. Run

```
docker run -p 8080:8080 prodigy-docker
```

6. Open Prodigy and annotate:

* Go to browser: `0.0.0.0:8080`
* If basic authentication is enabled (which is default for the `Dockerfile`), provide the `user` and `pass`. By default, this is specified in the `Dockerfile`; however, you likely may want to specify these environment variables in an alternative setup.
* If `PRODIGY_ALLOWED_SESSIONS` is set (which is by default), you'll need to extend the url to `?session=[an allowed username]` for example `0.0.0.0:8080?session=user1`. If you do not, you'll see a `ERROR: Can't fetch project. Make sure the server is running correctly.` in Prodigy.

7. Shut down your container

Open a new terminal and view any running containers:

```
$ docker ps
CONTAINER ID   IMAGE            COMMAND         CREATED         STATUS         PORTS                    NAMES
9a153cbfbd12   prodigy-docker   "bash run.sh"   8 seconds ago   Up 8 seconds   0.0.0.0:8080->8080/tcp   infallible_ishizaka
```

Run `docker stop` with the `CONTAINER ID`:

```
$ docker stop 9a153cbfbd12  
9a153cbfbd12
```

Alternatively, you can use Docker Desktop too. 

# Troubleshooting

> `[Errno 99] error while attempting to bind on address ('::1', 8080, 0, 0): cannot assign requested address`

There's two possibilities. First, make sure that your host is `0.0.0.0`. This is included in the default `prodigy.json`. See [this docs post](https://prodi.gy/docs/install#install-docker) or [this blog](https://pythonspeed.com/articles/docker-connection-refused/) for more details.

A second possibility is that there is another process running on port `8080`. For this, you'll need to modify your ports such that (for example, let's change to `8081`):

- Add `ENV PRODIGY_PORT 8081` in `Dockerfile`
- Modify `EXPOSE 8080` to `EXPOSE 8081` (Make sure to rebuild your image!)
- When running, use the command: `docker run -p 8080:8080 prodigy-docker`
- Now go to `0.0.0.0:8081` in a browser
