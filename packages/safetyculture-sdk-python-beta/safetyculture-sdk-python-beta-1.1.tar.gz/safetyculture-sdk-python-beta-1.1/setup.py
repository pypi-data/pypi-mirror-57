from setuptools import setup

setup(name = 'safetyculture-sdk-python-beta',
      version = '1.1',
      description = 'iAuditor Python SDK and integration tools',
      url = 'https://github.com/SafetyCulture/safetyculture-sdk-python/tree/beta',
      author = 'SafetyCulture',
      author_email = 'edd.abrahamsen@safetyculture.io',
      include_package_data=True,
      packages = ['safetypy', 'tools', 'tools/exporter', 'tools/import_grs', 'tools/export_users', 'tools/sync_users'],
      entry_points = {
            'console_scripts': [
                  'iauditor_exporter = tools.exporter.exporter:main',
                  'import_grs = tools.import_grs.import_grs:main',
                  'export_users = tools.export_users.export_users:main',
                  'sync_users = tools.sync_users.sync_users:main'
            ],
      },
      python_requires='>=3.6',
      long_description=open('tools/exporter/README.md', 'r').read(),
      long_description_content_type="text/markdown",
      install_requires = [
            'python-dateutil>=2.5.0',
            'pytz>=2015.7',
            'tzlocal>=1.3',
            'unicodecsv>=0.14.1',
            'requests>=2.10.0',
            'pyyaml>=3.11',
            'future>=0.16.0',
            'xlrd>=1.1.0',
            'pyOpenSSL>=17.5.0',
            'dataset>=1.1.2',
            'SQLAlchemy>=1.3.4',
            'pandas>=0.24.2',
            'numpy>=1.16.4',
            'sqlalchemy-pyodbc-mssql>=0.1.0'
      ],
      )
