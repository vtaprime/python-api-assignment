#!/bin/bash

###################################################
# Bash Shell script to execute psql command to create db, create table and insert some data
###################################################

#Execute few psql commands:
psql -h $DB_HOST -p $DB_PORT -d postgres -U $DB_USER -W -c "DROP DATABASE IF EXISTS customer_db"
psql -h $DB_HOST -p $DB_PORT -d postgres -U $DB_USER -W -c "CREATE DATABASE customer_db"
psql -h $DB_HOST -p $DB_PORT -d $DB_NAME -U $DB_USER -W -c "CREATE TABLE public.customer_tab(id serial PRIMARY KEY,name character(255) NOT NULL,dob date NOT NULL,created_at bigint NOT NULL,updated_at bigint NOT NULL,is_deleted smallint NOT NULL)"
psql -h $DB_HOST -p $DB_PORT -d $DB_NAME -U $DB_USER -W -c "INSERT INTO public.customer_tab (name, dob, created_at, updated_at, is_deleted) VALUES ('Anvesh', '1999-11-11', 1579534969, 1579534969, 0), ('Neevan', '1996-12-12', 1579535007, 1579535007, 0),('Roy', '1992-09-09', 1579535354, 1579535354, 0)"
