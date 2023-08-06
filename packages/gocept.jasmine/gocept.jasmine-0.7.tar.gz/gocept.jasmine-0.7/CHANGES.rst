=============================
Change log for gocept.jasmine
=============================

0.7 (2019-12-09)
================

- Remove version pinnings in buildout as this is a library which should
  run with the newest versions of its dependencies.

- Add a simple self test.

- Require ``pytest < 5`` to keep Python 2 support.

- Migrate to Github.

- Support Python 3.7 and 3.8.


0.6 (2017-03-21)
================

- Update to fanstatic 1.0a to use minifier.

- Ensure compatibility with `setuptools >= 30.0`.


0.5.1 (2014-06-10)
==================

- The last two releases (0.4 and 0.5) were brown bag releases, so we need to make a new one.


0.5 (2014-06-10)
================

- Add JS library to mock ajax calls during jasmine tests.


0.4 (2014-06-06)
================

- Make it possible to run multiple TestApps.


0.3 (2013-08-27)
================

- Fixed a problem where the testrunner finished `sucessfully` before all
  jasmine tests finished in browser.


0.2 (2013-08-17)
================

- Added helper function to ease test layer setup.

- Made it easier to debug jasmine tests in the browser.


0.1 (2013-08-16)
================

initial release
