Hackery is a python library that helps you track your hacks.

Before:
```python
if 'questionable_field' not in incoming_data:
     # this doesn't get set for some reason by version 1.4 of our iOS app
     incoming_data['questionable_field'] = 0 # HACK.
```

After:
```python
with VersionHack('ios-questionable-field', 'ios == 1.4', incoming_data) as hack:
    if hack:
        if 'questionable_field' not in incoming_data:
            hack.count('field-absent')
            incoming_data['questionable_field'] = 0
```

Keep your hacks **and** your sanity.
