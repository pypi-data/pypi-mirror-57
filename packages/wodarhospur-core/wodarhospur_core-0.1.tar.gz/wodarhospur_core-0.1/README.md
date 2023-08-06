Wodar Hospur
============
> **the lore keeper**

```
/
├── app                # The flask web api
├── docker             # The Docker+Compose for deploy
├── filewatch.py       # The file watch util
├── flasky.py          # 
├── pyclient           # The Python webclient
├── requirements.txt   # 
├── tests              # The pytests
└── watcher            # 

```


### Run the webapi

```
source venv/bin/activate
export FLASK_DEBUG=1
export FLASK_APP=flasky.py
flask run
```


### Run the tests

```
source venv/bin/activate
pip install pytest pytest-watch
ptw -vn -- --disable-warnings
```

### Build the service inside docker

```
docker-compose -f docker/docker-compose.yaml up --build
```

### Run the local filewatch

```
python filewatch.py
```


