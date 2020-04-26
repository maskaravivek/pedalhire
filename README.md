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

Calculate Disctance function

```
CREATE OR REPLACE FUNCTION calculate_distance(lat1 float, lon1 float, lat2 float, lon2 float, units varchar)
RETURNS float AS $dist$
    DECLARE
        dist float = 0;
        radlat1 float;
        radlat2 float;
        theta float;
        radtheta float;
    BEGIN
        IF lat1 = lat2 OR lon1 = lon2
            THEN RETURN dist;
        ELSE
            radlat1 = pi() * lat1 / 180;
            radlat2 = pi() * lat2 / 180;
            theta = lon1 - lon2;
            radtheta = pi() * theta / 180;
            dist = sin(radlat1) * sin(radlat2) + cos(radlat1) * cos(radlat2) * cos(radtheta);

            IF dist > 1 THEN dist = 1; END IF;

            dist = acos(dist);
            dist = dist * 180 / pi();
            dist = dist * 60 * 1.1515;

            IF units = 'K' THEN dist = dist * 1.609344; END IF;
            IF units = 'N' THEN dist = dist * 0.8684; END IF;

            RETURN dist;
        END IF;
    END;
$dist$ LANGUAGE plpgsql;
```

## API Docs

https://documenter.getpostman.com/view/164345/Szf9XTbi?version=latest

