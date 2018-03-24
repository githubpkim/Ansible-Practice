---

- name: IOS Config
  hosts: pynet-rtr1

  tasks:
     - name: IOS Configuration
       ios_config:
          provider: "{{ssh_provider}}"
          src: line_cmds.txt  
          backup: yes
