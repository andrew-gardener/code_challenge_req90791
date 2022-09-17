from django.urls import reverse
from rest_framework import status
from collections import OrderedDict
from echocatch_tours_kanban.tests import BaseAPITestCase
from echocatch_tours_kanban.models import Boat

class BoatTests(BaseAPITestCase):
    def test_create_boat(self):
        url = reverse('boat-list')
        current_boat_count = Boat.objects.count()

        data = {
            'name': 'test boat',
            'swimlane_id': self.swimlanes[2].id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Boat.objects.count(), current_boat_count+1)
        self.boat = Boat.objects.get(id=response.data.get('id'))
        self.assertEqual(self.boat.name, 'test boat')
        self.assertEqual(self.boat.swimlane.id, self.swimlanes[2].id)

    def test_list_boat(self):
        url = reverse('boat-list')

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 20)
        for index, value in enumerate(response.data):
            self.assertEqual(value, OrderedDict({
                'id': self.boats[index].id,
                'name': self.boats[index].name,
                'swimlane_id': self.boats[index].swimlane_id,
                'modified': self.boats[index].modified.strftime('%Y-%m-%d %H:%M:%S%z'),
            }))

    def test_retrieve_boat(self):
        self.boat = self.boats[5]
        url = reverse('boat-detail', kwargs={ 'pk': self.boat.id })

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict({
            'id': self.boat.id,
            'name': self.boat.name,
            'swimlane_id': self.boat.swimlane.id,
            'modified': self.boat.modified.strftime('%Y-%m-%d %H:%M:%S%z'),
        }))

    def test_update_boat(self):
        self.boat = self.boats[5]
        url = reverse('boat-detail', kwargs={ 'pk': self.boat.id })

        data = {
            'id': self.boat.id,
            'name': 'test name1',
            'swimlane_id': self.swimlanes[2].id,
            'modified': self.boat.modified.strftime('%Y-%m-%d %H:%M:%S%z'),
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict(data))

        data2 = {
            'id': 'test id',
            'name': 'test name2',
            'swimlane_id': self.swimlanes[1].id,
            'modified': self.boat.modified.strftime('%Y-%m-%d %H:%M:%S%z'),
        }
        response = self.client.put(url, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict({
            'id': self.boat.id,
            'name': 'test name2',
            'swimlane_id': self.swimlanes[1].id,
            'modified': self.boat.modified.strftime('%Y-%m-%d %H:%M:%S%z'),
        }))

    def test_partial_update_boat(self):
        self.boat = self.boats[5]
        url = reverse('boat-detail', kwargs={ 'pk': self.boat.id })

        data = {
            'name': 'test name1',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict({
            'id': self.boat.id,
            'name': 'test name1',
            'swimlane_id': self.boat.swimlane.id,
            'modified': self.boat.modified.strftime('%Y-%m-%d %H:%M:%S%z'),
        }))

        data2 = {
            'id': 'test id',
        }
        response = self.client.patch(url, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict({
            'id': self.boat.id,
            'name': 'test name1',
            'swimlane_id': self.boat.swimlane.id,
            'modified': self.boat.modified.strftime('%Y-%m-%d %H:%M:%S%z'),
        }))

    def test_destroy_boat(self):
        self.boat = self.boats[5]
        url = reverse('boat-detail', kwargs={ 'pk': self.boat.id })
        current_boat_count = Boat.objects.count()
        current_id = self.boat.id

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Boat.objects.count(), current_boat_count-1)
        self.assertFalse(Boat.objects.filter(id=current_id).exists())