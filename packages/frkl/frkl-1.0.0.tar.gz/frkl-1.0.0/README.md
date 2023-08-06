[![PyPI status](https://img.shields.io/pypi/status/frkl.svg)](https://pypi.python.org/pypi/frkl/)
[![PyPI version](https://img.shields.io/pypi/v/frkl.svg)](https://pypi.python.org/pypi/frkl/)
[![Pipeline status](https://gitlab.com/frkl/frkl/badges/develop/pipeline.svg)](https://gitlab.com/frkl/frkl/pipelines)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# frkl

*elastic dictionaries (and configuration)*


## Description

*frkl* is basically a string/object transformation library, with the main goal being enabling as minimal as possible initial state. I rather suspect that this here is one of those things whose value won't be immediately obvious (if there is one at all -- still not sure about that myself), and examples might be a better way of explaining what its use is.

*frkl* is most useful for cases where you have a list of similar configuration items, which might or might not inherit from each other. In those cases, you don't want to duplicate information that is needed for each of the items. To illustrate, here's some yaml:

    vars:
      location: at_home
      task_type: cleaning
    tasks:
      - clean_bathroom
      - clean_living_room
      - clean_desk:
          location: at_work

This task list describes how we want to clean three things, two of which are at home, and one is at work. Our robot would not like this way of describing it though, since it is much harder to parse. For example, there is no 'proper' schema, the list for example has mixed types, strings and a dictionary with one key/value pair. What our robot would want is:

    - task:
        name: clean_bathroom
      vars:
        location: at_home
        task_type: cleaning
    - task:
        name: clean_living_room
      vars:
        location: at_home
        task_type: cleaning
    - task:
        name: clean_desk
      vars:
        location: at_work
        task_type: cleaning

Basically, this is what *frkl* does: expanding (and also modifying if wanted) configuration from as minimal as possible to as comprehensive as necessary.

Now, of course, in this example the reduction in size is not that big. And, one might argue, not having a fixed schema might not be a good idea in the first place. I can even see the point, but I do like being able to express myself as simple and minimal as possible. Obviously we are introducing more fragility by loosening up our schema. But we gain clarity, and ease of use. Whether this trade-off is justifiable or not depends on the situation I think. This library is for the situations where it is :-)

*frkl* is written in Python.


Features
--------

- transform configurations, focusing on clarity and the removal of redundancy
- plug-able architecture
- pre-made string/object processors/filters (regex, url abbreviation, jinja templates, etc.)
- auto-downloading, merging of configuration items
- mix and match of local and remote configuration items

# Development

Assuming you use [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) for development, here's how to setup a 'frkl' development environment manually:

    pyenv install 3.7.3
    pyenv virtualenv 3.7.3 frkl
    git clone https://gitlab.com/frkl/frkl
    cd <frkl_dir>
    pyenv local frkl
    pip install -e .[develop,testing,docs]
    pre-commit install


## Copyright & license

[Parity Public License 6.0.0](https://licensezero.com/licenses/parity)


Please check the [LICENSE](/LICENSE) file in this repository (it's a short license!), also check out the [*freckles* license page](https://freckles.io/license) for more details.

### frkl product ids

Versions:

  - 0.9:
    - 97de2bf5-0fbb-4884-9d26-488217e1477c
  - 1.x.x:  
    - 97de2bf5-0fbb-4884-9d26-488217e1477c

[Copyright (c) 2019 frkl OÜ](https://frkl.io)
