# Gerenciamento de Instâncias EC2 com Python e GitHub Actions

Este projeto fornece um script em Python utilizando `boto3` para ligar e desligar instâncias EC2 na AWS, além de um pipeline GitHub Actions para que os usuários possam gerenciar suas instâncias diretamente através de inputs no workflow.

## Pré-requisitos

- **Python 3.x** instalado.
- Biblioteca `boto3` instalada. Você pode instalá-la com o comando:
  ```bash
  pip install boto3
