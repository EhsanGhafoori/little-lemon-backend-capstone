from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Menu, Booking
from django.utils import timezone


class MenuViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.menu_item = Menu.objects.create(title='Test Item', price=9.99, inventory=5)

    def test_menu_list_authenticated(self):
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_menu_detail(self):
        response = self.client.get(reverse('menu-detail', args=[self.menu_item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Item')


class BookingViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.booking = Booking.objects.create(
            name='Test Guest',
            no_of_guests=2,
            booking_date=timezone.now()
        )

    def test_booking_list_authenticated(self):
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_booking_detail(self):
        response = self.client.get(reverse('booking-detail', args=[self.booking.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Guest')
