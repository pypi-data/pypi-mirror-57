
Small toolbox of python utilities.


# I Requirements

- python >= 3.6



# II Installation

* Uncompress the package archive:
```sh
tar -zxvf fn\_python\_utils.0.0.1dev.tar.gz
```

* Go inside the uncompressed folder, whose name is like "fn\_python\_utils.0.0.1dev", for instance:
```sh
cd fn\_python\_utils.0.0.1dev
```  

* Install the toolbox:
```sh
python3 setup.py install
```
OR
```sh
pip install .
```


**Think about using a virtual environment**

In order to avoid conflicting software versions, we advise you to use `virtualenv` to create an 
installation that is local to the project. 



# III Tests

It is advised to use pytest to launch the tests.
To launch the tests, a possibility is to use this command, from the root of the uncompressed package:
``` 
python3 -m 'pytest' ./tests/ -vv
``` 



# IV Versioning

We use SemVer (http://semver.org/) for versioning.


## V History

* **0.0.2**
    * ADD: Implement new display utilities

* **0.0.1**
    * ADD: Implement singleton utilities
    * ADD: Implement io utilities
    * ADD: Implement memoize utilities
    * ADD: Implement timer utilities
    * ADD: Implement display utilities


# VI Authors

* **François NOYEZ**


# VII License

This project is licensed under the LGPL License - see the LICENSE.txt file for details
