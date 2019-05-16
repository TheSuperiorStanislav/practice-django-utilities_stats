from utilities.models import Utilities


def is_data_validation_error(data):
    not_service = [
        'owner',
        'date',
        'underpayment',
        'amount_to_pay',
        'payments_last_mouth',
        'to_pay'
    ]

    amount_to_pay = round(sum([
        data.get(key)
        for key in data.keys()
        if 'consumption' not in key and key not in not_service
        ]), 2)

    if amount_to_pay != data.get('amount_to_pay'):
        return 'Amount to pay(%r) != Services price(%r)' % (
            data.get('amount_to_pay'),
            amount_to_pay,
            )


def is_date_validation_error(owner, value):
    month = value.month
    year = value.year
    utilities_with_same_date = Utilities.objects.filter(
        owner=owner,
        date__month=month,
        date__year=year
    )

    if utilities_with_same_date:
        return utilities_with_same_date[0]
