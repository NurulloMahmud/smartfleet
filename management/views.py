from rest_framework.views import APIView
from users.models import User
from management import permissions as p 
from management import serializers as s 



class InviteUserView(APIView):
    permission_classes = (p.ManagerPermission, )

    def post(self, request):
        pass