# ABPersonChange
A quick and dirty Python script to track AGPersonChange from iOS AddressBook.sqlitedb.

There may be a time where you can recover notifications from iOS and either the name & phone number is inconsistent or does not now exist. This might be because the contact was subsequently deleted. The iOS AddressBook.sqlitedb tracks contact deletes in the ABPersonChange table, and so you should be able to match the ABPerson GUID of from the notification with the ABPerson GUID in the Addressbook. This should at least give you some idea about why you can't find that contact any more.

## Assumptions made:
 - Type 0 is create (tested OK)
 - Type 1 is modify (tested OK but seems to modify for each create)
 - Type 2 is delete (tested OK)

The datetime of each entry is based on the corresponding account GUID in ABPerson. Unfortunately there is only a single modified datetime associated with ABPerson, so any modification loses it's accurate date. I haven't had time to do only include the last modified time, so it just outputs it each time it finds a modification and leaves the rest up to you.

## Example Output
| Seq | Datetime | Change | GUID | Name |
|---|---|---|---|---|
|5|2025-02-07 21:12:21|CREATED|A001E905-8ACD-4AE2-86E7-A98B8AC1E895:ABPerson|Test1 Account|
|7|2025-02-07 21:16:52|MODIFIED|A001E905-8ACD-4AE2-86E7-A98B8AC1E895:ABPerson|Test1 Account|
|8|UNKNOWN|CREATED|3A94D5B2-DD5F-4391-BF94-278202035A75:ABPerson|UNKNOWN|
|10|UNKNOWN|MODIFIED|3A94D5B2-DD5F-4391-BF94-278202035A75:ABPerson|UNKNOWN|
|11|UNKNOWN|MODIFIED|3A94D5B2-DD5F-4391-BF94-278202035A75:ABPerson|UNKNOWN|
|12|2025-02-07 21:15:54|CREATED|77CD5B4F-E1D8-4EA1-96C7-58963BF4348E:ABPerson|Test3 Account|
|14|UNKNOWN|DELETED|3A94D5B2-DD5F-4391-BF94-278202035A75:ABPerson|UNKNOWN|
|15|2025-02-07 21:16:52|MODIFIED|A001E905-8ACD-4AE2-86E7-A98B8AC1E895:ABPerson|Test1 Account|
|16|2025-02-07 21:16:52|MODIFIED|A001E905-8ACD-4AE2-86E7-A98B8AC1E895:ABPerson|Test1 Account|
|17|2025-02-07 21:29:10|CREATED|AE8BF3E0-AE4D-4703-935A-432345993422:ABPerson|Derived Contact |
|19|2025-02-07 21:37:37|CREATED|C7B2B9EC-0238-421C-A259-518ABFD0693A:ABPerson|Edited Contact|
|21|2025-02-07 21:40:55|MODIFIED|C7B2B9EC-0238-421C-A259-518ABFD0693A:ABPerson|Edited Contact|
|22|2025-02-07 21:40:55|MODIFIED|C7B2B9EC-0238-421C-A259-518ABFD0693A:ABPerson|Edited Contact|
