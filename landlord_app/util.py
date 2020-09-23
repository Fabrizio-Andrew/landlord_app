from landlord_app.models import Units

def list_units():
    return models.Unit.objects.all()

def save_unit(submission):
    print(submission)
    x = Units(nickname=submission.get('nickname'),
        address_line1=submission.get('address_line1'),
        address_line2=submission.get('address_line2'),
        city=submission.get('city'),
        state=submission.get('state'),
        zipcode=submission.get('zipcode'),
        bedrooms=submission.get('bedrooms'),
        bathrooms=submission.get('bathrooms'))
    x.save()
    print('Saved')
