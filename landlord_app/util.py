from landlord_app.models import Units

def all_properties():
    return models.Unit.objects.all()

def saveproperty(submission):
    print(submission)
    x = Units(nickname=submission.get('nicknamevalue'), address=submission.get('addressvalue'), bedrooms=submission.get('bedvalue'), bathrooms=submission.get('bathvalue'))
    x.save()
    print('Saved')
