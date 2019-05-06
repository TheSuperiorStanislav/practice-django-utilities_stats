from celery import shared_task
from celery.utils.log import get_task_logger

from utilities.models import Utilities

logger = get_task_logger(__name__)


@shared_task(name="get_field_data")
def get_field_data(owner, field, years):
    field_data = {
        str(year): {
            'avg': Utilities.objects.avg_field(owner, year, field),
            'sum': Utilities.objects.sum_field(owner, year, field),
            'max': Utilities.objects.max_field(owner, year, field),
            'min': Utilities.objects.min_field(owner, year, field),
            'values': Utilities.objects.values_field(owner, year, field),
        }
        for year in years
    }
    return [field, field_data]
