from setuptools import setup, find_packages

def parse_requirements(req_file):
    """Parse a requirements.txt file to a list of requirements"""
    with open(req_file, 'r') as fb:
        reqs = [
            req for req in fb.readlines()
            if req.strip() and not req.startswith('#')
        ]
    return list(reqs)

install_requires = parse_requirements('requirements.txt')

setup(
    name='neb-tasks',
    author='OpenStax',
    author_email='info@cnx.org',
    url="https://github.com/openstax/neb-tasks",
    license='AGPL, See also LICENSE.txt',
    description='Content task addons to neb',
    install_requires=install_requires,
    entry_points={
        'neb.extension': 'tasks=nebtasks:load_modules',
    },
    packages=find_packages(),
    include_package_data=True
)