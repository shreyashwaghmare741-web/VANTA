import platform
import psutil


def battery():
    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information not available."

    status = "Charging" if battery.power_plugged else "Not Charging"

    return (
        f"🔋 Battery : {battery.percent}%\n"
        f"Status : {status}"
    )


def cpu():
    usage = psutil.cpu_percent(interval=1)

    return f"🖥 CPU Usage : {usage}%"


def ram():
    memory = psutil.virtual_memory()

    total = memory.total / (1024 ** 3)
    used = memory.used / (1024 ** 3)
    available = memory.available / (1024 ** 3)

    return (
        f"💾 RAM Usage\n"
        f"Used : {used:.2f} GB\n"
        f"Available : {available:.2f} GB\n"
        f"Total : {total:.2f} GB"
    )


def disk():
    drive = psutil.disk_usage("C:\\")

    total = drive.total / (1024 ** 3)
    used = drive.used / (1024 ** 3)
    free = drive.free / (1024 ** 3)

    return (
        f"💽 Disk Usage\n"
        f"Used : {used:.2f} GB\n"
        f"Free : {free:.2f} GB\n"
        f"Total : {total:.2f} GB"
    )


def system_info():
    return (
        f"System : {platform.system()}\n"
        f"Release : {platform.release()}\n"
        f"Processor : {platform.processor()}"
    )