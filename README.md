# Gestão de Ciclo de vida dos produtos

## Descrição do Projeto

O projeto é uma aplicação web desenvolvida com Flask que fornece informações detalhadas sobre embalagens e seus impactos ambientais, permitindo a visualização e filtragem dos dados com base em critérios específicos. Os usuários podem explorar informações como emissão de carbono, consumo de água, uso de energia e tempo de decomposição para cada tipo de embalagem. O objetivo é facilitar o acesso a dados ambientais, promovendo a conscientização sobre o impacto dos materiais e métodos de produção utilizados

## Funcionalidades
- Análise de Impacto Ambiental
- Simulação de Cenários Sustentáveis
- Controle de Materiais e Sustentabilidade
- Relatórios de Ciclo de Vida
- Sugestões de Melhoria e Redução de Impacto

## Tecnologias Usadas
- **Python**: Linguagem de programação usada para construir o backend.
- **FLASK**: Framework web usado para construir o servidor e o gerenciamento de dados.
- **Bootstrap**: Framework de front-end usado para criar uma interface de usuário responsiva e estilizada.
- **HTML/CSS**: Linguagens de marcação e estilo usadas para construir e estilizar a interface do usuário.

## Como Configurar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1. **Clone o Repositório**
- Usando HTTPS:
```bash
git clone https://github.com/htadmg/ciclo_de_vida_produtos.git
```
- Usando SSH:
```bash
git clone git@github.com:htadmg/ciclo_de_vida_produtos.git
```
- Navegue até o diretório do projeto:
```bash
cd .\ciclo_de_vida_produtos
```
2. **Crie e Ative um Ambiente Virtual (opcional, mas recomendado)**
- **Para Linux/MacOS:**
```bash
python -m .venv venv
source .venv/bin/activate
```

- **Para Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

### Iniciar o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento com o comando:

```bash
python app.py
```
### Acessar o Projeto
Abra um navegador e vá para http://127.0.0.1:5000/ para ver o aplicativo em funcionamento.
