#!/bin/bash

###################################################
# First Bash Shell script to execute psql command
###################################################

#Set the value of variable
database="customer_db"

#Execute few psql commands:
#Note: you can also add -h hostname -U username in the below commands.
psql -c "SELECT 'CREATE DATABASE customer_db' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'customer_db')\gexec"
psql -d $database -c "CREATE TABLE public.customer_tab(id serial PRIMARY KEY,name character(255) NOT NULL,dob date NOT NULL,created_at bigint NOT NULL,updated_at bigint NOT NULL,is_deleted smallint NOT NULL,)"
psql -d $database -c "INSERT INTO public.customer_tab (name, dob, created_at, updated_at, is_deleted) VALUES ('Anvesh', '1999-11-11', 1579534969, 1579534969, 0), ('Neevan', '1996-12-12', 1579535007, 1579535007, 0),('Roy', '1992-09-09', 1579535354, 1579535354, 0)"

