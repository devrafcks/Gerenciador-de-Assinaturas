# Sistema de Gerenciamento de Assinaturas



Esse projeto foi para o evento python week returnal de 2025 onde utilizei Python, SQL e frameworks como o `SQLModel`. A ideia era construir um sistema simples, mas completo, para gerenciar assinaturas mensais, com funcionalidades que envolvem desde o cadastro de novas assinaturas até a geração de relatórios financeiros, com gráficos dos gastos dos últimos 12 meses.

## O que aprendi e pratiquei durante o desenvolvimento

### 1. **Trabalhando com Banco de Dados usando SQLModel**

Uma das maiores vitórias desse projeto foi aprender e usar o `SQLModel`, uma ferramenta que combina o poder do SQLAlchemy com a simplicidade do Pydantic. Isso me ajudou bastante na hora de estruturar o banco de dados do sistema. Aqui, pude:
- **Criar e Organizar as Tabelas**: Definir e criar as tabelas `Subscription` e `Payments` no banco de dados.
- **Relacionar Tabelas**: Como em sistemas reais, as assinaturas precisam estar relacionadas aos pagamentos. Isso me fez entender melhor como usar o `SQLModel` para criar esses vínculos entre as tabelas e garantir que o sistema estivesse bem estruturado.
- **Operações de Banco de Dados (CRUD)**: Aprendi a realizar operações como adicionar, deletar e modificar dados diretamente no banco. O mais interessante foi conseguir fazer isso de forma muito mais fácil do que imaginava, sem precisar escrever SQL manualmente.

### 2. **Lógica de Negócio e Validação de Dados**

A lógica de negócios foi onde realmente testei minhas habilidades. Implementar validações e garantir que o sistema fosse robusto foi um processo interessante:
- **Validação de Data e Valor**: Quando o usuário adiciona uma nova assinatura, tive que me preocupar em garantir que os dados fossem válidos, como o formato correto da data e o valor correto da assinatura.
- **Evitar Pagamentos Duplicados**: Outro ponto crucial foi garantir que um pagamento não fosse registrado mais de uma vez no mesmo mês. Isso me desafiou a criar uma lógica de verificação antes de permitir o pagamento, o que foi um exercício ótimo para reforçar meus conhecimentos em controle de dados.
- **Tratamento de Erros**: Enfrentei alguns desafios de entrada de dados, como números e datas, mas logo encontrei soluções para validar tudo antes de registrar.

### 3. **Interface de Linha de Comando (CLI)**

Criar a interface de linha de comando foi uma das partes mais divertidas. Eu queria algo simples e intuitivo para que o usuário pudesse navegar pelas opções facilmente:
- **Menu Interativo**: Criei um menu que permite ao usuário escolher entre as opções de adicionar, remover ou pagar assinaturas, e até mesmo gerar relatórios.
- **Entrada de Dados**: Utilizei o `input()` para coletar informações do usuário, como o nome da empresa, o valor da assinatura e a data de vencimento, tudo com validações para garantir que a entrada fosse no formato certo.
- **Fluxo de Navegação**: A interface funciona de forma fluida, com o usuário podendo realizar várias ações seguidas, sem complicação.

### 4. **Gerando Relatórios com Matplotlib**

Uma das funcionalidades mais legais foi gerar gráficos para visualizar os gastos com as assinaturas. Aqui, aprendi como usar a biblioteca `matplotlib` para criar gráficos de linha que mostram os totais pagos por mês. Isso envolveu:
- **Manipulação de Datas**: Usei `datetime` para organizar os dados dos últimos 12 meses e gerar as visualizações corretas.
- **Gráfico de Gastos**: A partir desses dados, consegui criar um gráfico simples, mas que oferece uma visão clara dos gastos ao longo do tempo. Foi um excelente exercício de como trabalhar com dados e apresentar informações visualmente.

### 5. **Organização do Código**

Outro aprendizado importante foi como organizar o código de forma limpa e modular. Separei o projeto em diferentes arquivos, o que me ajudou a manter tudo mais organizado e fácil de entender:
- **Modelos de Dados**: Em `models/model.py`, coloquei toda a parte de definição das tabelas e relacionamentos.
- **Lógica de Negócio**: A classe `SubscriptionService` ficou responsável por toda a lógica de manipulação das assinaturas, como criação, exclusão e listagem.
- **Interface de Usuário**: Em `views/view.py`, criei a interface que interage diretamente com o usuário, tornando o processo de navegação fácil e direto.

### 6. **Desafios e Como Resolvi**

Esse projeto não foi fácil, e enfrentei vários desafios que me ajudaram a crescer como desenvolvedor:
- **Gerenciamento de Conexões com o Banco**: No início, tive dificuldade em entender como lidar com a sessão do banco de dados e garantir que não houvesse problemas de concorrência ou dados duplicados. Mas com o tempo, aprendi a usar o `SQLModel` para gerenciar isso de forma eficiente.
- **Validação de Entradas**: Uma das maiores dificuldades foi garantir que todas as entradas do usuário fossem válidas. Depois de alguns testes e erros, consegui implementar validações robustas para garantir que os dados estivessem corretos antes de serem processados.
- **Evitar Pagamentos Duplicados**: Esse foi um dos problemas mais complicados, mas também o mais gratificante de resolver. A lógica que criei para verificar e evitar pagamentos duplicados ajudou a garantir que os dados do sistema fossem consistentes.

## Conclusão

Esse projeto foi uma experiência de aprendizado incrível. Consegui aplicar muitos conceitos que aprendi durante os cursos e também me desafiei a aprender coisas novas, como trabalhar com o `SQLModel`, gerar gráficos com `matplotlib` e construir uma interface de linha de comando. Senti que cresci muito como desenvolvedor durante o processo.

