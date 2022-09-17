from django.urls import reverse
from rest_framework import status
from collections import OrderedDict
from echocatch_tours_kanban.tests import BaseAPITestCase
from model_bakery import baker
from echocatch_tours_kanban.models import Boat

class SwimlaneTests(BaseAPITestCase):
    def test_create_swimlane(self):
        url = reverse('swimlane-list')

        data = { 'name': 'test swimlane' }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_list_swimlane(self):
        url = reverse('swimlane-list')

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

        for index, value in enumerate(response.data):
            self.assertEqual(value, OrderedDict({
                'id': self.swimlanes[index].id,
                'name': self.swimlanes[index].name,
                'boats': [
                    OrderedDict({
                        'id': boat.id,
                        'name': boat.name,
                        'swimlane_id': boat.swimlane_id,
                        'modified': boat.modified.strftime('%Y-%m-%d %H:%M:%S%z'),
                    }) for boat in self.swimlanes[index].boats.all()
                ],
            }))

    def test_retrieve_swimlane(self):
        self.swimlane = self.swimlanes[2]
        url = reverse('swimlane-detail', kwargs={ 'pk': self.swimlane.id })

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, OrderedDict({
            'id': self.swimlane.id,
            'name': self.swimlane.name,
            'boats': [
                OrderedDict({
                    'id': boat.id,
                    'name': boat.name,
                    'swimlane_id': boat.swimlane_id,
                    'modified': boat.modified.strftime('%Y-%m-%d %H:%M:%S%z'),
                }) for boat in self.swimlane.boats.all()
            ],
        }))

    def test_update_swimlane(self):
        self.swimlane = self.swimlanes[2]
        url = reverse('swimlane-detail', kwargs={ 'pk': self.swimlane.id })

        data = {
            'id': self.swimlane.id,
            'name': 'test name',
            'boats': [],
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update_swimlane(self):
        self.swimlane = self.swimlanes[2]
        url = reverse('swimlane-detail', kwargs={ 'pk': self.swimlane.id })

        data = {
            'name': 'test name',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_destroy_swimlane(self):
        self.swimlane = self.swimlanes[2]
        url = reverse('swimlane-detail', kwargs={ 'pk': self.swimlane.id })

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_swimlane_boats(self):
        self.swimlane = self.swimlanes[2]
        url = reverse('swimlane-boats', kwargs={ 'pk': self.swimlane.id })

        current_boats = self.swimlane.boats.all()
        current_boat_ids = [boat.id for boat in current_boats]

        data = {
            'boats': reversed(current_boat_ids)
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict({
            'id': self.swimlane.id,
            'name': self.swimlane.name,
            'boats': [
                OrderedDict({
                    'id': boat.id,
                    'name': boat.name,
                    'swimlane_id': boat.swimlane_id,
                    'modified': boat.modified.strftime('%Y-%m-%d %H:%M:%S%z'),
                }) for boat in reversed(current_boats)
            ],
        }))

        new_boats = [
            baker.make(
                'echocatch_tours_kanban.Boat',
                swimlane=self.swimlane,
            ) for index in range(20)
        ]
        data2 = {
            'boats': [ boat.id for boat in new_boats ]
        }
        response = self.client.post(url, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict({
            'id': self.swimlane.id,
            'name': self.swimlane.name,
            'boats': [
                OrderedDict({
                    'id': boat.id,
                    'name': boat.name,
                    'swimlane_id': boat.swimlane_id,
                    'modified': boat.modified.strftime('%Y-%m-%d %H:%M:%S%z'),
                }) for boat in new_boats
            ],
        }))
        self.assertEqual(Boat.objects.filter(id__in=current_boat_ids).count(), 0)