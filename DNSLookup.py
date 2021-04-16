import socket
import dns.resolver

domain = input("Enter domain to check: https://")

# NameServer Lookup
try:
    for nameserver in dns.resolver.resolve(domain, 'NS'):
        print("Nameserver found:", nameserver)

except KeyboardInterrupt:
    print("Scan was cancelled.")
except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
    print("NoAnswer exception while fetching name server data (no record or server offline).")
except dns.resolver.Timeout:
    print("Timeout exception while fetching name server data (Timeout).")

# IP Lookups
try:
    for ip4 in dns.resolver.resolve(domain, 'A'):
        print("Web Hosting IPV4: ", ip4)

    for ip6 in dns.resolver.resolve(domain, 'AAAA'):
        print("Web Hosting IPV6: ", ip6)

    reverse_ip = socket.gethostbyname("www." + domain)
    reverse_name = dns.reversename.from_address(reverse_ip)
    print("ReverseName for DNS: ", reverse_name)
    print("ReverseName for to_address: ", dns.reversename.to_address(reverse_name))

except KeyboardInterrupt:
    print("Scan was cancelled.")
except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
    print("NoAnswer exception while fetching IP data (no record or server offline).")
except dns.resolver.Timeout:
    print("Timeout exception while fetching IP data (Timeout).")
except socket.gaierror:
    print("Error fetching ReverseName information.")

# Zone Lookup
try:
    for zone in dns.resolver.resolve(domain, 'SOA'):
        print("Start Of Authority (SOA): ", zone)

except KeyboardInterrupt:
    print("Scan was cancelled.")
except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
    print("NoAnswer exception while fetching SOA/Zone data (no record or server offline).")
except dns.resolver.Timeout:
    print("Timeout exception while fetching SOA/Zone data (Timeout).")

# MX Lookup
try:
    for mailex in dns.resolver.resolve(domain, 'MX'):
        print("MX Record found:", mailex)

except KeyboardInterrupt:
    print("Scan was cancelled.")
except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
    print("NoAnswer exception while fetching MX data (no record or server offline).")
except dns.resolver.Timeout:
    print("Timeout exception while fetching MX data (Timeout).")

# TXT Lookup
try:
    for txt in dns.resolver.resolve(domain, 'TXT'):
        print("TXT Record: ", txt)

except KeyboardInterrupt:
    print("Scan was cancelled.")
except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
    print("NoAnswer exception while fetching TXT data (no record or server offline).")
except dns.resolver.Timeout:
    print("Timeout exception while fetching TXT data (Timeout).")

# CNAME Lookup
try:
    for cname in dns.resolver.resolve(domain, 'CNAME'):
        print("CNAME Record: ", cname.target)

except KeyboardInterrupt:
    print("Scan was cancelled.")
except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
    print("NoAnswer exception while fetching CNAME data (no record or server offline).")
except dns.resolver.Timeout:
    print("Timeout exception while fetching CNAME data (Timeout).")

print("Domain DNS check complete.")
