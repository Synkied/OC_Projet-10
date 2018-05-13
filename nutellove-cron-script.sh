#!/bin/bash

sudo /usr/bin/wget https://fr.openfoodfacts.org/data/fr.openfoodfacts.org.products.csv -O /home/quentin/nutellove_project/fr.openfoodfacts.org.products.csv ; /home/quentin/virtualenvs/nutellove/bin/python3 /home/quentin/nutellove_project/csv_cleaner.py ; /home/quentin/virtualenvs/nutellove/bin/python3 /home/quentin/nutellove_project/db_feeding.py
