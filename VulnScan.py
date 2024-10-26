import socket
import json
import time

# طلب الرابط من المستخدم
target_url = input("Enter the target URL (without http/https): ")  # إدخال الرابط من المستخدم
start_port = int(input("Enter the starting port (e.g., 1): "))  # إدخال أول منفذ
end_port = int(input("Enter the ending port (e.g., 1024): "))  # إدخال آخر منفذ
output_file = input("Enter the path for the output file (e.g., scan_results.json): ")  # إدخال مسار الملف

# تحويل الرابط إلى عنوان IP
try:
    target_ip = socket.gethostbyname(target_url)
    print(f"Target IP for {target_url} is {target_ip}")
except socket.gaierror:
    print(f"Failed to resolve {target_url}")
    exit(1)

# دالة لفحص المنافذ باستخدام مكتبة socket
def scan_ports(ip, start_port, end_port):
    open_ports = []
    results = {}
    start_time = time.time()  # بدء توقيت الفحص
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # تحديد مهلة الاتصال بالثانية
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
            results[port] = "Open"
            print(f"[+] Open Port Found: {port}")
        else:
            results[port] = "Closed"
        sock.close()
    end_time = time.time()  # انتهاء توقيت الفحص
    elapsed_time = end_time - start_time
    return open_ports, results, elapsed_time

# فحص المنافذ في القائمة
print(f"Scanning IP: {target_ip} from port {start_port} to {end_port}")
open_ports, results, elapsed_time = scan_ports(target_ip, start_port, end_port)

# حفظ النتائج في الملف المحدد من قبل المستخدم
with open(output_file, 'w') as f:
    json.dump(results, f, indent=4)

# ملخص النتائج
total_ports = end_port - start_port + 1
total_open = len(open_ports)
total_closed = total_ports - total_open

print(f"\n[+] Scan complete. Results saved to {output_file}")
print(f"[+] Total Ports Scanned: {total_ports}")
print(f"[+] Open Ports: {total_open}")
print(f"[+] Closed Ports: {total_closed}")
print(f"[+] Time taken for scan: {elapsed_time:.2f} seconds")
