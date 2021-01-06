def generate_value(label, value):
    return {
        'label': label,
        'value': value
    }


def generate_statement(indicators, data):
    statement = {}
    for indicator in indicators:
        statement[indicator.get('name')] = generate_value(
            label=indicator.get('label'), value=data.get(indicator.get('name')).get('fmt'))
    return statement
