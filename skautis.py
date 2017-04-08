#!env/bin/python
from skautis import SkautisApi
import uuid

x = SkautisApi("xxxx")
print x.vivant.ExportFileAll()
