# Main script to run everything

from schema import create_table
from seed_data import seed_data
from queries import query_common_treatments

if __name__ == '__main__':
    create_table()
    seed_data()
    query_common_treatments