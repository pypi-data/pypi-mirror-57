# Copyright 2019 Catalin_Popescu, Inc.
# All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# THIS FILE IS MANAGED BY THE GLOBAL REQUIREMENTS REPO - DO NOT EDIT
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rmqworkers", # Replace with your own username
    version="0.0.3",
    author="Popescu Catalin-Ionut",
    author_email="popescu.catalin.ionut@gmail.com",
    description="Rabbit MQ wrapper implement with amqpstorm and with threading or multiprocessing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/popescu-catalin-ionut/rmqworkers",
    packages=setuptools.find_packages(),
    package_data={'examples': ['*.py', 'examples/*.py']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: System :: Networking",
        "Natural Language :: English",
    ],
    python_requires='>=3.6',
)