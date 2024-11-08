#!/bin/bash

# Set Working directory as Folder of file.
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

rm msg/*.msg
rm generated.py
# make shure to import ETSI-ITS-CDD last, as it might have duplicate messages that will be ignored this way.
./main.py rsc/ETSI/DRSC.asn rsc/ETSI/MAPEM-PDU-Descriptions.asn rsc/ETSI/SPATEM-PDU-Descriptions.asn rsc/ETSI/ETSI-ITS-CDD.asn
# ./main.py test.asn