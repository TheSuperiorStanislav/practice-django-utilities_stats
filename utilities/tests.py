import datetime
import pytz


from django.test import TestCase
from django.test.utils import override_settings
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

from .views import get_stat_data

from .models import Utilities
from .forms import UtilitiesForm
from users.models import UtilitiesUser
from api.serializers import UtilitiesSerializer


def createUtilitiesEntry(user, month, year):
    date = datetime.datetime.now(pytz.utc).replace(month=month, year=year)
    return Utilities.objects.create(
            owner=user,
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


class UtilitiesManagerTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = UtilitiesUser.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        cur_year = datetime.datetime.now(pytz.utc).year

        for month in range(1, 13):
            createUtilitiesEntry(user, month, cur_year)
        for year in range(2015, 2019):
            for month in range(1, 13):
                createUtilitiesEntry(user, month, year)

    def setUp(self):
        self.user = UtilitiesUser.objects.get(
            username='testuser'
        )

        self.cur_year = datetime.datetime.now(pytz.utc).year

    def test_string_representation(self):
        utilities = Utilities(date=datetime.datetime.now(pytz.utc))
        df = DateFormat(utilities.date)
        self.assertEqual(str(utilities), df.format(get_format('DATE_FORMAT')))

    def test_avg_manager(self):
        avg = Utilities.objects.avg_field(
            self.user,
            self.cur_year,
            'electricity_consumption'
            )
        self.assertEqual(avg, 650)

    def test_sum_manager(self):
        sum_val = Utilities.objects.sum_field(
            self.user,
            self.cur_year,
            'electricity_consumption'
            )
        self.assertEqual(sum_val, 7800)

    def test_max_manager(self):
        max_val = Utilities.objects.max_field(
            self.user,
            self.cur_year,
            'electricity_consumption'
            )
        self.assertEqual(max_val, 1200)

    def test_min_manager(self):
        min_val = Utilities.objects.min_field(
            self.user,
            self.cur_year,
            'electricity_consumption'
            )
        self.assertEqual(min_val, 100)

    def test_values_manager(self):
        values = Utilities.objects.values_field(
            self.user,
            self.cur_year,
            'electricity_consumption'
            )
        values_to_equal = [(i, 100.0 * i) for i in range(1, 13)]
        self.assertEqual(values, values_to_equal)


class UtilitiesViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = UtilitiesUser.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        cur_year = datetime.datetime.now(pytz.utc).year

        for month in range(1, 13):
            createUtilitiesEntry(user, month, cur_year)
        for year in range(2000, 2005):
            for month in range(1, 13):
                createUtilitiesEntry(user, month, year)

    def setUp(self):
        self.user = UtilitiesUser.objects.get(
            username='testuser',
        )

        self.cur_year = datetime.datetime.now(pytz.utc).year

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def test_get_stat_date(self):
        stat_data = get_stat_data(
            self.user,
            [
                'underpayment',
                'hws_cold_water_consumption',
                'cold_water_consumption',
                'sewage_consumption',
                'electricity_consumption',
            ]
        )

        self.assertEqual(
            stat_data['electricity_consumption'][str(self.cur_year)]['avg'],
            650
            )


class UtilitiesFormAndSerializerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = UtilitiesUser.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        cur_year = datetime.datetime.now(pytz.utc).year
        createUtilitiesEntry(user, 1, cur_year)
        createUtilitiesEntry(user, 2, cur_year)

    def setUp(self):
        self.user = UtilitiesUser.objects.get(
            username='testuser',
        )

        cur_year = datetime.datetime.now(pytz.utc).year

        self.date1 = datetime.datetime.now(pytz.utc).replace(
            month=1,
            year=cur_year
        )
        self.date2 = datetime.datetime.now(pytz.utc).replace(
            month=2,
            year=cur_year
        )

        self.data = {
            'owner': self.user,
            'date': self.date1,
            'date_last_edit': datetime.datetime.now(pytz.utc),
            'underpayment': 100.0,
            'amount_to_pay': 100.0 * 17.0,
            'payments_last_mouth': 100.0,
            'to_pay': 100.0,
            'housing_stock': 100.0,
            'hws_thermal_energy_cp': 100.0,
            'hws_cold_water_cp': 100.0,
            'cold_water_cp': 100.0,
            'sewage_cp': 100.0,
            'electricity_cp': 100.0,
            'special_account_for_overhaul': 100.0,
            'home_heating': 100.0,
            'hws_thermal_energy': 100.0,
            'hws_cold_water': 100.0,
            'cold_water': 100.0,
            'sewage': 100.0,
            'garbage_service': 100.0,
            'electricity': 100.0,
            'intercom_maintenance': 100.0,
            'gate_maintenance': 100.0,
            'cctv_maintenance': 100.0,
            'hws_cold_water_consumption': 100.0,
            'cold_water_consumption': 100.0,
            'sewage_consumption': 100.0,
            'electricity_consumption': 100.0,
        }

    def test_form_valid_exisiting_date(self):

        form = UtilitiesForm(
            user=self.user,
            data=self.data
            )
        self.assertFalse(form.is_valid())

    def test_edit_form_valid_edit_date(self):
        form = UtilitiesForm(
            user=self.user,
            pk=1,
            data=self.data
            )
        self.assertTrue(form.is_valid())

    def test_edit_form_valid_exisiting_date(self):
        data = self.data
        data['date'] = self.date2
        form = UtilitiesForm(
            user=self.user,
            pk=1,
            data=self.data
            )
        self.assertFalse(form.is_valid())

    def test_form_valid_amount_to_pay(self):
        data = self.data
        data['amount_to_pay'] = 1
        form = UtilitiesForm(
            user=self.user,
            data=data
            )
        self.assertFalse(form.is_valid())

    def test_serializer_valid_exisiting_date(self):
        data = self.data
        data['owner'] = 'http://127.0.0.1/api/users/%s/' % (self.user.pk)
        data['date'] = data['date'].strftime('%Y-%m-%d')
        serializer = UtilitiesSerializer(
            data=data
            )
        self.assertFalse(serializer.is_valid())

    def test_edit_serializer_valid_edit_date(self):
        data = self.data
        data['owner'] = 'http://127.0.0.1/api/users/%s/' % (self.user.pk)
        data['date'] = data['date'].strftime('%Y-%m-%d')
        serializer = UtilitiesSerializer(
            Utilities.objects.get(pk=1),
            data=data
            )
        self.assertTrue(serializer.is_valid())

    def test_edit_serializer_valid_exisiting_date(self):
        data = self.data
        data['owner'] = 'http://127.0.0.1/api/users/%s/' % (self.user.pk)
        data['date'] = self.date2.strftime('%Y-%m-%d')
        serializer = UtilitiesSerializer(
            Utilities.objects.get(pk=1),
            data=data
            )
        self.assertFalse(serializer.is_valid())

    def test_serializer_valid_amount_to_pay(self):
        data = self.data
        data['owner'] = 'http://127.0.0.1/api/users/%s/' % (self.user.pk)
        data['date'] = data['date'].strftime('%Y-%m-%d')
        data['amount_to_pay'] = 1
        serializer = UtilitiesSerializer(
            data=data
            )
        self.assertFalse(serializer.is_valid())
