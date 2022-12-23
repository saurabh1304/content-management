from datetime import datetime
import random
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.authorization_token = None
        self.email = "user{}@test.con".format(datetime.utcnow().strftime("%Y%m%d%H%M%S%f"))
        self.password = "NewMedia"
        self.user = None

    def user_registration_and_login(self):
        def request(client, data):
            return client.post(
                reverse("api:auth:user_login"),
                data=data,
                content_type="application/json",
            )

        self.test_register()

        data = {"email": self.email, "password": self.password}

        response = request(self.client, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIsNotNone(response.data["access_token"])

        self.authorization_token = "Bearer " + response.data["access_token"]

        return response

    def test_register(self):
        """
        Test Registration Process
        """

        def request(client, data):
            return client.post(
                reverse("api:auth:user_registration-list"),
                data=data,
                content_type="application/json",
            )

        self.email = "user{}@test.con".format(datetime.utcnow().strftime("%Y%m%d%H%M%S%f"))

        data = {
            "name": "Test User",
            "email": self.email,
            "password": self.password,
            "gender": random.choice([1, 2, 3, 4]),
            "birth_year": 1995,
        }
        response = request(self.client, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
