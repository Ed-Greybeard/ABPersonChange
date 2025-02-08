# ABPersonChange
A quick and dirty Python script to track AGPersonChange from iOS AddressBook.sqlitedb.

## Assumptions made:
 - Type 0 is create (tested OK)
 - Type 1 is modify (tested OK but seems to modify for each create)
 - Type 2 is delete (tested OK)

The datetime of each entry is based on the corresponding account GUID in ABPerson.