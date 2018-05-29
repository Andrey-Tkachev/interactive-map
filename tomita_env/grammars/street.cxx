#encoding "utf8"

HouseW -> 'дом';
StreetW -> 'проспект' | 'проезд' | 'улица' | 'шоссе' | 'бульвар' | 'переулок';
StreetShort -> 'пр' | 'просп' | 'пр-д' | 'ул' | 'ш' | 'б-р' | 'пер.' ;

StreetDescr -> StreetW | StreetShort;

NameNoun -> (Adj<gnc-agr[1]>) Word<gnc-agr[1],rt> (Word<gram="род">);

NumberW_1 -> AnyWord<wff=/[1-9]?[0-9]-?((ый)|(ий)|(ой)|й)/> {outgram="муж,ед,им"};
NumberW_2 -> AnyWord<wff=/[1-9]?[0-9]-?((ая)|(яя)|(ья)|я)/> {outgram="жен,ед,им"};
NumberW_3 -> AnyWord<wff=/[1-9]?[0-9]-?((ее)|(ье)|(ое)|е)/> {outgram="сред,ед,им"};

NumberW -> NumberW_1 | NumberW_2 | NumberW_3;
NameAdj -> Adj<h-reg1> Adj*;
NameAdj -> NumberW<gnc-agr[1]> Adj<gnc-agr[1]>;

NumberS -> 'номер' | '№';
House -> HouseW (NumberS) AnyWord<wff=/[1-9]?[0-9]/> interp (StreetFact.HouseNum);

Street -> (House) ('по') StreetDescr interp (StreetFact.Descr) NameNoun<gram="род", h-reg1> interp (StreetFact.Name::not_norm);
Street -> (House) StreetDescr interp (StreetFact.Descr) NameNoun<gram="им", h-reg1> interp (StreetFact.Name::not_norm);
Street -> (House) NameAdj<gnc-agr[1]> interp (StreetFact.Name) StreetW<gnc-agr[1]> interp (StreetFact.Descr);
Street -> (House) NameAdj interp (StreetFact.Name) StreetShort interp (StreetFact.Descr);

Street -> (House) StreetW<gnc-agr[1]> interp (StreetFact.Descr) NameAdj<gnc-agr[1]> interp (StreetFact.Name);
Street -> (House) StreetShort interp (StreetFact.Descr) NameAdj interp (StreetFact.Name);
