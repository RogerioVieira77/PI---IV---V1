# Sistema de Controle de Acesso - CEU Tres Pontes

Sistema IoT de controle de acesso e contagem de pessoas utilizando múltiplos protocolos de comunicação.

## 🎯 Fase Atual: FASE 2 - Gateway e MQTT ✅

### Status Fase 1
- ✅ Simulador LoRa
- ✅ Simulador ZigBee  
- ✅ Simulador Sigfox
- ✅ Simulador RFID
- ✅ Testes Automatizados
- ✅ Documentação

### Status Fase 2
- ✅ Gateway implementado
- ✅ Cliente MQTT (Publisher/Subscriber)
- ✅ Formatador de mensagens JSON
- ✅ Subscriber com callbacks
- ✅ Integração com Mosquitto
- ✅ Testes de integração
- ✅ Documentação completa

## 🚀 Quick Start

### Fase 1: Testar Sensores

```powershell
# Windows PowerShell
cd tests
python test_simuladores.py
```

### Fase 2: Sistema Completo (MQTT)

**1. Instalar Mosquitto:**
```powershell
# Via Chocolatey
choco install mosquitto

# Iniciar serviço
net start mosquitto
```

**2. Instalar dependências Python:**
```powershell
pip install -r backend\requirements-phase2.txt
```

**3. Executar teste de integração:**
```powershell
python tests\test_mqtt_integration.py
```

### Exemplo de Uso - Gateway

```python
from backend.gateway import Gateway
from sensores import LoRaSensor, ZigBeeSensor

# Criar gateway
gateway = Gateway()

# Registrar sensores
gateway.register_sensors([
    LoRaSensor(location="Entrada Principal"),
    ZigBeeSensor(location="Saída Norte")
])

# Iniciar (publica via MQTT automaticamente)
gateway.start()

# Ver estatísticas
print(gateway.get_stats())
```

## 📚 Documentação Completa

Veja a documentação detalhada em: [`docs/README.md`](docs/README.md)

## 🏗️ Estrutura do Projeto

```
PI - IV - V1/
├── sensores/          # Simuladores IoT (Fase 1) ✅
├── backend/
│   ├── gateway/       # Gateway e MQTT (Fase 2) ✅
│   └── config/        # Configurações MQTT ✅
├── frontend/          # Interface Web (Fase 3)
├── tests/             # Testes ✅
├── docs/              # Documentação ✅
└── logs/              # Logs do sistema
```

## 🌐 Protocolos Suportados

- **LoRa** - Longo alcance (até 15 km)
- **ZigBee** - Rede mesh
- **Sigfox** - LPWAN global
- **RFID** - Identificação por proximidade

## 🛠️ Tecnologias

**Em Uso:**
- Python 3.12.3
- Mosquitto MQTT Broker
- paho-mqtt 1.6.1

**Planejado:**
- Flask
- MySQL 8.0.43
- Docker 27.5.1
- RabbitMQ 3.13
- PowerBI

---

**Desenvolvido para o Parque CEU Tres Pontes**
