from rest_framework.test import APITestCase, APIClient

from apps.authentication.models import User
from apps.device.models import GlucoseDevice


class UserGlucoseLevelModelViewSetTest(APITestCase):
    def test_create_levels(self):
        # create user
        user = User.objects.create_user(username="misrax", password="misrax", email="misrax@misrax.com")
        # create device
        device = GlucoseDevice.objects.create(name="FreeStyle LibreLink", serial="2da283e0-2c18-444e-8f9b-801e90a2af5b")
        client = APIClient()
        create_date = client.post('/level/', {
            "meta": {},
            "device_timestamp": "2022-02-05T16:54:42.886Z",
            "recording_type": "string",
            "level": 0,
            "scan": 0,
            "non_numeric_rapid_insulin": 12,
            "rapid_acting_insulin": 12,
            "non_numeric_nutritional_data": 12,
            "carbohydrates": 12,
            "non_numeric_depot_insulin": 12,
            "depot_insulin": 12,
            "notes_Glucose_test": 0,
            "ketone": 12,
            "meal_insulin": 12,
            "correction_insulin": 12,
            "insulin_Change": 12,
            "user": user.id,
            "device": device.id
        }, format='json')
        self.assertEqual(create_date.status_code, 201)

    def test_list_levels(self):
        client = APIClient()
        create_date = client.get('/level/')
        self.assertEqual(create_date.status_code, 200)
