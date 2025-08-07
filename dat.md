Data Preprocessing:
It is a technique that involves cleaning, transformation, and organization of raw data to remove inconsistent, 
incomplete, incorrect, and unnecessary data, in order to avoid negative effects on model performance.

USED EXCEL:
->Remove duplicate Values:select Data tab then select data tools group in that remove duplicated since here the uniquec colum n fiels is WreHouse_id
thus based on that we need to check if there is any duplicate records thus select id
<img width="948" height="309" alt="{EC8073BB-303C-4A64-88C3-E108E767FFB2}" src="https://github.com/user-attachments/assets/462e620a-b666-4003-94e1-dcf26b4d0bec" />

->handle incomplete Data : in the dataset wh_est year is incomplete and it is required for the analaysis process thus remove the attribute
<img width="55" height="320" alt="{800C331F-F8CC-4868-9C6F-9D068BA30FAC}" src="https://github.com/user-attachments/assets/2a68e492-0464-4cc9-a6f0-2813af382fda" />

->handle mimatched data type:
Before:
<img width="93" height="320" alt="{43CD26A9-635E-4C19-B8CB-6B1D927C0773}" src="https://github.com/user-attachments/assets/f34bf659-ee54-4bf8-8fd7-7e0b57f83201" />
int the given dataset the WH_capacity_size is given in non numerical data but for model we need numeric data thus convert it into numeric data keep
Large =100,Mid =50, Small=25; Using Find and Replace
<img width="374" height="277" alt="{94A6BA0D-1D54-45E6-B911-98CB7DCA069B}" src="https://github.com/user-attachments/assets/801b4f4b-5dd6-4dc1-8dd9-1c4bb19b2441" />
After:
<img width="89" height="321" alt="{3716BCDA-9C72-4D8E-96BA-CD909F7A17E7}" src="https://github.com/user-attachments/assets/acc3df8b-9209-45c2-b3e2-6b252d0cc7ab" />




