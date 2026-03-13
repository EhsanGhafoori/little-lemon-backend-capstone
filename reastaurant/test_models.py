from django.test import TestCase
from django.utils import timezone
from .models import Menu, Booking


class MenuModelTest(TestCase):
    def test_create_menu_item(self):
        item = Menu.objects.create(
            title='Greek Salad',
            price=12.50,
            inventory=10
        )
        self.assertEqual(item.title, 'Greek Salad')
        self.assertEqual(float(item.price), 12.50)
        self.assertEqual(item.inventory, 10)
        self.assertIn('Greek Salad', str(item))
        self.assertIn('12.5', str(item))

    def test_menu_str(self):
        item = Menu(title='Lemonade', price=3.00, inventory=50)
        self.assertIn('Lemonade', str(item))
        self.assertIn('Lemonade', str(item))
        self.assertIn('3', str(item))


class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking_date = timezone.now()
        booking = Booking.objects.create(
            name='John Doe',
            no_of_guests=4,
            booking_date=booking_date
        )
        self.assertEqual(booking.name, 'John Doe')
        self.assertEqual(booking.no_of_guests, 4)
        self.assertEqual(booking.booking_date, booking_date)

    def test_booking_str(self):
        booking_date = timezone.now()
        booking = Booking(name='Jane', no_of_guests=2, booking_date=booking_date)
        self.assertIn('Jane', str(booking))
