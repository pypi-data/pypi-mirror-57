<p align="right">
<a href="https://badge.fury.io/py/fireo"><img src="https://badge.fury.io/py/fireo.svg" alt="PyPI version"></a>
<a href="https://travis-ci.org/octabytes/FireO"><img src="https://travis-ci.org/octabytes/FireO.svg?branch=master" alt="Build Status"></a>
</p>
<p>
    <h1 align="center"><img src="fireo_logo.png" height="100" alt="FireO Logo"></h1>
    <p align="center">
        A modern and simplest convenient ORM package in Python.
        FireO is specifically designed for the Google's Firestore, it's more than just ORM.
        It implements validation, type checking, relational model logic and much more facilities.
    </p>
    <p align="center">
        <strong>
            <a href="https://octabyte.io/FireO/">Get Started!</a>
        </strong>
    </p>
    <br><br><br>
</p>

## Installation

```python
pip install fireo
```

## Example Usage
```python
from fireo.models import Model
from fireo.fields import TextField

class User(Model):
    name = TextField()


u = User()
u.name = "Azeem Haider"
u.save()

# Get user
user = User.collection.get(u.key)
print(user.name)
```

## Documentation

Full documentation is available in the [FireO Doc](https://octabyte.io/FireO/).

## Contributing

Bug reports and pull requests are welcome. This project is intended to be a safe, welcoming 
space for collaboration, and contributors are expected to adhere to the 
[Contributor Covenant](https://github.com/octabytes/FireO/blob/master/CODE_OF_CONDUCT.md) code of conduct.

1. Check FireO [Project TODO list](https://github.com/octabytes/FireO/projects) or [newcomers contribute](https://github.com/octabytes/FireO/contribute)
2. Checkout [Feature](https://github.com/octabytes/FireO/tree/feature) branch (latest working branch)
3. Write tests for your functionality
4. Mention in [Documentation](https://github.com/octabytes/FireO/tree/gh-pages), what you has done and how other can use it  

## License

This is official [FireO](https://github.com/octabytes/FireO) Repository. Powered by [OctaByte](https://octabyte.io)
Licensed under [Apache License 2.0](https://github.com/octabytes/FireO/blob/master/LICENSE)
