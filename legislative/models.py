from django.db import models


class Legislator(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Bill(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    primary_sponsor = models.ForeignKey(Legislator, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Vote(models.Model):
    id = models.IntegerField(primary_key=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)


class VoteResult(models.Model):
    id = models.IntegerField(primary_key=True)
    legislator = models.ForeignKey(Legislator, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    vote_type = models.IntegerField()
