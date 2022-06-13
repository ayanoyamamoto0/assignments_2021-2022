# A&E Operation :ambulance:: Project Overview
* Created an application to support the accident and emergency (A&E) department’s operation in a hospital
  * When the patient is admitted to the department, the admission information recorded by the receptionist are stored in a Singly Linked List
  * Application informs the triage nurse of the next patient to see in a First In First Out (FIFO) order
  * Application informs the doctor of the next patient to see based on the priority values assigned by triage nurses to ensure that the patient with the most serious condition gets seen by the doctor first
* Full CRUD on the patients' information
* Patients and Treatment information are stored in a database file

## Code and Resources Used
* **Python Version**: 3.8.8
* **SQLite Version**: 3.12.2

## For Testing
* Patient IDs available are 1-1000
* Names can be searched with partial matches
* List of nurses and doctors names in the database are: Chandler Bing, Gunther, Janice Hosenstein, Joey Tribbiani, Mike Hannigan, Monica Geller, Phoebe Buffay, Rachel Green, Ross Geller

## Included DB File
* `ae.db` will be automatically loaded when the application starts
