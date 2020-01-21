SELECT name
FROM customer_tab WHERE dob IN
( SELECT dob
  FROM customer_tab
  order by dob desc limit 1
);