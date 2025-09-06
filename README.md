Django Pokédex (PokeAPI)

Instrucciones rápidas:
1. python -m venv .venv
2. source .venv/bin/activate   (Windows: .venv\Scripts\activate)
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver
6. Abrir http://127.0.0.1:8000/ en el navegador

Rutas:
- / -> lista paginada de pokemones (parámetro ?page=)
- /pokemon/<name>/ -> detalle del pokemon
