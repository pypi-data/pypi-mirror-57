###########################
lsst-sphinx-bootstrap-theme
###########################

.. image:: https://img.shields.io/travis/lsst-sqre/lsst-sphinx-bootstrap-theme.svg
   :alt: Travis build status

This is a prototype Sphinx theme for LSST Stack documentation, based on the Astropy Sphinx theme.

Getting started with development
================================

Get the repo::

    git clone https://github.com/lsst-sqre/lsst-sphinx-bootstrap-theme
    cd lsst-sphinx-bootstrap-theme

Install JavaScript dependencies::

    npm install -g gulp-cli
    npm install

Compile the assets and continue watching for changes::

    gulp

.. _codebase:

Codebase orientation
====================

- ``lsst_sphinx_bootstrap_theme/`` is the theme's Python package

  - ``static/`` is for static assets deployed onto the site. ``app.css`` is generated with ``gulp``, so don't edit it directly.

  - ``layout.html`` is the main Jinja2 template for the HTML. The other HTML files are blocks/partials.

- ``scss/`` contains Sass source files that get compiled into ``lsst_sphinx_bootstrap_theme/static/app.css``.

.. _gulp-commands:

Gulp commands
=============

This project uses Gulp_ to run its build pipelines.
This section describes the gulp commands you can run.

gulp
----

Use this default command for development.
It does the following:

- `sass <#gulp-scss>`__ (compile Sass)
- Watches for changes and recompiles assets as necessary.

.. _gulp-scss:

gulp scss
---------

Compile Sass into CSS (``app.css``).
We use the following features:

- Compile Sass.
- Add prefixes to CSS using Autoprefixer_ (via PostCSS_).
- Clean and compress the CSS using gulp-clean-css.

You can run this task alone, but usually through ``gulp`` (default task).

.. _gulp-pretty:

gulp pretty
-----------

Automatically format code.
See `Code style via Prettier <#code-style>`__.

.. _code-style:

Code style via Prettier
=======================

This project uses Prettier_ to make sure the Sass and JavaScript are formatted as you'd expect.
Like most projects, we use Prettier_ nearly as-is.
A couple minor exceptions are configured in ``.prettierrc.yaml``.

You can run Prettier_ two ways:

1. Manually, by running `gulp pretty <gulp-pretty>`__.
2. Automatically, by committing code.
   This is configured as a pre-commit hook in ``package.json``.

Note that `Prettier's`_ pre-commit hook and chunked git commits don't mix.
You'll want to manually run Prettier_ before committing a subset of the changed lines in your files.

.. _release-process:

Release process
===============

1. Update the change log (``CHANGELOG.rst``), commit, and marge work to ``master``.

2. Tag the release using a `PEP 440`_\ -compatible version string::

      git tag -s X.Y.Z -m "X.Y.Z"

   Push the tag::

      git tags --push

The Travis CI pipeline will create and upload the release to PyPI.

.. _`Prettier's`:
.. _Prettier: https://prettier.io
.. _Gulp: https://gulpjs.com
.. _Webpack: https://webpack.js.org
.. _Autoprefixer: https://github.com/postcss/autoprefixer/
.. _PostCSS: https://postcss.org
.. _gulp-clean-css: https://www.npmjs.com/package/gulp-clean-css
.. _PEP 440: https://www.python.org/dev/peps/pep-0440/
