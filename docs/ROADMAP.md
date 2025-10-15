# Roadmap do Projeto - CEU Tres Pontes

## 📅 Cronograma de Desenvolvimento

---

## ✅ FASE 1: SIMULADORES DE SENSORES (CONCLUÍDA)

**Duração:** Semanas 1-2  
**Status:** ✅ 100% Completo

### Entregáveis
- [x] Classe base abstrata para sensores
- [x] Simulador LoRa com SF ajustável
- [x] Simulador ZigBee com rede mesh
- [x] Simulador Sigfox com limite de mensagens
- [x] Simulador RFID com leitura de tags
- [x] Scripts de teste e exemplos
- [x] Documentação completa

### Arquivos Criados
```
sensores/
├── base_sensor.py
├── lora_sensor.py
├── zigbee_sensor.py
├── sigfox_sensor.py
└── rfid_sensor.py

tests/
├── test_simuladores.py
└── exemplo_uso.py
```

---

## 📋 FASE 2: GATEWAY E COMUNICAÇÃO MQTT

**Duração:** Semanas 3-4  
**Status:** ✅ 100% Completo

### Objetivos
✅ Implementar gateway para coletar dados dos sensores e enviar via MQTT.

### Tarefas Completadas
- [x] Instalar e configurar Mosquitto MQTT Broker
- [x] Criar classe Gateway para agregar dados dos sensores
- [x] Implementar protocolo de comunicação Sensor → Gateway
- [x] Implementar publicação MQTT (Gateway → Broker)
- [x] Criar topics MQTT por tipo de sensor
- [x] Implementar QoS e mensagens persistentes
- [x] Criar subscriber de teste
- [x] Documentar protocolo de mensagens
- [x] Criar testes de integração completos
- [x] Implementar sistema de logging

### Estrutura de Topics MQTT (Implementada)
```
ceu/tres_pontes/sensores/{sensor_id}
ceu/tres_pontes/status
ceu/tres_pontes/alertas
```

### Formato de Mensagem JSON (Implementado)
```json
{
  "message_id": "gateway_001_123",
  "gateway_id": "gateway_001",
  "timestamp": "2025-10-14T10:30:00.123456",
  "sensor": {
    "serial_number": "LORA-ABC12345",
    "protocol": "LoRa",
    "location": "Entrada Principal"
  },
  "data": {
    "activity": 1,
    "timestamp": "2025-10-14T10:30:00",
    "total_detections": 42
  },
  "metadata": {
    "rssi_dbm": -65.5,
    "battery_level": 98.5
  }
}
```

### Arquivos Criados
```
backend/
├── gateway/
│   ├── __init__.py
│   ├── gateway.py              # ✅ Gateway principal
│   ├── mqtt_client.py          # ✅ Cliente MQTT
│   ├── mqtt_subscriber.py      # ✅ Subscriber
│   ├── message_formatter.py    # ✅ Formatador JSON
│   └── config_loader.py        # ✅ Loader de config
├── config/
│   └── mqtt_config.ini         # ✅ Configurações
└── requirements-phase2.txt     # ✅ Dependências

tests/
└── test_mqtt_integration.py    # ✅ Teste integração

docs/
├── MOSQUITTO_SETUP.md          # ✅ Guia Mosquitto
└── FASE2_MQTT.md               # ✅ Documentação Fase 2
```

### Componentes Implementados

#### 1. Gateway (`gateway.py`)
- Gerenciamento de sensores
- Coleta automática de leituras
- Publicação MQTT em thread separada
- Sistema de alertas
- Estatísticas em tempo real

#### 2. Cliente MQTT (`mqtt_client.py`)
- Conexão com broker Mosquitto
- Publisher e Subscriber
- Reconexão automática
- QoS configurável (0, 1, 2)
- Callbacks customizáveis

#### 3. Subscriber (`mqtt_subscriber.py`)
- Recepção de mensagens
- Callbacks por tipo de mensagem
- Cache de dados (até 1000 msgs)
- Exportação para JSON

#### 4. Formatador (`message_formatter.py`)
- Mensagens padronizadas JSON
- IDs únicos
- Timestamps ISO 8601
- Metadados do gateway

### Como Testar

```powershell
# 1. Instalar Mosquitto
choco install mosquitto
net start mosquitto

# 2. Instalar dependências
pip install -r backend\requirements-phase2.txt

# 3. Executar teste de integração
python tests\test_mqtt_integration.py
```

### Documentação
- **Guia de Instalação:** `docs/MOSQUITTO_SETUP.md`
- **Documentação Completa:** `docs/FASE2_MQTT.md`
- **Configuração:** `backend/config/mqtt_config.ini`

---

## 📋 FASE 3: BACKEND COM FLASK

**Duração:** Semanas 5-7  
**Status:** 📅 Planejado

### Objetivos
Criar API REST para gerenciar dados e fornecer endpoints para frontend.

### Tarefas
- [ ] Configurar projeto Flask
- [ ] Implementar conexão com MySQL
- [ ] Criar models (SQLAlchemy):
  - Sensor
  - Reading (Leitura)
  - Alert (Alerta)
  - Statistics (Estatísticas)
- [ ] Implementar subscriber MQTT → Database
- [ ] Criar endpoints REST:
  - GET /api/sensors
  - GET /api/sensors/{id}
  - GET /api/readings
  - GET /api/statistics
  - POST /api/sensors
  - PUT /api/sensors/{id}
- [ ] Implementar WebSocket para dados em tempo real
- [ ] Integrar RabbitMQ para processamento assíncrono
- [ ] Criar workers para:
  - Agregação de dados
  - Detecção de anomalias
  - Geração de relatórios
- [ ] Implementar autenticação JWT
- [ ] Criar testes unitários

### Estrutura Backend
```
backend/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── sensors.py
│   │   ├── readings.py
│   │   └── statistics.py
│   ├── services/
│   │   ├── mqtt_subscriber.py
│   │   ├── data_processor.py
│   │   └── alert_manager.py
│   └── workers/
│       ├── aggregator.py
│       └── analyzer.py
├── config.py
├── requirements.txt
└── run.py
```

### Banco de Dados (MySQL)

#### Tabela: sensors
```sql
CREATE TABLE sensors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    serial_number VARCHAR(50) UNIQUE NOT NULL,
    protocol VARCHAR(20) NOT NULL,
    location VARCHAR(100) NOT NULL,
    status ENUM('active', 'inactive', 'maintenance') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

#### Tabela: readings
```sql
CREATE TABLE readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sensor_id INT NOT NULL,
    activity TINYINT(1) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    metadata JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sensor_id) REFERENCES sensors(id),
    INDEX idx_sensor_timestamp (sensor_id, timestamp)
);
```

#### Tabela: statistics
```sql
CREATE TABLE statistics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    hour INT NOT NULL,
    entries INT DEFAULT 0,
    exits INT DEFAULT 0,
    total_people INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uk_date_hour (date, hour)
);
```

---

## 📋 FASE 4: FRONTEND WEB

**Duração:** Semanas 8-9  
**Status:** 📅 Planejado

### Objetivos
Criar interface web para visualização e gerenciamento do sistema.

### Tarefas
- [ ] Estrutura HTML5 responsiva
- [ ] Estilização com CSS3
- [ ] Dashboard em tempo real
- [ ] Gráficos de ocupação (Chart.js)
- [ ] Mapa do parque com sensores
- [ ] Lista de sensores ativos
- [ ] Alertas e notificações
- [ ] Painel administrativo
- [ ] Exportação de relatórios (PDF/Excel)
- [ ] WebSocket para atualizações em tempo real

### Páginas
1. **Dashboard** - Visão geral em tempo real
2. **Sensores** - Lista e status de todos os sensores
3. **Histórico** - Dados históricos e gráficos
4. **Relatórios** - Geração de relatórios customizados
5. **Configurações** - Gerenciamento do sistema
6. **Alertas** - Central de notificações

### Estrutura Frontend
```
frontend/
├── index.html
├── css/
│   ├── style.css
│   ├── dashboard.css
│   └── responsive.css
├── js/
│   ├── app.js
│   ├── api.js
│   ├── dashboard.js
│   ├── charts.js
│   └── websocket.js
├── assets/
│   ├── images/
│   └── icons/
└── pages/
    ├── sensors.html
    ├── history.html
    └── reports.html
```

---

## 📋 FASE 5: ANALYTICS E POWERBI

**Duração:** Semana 10  
**Status:** 📅 Planejado

### Objetivos
Integrar com PowerBI para análises avançadas e dashboards executivos.

### Tarefas
- [ ] Configurar conexão PowerBI → MySQL
- [ ] Criar modelo de dados no PowerBI
- [ ] Desenvolver dashboards:
  - Fluxo de pessoas por hora/dia/mês
  - Análise de picos de ocupação
  - Comparativo mensal/anual
  - Heatmap de horários
  - Performance dos sensores
  - Alertas e anomalias
- [ ] Criar relatórios automatizados
- [ ] Configurar refresh automático
- [ ] Publicar no PowerBI Service (opcional)

### Dashboards PowerBI
1. **Visão Executiva** - KPIs principais
2. **Análise Temporal** - Tendências e padrões
3. **Mapa de Calor** - Áreas mais movimentadas
4. **Performance Técnica** - Status dos sensores
5. **Comparativo** - Períodos e eventos

---

## 📋 FASE 6: CONTAINERIZAÇÃO E DEPLOYMENT

**Duração:** Semanas 11-12  
**Status:** 📅 Planejado

### Objetivos
Containerizar aplicação e preparar para produção.

### Tarefas
- [ ] Criar Dockerfile para backend
- [ ] Criar Dockerfile para frontend
- [ ] Criar docker-compose.yml
- [ ] Configurar volumes persistentes
- [ ] Configurar rede entre containers
- [ ] Implementar NGINX como reverse proxy
- [ ] Configurar SSL/TLS (Let's Encrypt)
- [ ] Implementar logging centralizado
- [ ] Configurar monitoramento (Prometheus/Grafana)
- [ ] Criar scripts de backup automático
- [ ] Documentar processo de deployment
- [ ] Testes de carga e performance
- [ ] Deployment em Ubuntu Server

### Docker Compose Structure
```yaml
version: '3.8'
services:
  mysql:
    image: mysql:8.0.43
    
  rabbitmq:
    image: rabbitmq:3.13-management
    
  mosquitto:
    image: eclipse-mosquitto:latest
    
  backend:
    build: ./backend
    
  frontend:
    build: ./frontend
    
  nginx:
    image: nginx:1.29.1
```

### Arquivos de Deployment
```
deployment/
├── docker-compose.yml
├── nginx/
│   └── nginx.conf
├── scripts/
│   ├── backup.sh
│   ├── restore.sh
│   └── deploy.sh
└── monitoring/
    ├── prometheus.yml
    └── grafana/
```

---

## 📋 FASE 7: TESTES E OTIMIZAÇÃO

**Duração:** Semana 13  
**Status:** 📅 Planejado

### Objetivos
Garantir qualidade, performance e segurança do sistema.

### Tarefas
- [ ] Testes unitários (backend)
- [ ] Testes de integração
- [ ] Testes end-to-end (E2E)
- [ ] Testes de carga
- [ ] Testes de segurança
- [ ] Otimização de queries SQL
- [ ] Otimização de cache
- [ ] Auditoria de segurança
- [ ] Documentação técnica completa
- [ ] Manual do usuário
- [ ] Treinamento da equipe

---

## 🎯 Métricas de Sucesso

### Performance
- ⚡ Latência API < 100ms
- 📊 Dashboard atualiza a cada 2s
- 💾 Armazenamento de 1 ano de dados
- 🔄 99.9% uptime

### Funcionalidade
- ✅ Suporte a 15+ sensores simultâneos
- ✅ 10.000+ leituras por dia
- ✅ Detecção de anomalias em tempo real
- ✅ Relatórios automáticos diários

### Segurança
- 🔐 Autenticação JWT
- 🔒 Conexões criptografadas (SSL/TLS)
- 🛡️ Proteção contra SQL Injection
- 📝 Logs de auditoria

---

## 🛠️ Ferramentas e Tecnologias por Fase

| Fase | Ferramentas Principais |
|------|------------------------|
| 1 | Python, OOP |
| 2 | Mosquitto, MQTT, Python |
| 3 | Flask, MySQL, RabbitMQ, SQLAlchemy |
| 4 | HTML5, CSS3, JavaScript, Chart.js |
| 5 | PowerBI, MySQL Connector |
| 6 | Docker, Docker Compose, NGINX |
| 7 | pytest, Selenium, JMeter |

---

## 📈 Linha do Tempo Visual

```
Semanas:  1-2    3-4    5-7    8-9    10     11-12   13
         [===] [===] [=====] [===]  [==]  [=====] [==]
Fase:      1     2      3      4      5      6      7
Status:   ✅    ✅     📅     📅     📅     📅     📅
```

---

**Última atualização:** Outubro 2025  
**Fase atual:** 2 de 7 (✅ Concluída)  
**Próxima fase:** Backend com Flask (📅 Início planejado)
