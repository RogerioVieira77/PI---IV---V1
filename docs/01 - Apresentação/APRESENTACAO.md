# 🎯 PROJETO CEU TRES PONTES
## Sistema de Controle de Acesso e Contagem de Pessoas

---

## 📋 VISÃO GERAL

### O Desafio
Monitorar e contar o fluxo de pessoas no Parque CEU Tres Pontes de forma automatizada, utilizando tecnologias IoT modernas.

### A Solução
Sistema completo com sensores IoT, comunicação via múltiplos protocolos, backend robusto, interface web e analytics avançado.

---

## 🏗️ ARQUITETURA SIMPLIFICADA

```
┌─────────────────────────────────────────────┐
│           PARQUE CEU TRES PONTES            │
│                                             │
│  [LoRa]  [ZigBee]  [Sigfox]  [RFID]       │
│     ↓        ↓         ↓        ↓          │
└─────────────┼─────────────────────┘          
              ↓
         [Gateway]
              ↓
        [MQTT Broker]
              ↓
     [Backend - Flask]
         ↓        ↓
    [MySQL]   [RabbitMQ]
         ↓
   [Dashboard Web]
         ↓
     [PowerBI]
```

---

## 🔧 SENSORES IMPLEMENTADOS

### 1️⃣ LoRa - Longo Alcance
```
📡 Alcance: 2-15 km
🔋 Consumo: Muito Baixo
📊 Taxa: 0.3-50 kbps
✨ Ideal para: Áreas extensas
```

### 2️⃣ ZigBee - Rede Mesh
```
🕸️ Topologia: Malha
📡 Alcance: 10-100m
🔄 Vizinhos: Múltiplos
✨ Ideal para: Redundância
```

### 3️⃣ Sigfox - LPWAN Global
```
🌍 Cobertura: Global
📡 Alcance: até 50km
📬 Limite: 140 msg/dia
✨ Ideal para: Baixa frequência
```

### 4️⃣ RFID - Identificação
```
🎫 Tipos: LF, HF, UHF
📡 Alcance: 0.1-100m
🏷️ Tags: Únicas
✨ Ideal para: Controle preciso
```

---

## 📊 DADOS CAPTURADOS

### Por Cada Sensor:
✅ **Detecção Binária** (0 ou 1)  
✅ **Timestamp** (Data/Hora precisa)  
✅ **Serial Number** (ID único)  
✅ **Localização** (Entrada/Saída)  
✅ **Metadados** (Bateria, Sinal, etc)

### Agregados:
📈 Total de pessoas no parque  
📊 Entradas vs Saídas  
⏰ Fluxo por horário  
📅 Estatísticas diárias/mensais  
🔔 Alertas de capacidade

---

## 🎨 INTERFACE DO USUÁRIO

### Dashboard Principal
```
┌──────────────────────────────────────┐
│  CEU TRES PONTES - Dashboard         │
├──────────────────────────────────────┤
│  👥 Pessoas Agora:     245           │
│  ➡️  Entradas Hoje:    1,234         │
│  ⬅️  Saídas Hoje:      989           │
│  ⚠️  Capacidade:       49%           │
├──────────────────────────────────────┤
│  📊 [Gráfico de Fluxo Horário]      │
├──────────────────────────────────────┤
│  📍 Sensores Ativos:                 │
│     ✅ LoRa-001   | Entrada          │
│     ✅ ZigBee-002 | Saída Norte      │
│     ✅ Sigfox-003 | Portão Sul       │
│     ✅ RFID-004   | Catraca 1        │
└──────────────────────────────────────┘
```

---

## 📈 FASES DO PROJETO

### ✅ FASE 1: SIMULADORES (CONCLUÍDA)
- [x] Classe base de sensores
- [x] Simulador LoRa
- [x] Simulador ZigBee
- [x] Simulador Sigfox
- [x] Simulador RFID
- [x] Testes e documentação

### 📅 FASE 2: GATEWAY E MQTT
- [ ] Configurar Mosquitto
- [ ] Implementar Gateway
- [ ] Protocolo de mensagens
- [ ] Subscriber de teste

### 📅 FASE 3: BACKEND
- [ ] API REST (Flask)
- [ ] Banco MySQL
- [ ] RabbitMQ
- [ ] WebSocket
- [ ] Sistema de alertas

### 📅 FASE 4: FRONTEND
- [ ] Dashboard web
- [ ] Gráficos em tempo real
- [ ] Painel administrativo
- [ ] Exportação de relatórios

### 📅 FASE 5: ANALYTICS
- [ ] Integração PowerBI
- [ ] Dashboards executivos
- [ ] Relatórios automatizados

### 📅 FASE 6: DEPLOYMENT
- [ ] Docker containers
- [ ] NGINX
- [ ] Ubuntu Server
- [ ] Monitoramento

### 📅 FASE 7: TESTES E GO-LIVE
- [ ] Testes de carga
- [ ] Segurança
- [ ] Documentação final
- [ ] Treinamento

---

## 💻 TECNOLOGIAS UTILIZADAS

### Backend
```python
Python 3.12.3
Flask
MySQL 8.0.43
RabbitMQ 3.13
Mosquitto MQTT
```

### Frontend
```javascript
HTML5
CSS3
JavaScript ES6+
Chart.js
WebSocket
```

### Infraestrutura
```bash
Ubuntu 25.04
Docker 27.5.1
NGINX 1.29.1
```

### Analytics
```
PowerBI
Pandas
NumPy
PySpark
```

---

## 🎯 BENEFÍCIOS

### Para Gestão:
✅ Controle preciso de ocupação  
✅ Dados para tomada de decisão  
✅ Relatórios automatizados  
✅ Alertas de capacidade  
✅ Histórico completo  

### Para Visitantes:
✅ Melhor experiência  
✅ Informação de lotação  
✅ Segurança aumentada  
✅ Gestão de filas  

### Para Operação:
✅ Monitoramento em tempo real  
✅ Manutenção preditiva  
✅ Eficiência operacional  
✅ Redução de custos  

---

## 📊 MÉTRICAS DE SUCESSO

### Performance
- ⚡ Latência < 100ms
- 📊 Atualização a cada 2s
- 💾 Armazenamento de 1 ano
- 🔄 99.9% uptime

### Capacidade
- 👥 15+ sensores simultâneos
- 📈 10.000+ leituras/dia
- 🎯 Precisão > 95%
- ⚙️ Escalável horizontalmente

---

## 🔒 SEGURANÇA

### Camadas de Proteção:
1. 🔐 Autenticação JWT
2. 🔒 Comunicação TLS/SSL
3. 🛡️ Validação de inputs
4. 📝 Logs de auditoria
5. 🔑 Controle de acesso
6. 💾 Backup automático

---

## 📚 DOCUMENTAÇÃO

### Disponível:
📖 README completo  
🗺️ Roadmap detalhado (7 fases)  
🔌 Guia de integração  
📊 Resumo executivo  
💡 Exemplos de uso  
🧪 Testes automatizados  

---

## 🚀 QUICK START

### Testar Simuladores:
```bash
cd "C:\PI - IV - V1\tests"
python test_simuladores.py
```

### Exemplo Rápido:
```python
from sensores import LoRaSensor

sensor = LoRaSensor(location="Entrada")
reading = sensor.simulate_detection()
print(f"Detecção: {reading['activity']}")
```

---

## 📞 INFORMAÇÕES

**Projeto:** Sistema IoT de Controle de Acesso  
**Local:** Parque CEU Tres Pontes  
**Status:** Fase 1 Concluída ✅  
**Versão:** 1.0.0  
**Data:** Outubro 2025  

---

## 🌟 DESTAQUES

### 🏆 Diferenciais:
- Múltiplos protocolos IoT
- Simuladores realistas
- Arquitetura escalável
- Documentação completa
- Código limpo e testado

### 💡 Inovações:
- Simulação sem hardware
- Protocolos industriais
- Analytics avançado
- Containerização completa
- Dashboard em tempo real

---

## 🎓 APRENDIZADOS

### Conceitos Aplicados:
✓ IoT (Internet of Things)  
✓ Protocolos de Comunicação  
✓ Arquitetura de Software  
✓ Cloud & Containers  
✓ Big Data & Analytics  
✓ DevOps  

### Tecnologias Dominadas:
✓ Python Avançado  
✓ MQTT Protocol  
✓ REST APIs  
✓ Banco de Dados  
✓ Docker  
✓ Frontend Web  

---

## 🎉 CONCLUSÃO

### Fase 1: ✅ 100% Completa!

**Próximo Passo:**  
Iniciar Fase 2 - Gateway e MQTT

**Objetivo:**  
Sistema completo e operacional em 13 semanas

**Impacto:**  
Gestão inteligente do Parque CEU Tres Pontes

---

**🚀 Pronto para decolar! Fase 2 aguardando...**
