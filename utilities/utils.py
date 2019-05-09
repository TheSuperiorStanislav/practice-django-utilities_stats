from utilities.models import Utilities


def is_data_valid(data):
    not_service = [
        'owner',
        'date',
        'underpayment',
        'amount_to_pay',
        'payments_last_mouth'
    ]

    amount_to_pay = sum([
        data.get(key)
        for key in data.keys()
        if 'consumption' not in key and key not in not_service
    ])
    if amount_to_pay != data.get('amount_to_pay'):
        return False

    return True


def is_date_valid(owner, value):
    month = value.month
    year = value.year
    utilities_with_same_date = Utilities.objects.filter(
        owner=owner,
        date__month=month,
        date__year=year
    )

    if utilities_with_same_date:
        return False
    return True
