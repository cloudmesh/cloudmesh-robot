
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
        complete = False
        record = dict([ (k, None) for k in self._required.keys()])
        with open(self._inventory) as inv:
            for line in inv:
                line = line.replace("'", "")
                if line and line[0] != "#":
                    if unicode(line[0], 'utf-8').isnumeric():
                        record = dict([ (k, None) for k in self._required.keys()])
                        complete = False
                    else:
                        pair = line.split(':', 1)
                        try:
                            record[pair[0].strip()] = pair[1].strip()
                            if all(map(lambda x: not isinstance(x, type(None)), record.values())) and not complete:
                                self._write(record, path, dhcp)
                                complete = True
                        except IndexError:
                            pass

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
