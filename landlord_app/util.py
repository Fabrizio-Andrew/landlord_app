from landlord_app.models import Unit

# This is how I can access object attributes via queries and combine into python dicts nested in a list.  A "DickTucken"
# Might be better to loop through results on the html template.
def list_units_detailed():
    results = []
    for x in Unit.objects.all():
        d = {
            'nickname': x.nickname,
            'address_line1': x.address_line1,
            'address_line2': x.address_line2,
            'city': x.city,
            'state': x.state,
            'zipcode': x.zipcode,
            'bedrooms': x.bedrooms,
            'bathrooms': x.bathrooms
        }
        results.append(d)
    print(results)
    return results


# This is like a complete duplicate of views.save_unit.  Who wrote this garbage?
def save_unit(submission):
    print(submission)
    x = Unit(nickname=submission.get('nickname'),
        address_line1=submission.get('address_line1'),
        address_line2=submission.get('address_line2'),
        city=submission.get('city'),
        state=submission.get('state'),
        zipcode=submission.get('zipcode'),
        bedrooms=submission.get('bedrooms'),
        bathrooms=submission.get('bathrooms'))
    x.save()
    print('Saved')
