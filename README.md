Icinga Dynatrace Downtime-Integration
Integration to schedule maintenance between Icinga and Dynatrace at same time.

A small script to integrate two different tools Dynatrace and Icinga and schedule maintenance for all the infrastructure hosts and services . This will be very helpful for some one to schedule downtime at one shot via python script and dont have to jump between two different tools.

The script picks up all the hosts and service list from ICINGA in the last 15 minutes and collects the output data from ICINGA REST API and pass the output as a INPUT to DYNATRACE REST API.
