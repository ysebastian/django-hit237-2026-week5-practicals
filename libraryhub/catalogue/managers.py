from django.db import models


class LoanQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status='active')

    def for_member(self, member):
        return self.filter(member=member)


class LoanManager(models.Manager):
    def get_queryset(self):
        return LoanQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def for_member(self, member):
        return self.get_queryset().for_member(member)