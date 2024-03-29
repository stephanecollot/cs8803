# cs8803 Visual Data Analysis

Sensemaking using entities in a graph

Video demo: https://www.youtube.com/watch?v=adv3CvW96ws&feature=youtu.be

![screenshot](https://cloud.githubusercontent.com/assets/1184396/22908220/8a339124-f24d-11e6-9357-85b3c3c9b86c.png)

## Dev environment
Please put all the .txt files in ``stego_dataset/`` (they are ignored by git, irrelevant to commit)


Coding rules:
- Tabulation: use 2 spaces, not tab! __Set your IDE__.
- Variable name: variableName
- `KeyLocator` class should be named ``key_locator.py``

## Install
```
pip install django
pip install djangorestframework
pip install -U textblob
```

For NumPy:

Download it from http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

Copy the downloaded ```numpy-1.9.2+mkl-cp27-none-win_amd64.whl``` into your Python directory (C:\Python27\Scripts)

In cmd navigate to the above directory and run the command below: 
```
pip2.7.exe install "numpy-1.9.2+mkl-cp27-none-win_amd64.whl"
```


For SciPy, same method:

Download it from http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy

Copy the downloaded ```scipy-0.15.1-cp27-none-win_amd64.whl``` into your Python directory (C:\Python27\Scripts)

In cmd navigate to the above directory and run the command below: 
```
pip2.7.exe install "scipy-0.15.1-cp27-none-win_amd64.whl"
```

## Launch

Launch command in /django directory:
```
python manage.py runserver
```
Then you can access it here: http://127.0.0.1:8000/

The static directory is http://127.0.0.1:8000/s/test.txt
please put in the directory every images, js, etc
