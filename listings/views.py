from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
     'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    #Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'listing': listing,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)
