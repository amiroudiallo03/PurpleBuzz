from django.shortcuts import render,redirect,get_object_or_404
from . import models
from service import models as models_service
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    banners = models.BannerHome.objects.filter(status= True).all()
    websites = models.Website.objects.filter(status= True).first()
    cards = models_service.Card.objects.filter().all()
    categories = models_service.Categorie.objects.filter().all()
    icones = models.Icone.objects.filter().all()
    services = models.Service.objects.filter().first()
    reseaux = models.ReseauSociaux.objects.all()
    return render(request, 'index.html', locals())




def about(request):
    websites = models.Website.objects.filter(status= True).first()
    abouts = models.About.objects.filter().first()
    teams = models.Team.objects.filter().all()
    partners = models.Partner.objects.filter().all()
    creatives = models.Creative.objects.filter().first()
    progress = models.Progress.objects.filter().all()
    aboutchoices = models.AboutChoice.objects.filter().first()
    cardabouts = models.CardAbout.objects.filter().all()
    return render(request, 'about.html', locals())




def contact(request):
    return render(request, 'contact.html')




def pricing(request):
    websites = models.Website.objects.filter(status= True).first()
    pricings = models_service.Pricing.objects.filter().first()
    return render(request, 'pricing.html', locals())




def work(request):
    page = request.GET.get('page')
    page = page if page else 1
    websites = models.Website.objects.filter(status= True).first()
    bannerworks = models_service.BannerWork.objects.filter().first()
    categorieworks = models_service.CategorieWork.objects.all()
    works = models_service.Work.objects.all()
    futuredwork = models_service.FuturedWork.objects.filter().first()
    news = models_service.Image.objects.filter().order_by('-date_add')[:4]
    paginator = Paginator(works,3)
    try:
        works_list = paginator.page(page)
    except PageNotAnInteger:
        works_list = paginator.page(1)
    except EmptyPage:
        works_list = paginator.page(paginator.num_pages)
    worksid = get_object_or_404(models_service.Work, id=id)
    return render(request, 'work.html', locals())


def work_single(request):
    return render(request, 'work-single.html')


def NewsletterPost(request):
    NewMail = request.POST.get("email")
    New = models.Newsletter()
    New.email = NewMail
    New.save()
    retour = request.META.get("HTTP_REFERER")
    return redirect(retour, "/")