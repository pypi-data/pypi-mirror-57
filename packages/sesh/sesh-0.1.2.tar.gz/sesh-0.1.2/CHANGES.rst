
==========
Change Log
==========

0.1.1
-----

Changes:
~~~~~~~~

- Sesh now has full support for user login sessions.
    - Only one user may be logged-in at a time.
    - User roles are supported.
    - User roles include Staff, Instructor, and Student.
    - Users cannot yet be created, but 26 of them can be loaded in the
      sample data set.
    - The password for all sample users is ``mUs1caL*``
    - Users are automatically logged-out after five minutes of inactivity.


0.0.5
-----

Changes:
~~~~~~~~

- Revised data model (new/updated DB schema).


0.0.4
-----

Changes:
~~~~~~~~

- Fleshed-out Command Line Interface.
- Now creating SQLite DB as part of install.
- Added 'Role' to data model.

0.0.3
-----

Changes:
~~~~~~~~

- Added user and init_db modules.
- Revised base_config module.
- Updated data model.


0.0.2
-----

Changes:
~~~~~~~~

- Minor edits to remove references to old names.
- Added initial documentation.


0.0.1
-----

Changes:
~~~~~~~~

- Initial version.
