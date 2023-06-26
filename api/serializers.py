from rest_framework.serializers import ModelSerializer
from .models import Note


# Serializers convert object or query of django into json
class NoteSerializer(ModelSerializer):
    class Meta:
        model=Note
        fields='__all__'

