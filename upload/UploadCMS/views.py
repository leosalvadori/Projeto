from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Band, Member
from .forms import BandContactForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import  login as login_auth
from django.contrib.auth import logout as logout_auth


def home(request):
    return render(request, 'home.html')


def band_listing(request):
    """ A view of all UploadCMS. """
    repositories = Band.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        repositories = repositories.filter(name__icontains=var_get_search)
    return render(request, 'bands/band_listing.html', {'repositories': repositories})

def band_contact(request):
    """ A example of form """
    if request.method == 'POST':
        form = BandContactForm(request.POST)
    else:
        form = BandContactForm()
    return render(request, 'bands/band_contact.html', {'form': form})


def band_detail(request, pk):
    """ A view of all members by UploadCMS. """
    band = Band.objects.get(pk=pk)
    members = Member.objects.all().filter(band=band)
    context = {'members': members, 'band': band}
    return render(request, 'bands/band_detail.html', context)


class BandForm(CreateView):
    template_name = 'bands/band_form.html'
    model = Band
    success_url = reverse_lazy('repositories')
    fields = ['name', 'is_active', 'type']


class MemberForm(CreateView):
    template_name = 'bands/member_form.html'
    model = Member
    success_url = reverse_lazy('repositories')
    fields = ['name', 'instrument', 'band']


def login(request):
    if request.method == 'POST':
        try:
            usuario = authenticate(username=request.POST.get('login-username'), password=request.POST.get('login-password'))
            if usuario is not None:
                #Usuário encontrado, agora basta autenticá-lo e redirecioná-lo para a home:
                login_auth(request, usuario)
                return HttpResponse('home.html')
            else:
                #Usuário não encontrado, tomar alguma ação como, por exemplo, redirecioná-lo para a pagina de login novamente:
                return render(request, 'home.html', {'erro': 'Usuário não encontrado'})
        except:
            pass
    else:
        return render(request, 'bands/login_user.html')

@login_required(login_url='/accounts/login/')
def protected_view(request):
    """ A view that can only be accessed by logged-in users """
    return render(request, 'bands/protected.html', {'current_user': request.user})


def message(request):
    """ Message if is not authenticated. Simple view! """
    return HttpResponse('Access denied!')
