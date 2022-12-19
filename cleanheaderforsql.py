#!/bin/python3
#import 




def normalize_header( header_old ):
    header_new = []


    # TOO COMPACT forloop
    # [header_new.insert( 1, ''.join(filter(str.isalnum, i)) ) for i in header_old]

    for i in header_old:
        j = ''.join(filter(str.isalnum, i))
        header_new.insert( len(header_new), j )
    return(header_new)

if __name__ == '__main__':
    h = "BTS.,Site,CellCode,Sector,CellVersion,SID,SwitchNo,Latitude(DecDeg),Longitude(DecDeg),Site Name,Band,CBSC_ECP_BSC,ChannelNo,PN Ref.,PN,Azimuth,Dwntilt(Deg),Ant type,Ant Bw(deg),Ant gain (dBi),cable loss(dB),Antenna c/l (m),AMSL (m),PN Increment,Air Interface,Broadcast SID,Network ID,APIP Address,CLLI Code,VSM CLLI Code,EVDO BSC RNC,Vendor,MTX,Service Node,V Ant Bw(deg),PCI Grp Index,PCI Index,LTE TAC,LTE Mkt ID,eNodeB Sector ID,EVDO SectorID,PS Loc Code,Ant Elec Tilt(deg),Ant Tip Height (feet),Location ID,Transmission Type,Remote Radio Head,Remote Radio Head Model Name,Tower Top Amplifier,Tower Top Amplifier Model Name,LTE Cell Type,FIPS,LTE Total Pwr (W),Num Tx Antennas,Num Rx Antennas,eNodeB Cell Name,eNodeB Cell Alias,ECGI,RET (deg),E-911 Latitude (NAD83),E-911 Longitude (NAD83),Compliance Min Allowed Elec Tilt (deg),Compliance Max Allowed Elec Tilt (deg),Max Power for RFE (Watts),Max Allowed Power Setting,gNB DU ID"
    h_old = h.split(',')
    h_new = normalize_header( h_old )
#    print(h_old)
#    print(h_new)

    for x, y in zip(h_old, h_new):
        print(f"{x} -> {y}")

