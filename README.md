#### Setup

```
pip3 install -r requirements.txt
```

This installs the Flask API's dependencies. You now have to _configure the database_ in order for the SQL tables to be set up correctly. To do this, run the following commands:

```
export $(cat .env | xargs)

python3 -m pedalhire.models.manage db migrate
python3 -m pedalhire.models.manage db upgrade
```

## Deployment Process

Deployment settings are in `app.yaml`. 

Ref: https://cloud.google.com/appengine/docs/standard/python3/config/appref

```
gcloud app deploy
```

Deployment URL: https://cse546-group17.uc.r.appspot.com/

## Creating a task

```
python pedalhire/queues/create_task.py
```

## Migration

```
CREATE TYPE role AS ENUM ('USER', 'MERCHANT')
```

## API Docs
