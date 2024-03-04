# Game Proyecto

Para correr el juego hay que hacer lo siguente en la terminal:

```sh
cd game
python3 main.py
```
# App Proyect


```sh
git clone
cd app 
python3 -m venv env
env\Scripts\activate
pip3 install -r requirements.txt
python3 main.py
deactivate
env\Scripts\desactivate

```

```sh
CMD ["'uvicorn","main:app","--host","0.0.0.0","80'"] este es para algo para fast api recuerda que uvicorn es el coso que te permite correr para escuchar tus apis
CMD bash -c "while true; do sleep 1; done" 
docker-compose build # Para crear el docker
docker-compose up -d # Para lanzarlo
docker-compose ps # Para ver el estado del contenedor
docker-compose exec app-csv bash # Para ingresar al docker y desarrollar ahi
```