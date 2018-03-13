#encoding "utf8"

MedicineOrg -> 'больница' | 'госпиталь' | 'поликлиника' | 'морг';
EducationOrg -> 'школа' | 'лицей' | 'гимназия' | 'детский сад' | 'училище' | 'университет';
CultureOrg -> 'музей' | 'галерея' | 'библиотека';

Initial -> Word<wff=/[А-Я]\./>;
Initials -> Initial (Initial);
Surname -> Word;
FIO -> Initials Surname;
By -> 'они'<gram='дат'> | 'имя' <gram='дат'>;
ByPerson ->  By FIO<rt>;

OrgName -> MedicineOrg | EducationOrg | CultureOrg;
Org -> OrgName interp(OrgFact.Name) ByPerson interp(OrgFact.Descr);
