Changes
=======

0.20 (2019-12-03)
-----------------

* Drop wrong signature certificates with message and without failing.

0.19 (2019-08-03)
-----------------

* Fix download auto retrying function.


0.18 (2019-08-02)
-----------------

* Add download auto retrying function.

0.17 (2019-06-07)
-----------------

* Fix checksum verification of downloaded data when `.read()` is used.

0.16 (2018-06-15)
-----------------

* Verify checksum of downloaded data.
* Make indexing optional when uploading from command-line.

0.15 (2017-06-09)
-----------------

* Add support for Python 3.
* cli: new --suffix-key option.

0.14.5 (2015-09-25)
-------------------

* Support shacache-ca-file and shadir-ca-file options in networkcachehelper.

0.14.4 (2015-09-24)
-------------------

* Add shacache-ca-file and shadir-ca-file options, that are
  required to use a self-signed server certificate in python >= 2.7.9.

0.14.3 (2015-09-07)
-------------------

* Make information dict use str instead of unicode.

0.14.2 (2014-10-09)
-------------------

* Compatibility with pyOpenSSL >= 0.14

0.14.1 (2014-03-17)
-------------------

* Use 'openssl' executable if pyOpenSSL is not available.

0.14 (2013-07-12)
-----------------

* New scripts to download & upload manually from command line.
* Small API changes. `slapos.networkcachehelper` is deprecated.
* Many bugfixes and code cleanup.
* Performance/reliability improvements, by:

  - using `pyOpenSSL` instead of spawning `openssl` subprocesses
  - reducing the number of created temporary files

0.13.4 (2013-05-13)
-------------------

* Define timeouts for every connection we initiate. May allow not to hang
  forever in a hostile environment when connection to networkcache server
  can stall / be reset.

0.13.3 (2012-12-11)
-------------------

* Don't use logger.debug() but logger.info() in helpers so that it doesn't.
  silent an error.

0.13.2 (2012-09-04)
-------------------

* Fix regression where multiple certificates caused most of them to be
  ignored.

0.13.1 (2012-09-04)
-------------------

* Correctly return False if no entry is found while downloading.

0.13 (2012-09-02)
-----------------

* Add high-level helper functions to easily download/upload to networkcache.
* Set timeout in httplib connections.
* networkcache won't stupidly loop for 1000 iterations if "certificate"
  parameter is a string instead of a list.

0.12 (2012-02-09)
-----------------

* Binary cache support.

0.11 (2011-12-14)
-----------------

* If given key has multiple *signed* values pick up the first one.

0.10 (2011-09-05)
-----------------

* Create infinite certificates.

0.9 (2011-09-02)
----------------

* Bugfix: Do not trust received content.

0.8 (2011-09-02)
----------------

* Bugfix: Do not try to validate against empty signatures.

0.7 (2011-09-02)
----------------

* Remove M2Crypto dependency and rely on openssl binary presence.
* Fix signing and verification.
* Simplify key generation and use slapos.cfg file by default.
* Internals: Increase test coverage.

0.6 (2011-08-31)
----------------

* Authentication keys are supported.

0.5 (2011-08-25)
----------------

* Re-implemente signature support.
* Follow corrected specification.
* internals: Use urllib2.

0.4 (2011-08-10)
----------------

* Implement signature checking of downloaded content.

0.3 (2011-08-03)
----------------

* Deal with proxy in correct way.

0.2 (2011-07-01)
----------------

* Incompatible change: NetworkcacheClient.download returns opened temporary
  file object, which will be deleted on close. This minimises memory footprint.
* Minimise memory footprint during upload.
* Use PUT instead of POST during upload.

0.1 (2011-06-23)
----------------

* Initial version.

