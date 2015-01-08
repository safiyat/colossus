import datetime
from mongoengine import signals
from . import db


class BaseUser(db.Document):
   name = db.StringField(max_length=80)
   email = db.EmailField(max_length=255, unique=True)
   phone_no = db.StringField(max_length=31)
   date_of_birth = db.StringField(max_length=31)
   social_ref = db.ListField(db.StringField(), default=[])  #FB/google
   ref_username = db.ListField(db.StringField(), default=[])  #FB_username/GP_Username
   ref_image = db.ListField(db.URLField(), default=[])

   def __unicode__(self):
      return self.email


class AuthUser(BaseUser):
   ref_last_login = db.ListField(db.DateTimeField(), default=[])


class UserContacts(BaseUser):
   ref_user =  db.ListField(db.ReferenceField(AuthUser), default=[])
