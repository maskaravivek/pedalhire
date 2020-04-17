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