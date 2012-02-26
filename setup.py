try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
import argonaut.lib.version as version

readme_file = open('README','r')
long_description = readme_file.read()
readme_file.close()

setup(
    name='Argonaut',
    version=version.VERSION,
    description='Lightweight Pylons powered blogging engine.',
    author='Jason Robinson',
    author_email='jaywink@basshero.org',
    url='http://www.basshero.org',
    download_url='http://pypi.python.org/pypi/Argonaut',
    install_requires=[
        "WebHelpers==1.1",
        "WebOb==0.9.8",
        "Pylons>=1.0",
        "SQLAlchemy>=0.5",
        "repoze.what-pylons",
        "repoze.what-quickstart",
        "hashlib",
        "TurboMail"
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'argonaut': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'argonaut': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = argonaut.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Environment :: Web Environment",
        "Framework :: Pylons",
        "Framework :: Paste",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI"
    ],
    keywords='python pylons blogging cms blog',
    license='FreeBSD',
    long_description = long_description
)
