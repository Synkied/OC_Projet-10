#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

/usr/bin/wget https://fr.openfoodfacts.org/data/fr.openfoodfacts.org.products.csv -O /home/quentin/nutellove_project/fr.openfoodfacts.org.products.csv && cd /home/quentin/nutellove_project && /home/quentin/virtualenvs/nutellove/bin/python3 /home/quentin/nutellove_project/csv_cleaner.py && cd /home/quentin/nutellove_project && /home/quentin/virtualenvs/nutellove/bin/python3 /home/quentin/nutellove_project/db_feeding.py
