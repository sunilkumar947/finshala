from accounts.models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=('id', 'name', 'email','username', 'phone', 'role', 'access_token')

    def get_access_token(self,user):
        refresh = RefreshToken.for_user(user)
        return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        }
    
class AgentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    phone = serializers.CharField(source='user.phone', read_only=True)
    class Meta:
        model = Agent
        fields = "__all__"
    
class UccregisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Uccregister
        fields=('id','user','agent','member_code', 'email', 'regn_type', 'occupation_code', 'holding_code', 
                'primary_holder_exempt_category', 'second_holder_exempt_category', 'third_holder_exempt_category', 
                'guardian_exempt_category', 'client_type', 'account_type_1', 'account_type_2', 'account_type_3', 
                'account_type_4', 'account_type_5', 'div_pay_mode', 'state_code', 'country_code', 
                'communication_mode', 'nominee_1_relationship', 'nominee_2_relationship', 'nominee_3_relationship', 
                'guardian_relationship', 'primary_holder_kyc_type', 'second_holder_kyc_type', 'third_holder_kyc_type', 
                'guardian_holder_kyc_type', 'paperless_flag', 'filler_1_mobile_declaration_flag', 
                'filler_2_email_declaration_flag', 'second_holder_email_declaration', 'second_holder_mobile_declaration', 
                'third_holder_mobile_declaration', 'third_holder_email_declaration', 'nomination_auth_mode', 'mobile', 
                'param', 'tax_status', 'filler_1', 'filler_2','Signature_image', 'Term_conditions', 'is_submit',
                'created_time','utimestamp',)

    def update(self, instance, validated_data):
        param_data = validated_data.get("param", {})

        if instance.param is None:
            instance.param = {}

        if isinstance(param_data, dict):
            for key, value in param_data.items():
                instance.param[key] = value if value else instance.param.get(key, "")

        for key, value in validated_data.items():
            if key != "param":
                setattr(instance, key, value)

        instance.save()
        return instance


class FATCASerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatca
        fields = "__all__"

class MandateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandate
        fields = "__all__"
        
class EnachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enach
        fields = "__all__"

class AMCListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMCList
        fields = "__all__"

class XSIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = XSIPTransaction
        fields = "__all__"

# class AMCCartSerializer(serializers.ModelSerializer):
#     sip = XSIPSerializer()
#     class Meta:
#         model = SIPCart
#         fields = "__all__"

class AMCCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMCCart
        fields = "__all__"