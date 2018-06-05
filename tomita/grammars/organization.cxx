#encoding "utf8"

MedicineOrg -> 'больница' | 'госпиталь' | 'поликлиника' | 'морг';
EducationOrg -> 'школа' | 'лицей' | 'гимназия' | 'детский сад' | 'училище' | 'университет';
CultureOrg -> 'музей' | 'дом-музей' |'галерея' | 'библиотека' | 'кинотеатр';

Initial -> Word<wff=/[А-Я]\./>;
Initials -> Initial (Initial);
Surname -> Word<h-reg1>;
FIO -> Initials Surname;
By -> 'они' <gram='дат'> | 'имя' <gram='дат'>;

OrgDescrNoun -> (Adj<gnc-agr[1]>) Word<gnc-agr[1],rt> (Word<gram="род">);
ByPerson ->  By FIO<rt>;

OrgName -> MedicineOrg | EducationOrg | CultureOrg;
Org -> OrgName interp(OrgFact.Name) ByPerson interp(OrgFact.Descr::not_norm);
Org -> OrgName<gnc-agr[1]> interp(OrgFact.Name) OrgDescrNoun<gnc-agr[1]> interp(OrgFact.Descr);
