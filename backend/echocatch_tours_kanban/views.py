from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from echocatch_tours_kanban.models import Swimlane, Boat
from echocatch_tours_kanban.serializers import SwimlaneSerializer, BoatSerializer, SwimlaneReorderBoatsSerializer

class SwimlaneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Swimlane.objects.all()
    serializer_class = SwimlaneSerializer

    @action(detail=True, methods=['post'], serializer_class=SwimlaneReorderBoatsSerializer)
    def boats(self, request, pk=None):
        swimlane = self.get_object()
        serializer = SwimlaneReorderBoatsSerializer(data=request.data)
        if serializer.is_valid():
            boat_ids = serializer.validated_data.get('boats')
            touch_id = serializer.validated_data.get('touch')
            for index, boat_id in enumerate(boat_ids):
                update_value = {
                    'swimlane_id': swimlane.id,
                    'position': index,
                }
                if touch_id and touch_id == boat_id:
                    update_value['modified'] = timezone.now()

                Boat.objects.filter(id=boat_id).update(**update_value)
            Boat.objects.filter(swimlane_id=swimlane.id).exclude(id__in=boat_ids).delete()
            return Response(SwimlaneSerializer(swimlane).data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class BoatViewSet(viewsets.ModelViewSet):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer