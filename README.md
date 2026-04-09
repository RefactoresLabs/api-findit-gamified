# api-findit-gamified
API  e motor de gamificação para o ecossistema FindIt. Gerencia o inventário de itens, sistema de pontos, conquistas e autenticação de usuários universitários.

Estrutura de Pastas
```text
backend/
│
├── app/
│   │
│   ├── presentation/                 # Camada de apresentação (API REST)
│   │   ├── controllers/              # Controladores que recebem requisições HTTP e chamam os serviços da aplicação
│   │   ├── routes/                   # Definição das rotas/endpoints da API
│   │   ├── schemas/                  # Modelos de entrada e saída da API (validação e serialização - ex: Pydantic)
│   │
│   ├── application/                  # Camada de aplicação (casos de uso do sistema)
│   │   ├── services/                 # Implementação dos casos de uso e orquestração das regras de negócio
│   │   ├── dto/                      # Objetos de transferência de dados entre apresentação e domínio
│   │
│   ├── domain/                       # Núcleo do sistema (regras de negócio independentes de tecnologia)
│   │   ├── entities/                 # Entidades principais do sistema (Usuário, Item, Pedido de Devolução)
│   │   ├── value_objects/            # Objetos de valor imutáveis (Endereço, Coordenadas, Categoria)
│   │   ├── repositories/             # Interfaces de repositório (contratos de persistência)
│   │   ├── strategies/               # Implementações do padrão Strategy (ex: ordenação de itens)
│   │   ├── specifications/           # Implementações do padrão Specification (filtros e critérios de busca)
│   │   ├── states/                   # Implementações do padrão State (estados do pedido de devolução)
│   │   ├── observers/                # Implementações do padrão Observer (eventos e pontuação)
│   │   ├── enums/                    # Enumerações do domínio (ex: status, categorias)
│   │   ├── exceptions/               # Exceções específicas do domínio
│   │
│   ├── infrastructure/               # Camada de infraestrutura (detalhes técnicos e externos)
│   │   ├── persistence/
│   │   │   ├── models/               # Modelos do banco de dados (ORM)
│   │   │   ├── repositories/         # Implementações concretas dos repositórios
│   │   │
│   │   ├── external/
│   │   │   ├── maps/                 # Integração com APIs externas (Adapter Pattern - ex: geolocalização)
│   │   │
│   │   ├── security/                 # Serviços de segurança (hash de senha, autenticação, criptografia)
│   │   ├── storage/                  # Manipulação de arquivos (upload e armazenamento de imagens)
│   │   ├── config/                   # Configurações da aplicação (banco, variáveis de ambiente)
│   │
│   ├── shared/                       # Código compartilhado entre camadas
│   │   ├── utils/                    # Funções utilitárias
│   │   ├── validators/               # Validações genéricas reutilizáveis
│   │   ├── constants/                # Constantes globais do sistema
│   │
│   ├── main.py                       # Ponto de entrada da aplicação (inicialização do servidor)

