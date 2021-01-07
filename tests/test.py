from pls import pyli
from pls.pyli import slab
import os, sys
auth_id="" #Owner's Authentication Code
slab.auth(auth_id)
slab.user_id() #Print User id
username=''#User Name
password=''#Password
key=''#License key
slab.verify(username, password, key)
