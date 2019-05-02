import datetime
import pytz

from django.test import TestCase
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

from .models import Utilities
from users.models import UtilitiesUser


class UtilitiesManagerTests(TestCase):

    def createUtilitiesEntry(self, month):
        date = datetime.datetime.now(pytz.utc).replace(month=month)
        return Utilities.objects.create(
                owner=self.user,
                date=date,
                date_last_edit=datetime.datetime.now(pytz.utc),
                underpayment=100.0 * month,
                amount_to_pay=100.0 * month,
                payments_last_mouth=100.0 * month,
                to_pay=100.0 * month,
                housing_stock=100.0 * month,
                hws_thermal_energy_cp=100.0 * month,
                hws_cold_water_cp=100.0 * month,
                cold_water_cp=100.0 * month,
                sewage_cp=100.0 * month,
                electricity_cp=100.0 * month,
                special_account_for_overhaul=100.0 * month,
                home_heating=100.0 * month,
                hws_thermal_energy=100.0 * month,
                hws_cold_water=100.0 * month,
                cold_water=100.0 * month,
                sewage=100.0 * month,
                garbage_service=100.0 * month,
                electricity=100.0 * month,
                intercom_maintenance=100.0 * month,
                gate_maintenance=100.0 * month,
                cctv_maintenance=100.0 * month,
                hws_cold_water_consumption=100.0 * month,
                cold_water_consumption=100.0 * month,
                sewage_consumption=100.0 * month,
                electricity_consumption=100.0 * month,
            )

    def setUp(self):
        self.user = UtilitiesUser.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        for i in range(1, 13):
            self.createUtilitiesEntry(i)

    def test_string_representation(self):
        utilities = Utilities(date=datetime.datetime.now(pytz.utc))
        df = DateFormat(utilities.date)
        self.assertEqual(str(utilities), df.format(get_format('DATE_FORMAT')))

    def test_avg_manager(self):
        year = datetime.datetime.now(pytz.utc).year
        avg = Utilities.objects.avg_field(
            self.user,
            year,
            'electricity_consumption'
            )
        self.assertEqual(avg, 650)

    def test_sum_manager(self):
        year = datetime.datetime.now(pytz.utc).year
        sum_val = Utilities.objects.sum_field(
            self.user,
            year,
            'electricity_consumption'
            )
        self.assertEqual(sum_val, 7800)

    def test_max_manager(self):
        year = datetime.datetime.now(pytz.utc).year
        max_val = Utilities.objects.max_field(
            self.user,
            year,
            'electricity_consumption'
            )
        self.assertEqual(max_val, 1200)

    def test_min_manager(self):
        year = datetime.datetime.now(pytz.utc).year
        min_val = Utilities.objects.min_field(
            self.user,
            year,
            'electricity_consumption'
            )
        self.assertEqual(min_val, 100)

    def test_values_manager(self):
        year = datetime.datetime.now(pytz.utc).year
        values = Utilities.objects.values_field(
            self.user,
            year,
            'electricity_consumption'
            )
        values_to_equal = [(i, 100.0 * i) for i in range(1, 13)]
        self.assertEqual(values, values_to_equal)
