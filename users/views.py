from rest_framework.views import APIView
from werkzeug.security import check_password_hash, generate_password_hash



class UserPasswordSetup(APIView):
    def post(self, request, verification_link):
        pass