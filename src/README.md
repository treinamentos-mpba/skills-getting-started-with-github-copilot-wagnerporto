# API de Atividades da Mergington High School

Uma aplicação FastAPI super simples que permite que estudantes visualizem e se inscrevam em atividades extracurriculares.

## Funcionalidades

- Visualizar todas as atividades extracurriculares disponíveis
- Visualizar os participantes inscritos em cada atividade
- Inscrever-se em atividades
- Cancelar a inscrição de participantes

## Primeiros Passos

1. Na raiz do projeto, instale as dependências:

   ```sh
   python -m pip install -r requirements.txt
   ```

2. Execute a aplicação:

   ```sh
   python -m uvicorn src.app:app
   ```

3. Abra seu navegador e acesse:
   - Documentação da API: http://localhost:8000/docs
   - Documentação alternativa: http://localhost:8000/redoc

## Testes

Execute os testes de backend a partir da raiz do projeto:

```sh
python -m pytest -q tests/
```

## Endpoints da API

| Método | Endpoint                                                          | Descrição                                                                   |
| ------ | ----------------------------------------------------------------- | --------------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Obtém todas as atividades com seus detalhes e contagem atual de participantes |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Inscreve-se em uma atividade                                                |
| DELETE | `/activities/{activity_name}/signup?email=student@mergington.edu` | Cancela a inscrição de um participante                                      |

## Modelo de Dados

A aplicação usa um modelo de dados simples com identificadores significativos:

1. **Activities** - Usa o nome da atividade como identificador:

   - Descrição
   - Horário
   - Número máximo de participantes permitidos
   - Lista de emails dos estudantes inscritos

2. **Students** - Usa email como identificador:
   - Nome
   - Série/Ano escolar

Todos os dados são armazenados em memória, o que significa que os dados serão resetados quando o servidor reiniciar.
