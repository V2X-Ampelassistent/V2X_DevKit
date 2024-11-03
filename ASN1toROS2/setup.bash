#!/bin/bash

# Set Working directory as Folder of file.
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

# create and go to resource folder
mkdir rsc
cd rsc

# clone Etsi git repositories
git clone https://forge.etsi.org/rep/ITS/asn1/is_ts103301.git
git clone https://forge.etsi.org/rep/ITS/asn1/cdd_ts102894_2.git

# collect needed .asn files
mkdir ETSI

# make one big asn
cd is_ts103301
python3 asn2raw.py DSRC.asn >> ../ETSI/DRSC.asn
python3 asn2raw.py MAPEM-PDU-Descriptions.asn >> ../ETSI/MAPEM-PDU-Descriptions.asn
python3 asn2raw.py SPATEM-PDU-Descriptions.asn >> ../ETSI/SPATEM-PDU-Descriptions.asn
python3 asn2raw.py ../cdd_ts102894_2/ETSI-ITS-CDD.asn >> ../ETSI/ETSI-ITS-CDD.asn
