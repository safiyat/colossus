from users.models import AuthUser

class Quiz:
    user = db.ReferenceField(AuthUser)
    # more fields
    time_stamp = db.DateTimeField()

    def __unicode__(self):
        return "%s" % self.user
