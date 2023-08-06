
==========
Change Log
==========


0.2.3
-----

Changes:
~~~~~~~~

- Fixed KeyError: 'SESH_SESSION_TIMEOUT' bug (again).


0.2.2
-----

Changes:
~~~~~~~~

- Fixed TypeError: '>' not supported between instances of 'int' and 'str'


0.2.1
-----

Changes:
~~~~~~~~

- Fixed KeyError: 'SESH_SESSION_TIMEOUT' bug.


0.2.0
-----

Changes:
~~~~~~~~

- Implemented the ``show account`` command. This command is used to show
  a ledger of billable class sessions for a particular month, using the
  ``-m mm-yyyy`` option. The ability to use the ``-p`` option, for specifying
  an arbitrary period of time has not yet been implemented.

- Fixed some bugs around user acccess permissions.

- Added the ``SESH_SESSION_TIMEOUT`` enironment variable specification so
  that a custom number of seconds may be specified before the User's
  session times-out. (The default is 300 seconds).

- Updated and added to the online documentation.


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
