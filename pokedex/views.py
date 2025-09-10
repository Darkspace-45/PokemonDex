from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
import math, requests
from .models import Pokemon
from .forms import PokemonForm

POKEAPI_BASE = 'https://pokeapi.co/api/v2'
PAGE_SIZE = 20

# ---------------------------
# 🔹 VISTAS EXISTENTES (PokeAPI)
# ---------------------------

def index(request):
    try:
        page = int(request.GET.get('page', '1'))
        if page < 1:
            page = 1
    except ValueError:
        page = 1

    offset = (page - 1) * PAGE_SIZE
    url = f"{POKEAPI_BASE}/pokemon?limit={PAGE_SIZE}&offset={offset}"

    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        return render(request, 'pokedex/index.html', {'error': 'No se pudo obtener la lista de pokemones.'})

    data = resp.json()
    results = data.get('results', [])
    total = data.get('count', 0)
    total_pages = math.ceil(total / PAGE_SIZE)

    pokemons = []
    for r in results:
        name = r['name']
        pokemon_id = r['url'].rstrip('/').split('/')[-1]
        image = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
        pokemons.append({'name': name, 'id': pokemon_id, 'image': image})

    pages = range(1, total_pages + 1)

    context = {
        'pokemons': pokemons,
        'page': page,
        'total_pages': total_pages,
        'pages': pages,
        'page_size': PAGE_SIZE,
    }
    return render(request, 'pokedex/index.html', context)


def pokemon_list(request):
    try:
        page = int(request.GET.get('page', '1'))
        if page < 1:
            page = 1
    except ValueError:
        page = 1

    offset = (page - 1) * PAGE_SIZE
    url = f"{POKEAPI_BASE}/pokemon?limit={PAGE_SIZE}&offset={offset}"

    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        return render(request, 'pokedex/index.html', {'error': 'No se pudo obtener la lista de pokemones.'})

    data = resp.json()
    results = data.get('results', [])
    total = data.get('count', 0)
    total_pages = math.ceil(total / PAGE_SIZE)

    pokemons = []
    for r in results:
        name = r['name']
        pokemon_id = r['url'].rstrip('/').split('/')[-1]
        image = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
        pokemons.append({'name': name, 'id': pokemon_id, 'image': image})

    pages = range(1, total_pages + 1)

    context = {
        'pokemons': pokemons,
        'page': page,
        'total_pages': total_pages,
        'pages': pages,
        'page_size': PAGE_SIZE,
    }
    return render(request, 'pokedex/index.html', context)


def pokemon_detail(request, name):
    url = f"{POKEAPI_BASE}/pokemon/{name.lower()}/"
    resp = requests.get(url, timeout=10)
    if resp.status_code == 404:
        raise Http404('Pokemon no encontrado')
    if resp.status_code != 200:
        return render(request, 'pokedex/detail.html', {'error': 'No se pudo obtener el detalle del pokemon.'})

    data = resp.json()
    pokemon = {
        'name': data.get('name'),
        'id': data.get('id'),
        'base_experience': data.get('base_experience'),
        'height': data.get('height'),
        'weight': data.get('weight'),
        'types': [t['type']['name'] for t in data.get('types', [])],
        'abilities': [a['ability']['name'] for a in data.get('abilities', [])],
        'stats': [{'name': s['stat']['name'], 'base': s['base_stat']} for s in data.get('stats', [])],
        'sprite': data.get('sprites', {}).get('front_default'),
    }

    return render(request, 'pokedex/detail.html', {'pokemon': pokemon})


# ---------------------------
# 🔹 CRUD LOCAL (Base de Datos)
# ---------------------------
def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})

def pokemon_create(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pokedex:pokemon_list')
    else:
        form = PokemonForm()
    return render(request, 'pokedex/pokemon_form.html', {'form': form})

def pokemon_update(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:pokemon_list')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokedex/pokemon_form.html', {'form': form})

def pokemon_delete(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('pokedex:pokemon_list')
    return render(request, 'pokedex/pokemon_confirm_delete.html', {'pokemon': pokemon})
