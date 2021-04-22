minRegionId = -1
maxRegionId = 1
minRingId = 1
maxRingId = 3
minStationId0 = 0
minStationId = 1
# in the detId there is space to go up to 5 stations. Only 3 implemented now (0,1,2)
maxStationId = 2
minChamberId = 0
maxChamberId = 36
minLayerId = 0  # LayerId = 0 is superChamber
maxLayerId0 = 6
maxLayerId = 2  # GE1/GE2 has 2 layers
minEtaPartitionId = 0
maxEtaPartitionId = 16
minRollId = minEtaPartitionId
maxRollId = maxEtaPartitionId
RegionNumBits = 2
RegionStartBit = 0
RegionMask = 0x3
RingNumBits = 3
RingStartBit = RegionStartBit + RegionNumBits
RingMask = 0x7
StationNumBits = 3
StationStartBit = RingStartBit + RingNumBits
StationMask = 0x7
ChamberNumBits = 6
ChamberStartBit = StationStartBit + StationNumBits
ChamberStartBitM = RegionStartBit + RegionNumBits
ChamberMask = 0x3F
LayerNumBits = 5
LayerNumBitsP = 2
LayerStartBit = ChamberStartBit + ChamberNumBits
LayerStartBitM = ChamberStartBitM + ChamberNumBits
LayerMask = 0x1F
LayerMaskP = 0x3
EtaPartitionNumBits = 5
EtaPartitionStartBit = LayerStartBit + LayerNumBits
EtaPartitionStartBitP = LayerStartBit + LayerNumBitsP
EtaPartitionStartBitM = LayerStartBitM + LayerNumBits
EtaPartitionMask = 0x1F
FormatNumBits = 1
FormatStartBit = EtaPartitionStartBit + EtaPartitionNumBits
FormatMask = 0x1
kGEMIdFormat = 0x1000000
kMuonIdMask = 0xF0000000

kDetMask = 0xF
kSubdetMask = 0x7
kDetOffset = 28
kSubdetOffset = 25
det = 2 # muon
subdet = 4 # gem sub det

def GEMDetId(region, ring, station, layer, chamber, ieta):
    regionInBits = region - minRegionId
    ringInBits = ring - minRingId
    stationInBits = station - minStationId0
    layerInBits = layer - minLayerId
    chamberInBits = chamber - (minChamberId + 1)
    ietaInBits = ieta
    id_ = (((det & kDetMask) << kDetOffset) | ((subdet & kSubdetMask) << kSubdetOffset))
    id_ |= ((regionInBits & RegionMask) << RegionStartBit | (ringInBits & RingMask) << RingStartBit |
           (stationInBits & StationMask) << StationStartBit | (layerInBits & LayerMask) << LayerStartBit |
           (chamberInBits & ChamberMask) << ChamberStartBit | (ietaInBits & EtaPartitionMask) << EtaPartitionStartBit |
           kGEMIdFormat)
    return id_

for i in range(128*3):
    print(GEMDetId(1,1,1,1,1,1),i)
    print(GEMDetId(-1,1,1,1,20,8),i)
