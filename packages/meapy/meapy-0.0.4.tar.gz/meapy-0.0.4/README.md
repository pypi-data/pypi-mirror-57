![PyPI](https://img.shields.io/pypi/v/meapy?style=flat-square)
![PyPI - Status](https://img.shields.io/pypi/status/meapy?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/meapy?style=flat-square)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/meapy?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/meapy?style=flat-square)

# MeaPy
Python API Wrapper for Measurement Data

## Vision
MeaPy wants to be a easy-to-use and conformable API for working with measurement data in den Big Test Data environment.

## Getting Started
```
pip install meapy
```

## Usage
```python
from meapy import MeaPy

mp = MeaPy("http://madam-docker.int.kistler.com:8081/", "1234")

# direct search (limited)
result = mp.search("test")
# result is a list of meapy.measurement.Measurement

# search and iteration over the whole result set
ml = MeasurementList(mp)
count = 0
for mea in ml.items('Station.Id="d4f1ad55-72d5-403c-81b8-73b2942b58f4"'):
    count+=1
print(count)
```
