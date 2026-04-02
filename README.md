# api-findit-gamified
API  e motor de gamificação para o ecossistema FindIt. Gerencia o inventário de itens, sistema de pontos, conquistas e autenticação de usuários universitários.

Estrutura de Pastas
```text
.
├── /frontend              # Camada de Apresentação (Vue)
│   ├── /public            # Arquivos estáticos
│   └── /src
│       ├── /components    # Componentes reutilizáveis
│       ├── /hooks         # Lógica de Temas (Observer para Dark/Light)
│       └── /services      # Chamadas de API (Consome os DTOs)
