from django.db.models import fields
from rest_framework import serializers
from SII_API.models import Sii_Api, User

class ApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sii_Api
        fields = (  'idApp',
                    'date',
                    'type',
                    'valeur',
                    'alerte',
                    'messageAlerte', )

        # modelUser = User
        # fields = (  'userid',
        #             'username',
        #             'password',)
