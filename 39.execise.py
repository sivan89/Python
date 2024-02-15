""" Create a file with the below content (Event_logs.txt)
-----------------------------------------------------

Successfully scheduled Software Protection service for re-start at 2023-03-31T06:40:53Z. Reason: RulesEngine.
Windows Installer reconfigured the product. Product Name: Citrix Workspace(USB). Product Version: 22.10.5532. Product Language: 1033. Manufacturer: Citrix Systems, Inc.. Reconfiguration success or error status: 0.
The Software Protection service has completed licensing status check.
IP Address Configured: 23.56.245.2
Application Id=0ff1ce15-a989-479d-af46-f275c6370663
Windows Installer reconfigured the product. Product Name: icecap_collection_x64. Product Version: 16.10.31306. Product Language: 1033. Manufacturer: Microsoft Corporation. Reconfiguration success or error status: 0.
Backup IP Configured: 2.45.124.53

By using Regualr Expression,

1. Fetch Date related lines.
2. Fetch Product Versions
3. Fetch IP Address formats. """