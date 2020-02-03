from rest_framework import serializers
from ...core.loading import get_model

TABLE = get_model('loan', 'Loan')
APP = 'loan_api'
fields = ('user', 'book', 'request','status')


class LoanSerializer(serializers.ModelSerializer):
    update_url = serializers.HyperlinkedIdentityField(view_name=APP + ':update')
    delete_url = serializers.HyperlinkedIdentityField(view_name=APP + ':delete')

    class Meta:
        model = TABLE
        fields = fields + ('update_url', 'delete_url')

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.book = validated_data.get('book', instance.book)
        instance.request = validated_data.get('request', instance.request)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance

# For admin to change loan request status to either Accepted or Rejected
class LoanRequestStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = TABLE
        fields = ('request')

    def update(self, instance, validated_data):
        instance.request = validated_data.get('request', instance.request)
        instance.save()

        return instance

# For admin to change loan status to either Taken or Returned
class LoanStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = TABLE
        fields = ('status')

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance

# For member to request book loan
class LoanCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TABLE
        fields = ['book']

