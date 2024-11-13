### V2X Daten weiterleiten:

Zum Weiterleiten der V2X Daten per UDP auf dem Cohda Device:

```bash
/opt/cohda/test/runtest_monitor.sh 180 192.168.1.1 target
```

### GPS Daten weiterleiten:

Zunächst muss auf dem NUC der Port geöffnet werden, dazu
```bash
suco socat - UDP-Listen:37010,crlf
```
aufrufen **oder** den GPS Publisher mit
```bash
ros2 run v2x_cohdatoros GPS_Publisher
```
starten.

Auf dem Cohda-device können nun die GPS Daten per UDP weitergeleitet werden:
```bash
gpspipe -w | socat - UDP:192.168.101.121:37010
```

### Portbelegung bei der Weiterleitung:

Ports am NUC zum empfangen der Daten:

| Port  | Daten |
|-------|-------|
| 37008 |  DSRC |
| 37010 |   GPS |

### Aufzeichnen der Daten:

Zum aufzeichen auf dem NUC:
```bash
sudo tcpdump -i eno1 -w test.pcap
```

Für die Aufzeichnung auf dem Cohda-Device wurde auf dem Cohda-Device ein Verzeichnis für aufnahmen angelegt (```/home/user/recordings```).

### Zum filtern der Daten:

```bash
tshark -r <InputFile.pcap> -w <OutputFile.pcap> -Y <Filter, z.B. "UDP">
```