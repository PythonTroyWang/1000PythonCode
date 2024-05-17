import psutil


def get_mac_address():
    interfaces = psutil.net_if_addrs()

    for interface, addrs in interfaces.items():
        stats = psutil.net_if_stats()[interface]
        if stats.isup:
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    return addr.address
