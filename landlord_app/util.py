from landlord_app.models import Unit

def all_properties():
    return models.Unit.objects.all()

def saveproperty(submission):
    print(submission)
    x = Unit(nickname=submission.get('nicknamevalue'), address=submission.get('addressvalue'), bedrooms=submission.get('bedvalue'), bathrooms=submission.get('bathvalue'))
    x.save()
    print('Saved')
