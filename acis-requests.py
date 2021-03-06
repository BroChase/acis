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

    # FIPS_ids = ['08113', '08091', '08111', '08067', '08053', '08079', '08109', '08049', '08037', '08051','08065', '08097',
    #             '30031', '30043', '30001', '30081', '30061', '30087', '30007', '08107', '08057', '08069', '08013', '08019',
    #             '08117', '53037', '53007', '53053', '53077', '53073', '53009', '53047']
    # FIPS_ids = ['08037', '08049', '08051', '08053', '08057', '08065',
    #             '08067', '08069', '08079', '08091', '08097', '08107',
    #             '08109', '08111', '08113', '08117', '08013', '08015',
    #             '08019', '30001', '30007', '30031', '30043', '30061',
    #             '30081', '30087', '53007', '53009', '53037', '53047',
    #             '53053', '53073', '53077']

    FIPS_ids = ['24023', '42001', '26139', '30031', '36009', '30063', '35027', '51125', '55141', '49005', '41043',
                  '08045', '26047', '16003', '06043', '41063', '34003', '26053', '08113', '55031', '53009', '27157',
                  '53037', '36105', '56039', '50001', '36113', '16049', '08015', '55127', '53073', '08019', '23003',
                  '36069', '26061', '55095', '36023', '16013', '18029', '56001', '36031', '42011', '26029', '50015',
                  '35007', '55061', '30013', '26159', '26083', '55133', '42055', '55131', '30001', '04019', '17031',
                  '53033', '49049', '16005', '49035', '49043', '23001', '25011', '27145', '27163', '26135', '23021',
                  '50021', '06057', '26125', '33019', '08049', '23025', '50025', '01049', '33003', '50023', '35055',
                  '37189', '08007', '55117', '06093', '06071', '19155', '54075', '04001', '36111', '08107', '55097',
                  '33009', '26145', '39085', '55063', '23005', '39139', '56035', '55067', '16079', '36025', '41037',
                  '26103', '38019', '08013', '08067', '23007', '53047', '53063', '06037', '26071', '26005', '27049',
                  '09003', '41059', '30049', '33007', '16031', '39091', '42027', '48041', '16035', '32031', '42111',
                  '36039', '55025', '55059', '08097', '42025', '42049', '32003', '25009', '37087', '42003', '29189',
                  '30009', '16025', '06061', '53065', '36019', '36065', '27041', '29165', '08111', '36043', '33013',
                  '38059', '38009', '36067', '30081', '53041', '16017', '56023', '55081', '27061', '36045', '27007',
                  '36013', '42089', '08117', '35035', '55111', '08077', '08065', '37115', '50005', '30039', '06017',
                  '25021', '09005', '23017', '26131', '04005', '27031', '30057', '35028', '06019', '51017', '51171',
                  '19015', '26089', '30053', '25003', '56025', '33001', '36035', '17043', '19061', '16051', '17085',
                  '41027', '41005', '26165', '44009', '50007', '42103', '08037', '23019', '33011', '36033', '55021',
                  '08051', '53007', '41035', '06109', '09001', '26055', '26137', '42069', '53013', '27013', '25017',
                  '36029', '27005', '18117', '23013', '50027', '33005', '50019', '42009', '30029', '39153', '19153',
                  '26081', '25027', '55109', '42115', '06051', '49021', '25013', '41001', '26009', '46099', '27053',
                  '06003', '06029', '55073', '27137', '49057', '26093', '17161']

    print(len(FIPS_ids))

    # To collecting span years
    startdate = 1990
    # 'how many years to collect after startdate
    years = 26
    # datacollection.multi_year_data(FIPS_ids, startdate, years)

    datacollection.single_year_data(FIPS_ids)