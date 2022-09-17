
from rest_framework.test import APITestCase
from model_bakery import baker

class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.swimlanes = [
            baker.make('echocatch_tours_kanban.Swimlane', position=position) for position in range(5)
        ]
        self.boats = sorted(
            [
                baker.make(
                    'echocatch_tours_kanban.Boat',
                    swimlane=self.swimlanes[index % len(self.swimlanes)],
                    position=index
                ) for index in range(20)
            ],
            key=lambda boat: (boat.swimlane.position, boat.position)
        )