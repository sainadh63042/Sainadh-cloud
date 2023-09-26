import re

with open("simulated_records.txt", "r") as file:
    records = file.read()


def unique_dst_ip_addresses(records_arg):
    pattern = r"dst=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    unique_dst_ips = re.findall(pattern, records_arg)
    return unique_dst_ips


def count_unique_ip_addresses():
    unique_dst_ip_counts = {}
    unique_dst_ips = unique_dst_ip_addresses(records)
    for dst_ip in unique_dst_ips:
        if dst_ip in unique_dst_ip_counts:
            unique_dst_ip_counts[dst_ip] += 1
        else:
            unique_dst_ip_counts[dst_ip] = 1
    for dst_ip, count in unique_dst_ip_counts.items():
        if count >= 1:
            print(f"{dst_ip} count:{count}")
    print(f"No.of unique ip addresses: {len(unique_dst_ip_counts)}")


def main():
    count_unique_ip_addresses()


if __name__ == "__main__":
    main()
