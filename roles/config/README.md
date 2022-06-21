Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

# Common configuration procedure
- name: "HADOOP CONFIG| Create Hadoop configuration for '{{ _hadoop_version }}'"
  import_role: 
    name: soliverr.bigdata.config
  vars:
    bigdata_owner: "{{ (hadoop_user_create) | ternary(hadoop_user, 'root') }}"
    bigdata_group: "{{ (hadoop_user_create) | ternary(hadoop_group, 'root') }}"
    bigdata_install_dir: "{{ hadoop_install_dir }}"
    bigdata_configuration_pristine_dir: "{{ hadoop_install_dir }}/etc/hadoop"
    bigdata_configuration_pristine_copy: true
    bigdata_configuration_base_dir: "{{ hadoop_etc_base_dir }}"
    bigdata_etc_dir: "{{ hadoop_etc_dir }}"
    bigdata_log_dir: "{{ hadoop_log_dir }}"
    bigdata_profile_name: 'hadoop.sh'
    bigdata_profile_template: 'hadoop-profile.sh.j2'
    bigdata_service_set_default: hdfs_service_set_default
    bigdata_env_template: 'hadoop-env.sh.j2'
    bigdata_env_name: 'hadoop-env.sh'
    
License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
