from django.shortcuts import render
from rest_framework import viewsets
from .. import models
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
class OperacionViewset(viewsets.ModelViewSet):
    queryset = models.Getoperacion.objects.all()
    serializer_class = serializers.OpeSerializer
    
    
@api_view(['GET', 'POST'])
def test(request, n1 ,n2, operacion):
  
    try: 
        num1 = float(n1)
        num2 = float(n2)      
 
        if request.method == 'GET': 
 
            if  operacion =="+": 
                 dato = num1 + num2
        
            elif operacion =="-": 
                dato = num1 - num2 
             
            elif operacion =="*":
                dato = num1 * num2 
           
            elif operacion =="/":
               
                if num2 == 0:
                    dato= 'ERROR' 
                else:   
                 dato = num1 / num2
                
            elif operacion =="%":
                dato = num1*num2/100
                 
            else:
                dato= 'ERROR'
        else: 
           dato = "ERROR/"
        
    except ValueError:
        dato ='ERROR'  
         
    return Response(dato)    


    