from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from .models import VoteResult, Legislator, Bill


def legislator(request, legislator_id):
    legislator = get_object_or_404(Legislator, pk=legislator_id)

    # Query to count how many bills the legislator supported
    supported_bills_count = VoteResult.objects.filter(
        legislator_id=legislator_id,
        vote_type=1
    ).aggregate(support_count=Count('vote', distinct=True))

    # Query to count how many bills the legislator opposed
    opposed_bills_count = VoteResult.objects.filter(
        legislator_id=legislator_id,
        vote_type=2
    ).aggregate(oppose_count=Count('vote', distinct=True))

    context = {
        "legislator": legislator,
        "bills_supported": supported_bills_count['support_count'],
        "bills_opposed": opposed_bills_count['oppose_count']
    }
    return render(request, "legislative/legislator.html", context)


def bill(request, bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)

    # Query to count how many legislators supported the bill
    supporters_count = VoteResult.objects.filter(
        vote__bill_id=bill_id,
        vote_type=1
    ).aggregate(support_count=Count('legislator', distinct=True))

    # Query to count how many legislators opposed the bill
    opposers_count = VoteResult.objects.filter(
        vote__bill_id=bill_id,
        vote_type=2
    ).aggregate(oppose_count=Count('legislator', distinct=True))

    # Retrieve the primary sponsor of the bill
    primary_sponsor = bill.primary_sponsor.name

    context = {
        "bill": bill,
        "legislators_supported": supporters_count['support_count'],
        "legislators_opposed": opposers_count['oppose_count'],
        "primary_sponsor": primary_sponsor
    }
    return render(request, "legislative/bill.html", context)
