from rest_framework import serializers
from .models import Comments

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = (
            'id',
            'place',
            'comment',
            'created_at',
        )

    def to_representation(self, instance):
        
        return {
            'id': instance.id,
            'place': {
                'id': instance.place.id,
                'name': instance.place.name
                },
            'comment': instance.comment,
            'created_at': instance.created_at
        }

class CommentPlaceListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comments
            fields = (
                'id',
                'comment',
                'created_at',
            )