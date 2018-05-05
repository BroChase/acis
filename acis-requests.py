import datacollection


if __name__ == '__main__':

    # Washington
    # Kittatas 53037
    # Chelan 53007
    # Pierce 53053
    # Yakima 53077
    # Watcom 53073
    # Clallam 53009
    # Okanogan 53047
    # ['53037', '53007', '53053', '53077', '53073', '53009', '53047']

    # Montana
    # Gallatin 30031
    # Jefferson 30043
    # Beverhead 30001
    # Ravalli 30081
    # Mineral 30061
    # Sanders 30087
    # Broadwater 30007
    # Lewis and Clark 30049
    # ['30031', '30043', '30001', '30081', '30061', '30087', '30007']

    # Colorado
    # ['08113', '08091', '08111', '08067', '08053', '08079','08109', '08049', '08037', '08051','08065', '08097', '08117',
    # '08107', '08057', '08069', '08013', '08019']

    FIPS_ids = ['08113', '08091', '08111', '08067', '08053', '08079', '08109', '08049', '08037', '08051','08065', '08097',
                '30031', '30043', '30001', '30081', '30061', '30087', '30007', '08107', '08057', '08069', '08013', '08019',
                '08117', '53037', '53007', '53053', '53077', '53073', '53009', '53047']

    # To collecting span years
    # startdate = 1990
    # 'how many years to collect after startdate
    # years = 26
    #datacollection.multi_year_data(FIPS_ids, startdate, years)

    datacollection.single_year_data(FIPS_ids)