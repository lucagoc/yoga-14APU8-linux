#!/bin/sh

rpmbuild -bb --define "_topdir $(pwd)" --define "_sourcedir $(pwd)" acpi-yoga.spec
