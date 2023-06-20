# Prodigy Docker for Digital Ocean Deployment

Docker template for running Prodigy on Digital Ocean, using a Digital Ocean hosted PostgreSQL database. This repo follows along with [Prodigy's deployment docs](https://prodi.gy/docs/deployment.md#example-docker-on-digital-ocean-digital-ocean).

We recommend installing [Docker Desktop](https://www.docker.com/products/docker-desktop/), which can help managing images/containers, viewing logs, and easier start/run/close of containers.

# Setup

1. Clone this repo:

```
git clone -b digital-ocean https://github.com/wesslen/prodigy-docker-templates
```

2. Create a `.env` file with your `PRODIGY_KEY` and PostgreSQL DB details. You will need a Prodigy license key, see [docs](https://prodi.gy/docs/install) for details. For PostgreSQL, this example uses a Digital Ocean hosted database; although, you can replace the `.env` with another hosted database instead.

```
# .env
PRODIGY_KEY=1234-5678-ABCD-DEFG
POSTGRES_USER=doadmin
POSTGRES_PWD=***
POSTGRES_HOST=db-postgres-prodigy-do-user-243383-0.b.db.ondigitalocean.com
POSTGRES_PORT=25060
POSTGRES_DB_NAME=defaultdb
```

3. Modify `requirements.txt`, `run.sh`, `prodigy.json`, and `Dockerfile`:

- Add in new packages to `requirements.txt`
- Modify `run.sh` for import data, script (e.g., Prodigy command to run), etc.
- Modify `prodigy.json` for configuration settings
- Modify `Dockerfile` for other environmental variables (user names for session, etc.) 

4. Build:

This is built for Digital Ocean, not to run locally. 

```
docker build --progress=plain -t prodigy-docker-postgres .
```

5. Login, tag and push

See [this for more details](https://docs.digitalocean.com/products/container-registry/quickstart/#manage-images).

```
# if it's your first time, create a registry
doctl registry login
# assumes you have created a registry: ryan-prodigy
# need to use a different name for your registry
docker tag prodigy-docker-postgres registry.digitalocean.com/ryan-prodigy/prodigy-docker-postgres
docker push registry.digitalocean.com/ryan-prodigy/prodigy-docker-postgres
```

6. Create your app

Follow [these instructions](https://prodi.gy/docs/deployment.md#deploying) to create your own app based on your registry in Digital Ocean.

7. Shut down 

Make sure to delete your app, registry (if necessary), and PostgreSQL hosted database. If you don't, you'll continue to incur charges.