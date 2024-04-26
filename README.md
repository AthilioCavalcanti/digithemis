# ⚖️ Digithemis
>🐍 Desafio Python de 1° Ciclo - Alpha EdTech

![image](https://github.com/AthilioCavalcanti/digithemis/assets/106356096/49f14dcf-3b31-450c-8d00-30402a4278e7)

> É uma ferramenta de gestão para advogados, projetada para simplificar o processo de transição de um acervo físico de documentos para o digital, organização e acompanhamento de processos legais.\
Utilizando tecnologias como OCR e GED, permite o cadastro e busca de clientes, inserção de processos e atribuição automática de documentos, agilizando o fluxo de trabalho jurídico.

## Sumário
- [Ajustes e Melhorias](#-ajustes-e-melhorias)
- [Funcionalidades](#-funcionalidades)
- [Boas Práticas](#-boas-práticas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Colaboradores](#-colaboradores)

## 🔧 Ajustes e Melhorias

> O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [x] Atribuição automática de Documentos
- [x] Gestão de Documentos
- [x] Busca de Clientes
- [ ] Cadastro automático
- [ ] Recursos de Administração

## ⚙️ Funcionalidades

### Login e Registro de Usuário
- **Login:** Permite que usuários registrados acessem suas contas fornecendo suas credenciais.
- **Registro:** Novos usuários podem ser registrados através de usuários administradores fornecendo informações como nome, e-mail, senha, OAB, CPF, telefone.

### Tela de Menu
- **Menu Principal:** Após o login, os usuários são direcionados para a tela de menu, onde podem acessar todas as funcionalidades disponíveis.

### Tela de Busca
- **Busca de Clientes:** Permite aos usuários pesquisar clientes e seus processos ou documentos associados.

### Tela de Cadastro de Usuário
- **Cadastro de Novos Usuários:** A partir da tela de administração, os administradores podem cadastrar novos usuários no sistema.

### Cadastro de Cliente
- **Registro de Novos Clientes:** Os usuários podem adicionar novos clientes ao sistema, fornecendo informações como nome, CPF/CNPJ, endereço, etc.

### Outras Funcionalidades
- **Inserir Processo:** Capacidade de gerar relatórios personalizados sobre clientes, processos ou documentos.
- **Editar Perfil do Usuário:** Visando a necessidade de algumas alterações estarem disponíveis para o usuário, deixamos à disposição a possibilidade de alterar nome, OAB, telefone, e-mail, senha.
- **Perfil Advogado:** Uma página de perfil personalizada para cada advogado com suas informações e estatísticas relevantes.
- **Esqueci a Senha:** Funcionalidade para recuperar a senha através do envio de um e-mail de redefinição de senha.

## 👍 Boas Práticas

> Para uma experiência suave e colaborativa ao utilizar o Digithemis, recomendamos seguir algumas boas práticas:

- **Leia o README:** Antes de começar a utilizar o projeto, leia cuidadosamente o arquivo README. Ele contém informações importantes sobre a instalação, configuração, uso e contribuição.

- **Siga as instruções:** Siga as instruções de instalação e configuração fornecidas no README para configurar o projeto corretamente em seu ambiente.

- **Respeite as diretrizes:** Utilize o projeto de acordo com as diretrizes de uso e licença fornecidas. Respeite os direitos autorais e as políticas de uso.

- **Forneça feedback:** Se encontrar problemas, bugs ou tiver sugestões de melhoria, sinta-se à vontade para fornecer feedback. Abra uma issue detalhando o problema ou a sugestão.

## 💻 Pré-requisitos
- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- [PostgreSQL](https://www.postgresql.org/)
- [Poetry](https://python-poetry.org/)
- [Tesseract](https://github.com/tesseract-ocr/tesseract)
- [Poppler](https://pypi.org/project/python-poppler/)
- [PDF2Image](https://pypi.org/project/pdf2image/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [DOTENV](https://pypi.org/project/python-dotenv/)
- [Bcrypt](https://pypi.org/project/bcrypt/)

## 📥 Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/Digithemis.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd Digithemis
    ```
3. Instale as dependências utilizando o Poetry:
    ```sh
    poetry install
    ```

## 🤝 Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LucasDiego071" title="Lucas Diego">
        <img src="https://github.com/AthilioCavalcanti/digithemis/assets/106356096/688baaa7-aa59-40ef-835c-ee8670d0bb18" width="100px;" alt="Foto de Lucas Diego"/><br>
        <sub>
          <b>Lucas Diego</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/AthilioCavalcanti" title="Athílio Cavalcanti">
        <img src="https://github.com/AthilioCavalcanti/digithemis/assets/106356096/85ca663b-a866-44a1-ace4-fd6057645d83" width="100px;" alt="Foto de Athílio Cavalcanti"/><br>
        <sub>
          <b>Athílio Cavalcanti</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/CarlosMoura88" title="Carlos Moura">
        <img src="https://github.com/AthilioCavalcanti/digithemis/assets/106356096/96f6fe46-0708-4878-aadf-7e81d88e381f" width="100px;" alt="Foto de Carlos Moura"/><br>
        <sub>
          <b>Carlos Moura</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/KADS223" title="Kennendh Silva">
        <img src="https://github.com/AthilioCavalcanti/digithemis/assets/106356096/e67aafa0-1c06-4191-9dac-61283133d6c5" width="100px;" alt="Foto de Kennendh Silva"/><br>
        <sub>
          <b>Kennendh Silva</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/jooooou" title="Guilherme Barcelos">
        <img src="https://github.com/AthilioCavalcanti/digithemis/assets/106356096/0a1fa6fc-ae58-4ff6-9593-ea1a9c4bf401" height="100px" width="100px;" alt="Foto de Guilherme Barcelos"/><br>
        <sub>
          <b>Guilherme Barcelos</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
