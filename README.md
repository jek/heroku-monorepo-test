Multi-app monorepo test.


This test uses two apps, jek-monorepo-yellow and jek-monorepo-green. The two are
configured as below, with monorepo buildpack and a debugging buildpack to verify
the build environment. A Heroku remote is added for each app. Example below for
yellow:

    $ heroku buildpacks -a jek-monorepo-yellow
    === jek-monorepo-yellow Buildpack URLs
    1. https://github.com/lstoll/heroku-buildpack-monorepo
    2. https://github.com/jek/heroku-buildpack-recorder
    3. heroku/python
    $ heroku config:set -a jek-monorepo-yellow APP_BASE=yellow
    $ git remote add yellow https://git.heroku.com/jek-monorepo-yellow.git


