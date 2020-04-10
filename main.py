import scrape_conditions
import check_conditions


def main():

    # Scraping Skeleton Bay Conditons
    url = 'https://magicseaweed.com/Skeleton-Bay-Surf-Report/4591/?model=38'
    soup = scrape_conditions.get_HTML(url)

    # Scraping & Separating Swell size and period
    swell_list = scrape_conditions.scrape_swell(soup)

    swell_size = scrape_conditions.separate_swell_size(swell_list)

    swell_period = scrape_conditions.separate_swell_period(swell_list)

    # Scraping & Cleaning swell direction
    swell_dir_list1 = scrape_conditions.scrape_swell_direction_end(soup)
    swell_dir_list = scrape_conditions.scrape_swell_direction_initial(soup, swell_dir_list1)

    swell_direction_string = scrape_conditions.toList(swell_dir_list)

    clean_swell_direction_string = scrape_conditions.clean_string(swell_direction_string)

    swell_direction = scrape_conditions.string_to_list(clean_swell_direction_string)

    # Checking Conditions list of Swell size, period & direction
    swellsize_matrix = check_conditions.check_conditions(swell_size, 3, 10)
    swellperiod_matrix = check_conditions.check_conditions(swell_period, 9, 15)
    swelldirection_matrix = check_conditions.check_conditions(swell_direction, 180, 270)

    # Checking All condition matrices
    swell_variable_check = check_conditions.all_swellconditions_check(swellsize_matrix, swellperiod_matrix, swelldirection_matrix)
    print(swell_variable_check)

if __name__ == '__main__':
    main()
