#  Copyright  2019 Alexis Lopez Zubieta
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.

from AppImageBuilder import drivers
from AppImageBuilder import tools


class DpkgDependency(drivers.Dependency):
    package_name = None

    def __init__(self, driver=None, source=None, target=None, package_name=None):
        super().__init__(driver, source, target)
        self.package_name = package_name

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, DpkgDependency):
            # don't attempt to compare against unrelated types
            return False

        return super().__eq__(o) and self.package_name == o.package_name

    def __str__(self):
        return super().__str__()


class Dpkg(drivers.Driver):
    id = 'dpkg'
    dpkg = None
    cache = {}

    # Base packages are will be excluded from the deploy list
    base_packages = {
        'minimal': [
            'ucf',  # Update Configuration File
            'coreutils',  # basic file, shell and text manipulation utilities of the GNU operating system.
            'dpkg',  # Debian package management system
            'debconf',  # Debian configuration management system
            'cdebconf',  # Debian configuration management system
            'sensible-utils',  # Utilities for sensible alternative selection
            'qtchooser',  # Wrapper to select between Qt development binary versions
        ],
    }

    default_base_packages = 'minimal'

    def __init__(self):
        self.dpkg = tools.Dpkg()

    def list_base_dependencies(self, app_dir):
        dependencies = []
        if 'base' in self.config:
            self.default_base_packages = self.config['base']

        exclude_list = set()
        if self.default_base_packages in self.base_packages.keys():
            exclude_list.update(self.base_packages[self.default_base_packages])
        else:
            self.logger().error('Unknown dpkg base: %s' % self.default_base_packages)

        deploy_list = set()
        if 'include' in self.config:
            to_include = self.config['include']
            for package in to_include:
                if package in exclude_list:
                    self.logger().info('Forcing deployment of base package: %s' % package)
                    exclude_list.remove(package)

            self.logger().info('Listing dependencies of: %s' % ','.join(to_include))
            deploy_list.update(self.dpkg.list_dependencies(to_include))

        if 'exclude' in self.config:
            exclude_list.update(self.config['exclude'])

        for package in exclude_list:
            if package in deploy_list:
                deploy_list.remove(package)

        for package in deploy_list:
            self.logger().info('Including files of: %s', package)
            package_files = self.dpkg.list_package_files(package)
            for package_file in package_files:
                self.cache[package_file] = package

                dependencies.append(DpkgDependency(self, package_file, None, package))

        return dependencies
