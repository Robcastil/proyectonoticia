from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from noticias.models import Fuente, Titular
import datetime as dt
from dateutil.parser import *

#noticias de Mashable
mash = Fuente()
mash.nombre = 'Mashable'
mash.url = 'https://mashable.com/feeds/rss/all'
mash.save()
Mash_req = requests.get(mash.url)
soup = BeautifulSoup(Mash_req.content,'xml')
noticias = soup.findAll('item')

for n in noticias:
    titular = Titular()
    titular.fuente = mash
    titular.titulo = n.find('title').text
    titular.url = n.find('link').text
    titular.fecha = parse(n.find('pubDate').text)
    titular.save()
        
    
    
#noticias de The Verge
verg = Fuente()
verg.nombre = 'The Verge'
verg.url = 'https://www.theverge.com/rss/index.xml'
verg.save()
Verge_req = requests.get(verg.url)
soup = BeautifulSoup(Verge_req.content, 'xml')
noticias = soup.findAll('entry')

for n in noticias:
    titular = Titular()
    titular.fuente = verg
    titular.titulo = n.find('title').text
    titular.url = n.find('id').text
    titular.fecha = parse(n.find('published').text)
    titular.save()


#noticias de TechCrunch
techCr = Fuente()
techCr.nombre = 'TechCrunch'
techCr.url = 'https://techcrunch.com/feed/'
techCr.save()
TC_req = requests.get(techCr.url)
soup = BeautifulSoup(TC_req.content, 'xml')
noticias = soup.findAll('item')

for n in noticias:
    titular = Titular()
    titular.fuente = techCr
    titular.titulo = n.find('title').text
    titular.url = n.find('link').text
    titular.fecha = parse(n.find('pubDate').text)
    titular.save()
    

def index(req):
    t_mash = Titular.objects.filter(fuente__nombre='Mashable')[::-1][0:10]
    t_mash = [t.titulo for t in t_mash]    
    t_verge = Titular.objects.filter(fuente__nombre='The Verge')[::-1][0:10]
    t_verge = [t.titulo for t in t_verge]
    t_TC = Titular.objects.filter(fuente__nombre='TechCrunch')[::-1][0:10]
    t_TC = [t.titulo for t in t_TC]
    return render(req, 'noticias/index.html', {'t_mash': t_mash, 't_verge': t_verge, 't_TC': t_TC})

def rescatar(req):
    return redirect('../')
# Create your views here.
