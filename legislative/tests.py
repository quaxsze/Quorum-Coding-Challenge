from django.test import TestCase
from .models import Bill, Legislator, Vote, VoteResult


class BillModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Bill.objects.create(id=1, title='Bill Title', primary_sponsor=1)

    def test_bill_creation(self):
        bill = Bill.objects.get(id=1)
        self.assertTrue(isinstance(bill, Bill))
        self.assertEqual(bill.__str__(), bill.title)


class LegislatorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Legislator.objects.create(id=1, name='John Doe')

    def test_legislator_creation(self):
        legislator = Legislator.objects.get(id=1)
        self.assertTrue(isinstance(legislator, Legislator))
        self.assertEqual(legislator.__str__(), legislator.name)


class VoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        bill = Bill.objects.create(id=1, title='Bill Title', primary_sponsor=1)
        Vote.objects.create(id=1, bill=bill)

    def test_vote_creation(self):
        vote = Vote.objects.get(id=1)
        self.assertTrue(isinstance(vote, Vote))
        self.assertEqual(vote.bill.title, 'Bill Title')


class VoteResultModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        legislator = Legislator.objects.create(id=1, name='John Doe')
        bill = Bill.objects.create(id=1, title='Bill Title', primary_sponsor=1)
        vote = Vote.objects.create(id=1, bill=bill)
        VoteResult.objects.create(id=1, legislator=legislator, vote=vote, vote_type=1)

    def test_voteresult_creation(self):
        voteresult = VoteResult.objects.get(id=1)
        self.assertTrue(isinstance(voteresult, VoteResult))
        self.assertEqual(voteresult.legislator.name, 'John Doe')
        self.assertEqual(voteresult.vote.bill.title, 'Bill Title')
        self.assertEqual(voteresult.vote_type, 1)
