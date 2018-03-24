---

- name: IOS Config
  hosts: pynet-rtr1
#  vars: 
#     creds:
#        host: "{{ansible_host}}"
#        username: "{{username}}"
#        password: "{{password}}"

  tasks:
     - name: IOS FACT Gathering
       ios_facts:
          provider: "{{ssh_provider}}"
       tags: 
         - ios_fact_only
   
     - name: IOS Configuration
       ios_config:
          provider: "{{ssh_provider}}"
          lines:
             - "ip domain name bogus.com"
             - ip name-server {{name_server1}}
             - ip name-server {{name_server2}}
             - ntp server {{ntp_server1}}
             - ntp server {{ntp_server2}}
   
