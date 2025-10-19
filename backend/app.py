"""
Flask Application Entry Point
CEU Tres Pontes - Sistema de Controle de Acesso

Fase 3: Backend Flask + MySQL
"""

import os
from app import create_app, db
from app.models import Sensor, Reading, Alert, Statistics, User

# Criar aplicação
app = create_app(os.getenv('FLASK_ENV', 'development'))


@app.cli.command()
def init_db():
    """Inicializa o banco de dados (cria todas as tabelas)"""
    print("Criando tabelas do banco de dados...")
    db.create_all()
    print("✅ Tabelas criadas com sucesso!")


@app.cli.command()
def drop_db():
    """Remove todas as tabelas do banco de dados"""
    if input("⚠️  Tem certeza? Isso irá deletar TODOS os dados! (yes/no): ") == "yes":
        print("Removendo tabelas do banco de dados...")
        db.drop_all()
        print("✅ Tabelas removidas!")
    else:
        print("Operação cancelada.")


@app.cli.command()
def seed_db():
    """Popula o banco de dados com dados de exemplo"""
    print("Populando banco de dados com dados de exemplo...")
    
    # Criar usuário admin
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User.create_user(
            username='admin',
            email='admin@ceutrespontes.com',
            password='admin123',
            role='admin',
            full_name='Administrador do Sistema'
        )
        admin.is_verified = True
        db.session.add(admin)
        print("✅ Usuário admin criado (username: admin, password: admin123)")
    
    # Criar sensores de exemplo
    sensors_data = [
        {
            'serial_number': 'LORA-ENTRADA-01',
            'protocol': 'LoRa',
            'location': 'Entrada Principal',
            'description': 'Sensor LoRa na entrada principal do parque',
            'status': 'active'
        },
        {
            'serial_number': 'LORA-SAIDA-01',
            'protocol': 'LoRa',
            'location': 'Saída Principal',
            'description': 'Sensor LoRa na saída principal do parque',
            'status': 'active'
        },
        {
            'serial_number': 'ZIGB-LATERAL-01',
            'protocol': 'ZigBee',
            'location': 'Entrada Lateral Norte',
            'description': 'Sensor ZigBee na entrada lateral norte',
            'status': 'active'
        },
        {
            'serial_number': 'ZIGB-LATERAL-02',
            'protocol': 'ZigBee',
            'location': 'Entrada Lateral Sul',
            'description': 'Sensor ZigBee na entrada lateral sul',
            'status': 'active'
        },
        {
            'serial_number': 'SIGF-BANHEIRO-01',
            'protocol': 'Sigfox',
            'location': 'Banheiros',
            'description': 'Sensor Sigfox próximo aos banheiros',
            'status': 'active'
        },
        {
            'serial_number': 'RFID-PORTARIA-01',
            'protocol': 'RFID',
            'location': 'Portaria',
            'description': 'Leitor RFID na portaria',
            'status': 'active'
        }
    ]
    
    sensors_created = 0
    for sensor_data in sensors_data:
        sensor = Sensor.query.filter_by(serial_number=sensor_data['serial_number']).first()
        if not sensor:
            sensor = Sensor(**sensor_data)
            db.session.add(sensor)
            sensors_created += 1
    
    if sensors_created > 0:
        print(f"✅ {sensors_created} sensores criados!")
    else:
        print("ℹ️  Sensores já existem no banco.")
    
    # Commit
    try:
        db.session.commit()
        print("✅ Banco de dados populado com sucesso!")
    except Exception as e:
        db.session.rollback()
        print(f"❌ Erro ao popular banco: {e}")


@app.cli.command()
def create_admin():
    """Cria um usuário administrador"""
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    full_name = input("Nome completo: ")
    
    # Verificar se já existe
    if User.query.filter_by(username=username).first():
        print(f"❌ Usuário '{username}' já existe!")
        return
    
    if User.query.filter_by(email=email).first():
        print(f"❌ Email '{email}' já está em uso!")
        return
    
    # Criar admin
    admin = User.create_user(
        username=username,
        email=email,
        password=password,
        role='admin',
        full_name=full_name
    )
    admin.is_verified = True
    
    db.session.add(admin)
    db.session.commit()
    
    print(f"✅ Administrador '{username}' criado com sucesso!")


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
