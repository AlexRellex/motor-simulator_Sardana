from tango import Database, DbDevInfo

def main():
    db = Database()

    """Add device server motor"""
    new_device_name = "x/foo/motor"

    new_device_info_motor = DbDevInfo()
    new_device_info_motor._class = "DS_Motor"
    new_device_info_motor.server = "DS_Motor/aalonso"

    print("Creating device: %s" % new_device_name)
    new_device_info_motor.name = new_device_name
    db.add_device(new_device_info_motor)

if __name__ == '__main__':
    main()
