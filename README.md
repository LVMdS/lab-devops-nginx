# 🚀 Home Lab DevOps: Infraestrutura Automatizada (CI/CD)

![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

Este repositório contém a infraestrutura como código (IaC) de um Laboratório DevOps pessoal. O projeto transforma um servidor Linux convencional em um cluster de microsserviços totalmente containerizado, monitorado e com deploy automatizado via pipeline de CI/CD.

---

## 🏗️ Arquitetura e Serviços

O ambiente é orquestrado via **Docker Compose** e executa os seguintes serviços:

| Serviço | Função | Tecnologia |
| :--- | :--- | :--- |
| **Proxy Reverso** | Servidor Web e roteamento de tráfego. | `Nginx` |
| **DNS Sinkhole** | Bloqueio de anúncios e rastreadores em toda a rede local. | `AdGuard Home` |
| **Monitoramento** | Métricas em tempo real (CPU, RAM, Network, Docker). | `Netdata` |
| **YouTube Frontend** | Interface privada para YouTube (sem ads/tracking). | `Invidious` |
| **Database** | Persistência de dados para aplicações. | `PostgreSQL 14` |

---

## ⚙️ Automação (CI/CD)

O projeto implementa uma pipeline **Zero-Touch Deploy** utilizando **GitHub Actions Self-Hosted**.

1.  **Trigger:** `git push` na branch `main`.
2.  **Runner:** Um agente instalado no servidor detecta a mudança.
3.  **Action:** * Faz o checkout do código novo.
    * Ajusta permissões de arquivos sensíveis.
    * Executa `docker compose up -d --build`.
4.  **Resultado:** A infraestrutura se auto-atualiza em segundos sem intervenção manual via SSH.

---

## 🛠️ Guia de Instalação e Configuração

Se você deseja replicar este laboratório, siga os passos abaixo no seu servidor Linux (Ubuntu/Debian/Mint).

### 1. Pré-requisitos
* Docker e Docker Compose instalados.
* Git instalado.
* Portas 80, 53, 3000, 3001 e 19999 livres.

### 2. Preparação do Sistema (Porta 53)
Para o **AdGuard Home** funcionar, é necessário liberar a porta 53 (DNS) que geralmente é ocupada pelo `systemd-resolved` do Ubuntu.

```bash
# Desativar o resolvedor padrão do sistema
sudo systemctl stop systemd-resolved
sudo systemctl disable systemd-resolved

# Configurar DNS temporário para o servidor não perder conexão
sudo rm /etc/resolv.conf
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```
### 3. Instalação
```bash
git clone [https://github.com/LVMdS/lab-devops-nginx.git](https://github.com/LVMdS/lab-devops-nginx.git)
cd lab-devops-nginx
```
### importante: Ajuste as permissões para que o container invidious consiga ler o arquivo de configuração:
```bash
sudo chmod -R 777 config/
```
### Suba o ambiente
```bash
docker compose up -d
```
### 📡 Acesso aos serviços

### Após o deploy, os serviços estarão disponíveis no IP do seu servidor (http://SEU_IP:PORTA):

- 🌐 Site Institucional: Porta 80

- 🛡️ AdGuard Home: Porta 3000 (Setup Inicial) / 53 (DNS)

- 📊 Netdata Monitor: Porta 19999

- 📺 Invidious (YouTube): Porta 3001

### 🐛 Troubleshooting Comum
 - Erro: Invidious reiniciando (Restarting) Geralmente causado por falta de permissão no arquivo config.yml ou falta da hmac_key.

 - Solução: Rode sudo chmod -R 777 config/ e reinicie o container.

 - Erro: Porta 53 em uso

 - Solução: Verifique se executou o passo "Preparação do Sistema" acima para desligar o systemd-resolved.

### Screenshots

<a href="https://ibb.co/Nn701Z6k"><img src="https://i.ibb.co/DgLBG5D6/Ad-Guard.png" alt="Ad-Guard" border="0"></a>
<a href="https://ibb.co/PJkR90R"><img src="https://i.ibb.co/NfRXmbX/netlab.png" alt="netlab" border="0"></a>

### Autor
    Desenvolvido por Leonardo Vinicius Martins de Souza.

Linkedin: https://www.linkedin.com/in/leonardo-vinicius-martins-de-souza/
