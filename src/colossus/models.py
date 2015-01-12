import datetime
from mongoengine import signals
import mongoengine as db

class BaseUser(db.Document):
  name = db.StringField(max_length=80)
  email = db.EmailField(max_length=255, unique=True)
  phone_no = db.StringField(max_length=31)
  date_of_birth = db.StringField(max_length=31)
  social_ref = db.ListField(db.StringField(), default=[])  #FB/google
  ref_username = db.ListField(db.StringField(), default=[])  #FB_username/GP_Username
  ref_image = db.ListField(db.URLField(), default=[])

  def save_user(self, data, source):
    db.connect('colossus')
    name = email = phone_no = ''
    if source == 'google':
      try:
        name = data.title.text
      except Exception as e:
        pass
      try:
        phone_no = data.phone_number[0].uri
      except Exception as e:
        pass
      try:
        email = data.email[0].address
      except Exception as e:
        pass
      try:
        source = 'Google+ Plus'
      except Exception as e:
        pass
      print '%s %s %s %s' % (username, userphone, useremail, source)
    elif source == 'facebook':
      pass

    h = BaseUser(name=name, phone_no=phone_no, email=email, source=source )
    h.save()

  def __unicode__(self):
    return self.email


# class AuthUser(BaseUser):
#    ref_last_login = db.ListField(db.DateTimeField(), default=[])


# class UserContacts(BaseUser):
#    ref_user =  db.ListField(db.ReferenceField(AuthUser), default=[])




;