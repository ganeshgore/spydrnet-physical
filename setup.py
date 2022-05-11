import sys
import setuptools
import glob
from os import path

if sys.argv[-1] == "setup.py":
    print("To install, run 'python setup.py install'")
    print()

if sys.version_info[:2] < (3, 5):
    python_version = "{}.{}".format(sys.version_info[0], sys.version_info[1])
    msg = (
        "SpyDrNet 1.0+ requires Python 3.5 or later ({} detected).\n\n".format(
            python_version)
    )
    sys.stderr.write(msg + "\n")
    sys.exit(1)

# Write the version information.
sys.path.insert(0, 'spydrnet_physical')
import release
version = release.update_versionfile()
sys.path.pop(0)

with open("README.rst", "r") as fh:
    long_description = fh.read().replace(':ref:', '')

example_verilog_netlist = list()
folder_path = path.normpath(
    path.join( path.dirname(__file__), "spydrnet_physical", "support_files"))
for filename in glob.glob(path.join(folder_path, "**", "*"), recursive=True):
    if path.isfile(filename) and path.getsize(filename) < 1024 * 10:
        example_verilog_netlist.append(
            "support_files/" +
            str(filename)[len(folder_path) + 1:].replace('\\', '/'))

extras_require = {
    "all": [
        "pytest",
        "ply",
        "websock",
        "svgwrite",
        "ipython"
    ],
    "pytest": ["pytest"],
    "ply": ["ply"],
}

if __name__ == "__main__":

    setuptools.setup(
        name=release.name.lower(),
        version=version,
        maintainer=release.maintainer,
        maintainer_email=release.maintainer_email,
        author=release.authors['gore'][0],
        author_email=release.authors['gore'][1],
        description=release.description,
        keywords=release.keywords,
        long_description=long_description,
        license=release.license,
        platforms=release.platforms,
        url=release.url,
        project_urls=release.project_urls,
        classifiers=release.classifiers,
        package_data={'spydrnet_physical': [
            'VERSION'] + example_verilog_netlist},
        packages=setuptools.find_packages(),
        extras_require=extras_require,
        dependency_links=[
            "git+git://https://github.com/ganeshgore/spydrnet/main",
        ],
        python_requires='>=3.5',
        zip_safe=False,
        entry_points={
            'console_scripts': [
                'sdnphy = spydrnet_physical.util.shell:launch_shell',
                'clean_gsb = spydrnet_physical.util.clean_gsb:clean_gsb',
            ],
        },
    )
