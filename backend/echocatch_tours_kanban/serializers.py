from echocatch_tours_kanban.models import Swimlane, Boat
from rest_framework import serializers

class BoatSerializer(serializers.ModelSerializer):
    swimlane_id = serializers.PrimaryKeyRelatedField(
        source="swimlane",
        queryset=Swimlane.objects.all(),
    )

    class Meta:
        model = Boat
        fields = ['id', 'name', 'swimlane_id', 'modified']
        read_only_fields = ['id', 'modified']


class SwimlaneSerializer(serializers.ModelSerializer):
    boats = BoatSerializer(many=True)

    class Meta:
        model = Swimlane
        fields = ['id', 'name', 'boats']
        read_only_fields = ['id']

class SwimlaneReorderBoatsSerializer(serializers.Serializer):
    boats = serializers.ListField(
        child=serializers.CharField(min_length=22, max_length=22)
    )
    touch = serializers.CharField(min_length=22, max_length=22, required=False)

    class Meta:
        fields = ['boats', 'touch']