# Main script to run everything

from schema import create_tables
from seed_data import seed_data
from queries import query_common_treatments

if __name__ == '__main__':
    create_tables()
    seed_data()
    query_common_treatments