import sqlite3
from dataclasses import dataclass

@dataclass
class ABPerson:
    first: str
    last: str
    guid: str
    note: str
    created: str
    modified: str


db = sqlite3.connect("AddressBook.sqlitedb")

curr = db.cursor()

COCOA_CONST = 978307200

sql = f"select first, last, guid, Note," \
      f"datetime(CreationDate + {COCOA_CONST}, 'UNIXEPOCH') as Created, " \
      f"datetime(ModificationDate + {COCOA_CONST}, 'UNIXEPOCH') as Modified " \
      f"from ABPerson"

person_dict = {}

for result in curr.execute(sql).fetchall():
    first, last, guid, note, created, modified = result
    ab_person = ABPerson(first, last, guid, note, created, modified)
    person_dict[guid] = ab_person

print(person_dict)

changes = []

sql = "select type, guid, sequence_number from ABPersonChanges order by sequence_number"

CHANGE_ENUM = {0: 'CREATED', 1: 'MODIFIED', 2: 'DELETED'}

print("Seq\tDatetime\tChange\tGUID\tName\tNote")

for result in curr.execute(sql).fetchall():
    change_type, person_guid, sequence_number = result
    change = CHANGE_ENUM[change_type]

    if person_guid in person_dict:
        ab_person = person_dict[person_guid]
        person_name = f"{ab_person.first} {ab_person.last}"
        note = ab_person.note
        if note is not None:
            note = note.replace("\n", " | ")
        if change_type == 0:
            time_of_change = ab_person.created
        else:
            time_of_change = ab_person.modified

    else:
        person_name = "UNKNOWN"
        time_of_change = "UNKNOWN"
        note = ""

    print(f"{sequence_number}\t{time_of_change}\t{change}\t{person_guid}\t{person_name}\t{note}")