import sqlite3

import pandas as pd

if __name__ == '__main__':
    address_company = pd.read_csv('AddressCompany.csv', delimiter=';')
    address_building = pd.read_csv('AddressBuilding.csv', delimiter=';')
    company = pd.read_csv('Company.csv', delimiter=';')

    address_building_company = pd.merge(address_building, address_company, how='outer', on=['AddressCode'])
    company_address = pd.merge(address_building_company, company, how='outer', on=['CompanyIN'])
    company_address = company_address[company_address['AddressText'].notna()]
    print(company_address.head())
    company_address.to_csv('companies_info.csv', index=False)

    # Delete buildings for living with supermarket on the first flour
    offices = company_address[company_address['UsageCode'] != 3]  # objekt k bydleni
    offices = offices[offices['UsageCode'] != 6]  # bytovy dum
    offices = offices[offices['UsageCode'] != 7]  # rodinny dum
    # Delete theaters etc.
    offices = offices[offices['UsageCode'] != 5]  # objekt obcanske vybavenosti

    big_companies = offices[offices['EmployeeLowerBound'] >= 100].reset_index()
    big_companies_addresses = big_companies.AddressText.unique()

    other_companies = offices.loc[~offices['AddressText'].isin(big_companies_addresses)]
    other_companies_addresses = other_companies.AddressText.unique()

    offices = list(big_companies_addresses) + list(other_companies_addresses)
    companies_in_offices_buildings = company_address[company_address['AddressText'].isin(offices)].reset_index(
        drop=True)
    companies_in_offices_buildings.to_csv('companies_in_office_buildings.csv', index=False)
    print("Number of office buildings: ", len(offices))

    # In this case it is NOT necessary to store the results in DB, because we are not going to use it again.
    conn = sqlite3.connect('test.db')
    companies_in_offices_buildings.to_sql('CompaniesInOfficeBuildings', conn, if_exists='replace', index=False)
