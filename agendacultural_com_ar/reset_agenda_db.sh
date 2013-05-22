#!/bin/bash

./manage.py sqlclear agenda > /tmp/clearagendadb.sql
psql agendacultural_db -f /tmp/clearappdb.sql
./manage.py syncdb
