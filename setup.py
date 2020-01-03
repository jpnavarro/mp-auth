import os.path
import setuptools

# single source of truth for package version
version_ns = {}
with open(os.path.join('mp_auth', '__init__.py')) as f:
    exec(f.read(), version_ns)

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = []
with open('requirements.txt') as reqs:
    for line in reqs.readlines():
        req = line.strip()
        if not req or req.startswith('#'):
            continue
        install_requires.append(req)

setuptools.setup(
    name='mp-auth',
    version=version_ns['__version__'],
    description='Add Multi-provider auth for various providers',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Globus Team',
    author_email='support@globus.org',
    packages=setuptools.find_packages(),
    python_requires='>=3.0',
    install_requires=install_requires,
    include_package_data=True,
    keywords=['globus', 'django'],
    license='apache 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Communications :: File Sharing',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
