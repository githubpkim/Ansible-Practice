---

- name: EOS Config
  hosts: arista

  tasks:
     - name: EOS Configuration
       ios_config:
          provider: "{{ssh_provider}}"
          lines: "{{global_config}}"
