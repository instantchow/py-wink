if __name__ == "__main__":
    import time
    try:
        import wink
    except ImportError as e:
        import sys
        sys.path.insert(0, "..")
        import wink

    w = wink.init("../config.cfg")

    if "sensor_pod" not in w.device_types():
        raise RuntimeError(
            "you do not have a sensor_pod associated with your account!"
        )

    c = w.sensor_pod()

    print "found sensor_pod %s called %s!" % (c.id, c.data.get("name"))
    
    print "temperature of %d degrees last seen %s" % (c.get_temperature(), 
           time.ctime(c.get_temperature_updated_at()))
           
    print  "humidity of %d percent last seen %s" % (c.get_humidity(),
            time.ctime(c.get_humidity_updated_at()))
