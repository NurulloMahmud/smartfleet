from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.urls import reverse
from users.models import User

from management import permissions as p 
from management import serializers as s 

from werkzeug.security import generate_password_hash



class InviteUserView(APIView):
    permission_classes = [p.ManagerPermission, ]

    def post(self, request):
        # Deserialize the incoming data
        serializer = s.InviteUserSerializer(data=request.data)

        if serializer.is_valid():
            # Save the valid data
            serializer.save()

            # Generate a secure, one-time verification link
            verification_link = generate_password_hash(serializer.validated_data['username'])
            url = reverse("users:set-password", kwargs={"verification_link": verification_link})

            # Return a success response
            return Response({
                "success": True, 
                "message": "User has been created successfully",
                "url": url
            }, status=status.HTTP_200_OK)

        # Return a response with error details in case of invalid data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

