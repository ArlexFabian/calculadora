from .django3.views import  OperacionViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('operacion',OperacionViewset)
# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive