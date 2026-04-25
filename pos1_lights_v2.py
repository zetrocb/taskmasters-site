class HandGestureDetector:
    def __init__(self):
        self.addr = 0x68
        self.mock_mode = False

        try:
            import smbus2
            self.bus = smbus2.SMBus(1)
            self.bus.write_byte_data(self.addr, 0x6B, 0)  # Wake up MPU6050
            print("IMU detected on I2C bus.")
        except Exception as e:
            print("IMU not found. Switching to MOCK mode.")
            self.mock_mode = True
