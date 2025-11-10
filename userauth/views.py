
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.csrf import csrf_exempt
import traceback
# from .serializers import *
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout, authenticate
from django.utils.crypto import get_random_string
from datetime import datetime
from datetime import date
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import status
from django.db.models import Q



# Create your views here.
def UserLogin(request):
    pass