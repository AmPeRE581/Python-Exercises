import os
import time
import psutil
import matplotlib.pyplot as plt
import csv

# Soglie per allerta
CPU_THRESHOLD = 80  # Percentuale
MEMORY_THRESHOLD = 80  # Percentuale

# Dati per grafico
cpu_usage_history = []
memory_usage_history = []
disk_usage_history = []

def alert_if_critical():
    cpu_usage = psutil.cpu_percent()
    mem = psutil.virtual_memory()

    if cpu_usage > CPU_THRESHOLD:
        print(f"ALERT: CPU Usage is high: {cpu_usage}%")
    if mem.percent > MEMORY_THRESHOLD:
        print(f"ALERT: Memory Usage is high: {mem.percent}%")

def print_battery_info():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        plugged = battery.power_plugged
        print(f"Battery: {percent}% {'(Charging)' if plugged else '(Not Charging)'}")

def print_cpu_usage():
    cpu_times = psutil.cpu_times()
    user, nice, system, idle, iowait = cpu_times.user, cpu_times.nice, cpu_times.system, cpu_times.idle, cpu_times.iowait
    total = user + nice + system + idle + iowait
    prev_total = getattr(print_cpu_usage, 'prev_total', total)
    prev_idle = getattr(print_cpu_usage, 'prev_idle', idle)

    total_diff = total - prev_total
    idle_diff = idle - prev_idle

    if total_diff != 0:
        usage = 100.0 * (total_diff - idle_diff) / total_diff
        cpu_usage_history.append(usage)
        print(f"CPU Usage: {usage:.2f}%")

    print_cpu_usage.prev_total = total
    print_cpu_usage.prev_idle = idle

def print_memory_usage():
    mem = psutil.virtual_memory()
    total_virtual_mem = mem.total + psutil.swap_memory().total
    virtual_mem_used = mem.used + psutil.swap_memory().used

    usage_percent = 100.0 * virtual_mem_used / total_virtual_mem
    print(f"Memory Usage: {usage_percent:.2f}% ({100.0 * mem.used / mem.total:.2f}% of Physical Memory)")
    
    memory_usage_history.append(usage_percent)

def print_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage_history.append(disk.percent)
    print(f"Disk Usage: {disk.percent:.2f}% ({disk.used / (1024 ** 3):.2f} GB used, {disk.free / (1024 ** 3):.2f} GB free)")

def print_highest_priority_process():
    highest_prio_process = None
    highest_prio = float('inf')

    for proc in psutil.process_iter(['pid', 'name', 'nice', 'cpu_percent', 'memory_info']):
        try:
            if proc.info['nice'] < highest_prio:
                highest_prio = proc.info['nice']
                highest_prio_process = proc.info
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if highest_prio_process:
        print(f"Highest Priority Process: {highest_prio_process['name']} (PID: {highest_prio_process['pid']}, "
              f"CPU: {highest_prio_process['cpu_percent']}%, Memory: {highest_prio_process['memory_info'].rss / (1024 ** 2):.2f} MB)")

def print_network_usage():
    net_io = psutil.net_io_counters(pernic=True)
    for interface, counters in net_io.items():
        print(f"Interface: {interface}, TX: {counters.bytes_sent} bytes, RX: {counters.bytes_recv} bytes")

def print_dns_info():
    with open('/etc/resolv.conf', 'r') as file:
        print("DNS Servers:")
        for line in file:
            if line.startswith('nameserver'):
                dns_ip = line.split()[1]
                print(dns_ip, end='')
                if dns_ip in ["1.1.1.1", "1.0.0.1"]:
                    print(" (Cloudflare DNS)")
                elif dns_ip in ["8.8.8.8", "8.8.4.4"]:
                    print(" (Google DNS)")
                elif dns_ip in ["208.67.222.222", "208.67.220.220"]:
                    print(" (OpenDNS)")
                else:
                    print()

def print_cpu_threads_usage():
    cores = psutil.cpu_count(logical=False)
    active_threads = len(psutil.pids())
    print(f"CPU Threads Usage: {active_threads}/{cores}")

def log_statistics():
    with open("system_stats.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        cpu_usage = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        writer.writerow([time.ctime(), cpu_usage, mem.percent, disk.percent])

def plot_statistics():
    plt.figure(figsize=(10, 5))

    # CPU Usage
    plt.subplot(1, 3, 1)
    plt.plot(cpu_usage_history, label='CPU Usage (%)', color='blue')
    plt.title('CPU Usage Over Time')
    plt.xlabel('Time (20s intervals)')
    plt.ylabel('Usage (%)')
    plt.ylim(0, 100)
    plt.legend()

    # Memory Usage
    plt.subplot(1, 3, 2)
    plt.plot(memory_usage_history, label='Memory Usage (%)', color='green')
    plt.title('Memory Usage Over Time')
    plt.xlabel('Time (20s intervals)')
    plt.ylabel('Usage (%)')
    plt.ylim(0, 100)
    plt.legend()

    # Disk Usage
    plt.subplot(1, 3, 3)
    plt.plot(disk_usage_history, label='Disk Usage (%)', color='orange')
    plt.title('Disk Usage Over Time')
    plt.xlabel('Time (20s intervals)')
    plt.ylabel('Usage (%)')
    plt.ylim(0, 100)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    first_run = True

    # Initialize CSV file with headers
    with open("system_stats.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "CPU Usage (%)", "Memory Usage (%)", "Disk Usage (%)"])

    while True:
        print_cpu_usage()
        print_memory_usage()
        print_disk_usage()
        alert_if_critical()
        print_battery_info()
        log_statistics()  # Logga le statistiche

        if first_run:
            print_highest_priority_process()
            print_dns_info()
            print_cpu_threads_usage()
            first_run = False

        print_network_usage()
        time.sleep(20)  # Aggiorna ogni 20 secondi

        # Plot statistics every 60 seconds
        if len(cpu_usage_history) % 3 == 0:
            plot_statistics()