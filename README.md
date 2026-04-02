# api-findit-gamified
API  e motor de gamificação para o ecossistema FindIt. Gerencia o inventário de itens, sistema de pontos, conquistas e autenticação de usuários universitários.

Estrutura de Pastas
```text
.
├── /backend               # Camada de Lógica e Dados (Python)
   ├── /src
      ├── /api           # Controllers (Entrada da API e Autenticação)
      │   └── /dtos      # Objetos de Transferência de Dados
      │
      ├── /core          # Regras de Negócio
      │   ├── /entities  # Modelos de domínio (Item, Usuário)
      │   ├── /factories # Factory Pattern (Criação de tipos de itens)
      │   └── /services  # Lógica principal e Observers
      │
      ├── /infrastructure # Detalhes técnicos e ferramentas
      │   ├── /auth      # Implementação da Autenticação Básica
      │   ├── /security  # SHA-3 Adapter (Isolamento da criptografia)
      │   └── /storage   # Lógica de upload (Imagens 10MB)
      │
      ├── /repositories  # Repository Pattern (Interface com o Banco)
      │
      └── /utils # Diretório dedicado a armazenar funções, classes ou métodos auxiliares que realizam tarefas genéricas, repetitivas e de suporte técnico.
   
   
