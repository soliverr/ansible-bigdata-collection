#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: java_home
short_description: A module that detects default JAVA_HOME
version_added: "1.0"
description:
  - "A module that detects default Java HOME on the system."
options:
    version:
        description:
          - Java version to find JAVA HOME. If no value is provided the default
            value will be used.
        required: false
        type: str
        default: default
author:
    - Sergey Kryazhevskikh (soliverr@gmail.com)
'''

EXAMPLES = '''
# Find Java Home for Java OpenJDK 11
- name: Get JAVA HOME for OpenJDK 11
  java_home:
    version: "java-11-openjdk"
'''

RETURN = '''
fact:
  description: JAVA HOME directory or empty string
  type: str
  sample: /usr/lib/jvm/java/java-11-openjdk-amd64
'''

import random
import os
import re
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        version=dict(type='str', default='default'),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        changed=False,
        fact=''
    )

    found = False
    # Check for default JVM system layout
    try:
        for d in os.listdir('/usr/lib/jvm'):
            if re.search(module.params['version'], d) and os.path.isdir(f'/usr/lib/jvm/{d}'):
                result['fact'] = f'/usr/lib/jvm/{d}'
                found = True
                break
    except FileNotFoundError:
        pass

    # TODO: Check in update-alternatives --display java
    if not found:
        pass

    # TODO: Find default JVM with `which java`
    if not found and module.params['version'] == 'default':
        pass

    if module.check_mode:
        return result

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()