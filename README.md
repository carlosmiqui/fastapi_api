# fastapi_api

## Orientações para executar a API

Sugestão de versão do python: 3.10 ou superior

- Crie um ambiente virtual: `python -m venv venv`
- Ative o ambiente virtual (no Windows): `venv\Scripts\activate`
- Ative o ambiente virtual (no Linux): `source venv/bin/activate`
- Instale as bibliotecas: `pip install -r requirements.txt`
- Copie o arquivo `.env.sample` para `.env` e preencha as variáveis de ambiente
- Executar a API em ambiente de desenvolvimento: `fastapi dev main.py`
- Executar a API em ambiente de produção: `fastapi run main.py`


Apresentação: API para Otimização de Conversão em Clínicas Odontológicas com IA

Introdução (1 minuto)
Objetivo: Apresentar uma API desenvolvida para otimizar a conversão de orçamentos em clínicas odontológicas, utilizando Inteligência Artificial para análise de relatos de conversas com clientes e geração de estratégias de comunicação personalizadas.
Contexto: A conversão de orçamentos é um desafio crucial para clínicas odontológicas. A API visa automatizar e aprimorar esse processo, fornecendo insights e estratégias baseadas em dados.
Euquipe: 

Serviços de IA Implementados (2 minutos)

Serviço 1: Análise de Relatos de Conversas
Descrição: Recebe um relato em texto da conversa com o cliente e extrai informações chave como:
Identidade do cliente
Resumo do assunto (ex: cotação de facetas, implantes)
Valor do orçamento
Forma de pagamento
Informações relevantes mencionadas na conversa
Próximo passo agendado (se houver)
Tecnologia: LLM (Large Language Model) da Groq para processamento de linguagem natural e extração de informações.
Endpoint: POST /processar_relato

Serviço 2: Geração de Estratégias de Conversão Personalizadas
Descrição: Utiliza as informações extraídas do relato para gerar uma estratégia de comunicação personalizada para o cliente, incluindo:
Resumo dos interesses e necessidades do cliente
Datas específicas para próximos contatos (ex: 3 dias, 10 dias, 30 dias)
Instruções detalhadas sobre o que dizer e como abordar o cliente em cada contato
Sugestões para personalizar a comunicação
Tecnologia: LLM da Groq para geração de texto e personalização da estratégia.
Endpoint: POST /gerar_estrategia

Demonstração Funcional (3 minutos)
Cenário: Simulação de uma conversa com um cliente interessado em implantes dentários.
Passo 1: Envio do Relato:
Demonstrar o envio de um relato de conversa através do endpoint POST /processar_relato.
Exemplo de relato:
Hoje, 14 de fevereiro de 2025, por volta das 21h23, recebi um contato do Sr. João, um cliente em potencial interessado em melhorar o sorriso através de facetas dentárias. O Sr. João demonstrou grande entusiasmo ao falar sobre a possibilidade de transformar seus dentes e expressou o desejo de obter um orçamento detalhado para o procedimento.
Durante a conversa, expliquei os diferentes tipos de facetas disponíveis, desde as de resina composta até as de porcelana, detalhando os prós e contras de cada material. O Sr. João se mostrou particularmente interessado nas facetas de porcelana devido à sua durabilidade e aparência natural.
Apresentei um orçamento inicial de R$5000, que cobre a avaliação, o planejamento do tratamento e a aplicação das facetas. O Sr. João perguntou sobre as formas de pagamento, e informei que oferecemos a opção de pagamento à vista com um desconto de 10%, ou parcelamento em até 5 vezes no cartão de crédito. Ele pareceu satisfeito com as opções e mencionou que precisaria avaliar qual seria a melhor alternativa para o seu orçamento.
Para resumir, o Sr. João está interessado em realizar o tratamento com facetas, possui um orçamento de aproximadamente R$5000, e está considerando pagar à vista para obter o desconto ou parcelar em 5 vezes. Combinei de entrar em contato novamente em 30 dias para verificar se ele tomou uma decisão e agendar uma avaliação mais detalhada.

String:
Hoje, 14 de fevereiro de 2025, por volta das 21h23, recebi um contato do Sr. João, um cliente em potencial interessado em melhorar o sorriso através de facetas dentárias. O Sr. João demonstrou grande entusiasmo ao falar sobre a possibilidade de transformar seus dentes e expressou o desejo de obter um orçamento detalhado para o procedimento.\n\nDurante a conversa, expliquei os diferentes tipos de facetas disponíveis, desde as de resina composta até as de porcelana, detalhando os prós e contras de cada material. O Sr. João se mostrou particularmente interessado nas facetas de porcelana devido à sua durabilidade e aparência natural.\n\nApresentei um orçamento inicial de R$5000, que cobre a avaliação, o planejamento do tratamento e a aplicação das facetas. O Sr. João perguntou sobre as formas de pagamento, e informei sobre as opções disponíveis. Ele pareceu satisfeito e mencionou que precisaria avaliar qual seria a melhor alternativa para o seu orçamento.\n\nPara resumir, o Sr. João está interessado em realizar o tratamento com facetas, possui um orçamento de aproximadamente R$5000, e está considerando as opções de pagamento. Combinei de entrar em contato novamente em 30 dias para verificar se ele tomou uma decisão e agendar uma avaliação mais detalhada. Dr. Carlos



Informações Organizadas:
Interesse em facetas dentárias.
Orçamento de R$5000.
Pagamento à vista com 10% de desconto ou parcelado em 5x.
Próximo Passo:

Próximo contato em 30 dias para acompanhamento.

Passo 2: Análise e Extração de Informações:
Mostrar o JSON retornado com as informações extraídas:
json
Copiar
{
  "data_conversa": "2025-02-15 10:00:00",
  "identidade_cliente": "João",
  "identidade_atendente": "Assistente",
  "resumo_assunto": "Cotação de implante dentário",
  "valor_orcamento": 3500.00,
  "forma_pagamento": "À vista ou parcelado",
  "informacoes_organizadas": [
    "Interesse em implante dentário",
    "Orçamento de R$3500",
    "Pagamento à vista ou parcelado em 12x"
  ],
  "instrucoes_proximo_passo": "Retornar o contato em 7 dias"
}
Passo 3: Geração da Estratégia de Conversão:
Enviar o JSON extraído para o endpoint POST /gerar_estrategia.
Mostrar a estratégia de conversão gerada:
json
Copiar
{
  "estrategia": "Estratégia de conversão para João:\n\nResumo dos interesses: João demonstrou interesse em um implante dentário com orçamento de R$3500, com opções de pagamento à vista ou parcelado em 12x.\n\nDatas e instruções para os próximos contatos:\n\nPrimeiro contato (2025-02-18):\nLigar para João e perguntar se ele teve alguma dúvida sobre o orçamento e se podemos ajudá-lo a tomar uma decisão. Reforçar os benefícios do implante e a qualidade dos nossos serviços.\n\nSegundo contato (2025-02-25):\nEnviar uma mensagem para João, oferecendo um desconto especial para fechamento do implante nesta semana. Destacar a importância de agendar uma avaliação para garantir o melhor resultado.\n\nTerceiro contato (2025-03-17):\nCaso João ainda não tenha agendado, ligar novamente e oferecer um parcelamento diferenciado ou algum benefício adicional para incentivá-lo a marcar a consulta. Mostrar disponibilidade para esclarecer qualquer receio.\n\nPersonalização da comunicação:\nUtilizar uma linguagem amigável e atenciosa, mostrando empatia com as necessidades de João. Adaptar a abordagem de acordo com as respostas dele, buscando sempre oferecer soluções personalizadas e flexíveis."
}
{
  "estrategia": "
Estratégia de conversão para João:\n\n
Resumo dos interesses: João demonstrou interesse em um implante dentário com orçamento de R$3500, com opções de pagamento à vista ou parcelado em 12x.\n\n
Datas e instruções para os próximos contatos:\n\n
Primeiro contato (2025-02-18):\nLigar para João e perguntar se ele teve alguma dúvida sobre o orçamento e se podemos ajudá-lo a tomar uma decisão. Reforçar os benefícios do implante e a qualidade dos nossos serviços.\n\n
Segundo contato (2025-02-25):\nEnviar uma mensagem para João, oferecendo um desconto especial para fechamento do implante nesta semana. Destacar a importância de agendar uma avaliação para garantir o melhor resultado.\n\n
Terceiro contato (2025-03-17):\nCaso João ainda não tenha agendado, ligar novamente e oferecer um parcelamento diferenciado ou algum benefício adicional para incentivá-lo a marcar a consulta. Mostrar disponibilidade para esclarecer qualquer receio.\n\n
Personalização da comunicação:\n
Utilizar uma linguagem amigável e atenciosa, mostrando empatia com as necessidades de João. Adaptar a abordagem de acordo com as respostas dele, buscando sempre oferecer soluções personalizadas e flexíveis."
}

Conclusão: Demonstrar como a assistente pode utilizar a estratégia para otimizar o contato com o cliente.

Características Técnicas da Solução (3 minutos)

Framework: FastAPI
Motivação: Escolha devido à sua alta performance, facilidade de uso, validação de dados integrada e geração automática de documentação (Swagger).
Validação de Dados: Pydantic para garantir a integridade dos dados recebidos e enviados pela API.
Exemplo: Validação do formato da data, tipos de dados dos campos, etc.
Tratamento de Erros:
Implementação de HTTPException para retornar erros HTTP adequados em caso de falhas.
Logs detalhados para facilitar a identificação e correção de problemas.
Logs:
Utilização do módulo logging para registrar informações relevantes sobre o funcionamento da API.
Logs de entrada e saída de dados, erros, etc.
Segurança:
Autenticação via token (API_TOKEN) para proteger os endpoints.
CORS (Cross-Origin Resource Sharing) configurado para permitir acesso controlado à API.
Versionamento:
A API está na versão 1.0.0.
Em caso de novas funcionalidades ou mudanças significativas, o versionamento será atualizado (ex: 1.1.0, 2.0.0).
Código:
Modularização do código em arquivos routers, utils e models para melhor organização e manutenção.
Utilização de funções assíncronas (async def) para otimizar a performance da API.
Repositório GitHub: [Link para o Repositório]
Inclui instruções detalhadas para executar a API em outro computador.

Conclusão (1 minuto)

Benefícios da API:
Automatização do processo de análise de relatos e geração de estratégias.
Personalização da comunicação com os clientes.
Otimização da conversão de orçamentos.
Redução do tempo gasto pela assistente na criação de estratégias.

Próximos Passos:
Implementação de testes automatizados.
Integração com outras ferramentas de CRM.
Aprimoramento contínuo das estratégias de conversão com base em dados e feedback.



Características Técnicas Detalhadas da Solução
Esta seção detalha as características técnicas da API para otimização de conversão em clínicas odontológicas, abordando as decisões de design, tecnologias utilizadas e considerações de segurança.
1. Arquitetura e Design
•	Arquitetura: A API segue uma arquitetura modular, com separação clara de responsabilidades entre os componentes. Isso facilita a manutenção, escalabilidade e testabilidade do sistema.
•	Design: A API adota princípios RESTful, utilizando verbos HTTP (POST) para operações de criação e processamento. Os endpoints são nomeados de forma intuitiva e consistente.
•	Modularização: O código é organizado em três módulos principais:
o	routers: Contém os endpoints da API, definindo a lógica de roteamento e validação de dados.
o	utils: Implementa funções utilitárias, como a comunicação com a LLM, o processamento de relatos e a geração de estratégias.
o	models: Define os modelos de dados utilizados na API, garantindo a consistência e a validação dos dados.
2. Tecnologias Utilizadas
Framework: FastAPI
o	Motivação: Escolhido por sua alta performance, tipagem estática, validação de dados integrada (Pydantic), geração automática de documentação (Swagger/ReDoc) e facilidade de uso.
o	Performance: FastAPI é construído sobre Starlette e Uvicorn, o que garante alta performance e escalabilidade.
o	Tipagem Estática: A tipagem estática do Python (com mypy) ajuda a prevenir erros em tempo de desenvolvimento e melhora a legibilidade do código.
o	Documentação: A geração automática de documentação facilita o uso da API por outros desenvolvedores e a criação de interfaces de usuário.
LLM (Large Language Model): Groq
o	Motivação: Escolhido por sua capacidade de processamento de linguagem natural e geração de texto.
o	Processamento de Linguagem Natural (NLP): A LLM é utilizada para extrair informações relevantes de relatos de conversas e para gerar estratégias de comunicação personalizadas.
o	Geração de Texto: A LLM é utilizada para gerar textos claros, objetivos e persuasivos, adaptados às necessidades de cada cliente.
Pydantic:
o	Motivação: Utilizado para definir os modelos de dados da API, garantindo a validação e a consistência dos dados.
o	Validação de Dados: Pydantic permite definir regras de validação para cada campo dos modelos de dados, como tipos de dados, formatos, tamanhos, etc.
o	Serialização e Desserialização: Pydantic facilita a serialização de objetos Python em JSON e a desserialização de JSON em objetos Python.
Logging:
o	Motivação: Utilizado para registrar informações relevantes sobre o funcionamento da API, facilitando a identificação e correção de problemas.
o	Níveis de Log: A API utiliza diferentes níveis de log (DEBUG, INFO, WARNING, ERROR, CRITICAL) para registrar informações de diferentes gravidades.
o	Formato de Log: O formato de log inclui a data e hora, o nível de log e a mensagem.
CORS (Cross-Origin Resource Sharing):
o	Motivação: Utilizado para permitir acesso controlado à API a partir de diferentes origens (domínios).
o	Configuração: A API está configurada para permitir acesso a partir de todas as origens (allow_origins=["*"]), o que é útil para desenvolvimento. Em produção, é recomendado restringir o acesso a origens específicas.
Uvicorn:
o	Motivação: Servidor ASGI (Asynchronous Server Gateway Interface) de alta performance para executar a API.
o	Desempenho: Uvicorn é construído sobre uvloop e httptools, o que garante alta performance e escalabilidade.
uvloop:
o	Motivação: Implementação de event loop para asyncio mais rápida que a implementação padrão do Python.
o	Integração: Uvicorn utiliza uvloop por padrão, o que melhora o desempenho da API.
httptools:
o	Motivação: Parser HTTP de alta performance para Python.
o	Integração: Uvicorn utiliza httptools para processar requisições HTTP de forma eficiente.
3. Requisitos Básicos Implementados
Validação de Dados:
o	Utilização de Pydantic para validar os dados recebidos e enviados pela API.
o	Validação de tipos de dados, formatos, tamanhos, etc.
o	Retorno de erros HTTP adequados em caso de falhas de validação.
Tratamento de Erros:
o	Utilização de HTTPException para retornar erros HTTP adequados em caso de falhas.
o	Logs detalhados para facilitar a identificação e correção de problemas.
o	Tratamento de exceções específicas para diferentes cenários.
Logs:
o	Utilização do módulo logging para registrar informações relevantes sobre o funcionamento da API.
o	Logs de entrada e saída de dados, erros, etc.
o	Configuração de níveis de log para controlar a quantidade de informações registradas.
Segurança:
o	Autenticação via token (API_TOKEN) para proteger os endpoints.
o	CORS (Cross-Origin Resource Sharing) configurado para permitir acesso controlado à API.
Versionamento:
o	A API está na versão 1.0.0.
o	Em caso de novas funcionalidades ou mudanças significativas, o versionamento será atualizado (ex: 1.1.0, 2.0.0).
4. Considerações de Segurança
Autenticação:
o	A API utiliza um token de autenticação simples (API_TOKEN) para proteger os endpoints.
o	Em produção, é recomendado utilizar um sistema de autenticação mais robusto, como OAuth 2.0 ou JWT (JSON Web Tokens).
Autorização:
o	A API não implementa autorização, o que significa que todos os usuários autenticados têm acesso a todos os recursos.
o	Em produção, é recomendado implementar autorização para controlar o acesso a recursos específicos.
Proteção contra Ataques:
o	A API não implementa proteção contra ataques como SQL Injection, Cross-Site Scripting (XSS) e Cross-Site Request Forgery (CSRF).
o	Em produção, é recomendado implementar medidas de proteção contra esses ataques.
CORS:
o	A API está configurada para permitir acesso a partir de todas as origens (allow_origins=["*"]), o que é útil para desenvolvimento.
o	Em produção, é recomendado restringir o acesso a origens específicas para evitar ataques CSRF.
5. Escalabilidade
•	Arquitetura: A arquitetura modular da API facilita a escalabilidade horizontal, permitindo que novos servidores sejam adicionados para lidar com o aumento da carga.
•	Tecnologias: FastAPI, Uvicorn e uvloop são tecnologias de alta performance que permitem que a API lide com um grande número de requisições simultâneas.
•	Cache: A API não implementa cache, o que pode ser um gargalo em cenários de alta carga.
o	Em produção, é recomendado implementar cache para reduzir a carga no servidor e melhorar o desempenho da API.
6. Testabilidade
•	Modularização: A modularização do código facilita a testabilidade, permitindo que cada componente seja testado individualmente.
•	Testes Unitários: A API não implementa testes unitários, o que dificulta a identificação e correção de problemas.
o	Em produção, é recomendado implementar testes unitários para garantir a qualidade do código.
•	Testes de Integração: A API não implementa testes de integração, o que dificulta a verificação da interação entre os diferentes componentes.
o	Em produção, é recomendado implementar testes de integração para garantir que os diferentes componentes funcionem corretamente juntos.
7. Documentação
•	Geração Automática: FastAPI gera automaticamente a documentação da API (Swagger/ReDoc), o que facilita o uso da API por outros desenvolvedores.
•	Descrição dos Endpoints: A documentação inclui a descrição dos endpoints, os parâmetros de entrada e saída, os códigos de erro e exemplos de uso.
•	Modelos de Dados: A documentação inclui a definição dos modelos de dados utilizados na API, com a descrição de cada campo e suas regras de validação.

Perguntas Técnicas Comuns
Como a API lida com a autenticação e autorização?
o	A API utiliza um token de autenticação simples (API_TOKEN) para proteger os endpoints. Em produção, é recomendado utilizar um sistema de autenticação mais robusto, como OAuth 2.0 ou JWT (JSON Web Tokens). A API não implementa autorização, o que significa que todos os usuários autenticados têm acesso a todos os recursos. Em produção, é recomendado implementar autorização para controlar o acesso a recursos específicos.
o	
Como a API lida com a validação de dados?
o	A API utiliza Pydantic para validar os dados recebidos e enviados pela API. Pydantic permite definir regras de validação para cada campo dos modelos de dados, como tipos de dados, formatos, tamanhos, etc. Em caso de falhas de validação, a API retorna erros HTTP adequados.
o	
Como a API lida com o tratamento de erros?
o	A API utiliza HTTPException para retornar erros HTTP adequados em caso de falhas. A API também implementa logs detalhados para facilitar a identificação e correção de problemas. A API também implementa tratamento de exceções específicas para diferentes cenários.
o	
Como a API lida com a escalabilidade?
o	A arquitetura modular da API facilita a escalabilidade horizontal, permitindo que novos servidores sejam adicionados para lidar com o aumento da carga. FastAPI, Uvicorn e uvloop são tecnologias de alta performance que permitem que a API lide com um grande número de requisições simultâneas.
o	
Como a API lida com a testabilidade?
o	A modularização do código facilita a testabilidade, permitindo que cada componente seja testado individualmente. No entanto, a API não implementa testes unitários ou de integração, o que dificulta a identificação e correção de problemas. Em produção, é recomendado implementar testes unitários e de integração para garantir a qualidade do código.
o	
Como a API lida com a documentação?
o	FastAPI gera automaticamente a documentação da API (Swagger/ReDoc), o que facilita o uso da API por outros desenvolvedores. A documentação inclui a descrição dos endpoints, os parâmetros de entrada e saída, os códigos de erro e exemplos de uso. A documentação também inclui a definição dos modelos de dados utilizados na API, com a descrição de cada campo e suas regras de validação.
o	
Quais medidas de segurança foram implementadas na API?
o	A API utiliza um token de autenticação simples (API_TOKEN) para proteger os endpoints. A API também utiliza CORS (Cross-Origin Resource Sharing) para permitir acesso controlado à API a partir de diferentes origens (domínios). No entanto, a API não implementa proteção contra ataques como SQL Injection, Cross-Site Scripting (XSS) e Cross-Site Request Forgery (CSRF). Em produção, é recomendado implementar medidas de proteção contra esses ataques.
o	
Como a API interage com a LLM?
o	A API utiliza a LLM da Groq para processamento de linguagem natural e geração de texto. A API envia prompts para a LLM e recebe as respostas, que são processadas e retornadas aos clientes. A API utiliza a biblioteca groq-python para se comunicar com a API da Groq.
o	
Como a API lida com o versionamento?
o	A API está na versão 1.0.0. Em caso de novas funcionalidades ou mudanças significativas, o versionamento será atualizado (ex: 1.1.0, 2.0.0). O versionamento é importante para garantir a compatibilidade com clientes existentes e para facilitar a atualização da API.
o	
Quais são os próximos passos para o desenvolvimento da API?
o	Implementação de testes automatizados.
o	Integração com outras ferramentas de CRM.
o	Aprimoramento contínuo das estratégias de conversão com base em dados e feedback.
o	Implementação de um sistema de autenticação mais robusto (ex: OAuth 2.0 ou JWT).
o	Implementação de autorização para controlar o acesso a recursos específicos.
o	Implementação de medidas de proteção contra ataques como SQL Injection, Cross-Site Scripting (XSS) e Cross-Site Request Forgery (CSRF).
o	Implementação de cache para reduzir a carga no servidor e melhorar o desempenho da API.

