# Pequena aplicação em Flask para salvar cortes de imagens

### De base foram utilizado os repositórios
- https://github.com/renantescaro/front-save-piece-image
- https://github.com/renantescaro/flask-estrutura-basica


<br>

## Configurações ⚙️
* arquivo .env
* PATH_IMAGES caminho das imagens de origem
* PATH_CHARACTERS caminho do local de downloads dos cortes das imagens

<br>

## No Windows 🪟
1 - Instalar todas as dependências
```bash
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

2 - Executar
```bash
venv\Scripts\activate.bat
python run.py
```

<br>

## No Linux 🐧
1 - Instalar todas as dependências
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2 - Executar
```bash
source venv/bin/activate
python run.py
```

<br>

## Executar modo dev 🧪
```bash
python -m flask --app flaskr --debug run
```
