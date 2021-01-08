from ipaddress import IPv6Address

addr = IPv6Address('ff02::fa51%1')
print(addr.scope_id)
