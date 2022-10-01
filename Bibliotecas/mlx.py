from smbus2 import SMBus
from mlx90614 import MLX90614
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
print("Temperatura ambiente : ", sensor.get_amb_temp())
print("Tempertura de persona u objeto: ", sensor.get_obj_temp())
bus.close()
