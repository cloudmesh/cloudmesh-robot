import yaml

class NetworkInventory(object):
    def __init__(self, path):
        self._inventory = path
        self._required = {"name": False, "mac": False, "ip": False}

    def export(self, path):
        with open(path, 'w') as dhcp:
            dhcp.truncate()
            dhcp.write("subnet 10.0.0.0 netmask 255.255.0.0 {\n")
            dhcp.write("  option subnet-mask 255.255.0.0;\n")
            dhcp.write("  range 10.0.1.10 10.0.1.254;\n\n")
        
            self._create_records(path, dhcp)
        
            dhcp.write("}\n")

    def _create_records(self, path, dhcp):
        with open(self._inventory) as inv:
            ls = yaml.safe_load(inv)
            for k, entry in ls.items():
                if all([x in entry for x in self._required]):
                    self._write(entry, path, dhcp)
                else:
                    raise KeyError("Badly formatted inventory in item {}".format(k))

    def _write(self, record, path, dhcp):
        if record:
            dhcp.write("  host {} {{\n".format(record["name"]))
            dhcp.write("    hardware ethernet {};\n".format(record["mac"]))
            dhcp.write("    fixed-address {};\n".format(record["ip"]))
            dhcp.write("  }\n")

if __name__ == "__main__":
    import sys
    assert(len(sys.argv) == 3)
    inv = NetworkInventory(sys.argv[1])
    inv.export(sys.argv[2])
