from pymodbus.client import ModbusTcpClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import time
from .models import Parameter

PLC_IP = '192.168.0.10'
PLC_PORT = 502
MODBUS_ADDRESS = 1

client = ModbusTcpClient(PLC_IP, PLC_PORT)

DATABASE_URL = 'postgresql://user:password@db:5432/yourdatabase'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def read_and_store_parameter():
    try:
        result = client.read_holding_registers(MODBUS_ADDRESS, 1)
        if result.isError():
            print("Ошибка при чтении данных с ПЛК")
        else:
            parameter_value = result.registers[0]
            new_parameter = Parameter(value=parameter_value)
            session.add(new_parameter)
            session.commit()
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    while True:
        read_and_store_parameter()
        time.sleep(1)
